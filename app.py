import streamlit as st
import pandas as pd
import model
# 1. pressure',
pressure = st.number_input("Enter Pressure", min_value=0)

# 2. 'dewpoint'
dewpoint = st.number_input("Enter Dewpoint", min_value=0)

# 3. 'humidity'
humidity = st.number_input("Enter Humidity", min_value=0)

#4.'cloud'
cloud = st.number_input("Enter Cloud", min_value=0)
#5.  'sunshine',      
sushine = st.number_input("Enter Sunshine", min_value=0)
#6. winddirction
winddirection = st.number_input("Enter winddirection", min_value=0)
#7.  'windspeed'
windspeed = st.number_input("Enter windspeed", min_value=0)


print(pressure,dewpoint,cloud)
input_data = (pressure,dewpoint,humidity,cloud,sushine,winddirection,windspeed)
input_df = pd.DataFrame([input_data],columns=['pressure', 'dewpoint', 'humidity', 'cloud', 'sunshine','winddirection', 'windspeed'])
predict = model.model.predict(input_df)

if st.button("Predict"):
    if predict[0]: 
        st.write("There is a possibility of Rain accoding to data")
    else:
        st.write("There is no possibility of Rain accoding to data")