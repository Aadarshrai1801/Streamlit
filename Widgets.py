import streamlit as st 
import pandas as pd

st.title("Streamlit Text Input")

# Input box
name = st.text_input("Enter your name: ")
if name :
    st.write(f"Hello, {name}")

# Slider    
age = st.slider("Select your age: ", 0,100,25)
st.write(f"Your age is {age}")

# Option : Dropbox
options = ["C", "C++", "Java", "Python"]
choice = st.selectbox("Choose your favorite language: ", options=options)
st.write(f"Your favorite language is {choice}")

# Dataframe usage
data = {
    "Name" : ["John", "Alex", "Sid", "Andrew"],
    "Age" : [23,45,65,23],
    "City" : ["New York", "Delhi", "Chicago", "Canada"]
}

df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type = "csv")
if uploaded_file is not None :
    df = pd.read_csv(uploaded_file)
    st.write(df)