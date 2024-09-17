import mysql.connector
import streamlit as st

#connection
conn=mysql.connector.connect(
    host = "localhost",
    port = "3306",
    user = "root",
    passwd = "",
    db = "myDb"
)
c=conn.cursor()

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

def view_all_data10():
    c.execute('select * from current_rate order by id asc')
    data = c.fetchall()
    return data