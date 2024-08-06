#Necessary imports
# from query import *
from threading import Timer
from datetime import datetime
from mysql.connector import Error
from openpyxl import load_workbook
from datetime import datetime 
from streamlit_autorefresh import st_autorefresh
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector
import plotly.express as px
import streamlit as st
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import openpyxl
import altair as alt
import base64

# Set page config
st.set_page_config(page_title="MEPC Energy Trading Dashboard", page_icon="data/logo_only.png", layout="wide")

# Function to load an image and convert it to a base64 string
def get_image_as_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode()
    except FileNotFoundError:
        st.error(f"File not found: {image_path}")
        return None

# Path to your image
image_path = 'data/MORE_Power_Logo.png'

# Set the image's width to the column width
st.image(image_path, use_column_width=True)

# Connection
conn=mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    passwd = "",
    db = "myDb"
)

c = conn.cursor()

def view_all_data():
    c.execute('select * from timeintervals order by id asc')
    data=c.fetchall()
    return data

def view_all_data2():
    c.execute('select * from forecasted_energy order by id asc')
    data=c.fetchall()
    return data

def view_all_data3():
    c.execute('select * from total_bcq_nomination order by id asc')
    data=c.fetchall()
    return data

def view_all_data4():
    c.execute('select * from total_substation_load order by id asc')
    data=c.fetchall()
    return data

def view_all_data5():
    c.execute('select * from contestable_energy order by id asc')
    data=c.fetchall()
    return data

def view_all_data6():
    c.execute('select * from actual_energy order by id asc')
    data = c.fetchall()
    return data

def view_all_data7():
    c.execute('select * from wesm_exposure order by id asc')
    data = c.fetchall()
    return data

def view_all_data8():
    c.execute('select * from more_trading_node order by id asc')
    data = c.fetchall()
    return data

def view_all_data9():
    c.execute('select * from current_rate order by id asc')
    data = c.fetchall()
    return data

def view_all_data10():
    c.execute('select * from temp_data order by id asc')
    data = c.fetchall()
    return data

# -- START OF SO ADVISORIES HEADER --

# Load your Excel file
excel_file = r"C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\SO_ADVISORIES.xlsx"
df = pd.read_excel(excel_file)

# Convert TIME_MESSAGE to datetime format (if it's not already)
df['TIME_MESSAGE'] = pd.to_datetime(df['TIME_MESSAGE'], errors='coerce')

# Drop rows where TIME_MESSAGE couldn't be converted to datetime (if needed)
df = df.dropna(subset=['TIME_MESSAGE'])

# Sort dataframe by TIME_MESSAGE in descending order
df = df.sort_values(by='TIME_MESSAGE', ascending=False)

# Function to fetch latest 10 entries
def fetch_latest_10_entries():
    latest_10_entries = df.head(10)
    return latest_10_entries

# Prepare the initial data for scrolling
scrollable_content = []
latest_10_entries = fetch_latest_10_entries()
for index, row in latest_10_entries.iterrows():
    time_message = row['TIME_MESSAGE'].strftime('%Y/%m/%d %H:%M:%S')
    message = row['MESSAGE']
    entry_text = f"{time_message}: {message}"
    scrollable_content.append(entry_text)       

# -- END OF SO ADVISORIES HEADER --

# -- START OF MO ADVISORIES HEADER --
# Load your Excel file
excel_file = r"C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\MO_ADVISORIES.xlsx"
df = pd.read_excel(excel_file)

# Sort dataframe by TIMESTAMP in descending order
df = df.sort_values(by='TIMESTAMP', ascending=False)

# Function to fetch latest 10 entries
def fetch_latest_entry():
    latest_entry = df.head(1)
    return latest_entry

# Prepare the initial data for scrolling
scrollable_content_2 = []
latest_entry = fetch_latest_entry()
for index, row in latest_entry.iterrows():
    time_message_2 = row['TIMESTAMP']
    message_2 = row['ADVISORY']
    entry_text_2 = f"{time_message_2} - {message_2}"
    scrollable_content_2.append(entry_text_2)

# HTML and CSS for the tickers
html_code = f"""
<style>
* {{
  box-sizing: border-box;
}}
@-webkit-keyframes ticker {{
  0% {{
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    visibility: visible;
  }}
  100% {{
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
  }}
}}
@keyframes ticker {{
  0% {{
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    visibility: visible;
  }}
  100% {{
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
  }}
}}
.ticker-wrap {{
  position: fixed;
  bottom: 2.5rem;  /* Adjusted to make space between tickers */
  width: 100%;
  overflow: hidden;
  height: 2.5rem;
  background-color: #000000; 
  padding-left: 100%;
  box-sizing: content-box;
}}
.ticker {{
  display: inline-block;
  height: 2.5rem;
  line-height: 2.5rem;  
  white-space: nowrap;
  padding-right: 100%;
  box-sizing: content-box;
  -webkit-animation-iteration-count: infinite; 
  animation-iteration-count: infinite;
  -webkit-animation-timing-function: linear;
  animation-timing-function: linear;
  -webkit-animation-name: ticker;
  animation-name: ticker;
  -webkit-animation-duration: 180s;
  animation-duration: 180s;
}}
.ticker__item {{
  display: inline-block;
  padding: 0 0.5rem;
  font-size: 1rem;
  font-family: Helvetica;
  font-weight: bold;
  color: #FFFFFF;   
}}
body {{ margin: 0; padding-bottom: 5rem; }}
h1, h2, p {{ padding: 0 5%; }}
</style>
<div class="ticker-wrap">
  <div class="ticker">
"""

for entry in scrollable_content:
    html_code += f'<div class="ticker__item">{entry}</div>'

html_code += """
  </div>
</div>
<div class="ticker-wrap" style="bottom: 0;">
  <div class="ticker">
"""

for entry in scrollable_content_2:
    html_code += f'<div class="ticker__item">{entry}</div>'

html_code += """
  </div>
</div>
"""

# Display the HTML and CSS in Streamlit
st.components.v1.html(html_code, height=80)

# -- END OF MO ADVISORIES HEADER --

# -- START OF CURRENT INTERVAL SUMMARY --

def current_interval_summary():

    # Fetch Data
    result = view_all_data()
    result2 = view_all_data2()
    result3 = view_all_data3()
    result4 = view_all_data4()
    result5 = view_all_data5()
    result6 = view_all_data6()
    result7 = view_all_data7()
    result8 = view_all_data8()
    result9 = view_all_data9()
    result10 = view_all_data10()

    df = pd.DataFrame(result,columns=["id", "time_interval", "timestamp"])
    df2 = pd.DataFrame(result2, columns=["id", "net", "insert_time"])
    df3 = pd.DataFrame(result3, columns=["id", "total_bcq", "insert_time"])
    df4 = pd.DataFrame(result4, columns=["id", "substation_load", "insert_time"])
    df5 = pd.DataFrame(result5, columns=["id", "cc", "insert_time"])
    df6 = pd.DataFrame(result6, columns=["id", "actual_energy", "insert_time"])
    df7 = pd.DataFrame(result7, columns=["id", "wesm_exposure", "insert_time"])
    df8 = pd.DataFrame(result8, columns=["id", "final_total", "insert_time"])
    df9 = pd.DataFrame(result9, columns=["id", "rate", "insert_time"])
    df10 = pd.DataFrame(result10, columns=["id", "temp", "weather", "insert_time"])

    last_interval= df['time_interval'].iloc[-1]
    forecasted_energy = df2['net'].iloc[-1]
    total_bcq = df3['total_bcq'].iloc[-1]
    total_substation_load = df4['substation_load'].iloc[-1]
    contestable_energy = df5['cc'].iloc[-1]
    actual_energy= df6['actual_energy'].iloc[-1]
    wesm_exposure = df7['wesm_exposure'].iloc[-1]
    final_total = df8['final_total'].iloc[-1]
    current_rate = df9['rate'].iloc[-1]
    temperature = df10['temp'].iloc[-1]
    weather_condition = df10['weather'].iloc[-1]

    # # Datetime
    # st.markdown("""
    # <div style="background-color: #FFEB3B; padding: 10px; border-radius: 5px;">
    #     <h2 style="color: black;">Current Date 📅</h2>
    #     <p style="font-size: 18px;">{}</p>
    # </div>
    # """.format(datetime.now().strftime("%Y-%m-%d")), unsafe_allow_html=True)

    # # Current Interval
    # st.markdown("""
    # <div style="background-color: #9C27B0; padding: 10px; border-radius: 5px;">
    #     <h2 style="color: white;">Current Interval ⏱</h2>
    #     <p style="font-size: 18px;">{}</p>
    # </div>
    # """.format(last_interval), unsafe_allow_html=True)

    # # Temperature and Weather Condition
    # st.markdown("""
    # <div style="background-color: #B3E5FC; padding: 10px; border-radius: 5px;">
    #     <h2 style="color: black;">Temperature and Weather Condition 🌤️</h2>
    #     <p style="font-size: 18px;">Temperature: {}°C</p>
    #     <p style="font-size: 18px;">Weather Condition: {}</p>
    # </div>
    # """.format(temperature, weather_condition), unsafe_allow_html=True)

    # # Total Substation Load
    # st.markdown("""
    # <div style="background-color: #FFEB3B; padding: 10px; border-radius: 5px;">
    #     <h2 style="color: black;">Total Substation Load (kW) 🏭</h2>
    #     <p style="font-size: 18px;">{}</p>
    # </div>
    # """.format(total_substation_load), unsafe_allow_html=True)

    # # Actual Energy and Forecasted Energy
    # st.markdown("""
    # <div style="background-color: #9C27B0; padding: 10px; border-radius: 5px;">
    #     <h2 style="color: white;">Actual Energy (kWh) vs Forecasted Energy (kWh) ⚡</h2>
    #     <p style="font-size: 18px;">Actual Energy: {}</p>
    #     <p style="font-size: 18px;">Forecasted Energy: {}</p>
    # </div>
    # """.format(actual_energy, forecasted_energy), unsafe_allow_html=True)

    # # WESM Exposure and Contestable Energy
    # st.markdown("""
    # <div style="background-color: #B3E5FC; padding: 10px; border-radius: 5px;">
    #     <h2 style="color: black;">WESM Exposure (kWh) and Contestable Energy (kWh) ⚡</h2>
    #     <p style="font-size: 18px;">WESM Exposure: {}</p>
    #     <p style="font-size: 18px;">Contestable Energy: {}</p>
    # </div>
    # """.format(wesm_exposure, contestable_energy), unsafe_allow_html=True)

    # # Total BCQ Nomination
    # st.markdown("""
    # <div style="background-color: #FFEB3B; padding: 10px; border-radius: 5px;">
    #     <h2 style="color: black;">Total BCQ Nomination (kW)</h2>
    #     <p style="font-size: 18px;">{}</p>
    # </div>
    # """.format(total_bcq), unsafe_allow_html=True)

    # # MORE Trading Node
    # st.markdown("""
    # <div style="background-color: #9C27B0; padding: 10px; border-radius: 5px;">
    #     <h2 style="color: white;">MORE Trading Node (PhP/kWh)</h2>
    #     <p style="font-size: 18px;">{}</p>
    # </div>
    # """.format(final_total), unsafe_allow_html=True)

    # # PEDC Trading Node
    # st.markdown("""
    # <div style="background-color: #B3E5FC; padding: 10px; border-radius: 5px;">
    #     <h2 style="color: black;">PEDC Trading Node (PhP/kWh)</h2>
    #     <p style="font-size: 18px;">On Probation</p>
    # </div>
    # """, unsafe_allow_html=True)

    # # Current Rate
    # st.markdown("""
    # <div style="background-color: #FFEB3B; padding: 10px; border-radius: 5px;">
    #     <h2 style="color: black;">Current Rate (PhP/kWh) 📉</h2>
    #     <p style="font-size: 18px;">{}</p>
    # </div>
    # """.format(current_rate), unsafe_allow_html=True)

    # Define the current date
    c = datetime.now()
    formatted_date = c.strftime("%Y-%m-%d")

    # Create columns with small gap
    card1, card2, card3, card4, card5, card6, card7, card8, card9, card10 = st.columns(10, gap='small')

    # Custom CSS for styling
    st.markdown("""
        <style>
        /* Shorter in width */
        .custom-box {
            border: 1px solid #ddd;
            border-radius: 0px;
            padding: 0px;
            margin: 0px;
            background-color: #00B74C;
            height: 150px;
            width: 120%;
        }
        .custom-box h4, .custom-box p {
            display: inline-block;
            margin: 0;
            padding: 0;
        }
        .custom-box-2 h4, .custom-box p {
            display: inline-block;
            margin: 0;
            padding: 0;
        }
        .custom-box h4 {
            font-size: 14px;
            font-family: Helvetica;
            font-weight: normal;
            color: #000000;
        }
        .custom-box-2 h4 {
            font-size: 14px;
            font-family: Helvetica;
            font-weight: normal;
            color: #000000;
        }
        .custom-box p {
            font-size: 20px;
            font-family: Helvetica;
            font-weight: bold;
            color: #000000;
        }
        .custom-box-2 p {
            font-size: 20px;
            font-family: Helvetica;
            font-weight: bold;
            color: #000000;
        }
        </style>
    """, unsafe_allow_html=True)
    
    with card1:
        st.markdown('<div class="custom-box"><h4>Current Date</h4><p>{}</p></div>'.format(formatted_date), unsafe_allow_html=True)

    with card2:
        st.markdown('<div class="custom-box"><h4>Current Interval</h4><p>{}</p></div>'.format(last_interval), unsafe_allow_html=True)

    with card3:
        st.markdown('<div class="custom-box"><h4>Temperature</h4><p>{}°C</p><h4>Weather Condition</h4><p>{}</p></div>'.format(temperature, weather_condition), unsafe_allow_html=True)

    with card4:
        st.markdown('<div class="custom-box"><h4>Total Substation Load (kW)</h4><p>{}</p></div>'.format(total_substation_load), unsafe_allow_html=True)

    with card5:
        st.markdown('<div class="custom-box"><h4>Actual Energy (kWh)</h4><p>{}</p><h4>Contestable Energy (kWh)</h4><p>{}</p></div>'.format(actual_energy, forecasted_energy), unsafe_allow_html=True)

    with card6:
        st.markdown('<div class="custom-box"><h4>WESM Exposure (kWh)</h4><p>{}</p><h4>Contestable Energy (kWh)</h4><p>{}</p></div>'.format(wesm_exposure, contestable_energy), unsafe_allow_html=True)

    with card7:
        st.markdown('<div class="custom-box"><h4>Total BCQ Nomination (kW)</h4><p>{}</p></div>'.format(total_bcq), unsafe_allow_html=True)

    with card8:
        st.markdown('<div class="custom-box"><h4>MORE Trading Node (PhP/kWh)</h4><p>{}</p></div>'.format(final_total), unsafe_allow_html=True)

    with card9:
        st.markdown('<div class="custom-box"><h4>PEDC Trading Node (PhP/kWh)</h4><p>On Probation</p></div>', unsafe_allow_html=True)

    with card10:
        st.markdown('<div class="custom-box"><h4>Current Rate (PhP/kWh)</h4><p>{}</p></div>'.format(current_rate), unsafe_allow_html=True)


    # card1, card2, card3, card4, card5, card6, card7, card8, card9, card10 = st.columns(10, gap='small')
    
    # with card1:
    #     st.info('Current Date', icon="📅")
    #     c = datetime.now()
    #     formatted_date = c.strftime("%Y-%m-%d")
    #     st.metric(label="", value = formatted_date)
    
    # with card2:
    #     st.info('Current Interval', icon="⏱")
    #     st.metric(label='', value = last_interval)

    # with card3:
    #     st.info('Temperature and Weather Condition', icon="🌤️")
    #     st.metric(label = 'Temperature', value=f"{temperature}°C")
    #     st.metric(label = 'Weather Condition', value = weather_condition)

    # with card4:
    #     st.info('Total Substation Load (kW)',icon="🏭")
    #     st.metric(label='', value = total_substation_load)

    # with card5:
    #     st.info('Actual Energy (kWh) vs Forecasted Energy (kWh)',icon = "⚡")
    #     st.metric(label = 'Actual Energy', value = actual_energy)
    #     st.metric(label = 'Forecasted Energy', value = forecasted_energy)

    # with card6:
    #     st.info('WESM Exposure (kWh) and Contestable Energy (kWh)', icon = "⚡")
    #     st.metric(label='WESM Exposure (kWh)', value = wesm_exposure)
    #     st.metric(label='Contestable Energy (kWh)', value = contestable_energy)

    # with card7:
    #     st.info('Total BCQ Nomination (kW)')
    #     st.metric(label='', value = total_bcq)

    # with card8:
    #     st.info('MORE Trading Node (PhP/kWh)')
    #     st.metric(label='', value = final_total)

    # with card9:
    #     st.info('PEDC Trading Node (PhP/kWh)')
    #     st.markdown('On Probation')

    # with card10:
    #     st.info('Current Rate (PhP/kWh)', icon = "📉")
    #     st.metric(label='', value = current_rate)

