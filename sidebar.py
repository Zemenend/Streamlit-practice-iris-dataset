import streamlit as st


# Sidebar for navigation
page = st.sidebar.selectbox("Select a Page",["Home","Data Dashboard","About"])

# Display different pages based on selection

if page == "Home":
    st.title("Welcome to the Home Page")
    st.write("This is the home of our multiple page app.")

#Example of displaying a DataFrame and chart on the dashboard
    # Create Sample data
    import pandas as pd
    import plotly.express as px
    data = pd.DataFrame({'Category':['A','B','C','D','E','F','G'],
                         'Values':[20,45,36,78,24,19,90]})
    
    st.write("Here is a sample data.")
    st.dataframe(data)

    # Create and display a bar chart using plotly
    fig = px.bar(data,
                 x = 'Category',
                 y = 'Values',
                 title = "Category Values",
                 labels = {'Category':"Category","Values":"Values"})
    
    # Display the plot in streamlit app
    st.plotly_chart(fig)
elif page == "Data Dashboard":
    st.title("Data Dashboard")
    st.write("Here is where our data visualization and dashboard will go.")

elif page == "About":
    st.title("About us")
    st.write("This is a page where we write about our bussiness or our app.")
