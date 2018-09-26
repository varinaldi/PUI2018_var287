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


stops = open(sys.argv[3], "w")
stops.write('Latitude,Longitude,Stop Name,Stop Status' + '\n')

for i in range(len(vehicle[0]['VehicleActivity'])):
    stopinfo = [ vehicle[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], 
    vehicle[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'],
    vehicle[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName'],
    vehicle[0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']]
    
    str1 = ','.join(str(e) for e in stopinfo)
    stops.write(str1 + '\n')
   

print('{} successfully created'.format(sys.argv[3]))