# -- END OF CURRENT INTERVAL SUMMARY --

if __name__ == "__main__":
    current_interval_summary()

# -- START OF DISPLAYING THE BCQ NOMINATIONS PER SUPPLIER AREA CHART --

# Load the workbook and select the active sheet
filepath = r"C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\total_bcq_nomination.xlsx"
wb = openpyxl.load_workbook(filepath)
sheet = wb.active

# Create lists to store the data
hours = []
scpc_values = []
kspc1_values = []
kspc2_values = []
edc_values = []

# Loop through column 'A' to get values for each hour, skip the header
for row in sheet.iter_rows(min_row=2, max_row=25, min_col=1, max_col=4):
    hour = int(row[0].value)
    scpc = int(row[1].value)
    kspc = int(row[2].value)
    kspc1 = int(kspc/2)
    kspc2 = int(kspc/2)
    edc = int(row[3].value)

    # Store the values in the lists
    hours.append(hour)
    scpc_values.append(scpc)
    kspc1_values.append(kspc1)
    kspc2_values.append(kspc2)
    edc_values.append(edc)

# Create a DataFrame with proper structure
data = {
    'Hour': hours,
    'SCPC': scpc_values,
    'KSPC1': kspc1_values,
    'KSPC2': kspc2_values,
    'EDC': edc_values
}

df = pd.DataFrame(data)

# Melt the DataFrame for Altair
df_melted = df.melt('Hour', var_name='Supplier', value_name='Value')

# Create an Altair area chart
chart = alt.Chart(df_melted).mark_area().encode(
    x='Hour:O',
    y='Value:Q',
    color='Supplier:N'
).properties(
    width=600,  
    height=300
)

# -- END OF DISPLAYING THE BCQ NOMINATIONS PER SUPPLIER AREA CHART --

# -- START OF DISPLAYING THE ACTUAL VS FORECASTED ENERGY CHART --
# Lapaz, Molo, Mandurriao, Jaro, Megaworld, Diversion, Mobile SS 1, Mobile SS 2, BCQ Nomination, Forecasted Energy
# Lapaz, Molo, Mandurriao, Jaro, Megaworld, Diversion, Mobile SS 1, Mobile SS 2 - station_load_graph.xlsx
# BCQ Nomination - total_bcq_nomination.xlsx
# Forecasted Energy - forecasted_energy.xlsx

station_load_destination_path = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\station_load_graph.xlsx'
bcq_nomination_destination_path = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\total_bcq_nomination.xlsx'
forecasted_energy_destination_path = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\forecasted_energy.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(station_load_destination_path)

def safe_get(df, row, column):
    try:
        return df.at[row, column]
    except KeyError:
        return 0

# Initialize a dictionary to store the results
data = {'Hour': list(range(1, 25))}

# List of stations
stations = ['Lapaz', 'Jaro', 'Mandurriao', 'Molo', 'Diversion', 'Mobile SS 1', 'Mobile SS 2', 'Megaworld']

# Loop through each station and add their hourly values to the dictionary
for station in stations:
    data[station] = [safe_get(df, hour - 1, station) for hour in data['Hour']]

# Calculate total values for each hour
data['Total'] = [sum(data[station][hour - 1] for station in stations) for hour in data['Hour']]

# Convert the dictionary to a DataFrame
result_df = pd.DataFrame(data)

# Create a Figure object for the plot
fig = go.Figure()

# Add the first station as a bar trace
fig.add_trace(go.Bar(
    x=result_df['Hour'],      # Set the x-axis values to the hours
    y=result_df['Lapaz'],  # Set the y-axis values to the first station values
    name='Lapaz'    # Name of the first station
))

# Add the second station as a bar trace
fig.add_trace(go.Bar(
    x=result_df['Hour'],      # Set the x-axis values to the hours
    y=result_df['Jaro'],  # Set the y-axis values to the second station values
    name='Jaro'    # Name of the second station
))

# Add the second station as a bar trace
fig.add_trace(go.Bar(
    x=result_df['Hour'],      # Set the x-axis values to the hours
    y=result_df['Mandurriao'],  # Set the y-axis values to the second station values
    name='Mandurriao'    # Name of the second station
))

# Add the second station as a bar trace
fig.add_trace(go.Bar(
    x=result_df['Hour'],      # Set the x-axis values to the hours
    y=result_df['Molo'],  # Set the y-axis values to the second station values
    name='Molo'    # Name of the second station
))

# Add the second station as a bar trace
fig.add_trace(go.Bar(
    x=result_df['Hour'],      # Set the x-axis values to the hours
    y=result_df['Diversion'],  # Set the y-axis values to the second station values
    name='Diversion'    # Name of the second station
))

# Add the second station as a bar trace
fig.add_trace(go.Bar(
    x=result_df['Hour'],      # Set the x-axis values to the hours
    y=result_df['Mobile SS 1'],  # Set the y-axis values to the second station values
    name='Mobile SS 1'    # Name of the second station
))

# Add the second station as a bar trace
fig.add_trace(go.Bar(
    x=result_df['Hour'],      # Set the x-axis values to the hours
    y=result_df['Mobile SS 2'],  # Set the y-axis values to the second station values
    name='Mobile SS 2'    # Name of the second station
))

# Add the second station as a bar trace
fig.add_trace(go.Bar(
    x=result_df['Hour'],      # Set the x-axis values to the hours
    y=result_df['Megaworld'],  # Set the y-axis values to the second station values
    name='Megaworld'    # Name of the second station
))

df_2 = pd.read_excel(forecasted_energy_destination_path)

# Add the total as a scatter trace with a straight line
fig.add_trace(go.Scatter(
    x=df_2['HOUR'],      # Set the x-axis values to the hours
    y=df_2['NET'],     # Set the y-axis values to the total values
    mode='lines',      # Set the mode to lines
    name='Forecasted Energy'       
))

df_3 = pd.read_excel(bcq_nomination_destination_path)

# Add a crooked line for demonstration
fig.add_trace(go.Scatter(
    x=df_3['HOUR'],      # Set the x-axis values to the hours
    y=df_3['TOTAL_BCQ'],# Example values for the crooked line
    mode='lines+markers', # Set the mode to lines and markers
    name='BCQ Nomination',
    line=dict(color='white')
))

# Update the layout to set the bar mode to stacked and add a title
fig.update_layout(barmode='stack', height=300, width=600)

