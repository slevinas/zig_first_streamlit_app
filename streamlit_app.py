import streamlit as st

st.title('My Parents New Diner')

st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# set the df index to the fruits names
my_fruit_list = my_fruit_list.set_index('Fruit')

# adding a selector widget (multy-select. ie' filter)
selected_fruits = st.multiselect('Pick some Fruits:',list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[selected_fruits]

# this will output our df in the app(browser)
st.dataframe(fruits_to_show)
# New Section to display fruityvice api response
st.header('Fruityvice Fruit Advice!')
userinput_fruit_choice = st.text_input('what fruit would you like info about?', 'Kiwi')
st.write('The user entered', userinput_fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + userinput_fruit_choice)
# st.text(fruityvice_response.json())  # just writs the data to the screen

# take the json version of the response and normlize it 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# output it as a table 
st.dataframe(fruityvice_normalized)
import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)

# name = st.text_input('Name')
# if  name=="":
#   st.warning('Please input a name.')
#   st.stop()
# st.success('Thank you for inputting a name.')



# #print(my_fruit_list.head(5), end='\n\n')
# print(my_fruit_list.info() ,end="\n\n")
# # print(my_fruit_list.index ,end="\n\n")
# #print(my_fruit_list.loc['Strawberries'] ,end="\n\n")

# # adding a selector widget (multy-select. ie' filter)
# # st.multiselect('Pick some Fruits:',list(my_fruit_list.index))
# # # this will output our df in the app(browser)
# # st.dataframe(my_fruit_list)
