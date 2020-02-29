
import csv
from datetime import datetime
import matplotlib.pyplot as plt

open_file = open("death_valley_2018_simple.csv", "r")

place_name = ''
csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index,column_header in enumerate(header_row):
    print(index,column_header)

highs = []
dates =[]
lows =[]

date_index = header_row.index('DATE')
high_index = header_row.index('TMAX')
low_index = header_row.index('TMIN')
name_index = header_row.index('NAME')

for row in csv_file:
    place_name = row[name_index]
    try:
        high = int(row[high_index])
        low = int(row[low_index])
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    except ValueError:
        print(f"missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low) 
        dates.append(current_date)

#print(highs[:10])

fig, ax = plt.subplots()
ax.plot(dates, highs,color='red', alpha=0.5)
ax.plot(dates, lows,color='blue', alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
title = f"Daily High and Low Temps - 2018\n{place_name}"

open_file = open("sitka_weather_2018_simple.csv", "r")

place_name = ''
csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index,column_header in enumerate(header_row):
    print(index,column_header)

highs = []
dates =[]
lows =[]

date_index = header_row.index('DATE')
high_index = header_row.index('TMAX')
low_index = header_row.index('TMIN')
name_index = header_row.index('NAME')

for row in csv_file:
    place_name = row[name_index]
    try:
        high = int(row[high_index])
        low = int(row[low_index])
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    except ValueError:
        print(f"missing data for {current_date}")
    else:
        highs.append(high)
        lows.append(low) 
        dates.append(current_date)

ax.plot(dates, highs,color='red', alpha=0.5)
ax.plot(dates, lows,color='blue', alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

title += f"\n{place_name}"

plt.title(title,fontsize=16)
plt.xlabel("",fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis='both',which="major",labelsize=12)

fig.autofmt_xdate()

plt.show()
