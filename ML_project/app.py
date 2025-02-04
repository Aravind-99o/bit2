import os
import streamlit as st
import pandas as pd
import pickle
import numpy as np

with open('bitcoin.pkl', "rb") as file:
    data = pickle.load(file)

flag=0


  # Local image path
logo_path = "C:/aravind/data_science/ML_project/bitcoin-logo-icon.webp"

  # Read and encode the image to display in HTML
import base64
def get_base64_image(image_path):
      with open(image_path, "rb") as img_file:
          return base64.b64encode(img_file.read()).decode()

logo_base64 = get_base64_image(logo_path)

  # HTML & CSS to align the image with the title
st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: center;">
        <img src="data:image/webp;base64,{logo_base64}" width="100" style="margin-right: 5px;">
        <h1 style="margin: 0;">Bitcoin (BTC) Price</h1>
    </div>
    """,
    unsafe_allow_html=True
)


st.info('This project aims to predict the future price of Bitcoin using machine learning techniques.')






with st.sidebar:
  st.header('Input features')

  Open = st.number_input('Open', value=87371.22)
  High = st.number_input('High', value=96536.95)
  Low = st.number_input('Low', value=84908.25)
  Volume = st.number_input('Volume',value=86288)

  Volume=Volume/1000
  

  if st.button("Predict", type="primary"):
     flag=1




input_data = [[Open,High,Low,Volume]]  
# Create a 2D array with one row 

dat = {
    'Open': [Open],
    'High': [High],
    'Low': [Low],
    'Volume': [Volume]
}

df = pd.DataFrame(dat)

# Format Open, High, and Low columns with $ sign
df['Open'] = df['Open'].map(lambda x: f"$ {x:,.2f}")
df['High'] = df['High'].map(lambda x: f"$ {x:,.2f}")
df['Low'] = df['Low'].map(lambda x: f"$ {x:,.2f}")

# Display DataFrame and fit it to the screen width
st.write("DataFrame with Input Values (formatted with $):")
st.dataframe(df, use_container_width=True)




if flag==1:
  res = data.predict(input_data)  # Pass the formatted data to predict()

  number = res[0]
  rounded_number = round(number, 2)

  old_value = Open
  new_value = rounded_number

  percentage_change = ((new_value - old_value) / old_value) * 100

  






  
  # st.title('  Price Prediction')
 

  st.title(f"{rounded_number} USD")


  diff=round(rounded_number-Open,2)


  if percentage_change < 0:
    logo_path = "C:/aravind/data_science/ML_project/R.png"

    # Read and encode the image to display in HTML
    import base64
    def get_base64_image(image_path):
          with open(image_path, "rb") as img_file:
              return base64.b64encode(img_file.read()).decode()

    logo_base64 = get_base64_image(logo_path)

      # HTML & CSS to align the image with the title
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; justify-content: flex-start;">
            <img src="data:image/webp;base64,{logo_base64}" width="20" style="margin-right: 5px;">
            <h2 style="margin: 0; color: red;">{diff} ({percentage_change  :.2f})%</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


  if percentage_change > 0:
    logo_path = "C:/aravind/data_science/ML_project/R.jpg"

    # Read and encode the image to display in HTML
    import base64
    def get_base64_image(image_path):
          with open(image_path, "rb") as img_file:
              return base64.b64encode(img_file.read()).decode()

    logo_base64 = get_base64_image(logo_path)

      # HTML & CSS to align the image with the title
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; justify-content: flex-start;">
            <img src="data:image/webp;base64,{logo_base64}" width="20" style="margin-right: 5px;">
            <h2 style="margin: 0; color: #00ff00;">{diff} ({percentage_change  :.2f})%</h2>
        </div>
        """,
        unsafe_allow_html=True
    )




  import pandas as pd
  import plotly.graph_objects as go
  import streamlit as st

  # Load the dataset
  file_path = "Bitcoin Historical Data.csv"  # Update with your file path
  df = pd.read_csv(file_path)

  # Convert Date column to datetime format and sort data
  df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
  df = df.sort_values(by='Date')

  # Convert price-related columns to numeric values
  cols_to_convert = ['Price', 'Open', 'High', 'Low']
  df[cols_to_convert] = df[cols_to_convert].replace(',', '', regex=True).astype(float)

  # Create a candlestick chart
  fig = go.Figure(data=[go.Candlestick(
      x=df['Date'],
      open=df['Open'],
      high=df['High'],
      low=df['Low'],
      close=df['Price'],
      name="Bitcoin"
  )])

  # Update layout
  fig.update_layout(
      title="Bitcoin Price Candlestick Chart",
      xaxis_title="Date",
      yaxis_title="Price (USD)",
      xaxis_rangeslider_visible=False,
      template="plotly_dark",
      width=1000,
      height=600
  )

  # Show the chart within Streamlit (on the same page)
  st.plotly_chart(fig)
