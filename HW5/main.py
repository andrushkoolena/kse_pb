import requests
import pandas as pd
import datetime
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 50.45,                
    "longitude": 30.52,
    "hourly": "temperature_2m,wind_speed_10m",  
    "forecast_days": 7,              
    "timezone": "Europe/Kyiv"
}
res = requests.get(url, params=params)
data = res.json()
time = data['hourly']['time']
temperature = data['hourly']['temperature_2m']
wind_speed = data['hourly']['wind_speed_10m']
df = pd.DataFrame({
    "time": pd.to_datetime(time), 
    "temperature": temperature,
    "wind_speed": wind_speed
})
df_3days = df[df["time"] < (df["time"].min() + pd.Timedelta(days=3))]
min = df_3days['temperature'].min()
max = df_3days['temperature'].max()
serd = df_3days['temperature'].mean()
print(f"Мiнімум: {min}°C")
print(f"Максимум: {max}°C")
print(f"Середня: {serd}°C")
total_serd = df['wind_speed'].mean()
count_hours = (df['wind_speed'] > total_serd).sum()
print(f"Годин, коли швидкість вітру перевищує загальну середню ({total_serd} м/с): {count_hours} годин")
print(df)