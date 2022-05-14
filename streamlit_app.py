import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

def get_frutyvice_data(this_fruit_chice):
  """
  this fuction executes and api-get-requset given a fruitName(this_fruit_choice)
  """
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_chice)
   # take the json version of the response and normlize it 
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
 
st.title('My Parents New Diner')
st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = pd.read_csv("https://github.com/slevinas/zig_first_streamlit_app/blob/main/gggggg.csv")

# set the df index to the fruits names
my_fruit_list = my_fruit_list.set_index('Fruit')
# adding a selector widget (multy-select. ie' filter)
selected_fruits = st.multiselect('Pick some Fruits:',list(my_fruit_list.index),['Avocado', 'Strawberries']) ## # display output
fruits_to_show = my_fruit_list.loc[selected_fruits]
# this will output our df in the app(browser)
st.dataframe(fruits_to_show)                                              ## # display output
  # New Section to display fruityvice api response
st.header('Fruityvice Fruit Advice!')                                     ## # display output               
try:
  fruit_choice = st.text_input('what fruit would you like info about?')   # display text and a grey-text-box-placeholder below the text, to enter input on screen

  if not fruit_choice:
    st.error("Please select a fruit to get info. ")                       # display red-text-box(errot) and the text("Please select a fruit to get info.)
  else:
    fruityvice_normalized = get_frutyvice_data(fruit_choice)
    st.dataframe(fruityvice_normalized)                           # display output the api-results and display it as a table 
except URLError as e:
    st.error()
  

#st.stop()
st.header("View Our Fruit List-Add Your Favorites! ")
# snowflake related functions
def get_fruit_load_list():
  with  my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")           # reads a table from snowflake
    return my_cur.fetchall()

# Ass a button to load the fruit 
if st.button('Get Fruit List'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  st.dataframe(my_data_rows) ##                                # reads a table from snowflake
  
  
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute(" insert into fruit_load_list values('" +  new_fruit +"')")
    return "Thanks for adding " + "new_fruit"
 
add_my_fruit = st.text_input('what fruit would you like add?')     # display text and a grey-text-box-placeholder below the text, to enter input on screen
if st.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  st.text(back_from_function)                                              # display output 

  st.write('Thanks for adding ', add_my_fruit)                        # display output the text "Thanks for adding "
    
#userinput_fruit_choice =  st.text_input('what fruit would you like info about?')
#userinput_fruit_choice2 = st.text_input('what fruit would you like info about?','tomato')
#from_streamlit = userinput_fruit_choice2


# don't run anything past het while we trubleshoot
#st.stop()

#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# st.text("Hello from Snowflake:")
# st.text(my_data_row)








  

  
 

  
# fetchone()- returns one row..
#my_data_row = my_cur.fetchone()
#st.dataframe(my_data_row)      ##                        display a query-result from snowflake's tablez
# to returnt all the rows we use fetchall()
#my_data_rows = my_cur.fetchall()
#st.dataframe(my_data_rows)

#########


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
