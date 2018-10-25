import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import datetime as dt
import time
import pandas as pd

df = pd.read_csv('20181024.csv')

today = dt.datetime.strftime(dt.datetime.now(), '%Y-%m-%d')

fig, tx = plt.subplots()

tx.plot_date(df['datenum'][-100:-1], df['Temperature'][-100:-1], 'b-')
tx.set_xlabel('Date: %s' % today)
tx.set_ylabel('Temperature (C)', color='b')

tx.xaxis.set_major_formatter(md.DateFormatter('%H'))
tx.xaxis.set_major_locator(md.HourLocator())
tx.xaxis.set_minor_locator(md.MinuteLocator())

tx.set_xlim()

hx = tx.twinx()
hx.plot(df['datenum'][-100:-1], df['Humidity'][-100:-1], 'g-')
hx.set_ylabel('Humidity (%)', color='g')

fig.tight_layout()


plt.savefig(today+".png")

plt.show()


def plot_most_recent(df, hours=12):
    samples = -3600 * hours
    
    fig, temp_axis = plt.subplots()
    
    temp_axis.plot_date(df['datenum'][samples:-1], df['Temperature'][samples:-1], 'r-')
    temp_axis.set_xlabel('Last %d Hours'%hours)
    temp_axis.ylabel('Temperature (C)', color='r')
    
    temp_axis.set_major_formatter(md.DateFormatter('%b %d %H'))
    temp_axis.set_major_locator(md.DayLocator())
    temp_axis.set_minor_locator(md.HourLocator())
    
    hum_axis = temp_axis.twinx()
    hum_axis.plot(df['datenum'][samples:-1], df['Humidity'][samples:-1], 'g-')
    hum_axis.set_ylabel('Humidity (%)', color='g')
    
    fig.tight_layout()
    today = dt.datetime.strftime(dt.datetime.now(), '%Y%m%d_%H%M%S')
    plt.savefig(today +".png")
    plt.show()