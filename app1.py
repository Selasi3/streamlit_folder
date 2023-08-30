import streamlit as st

#create a header text for the app
st.header("st.button")

if st.button('say hello'):
    st.write("Why hello there")
else:
    st.write("Goodbye")