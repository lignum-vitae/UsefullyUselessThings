#!/usr/bin/python -u
import requests
from bs4 import BeautifulSoup
import json
import re

def main():
    """
    data_cols ={"YY":0, "MM":1, "DD":2, "hh":3, "mm":4, "WDIR":5, "WSPD":6, 
                       "GST":7, "WVHT":8, "DPD":9, "APD":10, "MWD":11, "PRES":12, 
                       "ATMP":13, "WTMP":14, "DEWP":15, "VIS": 16, "PTDY":17, "TIDE":18}
    output_json = {}
    #time is in UTC (local time is UTC-5)
    chesapeake_stations = ["BLTM2", "CHCM2", "TCBM2", "FSKM2", "CPVM2", "APAM2",
                           "44063", "TPLM2", "BSLM2", "CAMM2", "44062", "COVM2",
                           "SLIM2", "BISM2", "PPTM2", "44042"]
    for station in chesapeake_stations:
        data = requests.get(f'https://www.ndbc.noaa.gov/data/realtime2/{station}.txt')
        lines = limited_lines_read(data.text, 5, data_cols)
        output_json.setdefault(station, []).extend(lines[2:])
    print(json.dumps(output_json))
    """
    eotb_station_loc = {}
    response = requests.get('https://eyesonthebay.dnr.maryland.gov/bay_cond/bay_cond.cfm')
    soup = BeautifulSoup(response.text, 'html.parser')
    options = soup.find_all('table')[0].select('option')
    for option in options:
        m = re.search('>(.+)</', str(option))
        temp = m.group(1).split(' - ')
        eotb_station_loc[temp[0]]=temp[1]

    eotb_stations = [x.replace(".", "") for x in eotb_station_loc.keys()]
    parameters = ['bdo', 'wt', 'sec', 'sal', 'ph']
    for station in ['CB10']:
        for parameter in ['bdo']:
            payload = {'station':station,'param':parameter}
            res = requests.get("https://eyesonthebay.dnr.maryland.gov/bay_cond/bay_cond.cfm", params=payload)
            soup = BeautifulSoup(res.text, 'html.parser')
            print(soup.find_all('table')[3])
    #Need to format table data into json output
    #print(res.text)

#~240 readings per day
def limited_lines_read(url_data, numberoflines, titles):
    dataarray = []
    temp = [data.split() for data in url_data.split('\n')]
    temp = temp[2:numberoflines+1] #first two indexes are headers
    temp[:] = [[data_point if data_point != "MM" else "" for data_point in data] for data in temp]
    dataarray = [{t:d for (t,d) in zip(titles, data)} for data in temp]
    return dataarray

if __name__ == "__main__":
    main()
