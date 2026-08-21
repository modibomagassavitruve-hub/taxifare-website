import streamlit as st
import pandas as pd
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
import datetime

import datetime

def get_pickup_datetime():
    """Affiche les widgets date + heure et retourne un seul datetime combiné"""
    pickup_date = st.date_input("pickup date", datetime.date(2019, 7, 6))
    pickup_time = st.time_input("pickup time", datetime.time(8, 45))
    return f"{pickup_date} {pickup_time}"

pickup_datetime = get_pickup_datetime()

st.write('pickup datetime:', pickup_datetime)

pickup_longitude = st.number_input('Insert a pickup longitude')

st.write('The current number is ', pickup_longitude)

pickup_latitude = st.number_input('Insert a pickup latitude')

st.write('The current number is ', pickup_latitude)


dropoff_longitude = st.number_input('Insert a dropoff longitude')

st.write('The current number is ', dropoff_longitude)

dropoff_latitude = st.number_input('Insert a dropoff latitude')

st.write('The current number is ', dropoff_latitude)


option = st.slider('passenger count', 1, 10, 3)

st.write(option)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...
'''

params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': option
}

'''
3. Let's call our API using the `requests` package...
'''

url = 'https://taxifare.lewagon.ai/predict'
response = requests.get(url, params=params)

'''
4. Let's retrieve the prediction from the **JSON** returned by the API...
'''

prediction = response.json()
pred = prediction['fare']

'''
## Finally, we can display the prediction to the user
'''

st.header(f'Fare amount: ${round(pred, 2)}')
