import csv
import matplotlib.pyplot as plt
from datetime import datetime

dates, highs, lows = [], [], []

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get dates, high, and low temperatures from this file.
    for row in reader:
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# Format plot.
ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Tepmperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
