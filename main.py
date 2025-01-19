import requests
import streamlit as st

options = ["Hải Phòng", "Hà Nội", "Hải Dương"]

city_name = st.text_input("Nhập thành phố")



#st.image(f'https://openweathermap.org/img/wn/{weather_icon}@2x.png')

city1 = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=3&appid={API_key}")

data3 = city1.json()

lat = data3[0]['lat']
lon = data3[0]['lon']


responses = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
air_pollution = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_key}")

data = responses.json()
data2 = air_pollution.json()

name = data['name']
temp1 = data['main']['temp']
humid = data['main']['humidity']

temp = float(temp1)- 273.15
temp = round(temp, 2)

pm2_5 = data2['list'][0]['components']['pm2_5']
aqi = data2['list'][0]['main']['aqi']


try:
    st.title(f'Thời tiết hiện tại')
    st.write(f'Khu vực: {name}')
    st.write(f'Nhiệt độ: {temp} độ C')
    st.write(f'Độ ẩm: {humid}%')

    st.title(f'Mức độ ô nhiễm')
    st.write(f'Chỉ số AQI: {aqi}')
    st.write(f"Nồng độ bụi mịn PM 2.5: {pm2_5}")
except:
    print(data2)