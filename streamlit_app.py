import streamlit as st
st.write("""# Largest number identification
This app identifies largest of given 3 numbers
""")


st.header('User Input Parameters')  

first_number = st.number_input("FIRST_NUMBER")
second_number = st.number_input("SECOND_NUMBER")
third_number = st.number_input("THIRD_NUMBER")

largest_number = max(first_number,second_number, third_number)

st.subheader('User Input parameters')
st.write(first_number)
st.write(second_number)
st.write(third_number)

st.subheader("Largest number of given 3 numbers is")
st.write(largest_number)


