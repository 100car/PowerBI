import pandas as pd
import requests

# Координати Києва
LAT = 50.45
LON = 30.52


def get_detailed_weather():
    ## Запит до API (прогноз на 10 днів, щоденні дані)
    url = (f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}"
           f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,"
           f"precipitation_probability_max,relative_humidity_2m_max"
           f"&timezone=Europe%2fKyiv&forecast_days=10")

    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame({
        'Дата': pd.to_datetime(data['daily']['time']),
        'Макс_Темп_C': data['daily']['temperature_2m_max'],
        'Мін_Темп_C': data['daily']['temperature_2m_min'],
        'Опади_мм': data['daily']['precipitation_sum'],
        'Ймовірність_опадів_%': data['daily']['precipitation_probability_max'],
        'Вологість_%': data['daily']['relative_humidity_2m_max']
    })

    return df


if __name__ == "__main__":
    weather_df = get_detailed_weather()
    print(weather_df)
    weather_df.to_csv('kyiv_weather_pro.csv', index=False, encoding='utf-8-sig')
    print("\nФайл 'kyiv_weather_pro.csv' створено з усіма показниками!")
