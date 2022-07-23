from ast import Index
import pandas as pd
import numpy as np

data = pd.read_csv('data/power_outage.csv')

# Datasource processing before scraping - https://www.wunderground.com/history
'''
What must be altered
1. extract month from event date
2. locate specific locations from broad descriptions
'''
df = pd.DataFrame(data)

# Filtering Columns 
df =df[df['Date of Restoration'] != 'Unknown']
df =df[df['Number of Customers Affected'] != 'Unknown']
df = df[~df["Date of Restoration"].str.contains(':',na=False)]
df = df[df["Time Event Began"].str.contains(':',na=False)]
df = df[df["Time of Restoration"].str.contains(':',na=False)]

df = df[~df["Geographic Areas"].str.endswith(':',na=False)]
df = df[~df["Geographic Areas"].str.contains('Location Unknown','-', na=False)]
df = df[df["Demand Loss (MW)"].str.contains('\d', na=False)]
df = df[df["Number of Customers Affected"].str.contains('\d', na=False)]


'''
Types of outage causes associated with whether : Event Description
1. Severe Weather - Thunderstorms
2. Brush Fire
3. Earthquake / Earthquakes
4. Flood / Flooding
5. Heat Storm
6. Heat Wave
7. 
'''

'''
2. Geographic areas

must contain state
if contains ',' - should have correct format
if format is 'state:' - remove df[df['Geographic Areas'][:-1] == ':'].drop

'''
#df.dropna()
df.to_csv('power_data.csv')
print(df.head)