# -- END OF DISPLAYING THE ACTUAL VS FORECASTED ENERGY CHART --

# -- START OF DISPLAYING THE SUBSTATION LOAD (KW) BAR CHART -- 

def load_data_from_excel():
    # station_load_graph.xlsx
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet['A1'] = 'Hour'
    sheet['B1'] = 'Lapaz'
    sheet['C1'] = 'Jaro'
    sheet['D1'] = 'Mandurriao'
    sheet['E1'] = 'Molo'
    sheet['F1'] = 'Diversion'
    sheet['G1'] = 'Mobile SS 1'
    sheet['H1'] = 'Mobile SS 2'
    sheet['I1'] = 'Megaworld'
    workbook.save('station_load_graph.xlsx')
    workbook.close()
    print("Excel file 'station_load_graph.xlsx' created successfully.")

    # File path for destination Excel file
    destination_file_path_slg = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\station_load_graph.xlsx'
    source_file_path_slg = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\station_load.xlsx'

    # Load source workbook
    source_wb_slg = load_workbook(source_file_path_slg)  
    # Sheet name of the source workbook
    source_sheet_slg = source_wb_slg['Sheet1']

    # Load destination workbook
    dest_wb_slg = load_workbook(destination_file_path_slg)

    # Sheet name of the destination workbook
    dest_sheet_slg = dest_wb_slg['Sheet']

    # Define source and destination ranges
    source_ranges_slg = [('B2', 'B25'), ('C2', 'C25'), ('D2', 'D25'), ('E2', 'E25'), ('F2', 'F25'), ('G2', 'G25'), ('H2', 'H25'), ('I2', 'I25'), ('J2', 'J25')]
    dest_ranges_slg = [('A2', 'A25'), ('B2', 'B25'), ('C2', 'C25'), ('D2', 'D25'), ('E2', 'E25'), ('F2', 'F25'), ('G2', 'G25'), ('H2', 'H25'), ('I2', 'I25')]

    # Function to copy values from source range to destination range
    def copy_values_slg(source_sheet_slg, dest_sheet_slg, source_range_slg, dest_range_slg):
        source_start_slg, source_end_slg = source_range_slg
        dest_start_slg, dest_end_slg = dest_range_slg

        # Copy values from source to destination
        source_values_slg = []
        for row in source_sheet_slg[source_start_slg:source_end_slg]:
            for cell in row:
                source_values_slg.append(cell.value)
        
        dest_index_slg = 0
        for row_slg in dest_sheet_slg[dest_start_slg:dest_end_slg]:
            for cell_slg in row_slg:
                if dest_index_slg < len(source_values_slg):
                    cell_slg.value = source_values_slg[dest_index_slg]
                    dest_index_slg += 1
                else:
                    break
    
    # Copy data from source to destination based on specified ranges
    for i in range(len(source_ranges_slg)):
        copy_values_slg(source_sheet_slg, dest_sheet_slg, source_ranges_slg[i], dest_ranges_slg[i])
    
    # Save the destination workbook
    dest_wb_slg.save(destination_file_path_slg)

    # Read the Excel file into a Pandas Dataframe
    file_path = r"C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\station_load_graph.xlsx"
    df = pd.read_excel(file_path)

    # Connect to the MySQL Database
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='myDb',
            user='root',
            password=''
        )

        if connection.is_connected():
            print("Successfully connected to the database")
            cursor = connection.cursor()

            # Create a table
            table_name = 'station_load_graph'
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                Hour INT(11) NOT NULL,
                Lapaz INT(11) NOT NULL,
                Jaro INT(11) NOT NULL,
                Mandurriao INT(11) NOT NULL,
                Molo INT(11) NOT NULL,
                Diversion INT(11) NOT NULL,
                `Mobile SS 1` INT(11) NOT NULL,
                `Mobile SS 2` INT(11) NOT NULL,
                Megaworld INT(11) NOT NULL
            )
            """

            cursor.execute(create_table_query)
            print("Table created successfully or table already exists")

            # Insert data from dataframe into the MySQL table
            for i, row in df.iterrows():
                sql = f"INSERT INTO {table_name} (Hour, Lapaz, Jaro, Mandurriao, Molo, Diversion, `Mobile SS 1`, `Mobile SS 2`, Megaworld) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, tuple(row))
                print(f"Inserted row {i + 1}")

            # Commit the transaction
            connection.commit()
            print("Data committed to the database")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

    # Read the Excel file
    file_path = r"C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\station_load_graph.xlsx"
    df = pd.read_excel(file_path, sheet_name='Sheet')
    return df

# Load data
df_excel = load_data_from_excel()

# Get the current hour
now = datetime.now()
now_hour = now.hour

# Find the row where the hour matches the current hour
matching_row = df_excel[df_excel['Hour'] == now_hour]

hour_value = matching_row.iloc[0]['Hour']
lapaz_value = matching_row.iloc[0]['Lapaz']
jaro_value = matching_row.iloc[0]['Jaro']
mandurriao_value = matching_row.iloc[0]['Mandurriao']
molo_value = matching_row.iloc[0]['Molo']
diversion_value = matching_row.iloc[0]['Diversion']
mobile_ss1_value = matching_row.iloc[0]['Mobile SS 1']
mobile_ss2_value = matching_row.iloc[0]['Mobile SS 2']
megaworld_value = matching_row.iloc[0]['Megaworld']

# Prepare data for the bar chart
chart_data = pd.DataFrame({
    'Substation': ['Lapaz', 'Jaro', 'Mandurriao', 'Molo', 'Diversion', 'Mobile SS 1', 'Mobile SS 2', 'Megaworld'],
    'kW': [lapaz_value, jaro_value, mandurriao_value, molo_value, diversion_value, mobile_ss1_value, mobile_ss2_value, megaworld_value]
})

# Create the bar chart with Plotly
fig_ss_load = px.bar(chart_data, x='Substation', y='kW', text='kW')

# Customize the bar colors
colors = ['#e74c3c', '#e67e22', '#239b56', '#2874a6', '#5dade2', '#a569bd', '#FF69B4', '#48c9b0'] # COLORS: Red, Orange, Green, Dark Blue, Light Blue, Purple, Pink, Turquoise
fig_ss_load.update_traces(marker_color=colors)

# Customize the layout
fig_ss_load.update_traces(texttemplate='%{text:.2s}', textposition='outside')

fig_ss_load.update_layout(
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    width=600,  # Set the width of the bar chart
    height=300  # Set the height of the bar chart
)

# -- END OF DISPLAYING THE SUBSTATION LOAD (KW) BAR CHART -- 

col1, col2 = st.columns(2)
with col1:
    st.subheader("Substation Load (kW)", divider=True)
    st.plotly_chart(fig_ss_load)
with col2:
    st.subheader("Actual vs Forecasted Energy (kWh)", divider=True)
    st.plotly_chart(fig)

# -- START OF TRADING INTERVAL PRICE CALCULATION LINE CHART --

from datetime import datetime
import os
import pandas as pd
import streamlit as st

# Calculates the average of every 12 values in a list and stores them
def average_every_12(data):
    averages = []
    for i in range(0, len(data), 12):
        window = data[i:i+12]
        if window:
            averages.append(sum(window)/len(window))
    # Returns a list containing the averages for each 12-element window
    return averages

directory = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\MORE Trading Node'
now = datetime.now()
date_today = now.strftime("%Y%m%d")
contents = os.listdir(directory)
for item in contents:
    if item == date_today:
        folder_path = os.path.join(directory, item) 
        if os.path.isdir(folder_path):
            files_in_folder = os.listdir(folder_path) # MPI_LMP_DIPC_202407110000, etc.
            
            last_known_value = None

            list_botoca_g01 = []
            list_calaca_g01 = []
            list_calaca_g02 = []
            list_kal_g01 = []
            list_kal_g02 = []
            list_kal_g03 = []
            list_kal_g04 = []
            list_leyte_a = []
            list_kspc_g01 = []
            list_kspc_g02 = []
            list_bantap_l01 = []
            list_pedc_t1l1 = []
            list_pedc_t1l2 = []
            list_stbar_t1l1 = []

            results_botoca_g01 = []
            results_calaca_g01 = []
            results_calaca_g02 = []
            results_kal_g01 = []
            results_kal_g02 = []
            results_kal_g03 = []
            results_kal_g04 = []
            results_leyte_a = []
            results_kspc_g01 = []
            results_kspc_g02 = []
            results_bantap_l01 = []
            results_pedc_t1l1 = []
            results_pedc_t1l2 = []
            results_stbar_t1l1 = []
            
            # 03BOTOCA_G01
            for i in range(1, len(files_in_folder)):
                
                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_botoca_g01.append(last_known_value)
                    continue
                except IndexError:
                    break
                    
                try: 
                    search_value = '03BOTOCA_G01'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:

                        file_03BOTOCA_G01 = matching_row['DIPC_PRICE'].values[0]
                        list_botoca_g01.append(file_03BOTOCA_G01)
                        last_known_value = file_03BOTOCA_G01
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_botoca_g01.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_botoca_g01.append(last_known_value)
                    continue
                    
            # 03CALACA_G01
            for i in range(1, len(files_in_folder)):

                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_botoca_g01.append(last_known_value)
                    continue
                except IndexError:
                    break
                try: 
                    search_value = '03CALACA_G01'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:

                        file_03CALACA_G01 = matching_row['DIPC_PRICE'].values[0]
                        list_calaca_g01.append(file_03CALACA_G01)
                        last_known_value = file_03CALACA_G01
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_calaca_g01.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_calaca_g01.append(last_known_value)
                    continue
                  
            # 03CALACA_G02
            for i in range(1, len(files_in_folder)):
                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_calaca_g02.append(last_known_value)
                    continue
                except IndexError:
                    break
                try: 
                    search_value = '03CALACA_G02'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:
                        file_03CALACA_G02 = matching_row['DIPC_PRICE'].values[0]
                        list_calaca_g02.append(file_03CALACA_G02)
                        last_known_value = file_03CALACA_G02
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_calaca_g02.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_calaca_g02.append(last_known_value)
                    continue
            
            # 03KAL_G01
            for i in range(1, len(files_in_folder)):
                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_kal_g01.append(last_known_value)
                    continue
                except IndexError:
                    break
                try: 
                    search_value = '03KAL_G01'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:
                        file_03KAL_G01 = matching_row['DIPC_PRICE'].values[0]
                        list_kal_g01.append(file_03KAL_G01)
                        last_known_value = file_03KAL_G01
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_kal_g01.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_kal_g01.append(last_known_value)
                    continue
            
            # 03KAL_G02
            for i in range(1, len(files_in_folder)):
                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_kal_g02.append(last_known_value)
                    continue
                except IndexError:
                    break
                try: 
                    search_value = '03KAL_G02'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:
                        file_03KAL_G02 = matching_row['DIPC_PRICE'].values[0]
                        list_kal_g02.append(file_03KAL_G02)
                        last_known_value = file_03KAL_G02
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_kal_g02.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_kal_g02.append(last_known_value)
                    continue
            
            # 03KAL_G03
            for i in range(1, len(files_in_folder)):
                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_kal_g03.append(last_known_value)
                    continue
                except IndexError:
                    break
                try: 
                    search_value = '03KAL_G03'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:
                        file_03KAL_G03 = matching_row['DIPC_PRICE'].values[0]
                        list_kal_g03.append(file_03KAL_G03)
                        last_known_value = file_03KAL_G03
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_kal_g03.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_kal_g03.append(last_known_value)
                    continue
            
            # 03KAL_G04
            for i in range(1, len(files_in_folder)):
                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_kal_g04.append(last_known_value)
                    continue
                except IndexError:
                    break
                try: 
                    search_value = '03KAL_G04'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:
                        file_03KAL_G04 = matching_row['DIPC_PRICE'].values[0]
                        list_kal_g04.append(file_03KAL_G04)
                        last_known_value = file_03KAL_G04
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_kal_g04.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_kal_g04.append(last_known_value)
                    continue
            
            # 04LEYTE_A
            for i in range(1, len(files_in_folder)):
                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_leyte_a.append(last_known_value)
                    continue
                except IndexError:
                    break
                try: 
                    search_value = '04LEYTE_A'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:
                        file_04LEYTE_A = matching_row['DIPC_PRICE'].values[0]
                        list_leyte_a.append(file_04LEYTE_A)
                        last_known_value = file_04LEYTE_A
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_leyte_a.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_leyte_a.append(last_known_value)
                    continue
            
            # 05KSPC_G01
            for i in range(1, len(files_in_folder)):
                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_kspc_g01.append(last_known_value)
                    continue
                except IndexError:
                    break
                try: 
                    search_value = '05KSPC_G01'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:
                        file_05KSPC_G01 = matching_row['DIPC_PRICE'].values[0]
                        list_kspc_g01.append(file_05KSPC_G01)
                        last_known_value = file_05KSPC_G01
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_kspc_g01.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_kspc_g01.append(last_known_value)
                    continue
            
            # 05KSPC_G02
            for i in range(1, len(files_in_folder)):
                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_kspc_g02.append(last_known_value)
                    continue
                except IndexError:
                    break
                try: 
                    search_value = '05KSPC_G02'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:
                        file_05KSPC_G02 = matching_row['DIPC_PRICE'].values[0]
                        list_kspc_g02.append(file_05KSPC_G02)
                        last_known_value = file_05KSPC_G02
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_kspc_g02.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_kspc_g02.append(last_known_value)
                    continue
            
            # 08BANTAP_L01
            for i in range(1, len(files_in_folder)):
                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_bantap_l01.append(last_known_value)
                    continue
                except IndexError:
                    break
                try: 
                    search_value = '08BANTAP_L01'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:
                        file_08BANTAP_L01 = matching_row['DIPC_PRICE'].values[0]
                        list_bantap_l01.append(file_08BANTAP_L01)
                        last_known_value = file_08BANTAP_L01
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_bantap_l01.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_bantap_l01.append(last_known_value)
                    continue

            # 08PEDC_T1L1
            for i in range(1, len(files_in_folder)):
                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_pedc_t1l1.append(last_known_value)
                    continue
                except IndexError:
                    break
                try: 
                    search_value = '08PEDC_T1L1'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:
                        file_08PEDC_T1L1 = matching_row['DIPC_PRICE'].values[0]
                        list_pedc_t1l1.append(file_08PEDC_T1L1)
                        last_known_value = file_08PEDC_T1L1
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_pedc_t1l1.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_pedc_t1l1.append(last_known_value)
                    continue

            # 08PEDC_T1L2
            for i in range(1, len(files_in_folder)):
                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_pedc_t1l1.append(last_known_value)
                    continue
                except IndexError:
                    break
                try: 
                    search_value = '08PEDC_T1L2'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:
                        file_08PEDC_T1L2 = matching_row['DIPC_PRICE'].values[0]
                        list_pedc_t1l2.append(file_08PEDC_T1L2)
                        last_known_value = file_08PEDC_T1L2
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_pedc_t1l2.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_pedc_t1l2.append(last_known_value)
                    continue
            
            # 08STBAR_T1L1
            for i in range(1, len(files_in_folder)):
                filepath = os.path.join(folder_path, files_in_folder[i]) 

                try: 
                    df = pd.read_csv(filepath)
                except pd.errors.EmptyDataError:
                    if last_known_value is not None:
                        list_stbar_t1l1.append(last_known_value)
                    continue
                except IndexError:
                    break
                try: 
                    search_value = '08STBAR_T1L1'
                    matching_row = df[df['RESOURCE_NAME'] == search_value]
                    if not matching_row.empty:
                        file_08STBAR_T1L1 = matching_row['DIPC_PRICE'].values[0]
                        list_stbar_t1l1.append(file_08STBAR_T1L1)
                        last_known_value = file_08STBAR_T1L1
                    else:
                        # If no matching row is found, use the last known value
                        if last_known_value is not None:
                            list_stbar_t1l1.append(last_known_value)
                except KeyError:
                    # If RESOURCE_NAME column is missing, use the last known value
                    if last_known_value is not None:
                        list_stbar_t1l1.append(last_known_value)
                    continue

            filepath_0 = os.path.join(folder_path, files_in_folder[0]) 
            try:
                df_0 = pd.read_csv(filepath_0)
            except IndexError:
                break
            
            search_value_0 = '03BOTOCA_G01'
            matching_row_0 = df_0[df_0['RESOURCE_NAME'] == search_value_0]
            file_03BOTOCA_G01_0 = matching_row_0['DIPC_PRICE'].values[0]
            list_botoca_g01[-1] = file_03BOTOCA_G01_0

            search_value_1 = '03CALACA_G01'
            matching_row_1 = df_0[df_0['RESOURCE_NAME'] == search_value_1]
            file_03CALACA_G01_0 = matching_row_1['DIPC_PRICE'].values[0]
            list_calaca_g01[-1] = file_03CALACA_G01_0

            search_value_2 = '03CALACA_G02'
            matching_row_2 = df_0[df_0['RESOURCE_NAME'] == search_value_2]
            file_03CALACA_G02_0 = matching_row_2['DIPC_PRICE'].values[0]
            list_calaca_g02[-1] = file_03CALACA_G02_0

            search_value_3 = '03KAL_G01'
            matching_row_3 = df_0[df_0['RESOURCE_NAME'] == search_value_3]
            file_03KAL_G01_0 = matching_row_3['DIPC_PRICE'].values[0]
            list_kal_g01[-1] = file_03KAL_G01_0

            search_value_4 = '03KAL_G02'
            matching_row_4 = df_0[df_0['RESOURCE_NAME'] == search_value_4]
            file_03KAL_G02_0 = matching_row_4['DIPC_PRICE'].values[0]
            list_kal_g02[-1] = file_03KAL_G02_0

            search_value_5 = '03KAL_G03'
            matching_row_5 = df_0[df_0['RESOURCE_NAME'] == search_value_5]
            file_03KAL_G03_0 = matching_row_5['DIPC_PRICE'].values[0]
            list_kal_g03[-1] = file_03KAL_G03_0

            search_value_6 = '03KAL_G04'
            matching_row_6 = df_0[df_0['RESOURCE_NAME'] == search_value_6]
            file_03KAL_G04_0 = matching_row_6['DIPC_PRICE'].values[0]
            list_kal_g04[-1] = file_03KAL_G04_0

            search_value_7 = '04LEYTE_A'
            matching_row_7 = df_0[df_0['RESOURCE_NAME'] == search_value_7]
            file_04LEYTE_A_0 = matching_row_7['DIPC_PRICE'].values[0]
            list_leyte_a[-1] = file_04LEYTE_A_0

            search_value_8 = '05KSPC_G01'
            matching_row_8 = df_0[df_0['RESOURCE_NAME'] == search_value_8]
            file_05KSPC_G01_0 = matching_row_8['DIPC_PRICE'].values[0]
            list_kspc_g01[-1] = file_05KSPC_G01_0

            search_value_9 = '05KSPC_G02'
            matching_row_9 = df_0[df_0['RESOURCE_NAME'] == search_value_9]
            file_05KSPC_G02_0 = matching_row_9['DIPC_PRICE'].values[0]
            list_kspc_g02[-1] = file_05KSPC_G02_0

            search_value_10 = '08BANTAP_L01'
            matching_row_10 = df_0[df_0['RESOURCE_NAME'] == search_value_10]
            file_08BANTAP_L01_0 = matching_row_10['DIPC_PRICE'].values[0]
            list_bantap_l01[-1] = file_08BANTAP_L01_0

            search_value_11 = '08PEDC_T1L1'
            matching_row_11 = df_0[df_0['RESOURCE_NAME'] == search_value_11]
            file_08PEDC_T1L1_0 = matching_row_11['DIPC_PRICE'].values[0]
            list_pedc_t1l1[-1] = file_08PEDC_T1L1_0

            search_value_12 = '08PEDC_T1L2'
            matching_row_12 = df_0[df_0['RESOURCE_NAME'] ==  search_value_12]
            file_08PEDC_T1L2_0 = matching_row_12['DIPC_PRICE'].values[0]
            list_pedc_t1l2[-1] = file_08PEDC_T1L2_0

            search_value_13 = '08STBAR_T1L1'
            matching_row_13 = df_0[df_0['RESOURCE_NAME'] ==  search_value_13]
            file_08STBAR_T1L1_0 = matching_row_13['DIPC_PRICE'].values[0]
            list_stbar_t1l1[-1] = file_08STBAR_T1L1_0

            average_botoca_g01 = average_every_12(list_botoca_g01)
            average_calaca_g01 = average_every_12(list_calaca_g01)
            average_calaca_g02 = average_every_12(list_calaca_g02)
            average_kal_g01 = average_every_12(list_kal_g01)
            average_kal_g02 = average_every_12(list_kal_g02)
            average_kal_g03 = average_every_12(list_kal_g03)
            average_kal_g04 = average_every_12(list_kal_g04)
            average_leyte_a = average_every_12(list_leyte_a)
            average_kspc_g01 = average_every_12(list_kspc_g01)
            average_kspc_g02 = average_every_12(list_kspc_g02)
            average_bantap_l01 = average_every_12(list_bantap_l01)
            average_pedc_t1l1 = average_every_12(list_pedc_t1l1)
            average_pedc_t1l2 = average_every_12(list_pedc_t1l2)
            average_stbar_t1l1 = average_every_12(list_stbar_t1l1)

current_date = datetime.now()

current_time = datetime.now()
hour_value = current_time.strftime("%H")

if hour_value == "01":
    data = {
        "HOUR": ["01"],
        "03BOTOCA_G01": [average_botoca_g01[0]],
        "03CALACA_G01": [average_calaca_g01[0]],
        "03CALACA_G02": [average_calaca_g02[0]],
        "03KAL_G01": [average_kal_g01[0]], 
        "03KAL_G02": [average_kal_g02[0]], 
        "03KAL_G03": [average_kal_g03[0]],
        "03KAL_G04": [average_kal_g04[0]],
        "04LEYTE_A": [average_leyte_a[0]],
        "05KSPC_G01": [average_kspc_g01[0]],
        "05KSPC_G02": [average_kspc_g02[0]], 
        "08BANTAP_L01": [average_bantap_l01[0]],
        "08PEDC_T1L1": [average_pedc_t1l1[0]],
        "08PEDC_T1L2": [average_pedc_t1l2[0]],
        "08STBAR_T1L1": [average_stbar_t1l1[0]]
    }
elif hour_value == "02":
    data = {
        "HOUR": ["01", "02"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1]]
    }
elif hour_value == '03':
    data = {
        "HOUR": ["01", "02", "03"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2]]
    }
elif hour_value == '04':
    data = {
        "HOUR": ["01", "02", "03", "04"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3]]
    }
elif hour_value == '05':
    data = {
        "HOUR": ["01", "02", "03", "04", "05"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4]]
    }
elif hour_value == '06':
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5]]
    }
elif hour_value == '07':
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6]]
    }
elif hour_value == '08':
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7]]
    }
elif hour_value == "09":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8]]
    }
elif hour_value == "10":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9]]
    }
elif hour_value == "11":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10]]
    }
elif hour_value == "12":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10], average_botoca_g01[11]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10], average_calaca_g01[11]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10], average_calaca_g02[11]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10], average_kal_g01[11]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10], average_kal_g02[11]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10], average_kal_g03[11]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10], average_kal_g04[11]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10], average_leyte_a[11]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10], average_kspc_g01[11]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10], average_kspc_g02[11]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10], average_bantap_l01[11]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10], average_pedc_t1l1[11]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10], average_pedc_t1l2[11]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10], average_stbar_t1l1[11]]
    }
elif hour_value == "13":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10], average_botoca_g01[11], average_botoca_g01[12]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10], average_calaca_g01[11], average_calaca_g01[12]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10], average_calaca_g02[11], average_calaca_g02[12]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10], average_kal_g01[11], average_kal_g01[12]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10], average_kal_g02[11], average_kal_g02[12]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10], average_kal_g03[11], average_kal_g03[12]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10], average_kal_g04[11], average_kal_g04[12]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10], average_leyte_a[11], average_leyte_a[12]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10], average_kspc_g01[11], average_kspc_g01[12]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10], average_kspc_g02[11], average_kspc_g02[12]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10], average_bantap_l01[11], average_bantap_l01[12]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10], average_pedc_t1l1[11], average_pedc_t1l1[12]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10], average_pedc_t1l2[11], average_pedc_t1l2[12]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10], average_stbar_t1l1[11], average_stbar_t1l1[12]]
    }
elif hour_value == "14":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10], average_botoca_g01[11], average_botoca_g01[12], average_botoca_g01[13]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10], average_calaca_g01[11], average_calaca_g01[12], average_calaca_g01[13]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10], average_calaca_g02[11], average_calaca_g02[12], average_calaca_g02[13]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10], average_kal_g01[11], average_kal_g01[12], average_kal_g01[13]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10], average_kal_g02[11], average_kal_g02[12], average_kal_g02[13]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10], average_kal_g03[11], average_kal_g03[12], average_kal_g03[13]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10], average_kal_g04[11], average_kal_g04[12], average_kal_g04[13]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10], average_leyte_a[11], average_leyte_a[12], average_leyte_a[13]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10], average_kspc_g01[11], average_kspc_g01[12], average_kspc_g01[13]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10], average_kspc_g02[11], average_kspc_g02[12], average_kspc_g02[13]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10], average_bantap_l01[11], average_bantap_l01[12], average_bantap_l01[13]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10], average_pedc_t1l1[11], average_pedc_t1l1[12], average_pedc_t1l1[13]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10], average_pedc_t1l2[11], average_pedc_t1l2[12], average_pedc_t1l2[13]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10], average_stbar_t1l1[11], average_stbar_t1l1[12], average_stbar_t1l1[13]]
    }

elif hour_value == "15":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10], average_botoca_g01[11], average_botoca_g01[12], average_botoca_g01[13], average_botoca_g01[14]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10], average_calaca_g01[11], average_calaca_g01[12], average_calaca_g01[13], average_calaca_g01[14]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10], average_calaca_g02[11], average_calaca_g02[12], average_calaca_g02[13], average_calaca_g02[14]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10], average_kal_g01[11], average_kal_g01[12], average_kal_g01[13], average_kal_g01[14]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10], average_kal_g02[11], average_kal_g02[12], average_kal_g02[13], average_kal_g02[14]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10], average_kal_g03[11], average_kal_g03[12], average_kal_g03[13], average_kal_g03[14]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10], average_kal_g04[11], average_kal_g04[12], average_kal_g04[13], average_kal_g04[14]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10], average_leyte_a[11], average_leyte_a[12], average_leyte_a[13], average_leyte_a[14]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10], average_kspc_g01[11], average_kspc_g01[12], average_kspc_g01[13], average_kspc_g01[14]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10], average_kspc_g02[11], average_kspc_g02[12], average_kspc_g02[13], average_kspc_g02[14]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10], average_bantap_l01[11], average_bantap_l01[12], average_bantap_l01[13], average_bantap_l01[14]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10], average_pedc_t1l1[11], average_pedc_t1l1[12], average_pedc_t1l1[13], average_pedc_t1l1[14]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10], average_pedc_t1l2[11], average_pedc_t1l2[12], average_pedc_t1l2[13], average_pedc_t1l2[14]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10], average_stbar_t1l1[11], average_stbar_t1l1[12], average_stbar_t1l1[13], average_stbar_t1l1[14]]
    }

elif hour_value == "16":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10], average_botoca_g01[11], average_botoca_g01[12], average_botoca_g01[13], average_botoca_g01[14], average_botoca_g01[15]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10], average_calaca_g01[11], average_calaca_g01[12], average_calaca_g01[13], average_calaca_g01[14], average_calaca_g01[15]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10], average_calaca_g02[11], average_calaca_g02[12], average_calaca_g02[13], average_calaca_g02[14], average_calaca_g02[15]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10], average_kal_g01[11], average_kal_g01[12], average_kal_g01[13], average_kal_g01[14], average_kal_g01[15]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10], average_kal_g02[11], average_kal_g02[12], average_kal_g02[13], average_kal_g02[14], average_kal_g02[15]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10], average_kal_g03[11], average_kal_g03[12], average_kal_g03[13], average_kal_g03[14], average_kal_g03[15]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10], average_kal_g04[11], average_kal_g04[12], average_kal_g04[13], average_kal_g04[14], average_kal_g04[15]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10], average_leyte_a[11], average_leyte_a[12], average_leyte_a[13], average_leyte_a[14], average_leyte_a[15]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10], average_kspc_g01[11], average_kspc_g01[12], average_kspc_g01[13], average_kspc_g01[14], average_kspc_g01[15]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10], average_kspc_g02[11], average_kspc_g02[12], average_kspc_g02[13], average_kspc_g02[14], average_kspc_g02[15]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10], average_bantap_l01[11], average_bantap_l01[12], average_bantap_l01[13], average_bantap_l01[14], average_bantap_l01[15]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10], average_pedc_t1l1[11], average_pedc_t1l1[12], average_pedc_t1l1[13], average_pedc_t1l1[14], average_pedc_t1l1[15]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10], average_pedc_t1l2[11], average_pedc_t1l2[12], average_pedc_t1l2[13], average_pedc_t1l2[14], average_pedc_t1l2[15]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10], average_stbar_t1l1[11], average_stbar_t1l1[12], average_stbar_t1l1[13], average_stbar_t1l1[14], average_stbar_t1l1[15]]
    }
elif hour_value == "17":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10], average_botoca_g01[11], average_botoca_g01[12], average_botoca_g01[13], average_botoca_g01[14], average_botoca_g01[15], average_botoca_g01[16]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10], average_calaca_g01[11], average_calaca_g01[12], average_calaca_g01[13], average_calaca_g01[14], average_calaca_g01[15], average_calaca_g01[16]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10], average_calaca_g02[11], average_calaca_g02[12], average_calaca_g02[13], average_calaca_g02[14], average_calaca_g02[15], average_calaca_g02[16]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10], average_kal_g01[11], average_kal_g01[12], average_kal_g01[13], average_kal_g01[14], average_kal_g01[15], average_kal_g01[16]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10], average_kal_g02[11], average_kal_g02[12], average_kal_g02[13], average_kal_g02[14], average_kal_g02[15], average_kal_g02[16]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10], average_kal_g03[11], average_kal_g03[12], average_kal_g03[13], average_kal_g03[14], average_kal_g03[15], average_kal_g03[16]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10], average_kal_g04[11], average_kal_g04[12], average_kal_g04[13], average_kal_g04[14], average_kal_g04[15], average_kal_g04[16]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10], average_leyte_a[11], average_leyte_a[12], average_leyte_a[13], average_leyte_a[14], average_leyte_a[15], average_leyte_a[16]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10], average_kspc_g01[11], average_kspc_g01[12], average_kspc_g01[13], average_kspc_g01[14], average_kspc_g01[15], average_kspc_g01[16]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10], average_kspc_g02[11], average_kspc_g02[12], average_kspc_g02[13], average_kspc_g02[14], average_kspc_g02[15], average_kspc_g02[16]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10], average_bantap_l01[11], average_bantap_l01[12], average_bantap_l01[13], average_bantap_l01[14], average_bantap_l01[15], average_bantap_l01[16]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10], average_pedc_t1l1[11], average_pedc_t1l1[12], average_pedc_t1l1[13], average_pedc_t1l1[14], average_pedc_t1l1[15], average_pedc_t1l1[16]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10], average_pedc_t1l2[11], average_pedc_t1l2[12], average_pedc_t1l2[13], average_pedc_t1l2[14], average_pedc_t1l2[15], average_pedc_t1l2[16]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10], average_stbar_t1l1[11], average_stbar_t1l1[12], average_stbar_t1l1[13], average_stbar_t1l1[14], average_stbar_t1l1[15], average_stbar_t1l1[16]]
    }
elif hour_value == "18":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10], average_botoca_g01[11], average_botoca_g01[12], average_botoca_g01[13], average_botoca_g01[14], average_botoca_g01[15], average_botoca_g01[16], average_botoca_g01[17]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10], average_calaca_g01[11], average_calaca_g01[12], average_calaca_g01[13], average_calaca_g01[14], average_calaca_g01[15], average_calaca_g01[16], average_calaca_g01[17]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10], average_calaca_g02[11], average_calaca_g02[12], average_calaca_g02[13], average_calaca_g02[14], average_calaca_g02[15], average_calaca_g02[16], average_calaca_g02[17]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10], average_kal_g01[11], average_kal_g01[12], average_kal_g01[13], average_kal_g01[14], average_kal_g01[15], average_kal_g01[16], average_kal_g01[17]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10], average_kal_g02[11], average_kal_g02[12], average_kal_g02[13], average_kal_g02[14], average_kal_g02[15], average_kal_g02[16], average_kal_g02[17]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10], average_kal_g03[11], average_kal_g03[12], average_kal_g03[13], average_kal_g03[14], average_kal_g03[15], average_kal_g03[16], average_kal_g03[17]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10], average_kal_g04[11], average_kal_g04[12], average_kal_g04[13], average_kal_g04[14], average_kal_g04[15], average_kal_g04[16], average_kal_g04[17]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10], average_leyte_a[11], average_leyte_a[12], average_leyte_a[13], average_leyte_a[14], average_leyte_a[15], average_leyte_a[16], average_leyte_a[17]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10], average_kspc_g01[11], average_kspc_g01[12], average_kspc_g01[13], average_kspc_g01[14], average_kspc_g01[15], average_kspc_g01[16], average_kspc_g01[17]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10], average_kspc_g02[11], average_kspc_g02[12], average_kspc_g02[13], average_kspc_g02[14], average_kspc_g02[15], average_kspc_g02[16], average_kspc_g02[17]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10], average_bantap_l01[11], average_bantap_l01[12], average_bantap_l01[13], average_bantap_l01[14], average_bantap_l01[15], average_bantap_l01[16], average_bantap_l01[17]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10], average_pedc_t1l1[11], average_pedc_t1l1[12], average_pedc_t1l1[13], average_pedc_t1l1[14], average_pedc_t1l1[15], average_pedc_t1l1[16], average_pedc_t1l1[17]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10], average_pedc_t1l2[11], average_pedc_t1l2[12], average_pedc_t1l2[13], average_pedc_t1l2[14], average_pedc_t1l2[15], average_pedc_t1l2[16], average_pedc_t1l2[17]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10], average_stbar_t1l1[11], average_stbar_t1l1[12], average_stbar_t1l1[13], average_stbar_t1l1[14], average_stbar_t1l1[15], average_stbar_t1l1[16], average_stbar_t1l1[17]]
    }
elif hour_value == "19":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10], average_botoca_g01[11], average_botoca_g01[12], average_botoca_g01[13], average_botoca_g01[14], average_botoca_g01[15], average_botoca_g01[16], average_botoca_g01[17], average_botoca_g01[18]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10], average_calaca_g01[11], average_calaca_g01[12], average_calaca_g01[13], average_calaca_g01[14], average_calaca_g01[15], average_calaca_g01[16], average_calaca_g01[17], average_calaca_g01[18]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10], average_calaca_g02[11], average_calaca_g02[12], average_calaca_g02[13], average_calaca_g02[14], average_calaca_g02[15], average_calaca_g02[16], average_calaca_g02[17], average_calaca_g02[18]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10], average_kal_g01[11], average_kal_g01[12], average_kal_g01[13], average_kal_g01[14], average_kal_g01[15], average_kal_g01[16], average_kal_g01[17], average_kal_g01[18]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10], average_kal_g02[11], average_kal_g02[12], average_kal_g02[13], average_kal_g02[14], average_kal_g02[15], average_kal_g02[16], average_kal_g02[17], average_kal_g02[18]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10], average_kal_g03[11], average_kal_g03[12], average_kal_g03[13], average_kal_g03[14], average_kal_g03[15], average_kal_g03[16], average_kal_g03[17], average_kal_g03[18]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10], average_kal_g04[11], average_kal_g04[12], average_kal_g04[13], average_kal_g04[14], average_kal_g04[15], average_kal_g04[16], average_kal_g04[17], average_kal_g04[18]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10], average_leyte_a[11], average_leyte_a[12], average_leyte_a[13], average_leyte_a[14], average_leyte_a[15], average_leyte_a[16], average_leyte_a[17], average_leyte_a[18]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10], average_kspc_g01[11], average_kspc_g01[12], average_kspc_g01[13], average_kspc_g01[14], average_kspc_g01[15], average_kspc_g01[16], average_kspc_g01[17], average_kspc_g01[18]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10], average_kspc_g02[11], average_kspc_g02[12], average_kspc_g02[13], average_kspc_g02[14], average_kspc_g02[15], average_kspc_g02[16], average_kspc_g02[17], average_kspc_g02[18]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10], average_bantap_l01[11], average_bantap_l01[12], average_bantap_l01[13], average_bantap_l01[14], average_bantap_l01[15], average_bantap_l01[16], average_bantap_l01[17], average_bantap_l01[18]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10], average_pedc_t1l1[11], average_pedc_t1l1[12], average_pedc_t1l1[13], average_pedc_t1l1[14], average_pedc_t1l1[15], average_pedc_t1l1[16], average_pedc_t1l1[17], average_pedc_t1l1[18]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10], average_pedc_t1l2[11], average_pedc_t1l2[12], average_pedc_t1l2[13], average_pedc_t1l2[14], average_pedc_t1l2[15], average_pedc_t1l2[16], average_pedc_t1l2[17], average_pedc_t1l2[18]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10], average_stbar_t1l1[11], average_stbar_t1l1[12], average_stbar_t1l1[13], average_stbar_t1l1[14], average_stbar_t1l1[15], average_stbar_t1l1[16], average_stbar_t1l1[17], average_stbar_t1l1[18]]
    }
elif hour_value == "20":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10], average_botoca_g01[11], average_botoca_g01[12], average_botoca_g01[13], average_botoca_g01[14], average_botoca_g01[15], average_botoca_g01[16], average_botoca_g01[17], average_botoca_g01[18], average_botoca_g01[19]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10], average_calaca_g01[11], average_calaca_g01[12], average_calaca_g01[13], average_calaca_g01[14], average_calaca_g01[15], average_calaca_g01[16], average_calaca_g01[17], average_calaca_g01[18], average_calaca_g01[19]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10], average_calaca_g02[11], average_calaca_g02[12], average_calaca_g02[13], average_calaca_g02[14], average_calaca_g02[15], average_calaca_g02[16], average_calaca_g02[17], average_calaca_g02[18], average_calaca_g02[19]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10], average_kal_g01[11], average_kal_g01[12], average_kal_g01[13], average_kal_g01[14], average_kal_g01[15], average_kal_g01[16], average_kal_g01[17], average_kal_g01[18], average_kal_g01[19]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10], average_kal_g02[11], average_kal_g02[12], average_kal_g02[13], average_kal_g02[14], average_kal_g02[15], average_kal_g02[16], average_kal_g02[17], average_kal_g02[18], average_kal_g02[19]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10], average_kal_g03[11], average_kal_g03[12], average_kal_g03[13], average_kal_g03[14], average_kal_g03[15], average_kal_g03[16], average_kal_g03[17], average_kal_g03[18], average_kal_g03[19]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10], average_kal_g04[11], average_kal_g04[12], average_kal_g04[13], average_kal_g04[14], average_kal_g04[15], average_kal_g04[16], average_kal_g04[17], average_kal_g04[18], average_kal_g04[19]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10], average_leyte_a[11], average_leyte_a[12], average_leyte_a[13], average_leyte_a[14], average_leyte_a[15], average_leyte_a[16], average_leyte_a[17], average_leyte_a[18], average_leyte_a[19]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10], average_kspc_g01[11], average_kspc_g01[12], average_kspc_g01[13], average_kspc_g01[14], average_kspc_g01[15], average_kspc_g01[16], average_kspc_g01[17], average_kspc_g01[18], average_kspc_g01[19]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10], average_kspc_g02[11], average_kspc_g02[12], average_kspc_g02[13], average_kspc_g02[14], average_kspc_g02[15], average_kspc_g02[16], average_kspc_g02[17], average_kspc_g02[18], average_kspc_g02[19]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10], average_bantap_l01[11], average_bantap_l01[12], average_bantap_l01[13], average_bantap_l01[14], average_bantap_l01[15], average_bantap_l01[16], average_bantap_l01[17], average_bantap_l01[18], average_bantap_l01[19]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10], average_pedc_t1l1[11], average_pedc_t1l1[12], average_pedc_t1l1[13], average_pedc_t1l1[14], average_pedc_t1l1[15], average_pedc_t1l1[16], average_pedc_t1l1[17], average_pedc_t1l1[18], average_pedc_t1l1[19]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10], average_pedc_t1l2[11], average_pedc_t1l2[12], average_pedc_t1l2[13], average_pedc_t1l2[14], average_pedc_t1l2[15], average_pedc_t1l2[16], average_pedc_t1l2[17], average_pedc_t1l2[18], average_pedc_t1l2[19]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10], average_stbar_t1l1[11], average_stbar_t1l1[12], average_stbar_t1l1[13], average_stbar_t1l1[14], average_stbar_t1l1[15], average_stbar_t1l1[16], average_stbar_t1l1[17], average_stbar_t1l1[18], average_stbar_t1l1[19]]
    }
elif hour_value == "21":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10], average_botoca_g01[11], average_botoca_g01[12], average_botoca_g01[13], average_botoca_g01[14], average_botoca_g01[15], average_botoca_g01[16], average_botoca_g01[17], average_botoca_g01[18], average_botoca_g01[19], average_botoca_g01[20]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10], average_calaca_g01[11], average_calaca_g01[12], average_calaca_g01[13], average_calaca_g01[14], average_calaca_g01[15], average_calaca_g01[16], average_calaca_g01[17], average_calaca_g01[18], average_calaca_g01[19], average_calaca_g01[20]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10], average_calaca_g02[11], average_calaca_g02[12], average_calaca_g02[13], average_calaca_g02[14], average_calaca_g02[15], average_calaca_g02[16], average_calaca_g02[17], average_calaca_g02[18], average_calaca_g02[19], average_calaca_g02[20]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10], average_kal_g01[11], average_kal_g01[12], average_kal_g01[13], average_kal_g01[14], average_kal_g01[15], average_kal_g01[16], average_kal_g01[17], average_kal_g01[18], average_kal_g01[19], average_kal_g01[20]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10], average_kal_g02[11], average_kal_g02[12], average_kal_g02[13], average_kal_g02[14], average_kal_g02[15], average_kal_g02[16], average_kal_g02[17], average_kal_g02[18], average_kal_g02[19], average_kal_g02[20]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10], average_kal_g03[11], average_kal_g03[12], average_kal_g03[13], average_kal_g03[14], average_kal_g03[15], average_kal_g03[16], average_kal_g03[17], average_kal_g03[18], average_kal_g03[19], average_kal_g03[20]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10], average_kal_g04[11], average_kal_g04[12], average_kal_g04[13], average_kal_g04[14], average_kal_g04[15], average_kal_g04[16], average_kal_g04[17], average_kal_g04[18], average_kal_g04[19], average_kal_g04[20]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10], average_leyte_a[11], average_leyte_a[12], average_leyte_a[13], average_leyte_a[14], average_leyte_a[15], average_leyte_a[16], average_leyte_a[17], average_leyte_a[18], average_leyte_a[19], average_leyte_a[20]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10], average_kspc_g01[11], average_kspc_g01[12], average_kspc_g01[13], average_kspc_g01[14], average_kspc_g01[15], average_kspc_g01[16], average_kspc_g01[17], average_kspc_g01[18], average_kspc_g01[19], average_kspc_g01[20]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10], average_kspc_g02[11], average_kspc_g02[12], average_kspc_g02[13], average_kspc_g02[14], average_kspc_g02[15], average_kspc_g02[16], average_kspc_g02[17], average_kspc_g02[18], average_kspc_g02[19], average_kspc_g02[20]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10], average_bantap_l01[11], average_bantap_l01[12], average_bantap_l01[13], average_bantap_l01[14], average_bantap_l01[15], average_bantap_l01[16], average_bantap_l01[17], average_bantap_l01[18], average_bantap_l01[19], average_bantap_l01[20]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10], average_pedc_t1l1[11], average_pedc_t1l1[12], average_pedc_t1l1[13], average_pedc_t1l1[14], average_pedc_t1l1[15], average_pedc_t1l1[16], average_pedc_t1l1[17], average_pedc_t1l1[18], average_pedc_t1l1[19], average_pedc_t1l1[20]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10], average_pedc_t1l2[11], average_pedc_t1l2[12], average_pedc_t1l2[13], average_pedc_t1l2[14], average_pedc_t1l2[15], average_pedc_t1l2[16], average_pedc_t1l2[17], average_pedc_t1l2[18], average_pedc_t1l2[19], average_pedc_t1l2[20]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10], average_stbar_t1l1[11], average_stbar_t1l1[12], average_stbar_t1l1[13], average_stbar_t1l1[14], average_stbar_t1l1[15], average_stbar_t1l1[16], average_stbar_t1l1[17], average_stbar_t1l1[18], average_stbar_t1l1[19], average_stbar_t1l1[20]]
    }
elif hour_value == "22":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10], average_botoca_g01[11], average_botoca_g01[12], average_botoca_g01[13], average_botoca_g01[14], average_botoca_g01[15], average_botoca_g01[16], average_botoca_g01[17], average_botoca_g01[18], average_botoca_g01[19], average_botoca_g01[20], average_botoca_g01[21]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10], average_calaca_g01[11], average_calaca_g01[12], average_calaca_g01[13], average_calaca_g01[14], average_calaca_g01[15], average_calaca_g01[16], average_calaca_g01[17], average_calaca_g01[18], average_calaca_g01[19], average_calaca_g01[20], average_calaca_g01[21]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10], average_calaca_g02[11], average_calaca_g02[12], average_calaca_g02[13], average_calaca_g02[14], average_calaca_g02[15], average_calaca_g02[16], average_calaca_g02[17], average_calaca_g02[18], average_calaca_g02[19], average_calaca_g02[20], average_calaca_g02[21]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10], average_kal_g01[11], average_kal_g01[12], average_kal_g01[13], average_kal_g01[14], average_kal_g01[15], average_kal_g01[16], average_kal_g01[17], average_kal_g01[18], average_kal_g01[19], average_kal_g01[20], average_kal_g01[21]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10], average_kal_g02[11], average_kal_g02[12], average_kal_g02[13], average_kal_g02[14], average_kal_g02[15], average_kal_g02[16], average_kal_g02[17], average_kal_g02[18], average_kal_g02[19], average_kal_g02[20], average_kal_g02[21]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10], average_kal_g03[11], average_kal_g03[12], average_kal_g03[13], average_kal_g03[14], average_kal_g03[15], average_kal_g03[16], average_kal_g03[17], average_kal_g03[18], average_kal_g03[19], average_kal_g03[20], average_kal_g03[21]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10], average_kal_g04[11], average_kal_g04[12], average_kal_g04[13], average_kal_g04[14], average_kal_g04[15], average_kal_g04[16], average_kal_g04[17], average_kal_g04[18], average_kal_g04[19], average_kal_g04[20], average_kal_g04[21]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10], average_leyte_a[11], average_leyte_a[12], average_leyte_a[13], average_leyte_a[14], average_leyte_a[15], average_leyte_a[16], average_leyte_a[17], average_leyte_a[18], average_leyte_a[19], average_leyte_a[20], average_leyte_a[21]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10], average_kspc_g01[11], average_kspc_g01[12], average_kspc_g01[13], average_kspc_g01[14], average_kspc_g01[15], average_kspc_g01[16], average_kspc_g01[17], average_kspc_g01[18], average_kspc_g01[19], average_kspc_g01[20], average_kspc_g01[21]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10], average_kspc_g02[11], average_kspc_g02[12], average_kspc_g02[13], average_kspc_g02[14], average_kspc_g02[15], average_kspc_g02[16], average_kspc_g02[17], average_kspc_g02[18], average_kspc_g02[19], average_kspc_g02[20], average_kspc_g02[21]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10], average_bantap_l01[11], average_bantap_l01[12], average_bantap_l01[13], average_bantap_l01[14], average_bantap_l01[15], average_bantap_l01[16], average_bantap_l01[17], average_bantap_l01[18], average_bantap_l01[19], average_bantap_l01[20], average_bantap_l01[21]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10], average_pedc_t1l1[11], average_pedc_t1l1[12], average_pedc_t1l1[13], average_pedc_t1l1[14], average_pedc_t1l1[15], average_pedc_t1l1[16], average_pedc_t1l1[17], average_pedc_t1l1[18], average_pedc_t1l1[19], average_pedc_t1l1[20], average_pedc_t1l1[21]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10], average_pedc_t1l2[11], average_pedc_t1l2[12], average_pedc_t1l2[13], average_pedc_t1l2[14], average_pedc_t1l2[15], average_pedc_t1l2[16], average_pedc_t1l2[17], average_pedc_t1l2[18], average_pedc_t1l2[19], average_pedc_t1l2[20], average_pedc_t1l2[21]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10], average_stbar_t1l1[11], average_stbar_t1l1[12], average_stbar_t1l1[13], average_stbar_t1l1[14], average_stbar_t1l1[15], average_stbar_t1l1[16], average_stbar_t1l1[17], average_stbar_t1l1[18], average_stbar_t1l1[19], average_stbar_t1l1[20], average_stbar_t1l1[21]]
    }
elif hour_value == "23":
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10], average_botoca_g01[11], average_botoca_g01[12], average_botoca_g01[13], average_botoca_g01[14], average_botoca_g01[15], average_botoca_g01[16], average_botoca_g01[17], average_botoca_g01[18], average_botoca_g01[19], average_botoca_g01[20], average_botoca_g01[21], average_botoca_g01[22]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10], average_calaca_g01[11], average_calaca_g01[12], average_calaca_g01[13], average_calaca_g01[14], average_calaca_g01[15], average_calaca_g01[16], average_calaca_g01[17], average_calaca_g01[18], average_calaca_g01[19], average_calaca_g01[20], average_calaca_g01[21], average_calaca_g01[22]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10], average_calaca_g02[11], average_calaca_g02[12], average_calaca_g02[13], average_calaca_g02[14], average_calaca_g02[15], average_calaca_g02[16], average_calaca_g02[17], average_calaca_g02[18], average_calaca_g02[19], average_calaca_g02[20], average_calaca_g02[21], average_calaca_g02[22]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10], average_kal_g01[11], average_kal_g01[12], average_kal_g01[13], average_kal_g01[14], average_kal_g01[15], average_kal_g01[16], average_kal_g01[17], average_kal_g01[18], average_kal_g01[19], average_kal_g01[20], average_kal_g01[21], average_kal_g01[22]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10], average_kal_g02[11], average_kal_g02[12], average_kal_g02[13], average_kal_g02[14], average_kal_g02[15], average_kal_g02[16], average_kal_g02[17], average_kal_g02[18], average_kal_g02[19], average_kal_g02[20], average_kal_g02[21], average_kal_g02[22]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10], average_kal_g03[11], average_kal_g03[12], average_kal_g03[13], average_kal_g03[14], average_kal_g03[15], average_kal_g03[16], average_kal_g03[17], average_kal_g03[18], average_kal_g03[19], average_kal_g03[20], average_kal_g03[21], average_kal_g03[22]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10], average_kal_g04[11], average_kal_g04[12], average_kal_g04[13], average_kal_g04[14], average_kal_g04[15], average_kal_g04[16], average_kal_g04[17], average_kal_g04[18], average_kal_g04[19], average_kal_g04[20], average_kal_g04[21], average_kal_g04[22]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10], average_leyte_a[11], average_leyte_a[12], average_leyte_a[13], average_leyte_a[14], average_leyte_a[15], average_leyte_a[16], average_leyte_a[17], average_leyte_a[18], average_leyte_a[19], average_leyte_a[20], average_leyte_a[21], average_leyte_a[22]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10], average_kspc_g01[11], average_kspc_g01[12], average_kspc_g01[13], average_kspc_g01[14], average_kspc_g01[15], average_kspc_g01[16], average_kspc_g01[17], average_kspc_g01[18], average_kspc_g01[19], average_kspc_g01[20], average_kspc_g01[21], average_kspc_g01[22]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10], average_kspc_g02[11], average_kspc_g02[12], average_kspc_g02[13], average_kspc_g02[14], average_kspc_g02[15], average_kspc_g02[16], average_kspc_g02[17], average_kspc_g02[18], average_kspc_g02[19], average_kspc_g02[20], average_kspc_g02[21], average_kspc_g02[22]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10], average_bantap_l01[11], average_bantap_l01[12], average_bantap_l01[13], average_bantap_l01[14], average_bantap_l01[15], average_bantap_l01[16], average_bantap_l01[17], average_bantap_l01[18], average_bantap_l01[19], average_bantap_l01[20], average_bantap_l01[21], average_bantap_l01[22]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10], average_pedc_t1l1[11], average_pedc_t1l1[12], average_pedc_t1l1[13], average_pedc_t1l1[14], average_pedc_t1l1[15], average_pedc_t1l1[16], average_pedc_t1l1[17], average_pedc_t1l1[18], average_pedc_t1l1[19], average_pedc_t1l1[20], average_pedc_t1l1[21], average_pedc_t1l1[22]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10], average_pedc_t1l2[11], average_pedc_t1l2[12], average_pedc_t1l2[13], average_pedc_t1l2[14], average_pedc_t1l2[15], average_pedc_t1l2[16], average_pedc_t1l2[17], average_pedc_t1l2[18], average_pedc_t1l2[19], average_pedc_t1l2[20], average_pedc_t1l2[21], average_pedc_t1l2[22]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10], average_stbar_t1l1[11], average_stbar_t1l1[12], average_stbar_t1l1[13], average_stbar_t1l1[14], average_stbar_t1l1[15], average_stbar_t1l1[16], average_stbar_t1l1[17], average_stbar_t1l1[18], average_stbar_t1l1[19], average_stbar_t1l1[20], average_stbar_t1l1[21], average_stbar_t1l1[22]]
    }

else:
    data = {
        "HOUR": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"],
        "03BOTOCA_G01": [average_botoca_g01[0], average_botoca_g01[1], average_botoca_g01[2], average_botoca_g01[3], average_botoca_g01[4], average_botoca_g01[5], average_botoca_g01[6], average_botoca_g01[7], average_botoca_g01[8], average_botoca_g01[9], average_botoca_g01[10], average_botoca_g01[11], average_botoca_g01[12], average_botoca_g01[13], average_botoca_g01[14], average_botoca_g01[15], average_botoca_g01[16], average_botoca_g01[17], average_botoca_g01[18], average_botoca_g01[19], average_botoca_g01[20], average_botoca_g01[21], average_botoca_g01[22], average_botoca_g01[23]],
        "03CALACA_G01": [average_calaca_g01[0], average_calaca_g01[1], average_calaca_g01[2], average_calaca_g01[3], average_calaca_g01[4], average_calaca_g01[5], average_calaca_g01[6], average_calaca_g01[7], average_calaca_g01[8], average_calaca_g01[9], average_calaca_g01[10], average_calaca_g01[11], average_calaca_g01[12], average_calaca_g01[13], average_calaca_g01[14], average_calaca_g01[15], average_calaca_g01[16], average_calaca_g01[17], average_calaca_g01[18], average_calaca_g01[19], average_calaca_g01[20], average_calaca_g01[21], average_calaca_g01[22], average_calaca_g01[23]],
        "03CALACA_G02": [average_calaca_g02[0], average_calaca_g02[1], average_calaca_g02[2], average_calaca_g02[3], average_calaca_g02[4], average_calaca_g02[5], average_calaca_g02[6], average_calaca_g02[7], average_calaca_g02[8], average_calaca_g02[9], average_calaca_g02[10], average_calaca_g02[11], average_calaca_g02[12], average_calaca_g02[13], average_calaca_g02[14], average_calaca_g02[15], average_calaca_g02[16], average_calaca_g02[17], average_calaca_g02[18], average_calaca_g02[19], average_calaca_g02[20], average_calaca_g02[21], average_calaca_g02[22], average_calaca_g02[23]],
        "03KAL_G01": [average_kal_g01[0], average_kal_g01[1], average_kal_g01[2], average_kal_g01[3], average_kal_g01[4], average_kal_g01[5], average_kal_g01[6], average_kal_g01[7], average_kal_g01[8], average_kal_g01[9], average_kal_g01[10], average_kal_g01[11], average_kal_g01[12], average_kal_g01[13], average_kal_g01[14], average_kal_g01[15], average_kal_g01[16], average_kal_g01[17], average_kal_g01[18], average_kal_g01[19], average_kal_g01[20], average_kal_g01[21], average_kal_g01[22], average_kal_g01[23]], 
        "03KAL_G02": [average_kal_g02[0], average_kal_g02[1], average_kal_g02[2], average_kal_g02[3], average_kal_g02[4], average_kal_g02[5], average_kal_g02[6], average_kal_g02[7], average_kal_g02[8], average_kal_g02[9], average_kal_g02[10], average_kal_g02[11], average_kal_g02[12], average_kal_g02[13], average_kal_g02[14], average_kal_g02[15], average_kal_g02[16], average_kal_g02[17], average_kal_g02[18], average_kal_g02[19], average_kal_g02[20], average_kal_g02[21], average_kal_g02[22], average_kal_g02[23]], 
        "03KAL_G03": [average_kal_g03[0], average_kal_g03[1], average_kal_g03[2], average_kal_g03[3], average_kal_g03[4], average_kal_g03[5], average_kal_g03[6], average_kal_g03[7], average_kal_g03[8], average_kal_g03[9], average_kal_g03[10], average_kal_g03[11], average_kal_g03[12], average_kal_g03[13], average_kal_g03[14], average_kal_g03[15], average_kal_g03[16], average_kal_g03[17], average_kal_g03[18], average_kal_g03[19], average_kal_g03[20], average_kal_g03[21], average_kal_g03[22], average_kal_g03[23]],
        "03KAL_G04": [average_kal_g04[0], average_kal_g04[1], average_kal_g04[2], average_kal_g04[3], average_kal_g04[4], average_kal_g04[5], average_kal_g04[6], average_kal_g04[7], average_kal_g04[8], average_kal_g04[9], average_kal_g04[10], average_kal_g04[11], average_kal_g04[12], average_kal_g04[13], average_kal_g04[14], average_kal_g04[15], average_kal_g04[16], average_kal_g04[17], average_kal_g04[18], average_kal_g04[19], average_kal_g04[20], average_kal_g04[21], average_kal_g04[22], average_kal_g04[23]],
        "04LEYTE_A": [average_leyte_a[0], average_leyte_a[1], average_leyte_a[2], average_leyte_a[3], average_leyte_a[4], average_leyte_a[5], average_leyte_a[6], average_leyte_a[7], average_leyte_a[8], average_leyte_a[9], average_leyte_a[10], average_leyte_a[11], average_leyte_a[12], average_leyte_a[13], average_leyte_a[14], average_leyte_a[15], average_leyte_a[16], average_leyte_a[17], average_leyte_a[18], average_leyte_a[19], average_leyte_a[20], average_leyte_a[21], average_leyte_a[22], average_leyte_a[23]],
        "05KSPC_G01": [average_kspc_g01[0], average_kspc_g01[1], average_kspc_g01[2], average_kspc_g01[3], average_kspc_g01[4], average_kspc_g01[5], average_kspc_g01[6], average_kspc_g01[7], average_kspc_g01[8], average_kspc_g01[9], average_kspc_g01[10], average_kspc_g01[11], average_kspc_g01[12], average_kspc_g01[13], average_kspc_g01[14], average_kspc_g01[15], average_kspc_g01[16], average_kspc_g01[17], average_kspc_g01[18], average_kspc_g01[19], average_kspc_g01[20], average_kspc_g01[21], average_kspc_g01[22], average_kspc_g01[23]],
        "05KSPC_G02": [average_kspc_g02[0], average_kspc_g02[1], average_kspc_g02[2], average_kspc_g02[3], average_kspc_g02[4], average_kspc_g02[5], average_kspc_g02[6], average_kspc_g02[7], average_kspc_g02[8], average_kspc_g02[9], average_kspc_g02[10], average_kspc_g02[11], average_kspc_g02[12], average_kspc_g02[13], average_kspc_g02[14], average_kspc_g02[15], average_kspc_g02[16], average_kspc_g02[17], average_kspc_g02[18], average_kspc_g02[19], average_kspc_g02[20], average_kspc_g02[21], average_kspc_g02[22], average_kspc_g02[23]], 
        "08BANTAP_L01": [average_bantap_l01[0], average_bantap_l01[1], average_bantap_l01[2], average_bantap_l01[3], average_bantap_l01[4], average_bantap_l01[5], average_bantap_l01[6], average_bantap_l01[7], average_bantap_l01[8], average_bantap_l01[9], average_bantap_l01[10], average_bantap_l01[11], average_bantap_l01[12], average_bantap_l01[13], average_bantap_l01[14], average_bantap_l01[15], average_bantap_l01[16], average_bantap_l01[17], average_bantap_l01[18], average_bantap_l01[19], average_bantap_l01[20], average_bantap_l01[21], average_bantap_l01[22], average_bantap_l01[23]],
        "08PEDC_T1L1": [average_pedc_t1l1[0], average_pedc_t1l1[1], average_pedc_t1l1[2], average_pedc_t1l1[3], average_pedc_t1l1[4], average_pedc_t1l1[5], average_pedc_t1l1[6], average_pedc_t1l1[7], average_pedc_t1l1[8], average_pedc_t1l1[9], average_pedc_t1l1[10], average_pedc_t1l1[11], average_pedc_t1l1[12], average_pedc_t1l1[13], average_pedc_t1l1[14], average_pedc_t1l1[15], average_pedc_t1l1[16], average_pedc_t1l1[17], average_pedc_t1l1[18], average_pedc_t1l1[19], average_pedc_t1l1[20], average_pedc_t1l1[21], average_pedc_t1l1[22], average_pedc_t1l1[23]],
        "08PEDC_T1L2": [average_pedc_t1l2[0], average_pedc_t1l2[1], average_pedc_t1l2[2], average_pedc_t1l2[3], average_pedc_t1l2[4], average_pedc_t1l2[5], average_pedc_t1l2[6], average_pedc_t1l2[7], average_pedc_t1l2[8], average_pedc_t1l2[9], average_pedc_t1l2[10], average_pedc_t1l2[11], average_pedc_t1l2[12], average_pedc_t1l2[13], average_pedc_t1l2[14], average_pedc_t1l2[15], average_pedc_t1l2[16], average_pedc_t1l2[17], average_pedc_t1l2[18], average_pedc_t1l2[19], average_pedc_t1l2[20], average_pedc_t1l2[21], average_pedc_t1l2[22], average_pedc_t1l2[23]],
        "08STBAR_T1L1": [average_stbar_t1l1[0], average_stbar_t1l1[1], average_stbar_t1l1[2], average_stbar_t1l1[3], average_stbar_t1l1[4], average_stbar_t1l1[5], average_stbar_t1l1[6], average_stbar_t1l1[7], average_stbar_t1l1[8], average_stbar_t1l1[9], average_stbar_t1l1[10], average_stbar_t1l1[11], average_stbar_t1l1[12], average_stbar_t1l1[13], average_stbar_t1l1[14], average_stbar_t1l1[15], average_stbar_t1l1[16], average_stbar_t1l1[17], average_stbar_t1l1[18], average_stbar_t1l1[19], average_stbar_t1l1[20], average_stbar_t1l1[21], average_stbar_t1l1[22], average_stbar_t1l1[23]]
    }
    
# Create a DataFrame
df_tipc = pd.DataFrame(data)

# Melt the DataFrame to a long format
df_long = df_tipc.melt(id_vars=['HOUR'], var_name='Resource', value_name='Value')

# Pivot the DataFrame to prepare for hover information
df_pivot = df_long.pivot(index='HOUR', columns='Resource', values='Value').fillna(0)
df_pivot.reset_index(inplace=True)

# Generate hover information
hover_info = df_pivot.set_index('HOUR').apply(lambda x: '<br>'.join([f'{col}: {x[col]}' for col in x.index]), axis=1).to_dict()

# Merge hover information into long DataFrame
df_long['Hover'] = df_long['HOUR'].map(hover_info)

# Create the interactive line chart with Plotly
fig_tipc = px.line(df_long, x='HOUR', y='Value', color='Resource', width=600, height=300)

# Customize hover information
fig_tipc.update_traces(hovertemplate='%{customdata[0]}', customdata=df_long[['Hover']].values)

# -- END OF TRADING INTERVAL PRICE CALCULATION LINE CHART --

# -- START OF DISPLAYING THE GENERATION MIX DONUT CHART --

# CASE A. ACTUAL ENERGY <= BCQ
# SCPC, KSPC1, KSPC2, EDC

# CASE B. ACTUAL ENERGY > BCQ
# SCPC, KSPC1, KSPC2, EDC, WESM

# Load the workbooks
total_bcq_nomination_wb = openpyxl.load_workbook('total_bcq_nomination.xlsx')
total_bcq_nomination_sheet = total_bcq_nomination_wb['Sheet']
wesm_exposure_wb = openpyxl.load_workbook('wesm_exposure.xlsx')
wesm_exposure_sheet = wesm_exposure_wb['Sheet']

# Column containing the hour values
hour_column = 'HOUR'

# Get current hour
now = datetime.now()
current_hour = int(now.strftime("%H"))

# Find the hour column index
hour_index = None
for col_idx in range(1, sheet.max_column + 1):
    if sheet.cell(row=1, column=col_idx).value == hour_column:
        hour_index = col_idx
        break

if hour_index is None:
    raise ValueError(f"Column '{hour_column}' not found in the sheet.")

# Function to compare values based on hour
def compare_values(row):
    hour = row[hour_index - 1].value
    if hour == current_hour:
        if row[1].value > row[2].value:
            # Find the row matching the current hour in the second file
            comparison_row = None
            for comparison_row in total_bcq_nomination_sheet.iter_rows():
                if comparison_row[0].value == current_hour:
                    break

            comparison_row2 = None
            for comparison_row2 in wesm_exposure_sheet.iter_rows():
                if comparison_row2[0].value == current_hour:
                    break

            # Check if a matching row was found
            if comparison_row is not None and comparison_row2 is not None:
                # Extract desired values from the matching row
                scpc_value = comparison_row[1].value
                kspc_value = comparison_row[2].value
                kspc1_value = int(kspc_value / 2)
                kspc2_value = int(kspc_value / 2)
                edc_value = comparison_row[3].value
                wesm_value = comparison_row2[3].value

                labels = ['SCPC', 'KSPC1', 'KSPC2', 'EDC', 'WESM']
                sizes = [scpc_value, kspc1_value, kspc2_value, edc_value, wesm_value]

                # Create the donut chart data
                data = [
                    go.Pie(
                        labels=labels,
                        values=sizes,
                        hole=0.5,
                        textinfo='label+percent',
                        textposition='inside',
                        marker={'colors': ['lightcoral', 'lightskyblue', 'lightgreen', 'yellow', 'orange']},
                    )
                ]
                layout = go.Layout(
                    width=600,
                    height=300,
                )
                fig = go.Figure(data=data, layout=layout)
                return fig
            else:
                print(f"No matching hour found in comparison data for {current_hour}")
                return None
        else:
            # Handle the case where ACTUAL_ENERGY is not greater than TOTAL_BCQ_NOMINATION (optional)
            if row[1].value <= row[2].value:
                comparison_row = None
                for comparison_row in total_bcq_nomination_sheet.iter_rows():
                    if comparison_row[0].value == current_hour:
                        break

                if comparison_row is not None:
                    scpc_value = comparison_row[1].value
                    kspc_value = comparison_row[2].value
                    kspc1_value = int(kspc_value / 2)
                    kspc2_value = int(kspc_value / 2)
                    edc_value = comparison_row[3].value

                    labels = ['SCPC', 'KSPC1', 'KSPC2', 'EDC', 'WESM']
                    sizes = [scpc_value, kspc1_value, kspc2_value, edc_value, 0]  # wesm_value is 0 here

                    data = [
                        go.Pie(
                            labels=labels,
                            values=sizes,
                            hole=0.5,
                            textinfo='label+percent',
                            textposition='inside',
                            marker={'colors': ['lightcoral', 'lightskyblue', 'lightgreen', 'yellow', 'orange']},
                        )
                    ]
                    layout = go.Layout(
                        width=600,
                        height=300,
                    )
                    fig = go.Figure(data=data, layout=layout)
                    return fig
                else:
                    print(f"No matching hour found in comparison data for {current_hour}")
                    return None

# Process rows in the sheet (assuming you want to process all rows)
for row in sheet.iter_rows(min_row=2):  # Start from row 2 (assuming header row)
    chart_data = compare_values(row)
    if chart_data is not None:
        break
    
# -- END OF DISPLAYING THE GENERATION MIX DONUT CHART --

col1, col2, col3 = st.columns(3)
# BCQ Nominations per Supplier
with col1:
    st.subheader("BCQ Nominations per Supplier", divider=True)
    st.altair_chart(chart)
# Trading Interval Price Calculation
with col2:
    st.subheader("Trading Interval Price Calculation", divider=True)
    st.plotly_chart(fig_tipc)
# Generation Mix
with col3:
    st.subheader("Generation Mix", divider=True)
    if chart_data:
        st.plotly_chart(figure_or_data=chart_data)