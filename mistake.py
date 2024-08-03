import sqlalchemy
import pandas as pd
import openpyxl as xl
import shutil
import os
import re
import datetime
import numpy as np

file_loc = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\\'
current_day = datetime.datetime.today()


def query_substation_data():
    try:
        # SQLAlchemy connection
        engine = sqlalchemy.create_engine('mysql+mysqlconnector://mepcadmi_guest:hJER8pBv8WyS@192.185.52.175/mepcadmi_empower')

        query = (
            "SELECT substation, feeder_no, date_entered, time_entered, load_kw, meter_reading, main_meter "
            "FROM substation_load "
            "WHERE date_entered = '{}'").format(current_day.strftime('%Y-%m-%d'))

        substation_load_df = pd.read_sql(query, engine, parse_dates={"date_entered": {"format": "%d/%m/%y"}})
        substation_load_df = substation_load_df.sort_values(by=['date_entered', 'time_entered'])

        substation_load_df = pd.pivot_table(substation_load_df, values='load_kw',
                                            index=['date_entered', 'time_entered'], columns='substation',
                                            aggfunc='sum')
        substation_load_df['10 MVA Mobile SS - MS1'] = 0
        substation_load_df['MOLO SUBSTATION'] = 0

        substation_load_df = substation_load_df[
            ['LAPAZ SUBSTATION', 'JARO SUBSTATION', 'MANDURRIAO SUBSTATION', 'MOLO SUBSTATION',
             'DIVERSION SUBSTATION', '10 MVA Mobile SS - MS1', '36 MVA Mobile SS - MS2', '36 MVA Megaworld SS - MGW']]
        substation_load_df = substation_load_df.reset_index()
        substation_load_df.columns = ['Date', 'Hour', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']
        substation_load_df['Total'] = substation_load_df['S1'] + substation_load_df['S2'] + substation_load_df['S3'] + \
                                      substation_load_df['S4'] + substation_load_df['S5'] + substation_load_df['S6'] + \
                                      substation_load_df['S7'] + substation_load_df['S8']
        substation_load_df['eS1'] = substation_load_df['S1'] * 1.0001
        substation_load_df['eS2'] = substation_load_df['S2'] * 1.0001
        substation_load_df['eS3'] = substation_load_df['S3'] * 1.0001
        substation_load_df['eS4'] = substation_load_df['S4'] * 1.0001
        substation_load_df['eS5'] = substation_load_df['S5'] * 1.0001
        substation_load_df['eS6'] = substation_load_df['S6'] * 1.0001
        substation_load_df['eS7'] = substation_load_df['S7'] * 1.0001
        substation_load_df['eS8'] = substation_load_df['S8'] * 1.0001
        substation_load_df = substation_load_df[substation_load_df['Hour'] != 0]
        substation_load_df = substation_load_df.fillna(0)
        substation_load_df['eTotal'] = substation_load_df['eS1'] + substation_load_df['eS2'] + substation_load_df[
            'eS3'] + substation_load_df['eS4'] + substation_load_df['eS5'] + substation_load_df['eS6'] + \
                                       substation_load_df['eS7'] + substation_load_df['eS8']

        substation_load_df.to_csv(file_loc + 'StationLoad.csv', index=False)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    query_substation_data()