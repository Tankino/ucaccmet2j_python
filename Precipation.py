#finding code for seattle station
with open('stations.csv') as csvfile:
    for line in csvfile:
        location, state, station = line.strip().split(',')
        if location == 'Seattle':
            seattle_station= station

print(seattle_station)

   
#importing json file
import json

with open('precipitation.json') as jsonfile:
    preticipation_data = json.load(jsonfile)

preticipation_total=[0]*12
for measurement in preticipation_data:
    if measurement ['station'] == seattle_station:
        splitted_dates=measurement['date'].strip().split('-')
        month = splitted_dates[1]
        month= int(month)
        preticipation_total[month-1] += measurement['value']

print(preticipation_total)

with open('participation_total.json', 'w') as f:
    json.dump(preticipation_total, f)
#summing all the monthly preticipation (first splitting per month)
        

    


