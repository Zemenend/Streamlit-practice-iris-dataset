import streamlit as st

# Title
st.title("My First Streamlit App")

# Write some text
st.write("Welcome to my first Streamlit app!!")

# Add a slider
number= st.slider("Pick a number")

# Display the result
st.write(f"You pick number:{number}")

age = st.slider("How old are you?",0,100,22)
st.write("I'm ",age," years old.")

values = st.slider("Select a range of values",0.0,100.0,(0.5,40.75))
st.write("You selected", values)