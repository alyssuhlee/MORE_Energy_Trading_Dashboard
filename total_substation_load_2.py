# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:27:41 2021

@author: rtribiano
"""

import pyodbc
import mysql.connector
import pandas as pd
import openpyxl as xl
import shutil
import os
import re
import datetime
import numpy as np
#from datetime import datetime, timedelta

file_loc=r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\station_load_2.csv'
current_day = datetime.datetime.today()

def query_substation_data():
    
    try:
        
        cnx = mysql.connector.connect(user='mepcadmi_guest', password='hJER8pBv8WyS',
                              host=' 192.185.52.175',
                              database='mepcadmi_empower')
        
        query = ("select substation, feeder_no, date_entered, time_entered, load_kw, meter_reading, main_meter  from mepcadmi_empower.substation_load where date_entered = '{}' ").format(current_day.strftime('%Y-%m-%d'))
      
        
        substation_load_df = pd.read_sql(query, cnx,  parse_dates={"date_entered": {"format": "%d/%m/%y"}})
        substation_load_df = substation_load_df.sort_values(by=['date_entered', 'time_entered'])
       #substation_load_df['time_entered'] = substation_load_df['time_entered'].apply(lambda x:x-1)
        
        substation_load_df = pd.pivot_table(substation_load_df, values='load_kw',index = ['date_entered', 'time_entered'], columns='substation', aggfunc= np.sum)
        substation_load_df['10/12.5 MVA MOBILE SUBSTATION'] = 0
        substation_load_df = substation_load_df[['LAPAZ SUBSTATION', 'JARO SUBSTATION', 'MANDURRIAO SUBSTATION', 'MOLO SUBSTATION', 'CITY PROPER SUBSTATION']]
        substation_load_df = substation_load_df.reset_index()
        substation_load_df.columns = ['Date', 'Hour', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6']
        substation_load_df['Total'] = substation_load_df['S1'] + substation_load_df['S2'] + substation_load_df['S3'] + substation_load_df['S4'] + substation_load_df['S5'] + substation_load_df['S6']
        substation_load_df['eS1'] = substation_load_df['S1'] * 1.0001
        substation_load_df['eS2'] = substation_load_df['S2'] * 1.0001
        substation_load_df['eS3'] = substation_load_df['S3'] * 1.0001
        substation_load_df['eS4'] = substation_load_df['S4'] * 1.0001
        substation_load_df['eS5'] = substation_load_df['S5'] * 1.0001
        substation_load_df['eS6'] = substation_load_df['S6'] * 1.0001
        substation_load_df = substation_load_df[substation_load_df['Hour'] != 0] 
        substation_load_df = substation_load_df.fillna(0)
        substation_load_df['eTotal'] = substation_load_df['eS1'] + substation_load_df['eS2'] + substation_load_df['eS3'] + substation_load_df['eS4'] + substation_load_df['eS5'] + substation_load_df['eS6']

        substation_load_df.to_csv(file_loc,index=False)
                
        
        cnx.close()
        
        
        
    except Exception as e:
    
        #cnx.close()
        print(e)
        
        
if __name__ == "__main__":
    
    query_substation_data()