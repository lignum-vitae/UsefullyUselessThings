#!/usr/bin/python -u
#import requests as req
#from bs4 import BeautifulSoup
import sys
import urllib.request
import urllib.parse as urlparse
from urllib.parse import urlencode

def add_url_params(url, params):
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)

    url_parts[4] = urlencode(query)
    query_url = urlparse.urlunparse(url_parts)
    return query_url

#payload = {'station':'AEB','parameter':'wtemp','StartDate':'2024-11-01','EndDate':'2024-11-29','outputtype':'1'}
#res = req.get("https://eyesonthebay.dnr.maryland.gov/contmon/ContMon.cfm", paramsid=payload)
#print(res.text)
"""
with open('token.txt') as file:
    token = str(file.read()).strip()
"""
urlid = 'https://www.ncei.noaa.gov/cdo-web/api/v2/data'
paramsid = {'datasetid':'TOBS','stationid':'8574680', 'units':'standard', 'startdate':'2024-11-01', 'enddate':'2024-11-30'}

#time is in UTC (local time is UTC-5)
data = urllib.request.urlopen('https://www.ndbc.noaa.gov/data/realtime2/BLTM2.txt')

#~240 readings per day
def limited_lines_read(url_data, numberoflines, linearray):
    for _ in range(numberoflines+1):
        linearray.append(url_data.readline().decode("utf-8").strip())
    return linearray
dataarray = []
for line in limited_lines_read(data, 6, dataarray):
    print(f"<li>{line}</li>")

#print(type(dataarray[0]))
acronym_to_index ={"YY":0, "MM":1, "DD":2, "hh":3, "mm":4, "WDIR":5, "WSPD":6, 
                   "GST":7, "WVHT":8, "DPD":9, "APD":10, "MWD":11, "PRES":12, 
                   "ATMP":13, "WTMP":14, "DEWP":15, "VIS": 16, "PTDY":17, "TIDE":18}
#print(acronym_to_index)
