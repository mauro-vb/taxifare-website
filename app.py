import streamlit as st
import requests
import datetime

'''
# NYC taxi fare prediction
'''
#st.sidebar.markdown(f"""# Parameters""")


time = st.sidebar.time_input('Pickup time', datetime.time(8, 45))
date = st.sidebar.date_input("Pickup date",datetime.date(2019, 7, 6))
pickup_datetime = datetime.datetime.strptime((str(date) + ' ' + str(time)),'%Y-%m-%d %H:%M:%S'),

p_lon = st.sidebar.number_input('Insert the pick-up longitude')
p_lat = st.sidebar.number_input('Insert the pick-up latitude')
d_lon = st.sidebar.number_input('Insert the drop-off longitude')
d_lat = st.sidebar.number_input('Insert the drop-off latitude')

passengers = st.slider('Select number of passengers',1,10,1)

params = dict(
            key=[0],  # useless but the pipeline requires it
            pickup_datetime=[pickup_datetime],
            pickup_longitude=[p_lon],
            pickup_latitude=[p_lat],
            dropoff_longitude=[d_lon],
            dropoff_latitude=[d_lat],
            passenger_count=[passengers]
        )


url = 'https://miapiight-bjp5b3mjla-ew.a.run.app/predict'

response = requests.get(url,params = params).json()

if st.button('Predict'):
    # print is visible in the server output, not in the page
    col1, col2, col3 = st.columns(3)
    #col1.metric("SPDR S&P 500", "$437.8", "-$1.25")
    col2.metric("US$", response['fare_amount'], 'your taxi fare prediction')
    #col3.metric("BTC", "$46,583.91", "+4.87%")
else:
    st.write('No prediction yet...')
