# Import the Streamlit library
import streamlit as st

# Title of the dashboard
st.title('User analytics in Telecommunication industry ')

# Add some text or headers
st.header('This is a header')
st.write("Welcome to my Streamlit Dashboard!")

# Add some interactive widgets
number = st.number_input('Enter a number')

# Display the number squared
squared_number = number ** 2
st.write(f"The square of {number} is {squared_number}")

# Adding a chart to the dashboard
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample data
data = np.random.randn(100, 2)
df = pd.DataFrame(data, columns=['A', 'B'])

# Create a scatter plot
st.subheader('Scatter Plot')
st.write(df)
st.pyplot(plt.scatter(df['A'], df['B']))


import streamlit as st

# Title of the dashboard
st.title('Subscribe to Updates')

# Add a form to collect email
email = st.text_input('Enter your email address', '')

if st.button('Subscribe'):
    if email:
        # Save the email address or perform subscription-related tasks
        st.success(f'You have subscribed with email: {email}')
    else:
        st.warning('Please enter an email address.')

