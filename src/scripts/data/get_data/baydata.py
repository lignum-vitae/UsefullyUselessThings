#!/usr/bin/python -u
import requests
from bs4 import BeautifulSoup
import json
import re

def main():
    chesapeake_stations = ["BLTM2", "CHCM2", "TCBM2", "FSKM2", "CPVM2", "APAM2",
                           "44063", "TPLM2", "BSLM2", "CAMM2", "44062", "COVM2",
                           "SLIM2", "BISM2", "PPTM2", "44042"]
    real_time_data = process_noaa_rt_stations(chesapeake_stations, 5)
    print(real_time_data)
    eotb_station_loc, eotb_stations = get_eotb_stations()
    monthly_data = eotb_stations_to_json(['CB10'])
    print(monthly_data)


#~240 readings per day
def noaa_data_to_json(url_data, numberoflines, titles):
    dataarray = []
    temp = [data.split() for data in url_data.split('\n')]
    temp = temp[2:numberoflines+1] #first two indexes are headers
    temp[:] = [[data_point if data_point != "MM" else "" for data_point in data] for data in temp]
    dataarray = [{t:d for (t,d) in zip(titles, data)} for data in temp]
    return dataarray

def process_noaa_rt_stations(stations, NumberOfPoints):
    data_cols ={"YY":0, "MM":1, "DD":2, "hh":3, "mm":4, "WDIR":5, "WSPD":6, 
                       "GST":7, "WVHT":8, "DPD":9, "APD":10, "MWD":11, "PRES":12, 
                       "ATMP":13, "WTMP":14, "DEWP":15, "VIS": 16, "PTDY":17, "TIDE":18}
    json_formatted_data = {}
    #time is in UTC (EST is UTC-5)
    for station in stations:
        data = requests.get(f'https://www.ndbc.noaa.gov/data/realtime2/{station}.txt')
        lines = noaa_data_to_json(data.text, NumberOfPoints, data_cols)
        json_formatted_data.setdefault(station, []).extend(lines[2:])
    json_output = json.dumps(json_formatted_data)
    return json_output

def get_eotb_stations():
    #These stations provide monthly readings
    station_locations = {}
    response = requests.get('https://eyesonthebay.dnr.maryland.gov/bay_cond/bay_cond.cfm')
    soup = BeautifulSoup(response.text, 'html.parser')
    station_options = soup.find_all('table')[0].select('option')
    for option in station_options:
        match = re.search('>(.+)</', str(option))
        temp = match.group(1).split(' - ')
        station_locations[temp[0]]=temp[1] #{Station code: Station location}
    station_ids = [x.replace(".", "") for x in station_locations.keys()]
    return station_locations, station_ids

def eotb_stations_to_json(stations):
    dataarray = []
    parameters = ['bdo', 'wt', 'sec', 'sal', 'ph']
    for station in stations:
        for parameter in ['bdo']:
            payload = {'station':station,'param':parameter}
            res = requests.get("https://eyesonthebay.dnr.maryland.gov/bay_cond/bay_cond.cfm", params=payload)
            soup = BeautifulSoup(res.text, 'html.parser')
            souparray = str(soup.find_all('table')[3].prettify()).split('\n')
            raw_data = [data.strip() for data in souparray if "<" not in data]
            dataarray.append(raw_data)
    #Need to format table data into json output
    #dataarray will not be final output
    return dataarray

if __name__ == "__main__":
    main()
