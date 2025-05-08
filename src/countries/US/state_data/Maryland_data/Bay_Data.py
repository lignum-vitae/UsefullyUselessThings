#!/usr/bin/python -u
import requests
from bs4 import BeautifulSoup
import json
import re

def main():
    chesapeake_stations = ["BLTM2", "CHCM2", "TCBM2", "FSKM2", "CPVM2", "APAM2",
                           "44063", "TPLM2", "BSLM2", "CAMM2", "44062", "COVM2",
                           "SLIM2", "BISM2", "PPTM2", "44042"]
    #real_time_data: str = process_noaa_rt_stations(chesapeake_stations, 5) #json formatted string
    #print(real_time_data)
    eotb_station_loc, eotb_stations = get_eotb_stations()
    monthly_data: str = eotb_stations_to_json(['CB10', 'CB11', 'WT51', 'CB32', 'WT41', 'CB31']) #json formatted string
    print(monthly_data)

def process_noaa_rt_stations(stations: list[str], NumberOfPoints: int) -> str:
    data_cols ={"YY":0, "MM":1, "DD":2, "hh":3, "mm":4, "WDIR":5, "WSPD":6, 
                       "GST":7, "WVHT":8, "DPD":9, "APD":10, "MWD":11, "PRES":12, 
                       "ATMP":13, "WTMP":14, "DEWP":15, "VIS": 16, "PTDY":17, "TIDE":18}
    json_formatted_data = {} #dict[str, list[dict[str,str]]]
    #time is in UTC (EST is UTC-5)
    for station in stations:
        data = requests.get(f'https://www.ndbc.noaa.gov/data/realtime2/{station}.txt')
        lines = noaa_data_to_json(data.text, NumberOfPoints, data_cols)
        json_formatted_data.setdefault(station, []).extend(lines[2:])
    json_output: str = json.dumps(json_formatted_data, indent=4)
    return json_output

#~240 readings per day
def noaa_data_to_json(url_data: str, numberoflines: int, titles: dict[str, int]) -> list[dict[str,str]]:
    #formats noaa data in a JSON friendly way
    dataarray = []
    temp = [data.split() for data in url_data.split('\n')]
    temp = temp[2:numberoflines+1] #first two indexes are headers
    temp[:] = [[data_point if data_point != "MM" else "" for data_point in data] for data in temp]
    dataarray = [{t:d for (t,d) in zip(titles, data)} for data in temp]
    return dataarray

def get_eotb_stations() -> tuple[dict[str,str], list[str]]:
    #These stations provide monthly readings
    station_locations = {}
    response = requests.get('https://eyesonthebay.dnr.maryland.gov/bay_cond/bay_cond.cfm')
    soup = BeautifulSoup(response.text, 'html.parser')
    station_options: list[str] = soup.find_all('table')[0].select('option')
    for option in station_options:
        match = re.search('>(.+)</', str(option))
        temp = match.group(1).split(' - ')
        station_locations[temp[0]]=temp[1] #{Station code: Station location}
    station_ids = [x.replace(".", "") for x in station_locations.keys()]
    return station_locations, station_ids

def eotb_stations_to_json(stations: list[str]) -> str:
    jsondata = {}
    parameters = ['bdo', 'wt', 'sec', 'sal', 'ph']
    for station in stations:
        jsondata[station] = {} #dict[str, dict[str, dict[str, dict[str, str]]]]
        #jsondata[station_id][parameter][month][data_title] = data
        for parameter in parameters:
            payload: dict[str,str] = {'station':station,'param':parameter}
            response = requests.get("https://eyesonthebay.dnr.maryland.gov/bay_cond/bay_cond.cfm", params=payload)
            soup = BeautifulSoup(response.text, 'html.parser')
            souparray: list[str] = str(soup.find_all('table')[3].prettify()).split('\n')
            raw_data: list[str] = [data.strip() for data in souparray if "<" not in data]
            data_titles: list[str] = raw_data[3:8]
            #range explained: 9 = first data position. 80 = offset to start of data(8)+number of months(12)*len(titles)(6)
            temp = {raw_data[i-1]:{data_titles[x]:raw_data[i+x] for x in range(len(data_titles))} for i in range(9,80,6)}
            jsondata[station].setdefault(parameter, {}).update(temp)
    json_output = json.dumps(jsondata, indent=4)
    return json_output

if __name__ == "__main__":
    main()
