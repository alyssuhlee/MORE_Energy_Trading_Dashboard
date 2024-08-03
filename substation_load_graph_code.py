from mysql.connector import Error
import pandas as pd
import mysql.connector

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
        print("Table created successfully or already exists")

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
        print("MySQL connection is closed")