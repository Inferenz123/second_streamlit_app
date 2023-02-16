import streamlit
streamlit.title('My Mom New Healthy Diner')

streamlit.header( 'Breakfast fav')
streamlit.text( ' omega 3 and blueberry oatmeal')
streamlit.text('kale, spinach and smoothie')
streamlit.text('hard-boiled free-range egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
               
