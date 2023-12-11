import pandas as pd
import zipfile
import kaggle

# !kaggle datasets download -d hmavrodiev/london-bike-sharing-dataset

# zipfile_name = 'london-bike-sharing-dataset.zip'
# with zipfile.ZipFile(zipfile_name, 'r') as file:
#     file.extractall()

bikes = pd.read_csv('london_merged.csv')
# bikes.info()
# print(bikes.shape)
# print(bikes)

# print(bikes.weather_code.value_counts())
# print(bikes.season.value_counts())

# Specifying the column names for self
new_cols_dict ={
    'timestamp':'time',
    'cnt':'count', 
    't1':'temp_real_C',
    't2':'temp_feels_like_C',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kph',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
}

# Renaming the columns to the specified column names
bikes.rename(new_cols_dict, axis=1, inplace=True)

# Changing the humidity values to percentage (i.e. a value between 0 and 1)
bikes.humidity_percent = bikes.humidity_percent / 100

# Creating a season dictionary so that we can map the integers 0-3 to the actual written values
season_dict = {
    '0.0':'spring',
    '1.0':'summer',
    '2.0':'autumn',
    '3.0':'winter'
}

# Creating a weather dictionary so that we can map the integers to the actual written values
weather_dict = {
    '1.0':'Clear',
    '2.0':'Scattered clouds',
    '3.0':'Broken clouds',
    '4.0':'Cloudy',
    '7.0':'Rain',
    '10.0':'Rain with thunderstorm',
    '26.0':'Snowfall'
}

bikes.season = bikes.season.astype('str')
bikes.season = bikes.season.map(season_dict)
bikes.weather = bikes.weather.astype('str')
bikes.weather = bikes.weather.map(weather_dict)

# print(bikes.head())

bikes.to_excel('london_bikes_final.xlsx', sheet_name='Data')
