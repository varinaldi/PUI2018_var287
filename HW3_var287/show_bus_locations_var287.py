from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys


MTA_KEY = sys.argv[1]
BUS_LINE = 'MTA%20NYCT_'+sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&LineRef=%s"%(MTA_KEY, BUS_LINE)

#print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
BusData = json.loads(data)


vehicle = BusData['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']

print("Bus Line: {}".format(BUS_LINE))
print("Number of Active Buses: {} ".format(len(vehicle[0]['VehicleActivity'])))

for i in range(len(vehicle[0]['VehicleActivity'])):
    print("Bus {} is at latitude {} and longitude {}".format(i, vehicle[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], vehicle[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))