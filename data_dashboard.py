import streamlit as st
import pandas as pd 
import plotly.express as px



# Title
st.title("Sample Data Dashboard")

# Add sliders for each category with default values
value_a = st.slider("Value for Category A",0,100,47)
value_b = st.slider("Value for Category B",0,100,41)
value_c = st.slider("Value for Category C",0,100,64)
value_d = st.slider("Value for Category D",0,100,34)
value_e = st.slider("Value for Category E",0,100,50)

# Update teh DataFrame based on user input
data =pd.DataFrame({'Category':['A','B','C','D','E'],
                    'Values':[value_a,value_b,value_c,value_d,value_e]})


# Write text and display DataFrame

st.write("Here is the sample data")
st.dataframe(data)

# Update the plot based on user input using Plotly


fig = px.bar(data, x = 'Category',
             y = 'Values',
             title = 'Category Values',
             labels={'Category':'Category',"Values":"Values"})

# Display the plot in Streamlit
st.plotly_chart(fig)