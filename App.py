import streamlit as st 
import pandas as pd
import numpy as np

# Title of the application
st.title("Hello, Myself Aadarsh")

# Display a Simple text
st.write("This is a Simple text")

# Create a simple Dataframe
df = pd.DataFrame({
    "first column" : [1,2,3,4],
    "second column" : [5,6,7,8]
})

# Display the DataFrame
st.write("Here is the Dataframe")
st.write(df)

# Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns = ["a","b","c"]
)
st.line_chart(chart_data)