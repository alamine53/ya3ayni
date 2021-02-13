import pandas as pd 
from datetime import datetime, date, timedelta
url = "standings.csv"
df = pd.read_csv(url)
df['dates'] = pd.to_datetime(df['date'])
df = df[df['dates'] > max(df['dates']) - timedelta(15)]
print(df[['Team', 'date', 'PTS', 'GP']])

print(date.today())
print(date.today() - timedelta(5))
print(df['Team'].unique())
# date_range = 'last15'
# df['datetime'] = pd.to_datetime(df['date'])
# if date_range == 'last5':
# 	df = df[df['datetime'] > date.today() - 5]
# elif date_range == 'last15':
# 	df = df[df['datetime'] > date.today() - 15]
# 	print(df)



# print(df)

# date_range = pd.to_datetime(df['date'].unique())


# print(min(date_range))
# print(date.today())