from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys

import pandas as pd

MTA_KEY = sys.argv[1]
BUS_LINE = 'MTA%20NYCT_'+sys.argv[2]
filename = sys.argv[3]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s"%(MTA_KEY, BUS_LINE)

#print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
BusData = json.loads(data)


vehicle = BusData['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']

latitude = []
longitude = []
stop_name = []
stop_status= []

for i in range(len(vehicle[0]['VehicleActivity'])):
    latitude.append(vehicle[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    longitude.append(vehicle[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    stop_name.append(vehicle[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName'])
    stop_status.append(vehicle[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance'])
    
    
d = {'Latitude':latitude, 
          'Longitude':longitude,
          'Stop Name':stop_name , 
          'Stop Status':stop_status }

stops_df = pd.DataFrame(data=d)
stops_df.to_csv(filename, index =False)