import streamlit as st

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

d = st.date_input(
    "date and time",
    datetime.date(2019, 7, 6))
st.write('date and time:', d)

t = st.time_input('date and time', datetime.time(8, 45))

st.write('date and time', t)

number = st.number_input('Insert a pickup longitude')

st.write('The current number is ', number)

number = st.number_input('Insert a pickup latitude')

st.write('The current number is ', number)


number = st.number_input('Insert a dropoff longitude')

st.write('The current number is ', number)

number = st.number_input('Insert a dropoff latitude')

st.write('The current number is ', number)


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

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
