#!/usr/bin/python -u
#import requests
#from bs4 import BeautifulSoup
import urllib.request
import urllib.parse as urlparse
from urllib.parse import urlencode
import json

def main():
    data_cols ={"YY":0, "MM":1, "DD":2, "hh":3, "mm":4, "WDIR":5, "WSPD":6, 
                       "GST":7, "WVHT":8, "DPD":9, "APD":10, "MWD":11, "PRES":12, 
                       "ATMP":13, "WTMP":14, "DEWP":15, "VIS": 16, "PTDY":17, "TIDE":18}
    output_json = {}
    #time is in UTC (local time is UTC-5)
    chesapeake_stations = ["BLTM2", "CHCM2", "TCBM2", "FSKM2", "CPVM2", "APAM2",
                           "44063", "TPLM2", "BSLM2", "CAMM2", "44062", "COVM2",
                           "SLIM2", "BISM2", "PPTM2", "44042"]
    for station in chesapeake_stations:
        data = urllib.request.urlopen(f'https://www.ndbc.noaa.gov/data/realtime2/{station}.txt')
        lines = limited_lines_read(data, 240, data_cols)
        output_json.setdefault(station, []).extend(lines[2:])
    print(json.dumps(output_json))
"""
    payload = {'station':'AEB','parameter':'wtemp','StartDate':'2024-11-01','EndDate':'2024-11-29','outputtype':'1'}
    res = requests.get("https://eyesonthebay.dnr.maryland.gov/contmon/ContMon.cfm", params=payload)
    print(res.text)
"""
def add_url_params(url, params):
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)

    url_parts[4] = urlencode(query)
    query_url = urlparse.urlunparse(url_parts)
    return query_url

"""
with open('token.txt') as file:
    token = str(file.read()).strip()
urlid = 'https://www.ncei.noaa.gov/cdo-web/api/v2/data'
paramsid = {'datasetid':'TOBS','stationid':'8574680', 'units':'standard', 'startdate':'2024-11-01', 'enddate':'2024-11-30'}
"""

#~240 readings per day
def limited_lines_read(url_data, numberoflines, titles):
    dataarray = []
    for _ in range(numberoflines+1):
        temp = url_data.readline().decode("utf-8").strip().split()
        temp[:] = [x if x != "MM" else "" for x in temp]
        dataarray.append(dict(zip(titles, temp)))
    return dataarray

if __name__ == "__main__":
    main()
