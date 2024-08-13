import streamlit as st
import requests

# OpenWeatherMap API 키 설정
API_KEY = 'eeb25092d9b34b41669d84fbf47c2bcf'

# 도시 이름 입력 받기
st.title("날씨 정보 앱")
city = st.text_input("도시 이름을 입력하세요:", "Seoul")

# 날씨 정보 가져오기
if city:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    if weather_data.get("cod") != 200:
        st.error("도시 정보를 찾을 수 없습니다. 다시 시도해 주세요.")
    else:
        # 날씨 정보 출력
        st.subheader(f"{city}의 날씨 정보")
        st.write(f"온도: {weather_data['main']['temp']}°C")
        st.write(f"날씨: {weather_data['weather'][0]['description']}")
        st.write(f"습도: {weather_data['main']['humidity']}%")
        st.write(f"풍속: {weather_data['wind']['speed']} m/s")
