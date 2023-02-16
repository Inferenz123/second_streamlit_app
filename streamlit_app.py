import streamlit
streamlit.title('My Mom New Healthy Diner')

streamlit.header( 'Breakfast fav')
streamlit.text( ' omega 3 and blueberry oatmeal')
streamlit.text('kale, spinach and smoothie')
streamlit.text('hard-boiled free-range egg')

streamlit.header( 'BUILD YOUR OWN SMOOTHIE')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','strawberries'])

#Display the table on the page.
streamlit.dataframe(my_fruit_list)


               
