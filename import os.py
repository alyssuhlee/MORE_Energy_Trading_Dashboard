import os
import plotly.io as pio
import streamlit as st

# Function to save chart as JSON
def save_chart(chart, file_path):
    try:
        chart_json = pio.to_json(chart)
        with open(file_path, 'w') as f:
            f.write(chart_json)
    except IOError as e:
        st.error(f"Failed to save chart: {e}")

# Function to load saved chart from JSON
def load_chart(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except IOError as e:
        st.error(f"Failed to load chart: {e}")
        return None

# Streamlit component
with st.container():
    file_path_tipc_chart = r"C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\latest_tipc_chart.json"
    
    try:
        latest_chart_tipc = tipc_func()  # Assuming tipc_func() returns a Plotly chart
        st.plotly_chart(latest_chart_tipc)
        save_chart(latest_chart_tipc, file_path_tipc_chart)
    except:
        chart_json_tipc = load_chart(file_path_tipc_chart)
        latest_chart_tipc = pio.from_json(chart_json_tipc)
        st.plotly_chart(latest_chart_tipc)