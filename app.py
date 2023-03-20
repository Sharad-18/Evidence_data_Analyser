import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
# import data
st.title('Evidence Analysis')
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load the data into a pandas DataFrame
df = pd.read_json('data/newdata.json')

data = pd.DataFrame(df)
print(data)

# Convert the 'date' column to a datetime format
data['date'] = pd.to_datetime(data['date'])

# Add new columns for month, year, and day
data['day'] = data['date'].dt.day
data['month'] = data['date'].dt.month
data['year'] = data['date'].dt.year

# Choose a grouping level
grouping = st.selectbox('Choose a grouping level', ['Day', 'Month', 'Year'])
grouping1 = st.selectbox('Choose a file type', ['image', 'video', 'pdf', 'doc'])

# Filter the data based on the selected file type/category
df = data[data['name'] == grouping1]


if grouping == 'Day':
    # Choose a specific day to analyze
    selected_day=st.date_input('Select a date', value=date(2023, 3, 19), min_value=date(2023, 3, 1), max_value=date(2023, 3, 31))

    # Convert the selected day to a string in the same format as the date column in the DataFrame
    selected_day_str = selected_day.strftime('%d/%m/%Y')

    # Filter the data to show only the selected day
    filtered_data = df[df['date'] == selected_day_str]

    if len(filtered_data) == 0:
        st.write('No data found for the selected day')
    else:
        # Plot the data for each file type/category
        grouped_data = filtered_data.groupby('name').sum()['count']
        grouped_data.plot(kind='bar', title='Analysis of ' + grouping1 + ' on ' + str(selected_day))
        plt.xlabel('File Type/Category')
        plt.ylabel('Count')
        st.pyplot()

elif grouping == 'Month':
    # Plot the data for each month
    grouped_data = df.groupby(['name', 'month']).sum()['count'].unstack('name')
    grouped_data.plot(kind='bar', title='Analysis of ' + grouping1 + ' by month')
    plt.xlabel('Month')
    plt.ylabel('Count')
    st.pyplot()



else:
    # Plot the data for each year
    grouped_data = df.groupby(['name', 'year']).sum()['count'].unstack('name')
    grouped_data.plot(kind='bar', title='Analysis of ' + grouping1 + ' by year')
    plt.xlabel('Year')
    plt.ylabel('Count')
    st.pyplot()

st.title('Over All Analysis')

grouping2 = st.selectbox('Choose grouping level', ['Day By Day', 'Month By Month', 'Year By Year'])

if grouping2 == 'Day By Day':
        # Plot the data for each day
    grouped_data = data.groupby(['name', 'day']).sum()['count'].unstack('name')
    grouped_data.plot(kind='bar', title='Analysis day by day')
    
    plt.xlabel('Day')
    plt.ylabel('Count')
    st.pyplot()
elif grouping2 == 'Month By Month':
        # Plot the data for each month
        grouped_data = data.groupby(['name', 'month']).sum()['count'].unstack('name')
        grouped_data.plot(kind='bar', title='Analysis month by month')
        plt.xlabel('Month')
        plt.ylabel('Count')
        st.pyplot()

else:
        # Plot the data for each year
        grouped_data = data.groupby(['name', 'year']).sum()['count'].unstack('name')
        grouped_data.plot(kind='bar', title='Analysis year by year')
        plt.xlabel('Year')
        plt.ylabel('Count')
        st.pyplot()
# hello()
