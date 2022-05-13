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
st.dataframe(fruits_to_show) ##                                                                   First output display of a fruit list 

# New Section to display fruityvice api response
st.header('Fruityvice Fruit Advice!')
userinput_fruit_choice = st.text_input('what fruit would you like info about?', 'Kiwi')
st.write('The user entered', userinput_fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + userinput_fruit_choice)
# st.text(fruityvice_response.json())  # just writs the data to the screen

# take the json version of the response and normlize it 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

st.dataframe(fruityvice_normalized)                           # = output the api-results and display it as a table 

import snowflake.connector

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# st.text("Hello from Snowflake:")
# st.text(my_data_row)

my_cur.execute("select * from fruit_load_list") # reads a table from snowflake
my_data_rows = my_cur.fetchall()
st.dataframe(my_data_rows)

# fetchone()- returns one row..
#my_data_row = my_cur.fetchone()
#st.dataframe(my_data_row)      ##                        display a query-result from snowflake's tablez
# to returnt all the rows we use fetchall()
#my_data_rows = my_cur.fetchall()
#st.dataframe(my_data_rows)

#########

userinput_fruit_choice2 = st.text_input('what fruit would you like info about?', 'mango')

from_streamlit = userinput_fruit_choice2
st.write('The user entered', userinput_fruit_choice2)

my_cur.execute("insert into fruit_load_list values ('from_streamlit')")








st.header("The Fruit load list contains:")
my_cur.execute("select * from fruit_load_list") # reads a table from snowflake
my_data_rows = my_cur.fetchall()
st.dataframe(my_data_rows)        ##                 Last display a query-result from snowflake's tablez

              



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
