from datetime import datetime
import os
import pandas as pd
import mysql.connector
import time
import threading 

def find_total():
    directory = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\MORE Trading Node'
    now = datetime.now()
    # Example folder name: 20240711
    date_today = now.strftime("%Y%m%d")
    contents = os.listdir(directory)
    for item in contents:
        if item == date_today:
            folder_path = os.path.join(directory, item) 
            if os.path.isdir(folder_path):
                files_in_folder = os.listdir(folder_path) # MPI_LMP_DIPC_202407110000, etc.
                current_hour = now.strftime("%H")
                if current_hour == '01':
                    first_file_path = os.path.join(folder_path, files_in_folder[1])
                    df = pd.read_csv(first_file_path)
                    pedc_til1 = df.iloc[751,5]
                    pedc_til2 = df.iloc[752,5]
                    stbar_til1 = df.iloc[766,5]
                    total_1st = (pedc_til1 + pedc_til2 + stbar_til1)/3
                    second_file_path = os.path.join(folder_path, files_in_folder[2])
                    second_df = pd.read_csv(second_file_path)
                    second_pedc_til1 = second_df.iloc[751,5]
                    second_pedc_til2 = second_df.iloc[752,5]
                    second_stbar_til1 = second_df.iloc[766,5]
                    total_2nd = (second_pedc_til1 + second_pedc_til2 + second_stbar_til1)/3
                    third_file_path = os.path.join(folder_path, files_in_folder[3])
                    third_df = pd.read_csv(third_file_path)
                    third_pedc_til1 = third_df.iloc[751,5]
                    third_pedc_til2 = third_df.iloc[752,5]
                    third_stbar_til1 = third_df.iloc[766,5]
                    total_3rd = (third_pedc_til1 + third_pedc_til2 + third_stbar_til1)/3
                    fourth_file_path = os.path.join(folder_path, files_in_folder[4])
                    fourth_df = pd.read_csv(fourth_file_path)
                    fourth_pedc_til1 = fourth_df.iloc[751,5]
                    fourth_pedc_til2 = fourth_df.iloc[752,5]
                    fourth_stbar_til1 = fourth_df.iloc[766,5]
                    total_4th = (fourth_pedc_til1 + fourth_pedc_til2 + fourth_stbar_til1)/3
                    fifth_file_path = os.path.join(folder_path, files_in_folder[5])
                    fifth_df = pd.read_csv(fifth_file_path)
                    fifth_pedc_til1 = fifth_df.iloc[751,5]
                    fifth_pedc_til2 = fifth_df.iloc[752,5]
                    fifth_stbar_til1 = fifth_df.iloc[766,5]
                    total_5th = (fifth_pedc_til1 + fifth_pedc_til2 + fifth_stbar_til1)/3
                    sixth_file_path = os.path.join(folder_path, files_in_folder[6])
                    sixth_df = pd.read_csv(sixth_file_path)
                    sixth_pedc_til1 = sixth_df.iloc[751,5]
                    sixth_pedc_til2 = sixth_df.iloc[752,5]
                    sixth_stbar_til1 = sixth_df.iloc[766,5]
                    total_6th = (sixth_pedc_til1 + sixth_pedc_til2 + sixth_stbar_til1)/3
                    seventh_file_path = os.path.join(folder_path, files_in_folder[7])
                    seventh_df = pd.read_csv(seventh_file_path)
                    seventh_pedc_til1 = seventh_df.iloc[751,5]
                    seventh_pedc_til2 = seventh_df.iloc[752,5]
                    seventh_stbar_til1 = seventh_df.iloc[766,5]
                    total_7th = (seventh_pedc_til1 + seventh_pedc_til2 + seventh_stbar_til1)/3
                    eighth_file_path = os.path.join(folder_path, files_in_folder[8])
                    eighth_df = pd.read_csv(eighth_file_path)
                    eighth_pedc_til1 = eighth_df.iloc[751,5]
                    eighth_pedc_til2 = eighth_df.iloc[752,5]
                    eighth_stbar_til1 = eighth_df.iloc[766,5]
                    total_8th = (eighth_pedc_til1 + eighth_pedc_til2 + eighth_stbar_til1)/3
                    ninth_file_path = os.path.join(folder_path, files_in_folder[9])
                    ninth_df = pd.read_csv(ninth_file_path)
                    ninth_pedc_til1 = ninth_df.iloc[751,5]
                    ninth_pedc_til2 = eighth_df.iloc[752,5]
                    ninth_stbar_til1 = ninth_df.iloc[766,5]
                    total_9th = (ninth_pedc_til1 + ninth_pedc_til2 + ninth_stbar_til1)/3
                    tenth_file_path = os.path.join(folder_path, files_in_folder[10])
                    tenth_df = pd.read_csv(tenth_file_path)
                    tenth_pedc_til1 = tenth_df.iloc[751,5]
                    tenth_pedc_til2 = tenth_df.iloc[752,5]
                    tenth_stbar_til1 = tenth_df.iloc[766,5]
                    total_10th = (tenth_pedc_til1 + tenth_pedc_til2 + tenth_stbar_til1)/3
                    eleventh_file_path = os.path.join(folder_path, files_in_folder[11])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    eleventh_pedc_til1 = eleventh_df.iloc[751,5]
                    eleventh_pedc_til2 = eleventh_df.iloc[752,5]
                    eleventh_stbar_til1 = eleventh_df.iloc[766,5]
                    total_11th = (eleventh_pedc_til1 + eleventh_pedc_til2 + eleventh_stbar_til1)/3
                    twelvth_file_path = os.path.join(folder_path, files_in_folder[12])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    twelvth_pedc_til1 = twelvth_df.iloc[751,5]
                    twelvth_pedc_til2 = twelvth_df.iloc[752,5]
                    twelvth_stbar_til1 = twelvth_df.iloc[766,5]
                    total_12th = (twelvth_pedc_til1 + twelvth_pedc_til2 + twelvth_stbar_til1)/3
                    final_total = (total_1st + total_2nd + total_3rd + total_4th + total_5th + total_6th + total_7th + total_8th + total_9th + total_10th + total_11th + total_12th)/12
                    return final_total
                elif current_hour == '02':
                    first_file_path = os.path.join(folder_path, files_in_folder[13])
                    df = pd.read_csv(first_file_path)
                    pedc_til1 = df.iloc[751,5]
                    pedc_til2 = df.iloc[752,5]
                    stbar_til1 = df.iloc[766,5]
                    total_1st = (pedc_til1 + pedc_til2 + stbar_til1)/3
                    second_file_path = os.path.join(folder_path, files_in_folder[14])
                    second_df = pd.read_csv(second_file_path)
                    second_pedc_til1 = second_df.iloc[751,5]
                    second_pedc_til2 = second_df.iloc[752,5]
                    second_stbar_til1 = second_df.iloc[766,5]
                    total_2nd = (second_pedc_til1 + second_pedc_til2 + second_stbar_til1)/3
                    third_file_path = os.path.join(folder_path, files_in_folder[15])
                    third_df = pd.read_csv(third_file_path)
                    third_pedc_til1 = third_df.iloc[751,5]
                    third_pedc_til2 = third_df.iloc[752,5]
                    third_stbar_til1 = third_df.iloc[766,5]
                    total_3rd = (third_pedc_til1 + third_pedc_til2 + third_stbar_til1)/3
                    fourth_file_path = os.path.join(folder_path, files_in_folder[16])
                    fourth_df = pd.read_csv(fourth_file_path)
                    fourth_pedc_til1 = fourth_df.iloc[751,5]
                    fourth_pedc_til2 = fourth_df.iloc[752,5]
                    fourth_stbar_til1 = fourth_df.iloc[766,5]
                    total_4th = (fourth_pedc_til1 + fourth_pedc_til2 + fourth_stbar_til1)/3
                    fifth_file_path = os.path.join(folder_path, files_in_folder[17])
                    fifth_df = pd.read_csv(fifth_file_path)
                    fifth_pedc_til1 = fifth_df.iloc[751,5]
                    fifth_pedc_til2 = fifth_df.iloc[752,5]
                    fifth_stbar_til1 = fifth_df.iloc[766,5]
                    total_5th = (fifth_pedc_til1 + fifth_pedc_til2 + fifth_stbar_til1)/3
                    sixth_file_path = os.path.join(folder_path, files_in_folder[18])
                    sixth_df = pd.read_csv(sixth_file_path)
                    sixth_pedc_til1 = sixth_df.iloc[751,5]
                    sixth_pedc_til2 = sixth_df.iloc[752,5]
                    sixth_stbar_til1 = sixth_df.iloc[766,5]
                    total_6th = (sixth_pedc_til1 + sixth_pedc_til2 + sixth_stbar_til1)/3
                    seventh_file_path = os.path.join(folder_path, files_in_folder[19])
                    seventh_df = pd.read_csv(seventh_file_path)
                    seventh_pedc_til1 = seventh_df.iloc[751,5]
                    seventh_pedc_til2 = seventh_df.iloc[752,5]
                    seventh_stbar_til1 = seventh_df.iloc[766,5]
                    total_7th = (seventh_pedc_til1 + seventh_pedc_til2 + seventh_stbar_til1)/3
                    eighth_file_path = os.path.join(folder_path, files_in_folder[20])
                    eighth_df = pd.read_csv(eighth_file_path)
                    eighth_pedc_til1 = eighth_df.iloc[751,5]
                    eighth_pedc_til2 = eighth_df.iloc[752,5]
                    eighth_stbar_til1 = eighth_df.iloc[766,5]
                    total_8th = (eighth_pedc_til1 + eighth_pedc_til2 + eighth_stbar_til1)/3
                    ninth_file_path = os.path.join(folder_path, files_in_folder[21])
                    ninth_df = pd.read_csv(ninth_file_path)
                    ninth_pedc_til1 = ninth_df.iloc[751,5]
                    ninth_pedc_til2 = eighth_df.iloc[752,5]
                    ninth_stbar_til1 = ninth_df.iloc[766,5]
                    total_9th = (ninth_pedc_til1 + ninth_pedc_til2 + ninth_stbar_til1)/3
                    tenth_file_path = os.path.join(folder_path, files_in_folder[22])
                    tenth_df = pd.read_csv(tenth_file_path)
                    tenth_pedc_til1 = tenth_df.iloc[751,5]
                    tenth_pedc_til2 = tenth_df.iloc[752,5]
                    tenth_stbar_til1 = tenth_df.iloc[766,5]
                    total_10th = (tenth_pedc_til1 + tenth_pedc_til2 + tenth_stbar_til1)/3
                    eleventh_file_path = os.path.join(folder_path, files_in_folder[23])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    eleventh_pedc_til1 = eleventh_df.iloc[751,5]
                    eleventh_pedc_til2 = eleventh_df.iloc[752,5]
                    eleventh_stbar_til1 = eleventh_df.iloc[766,5]
                    total_11th = (eleventh_pedc_til1 + eleventh_pedc_til2 + eleventh_stbar_til1)/3
                    twelvth_file_path = os.path.join(folder_path, files_in_folder[24])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    twelvth_pedc_til1 = twelvth_df.iloc[751,5]
                    twelvth_pedc_til2 = twelvth_df.iloc[752,5]
                    twelvth_stbar_til1 = twelvth_df.iloc[766,5]
                    total_12th = (twelvth_pedc_til1 + twelvth_pedc_til2 + twelvth_stbar_til1)/3
                    final_total = (total_1st + total_2nd + total_3rd + total_4th + total_5th + total_6th + total_7th + total_8th + total_9th + total_10th + total_11th + total_12th)/12
                    return final_total
                
# Function to insert value into MySQL database
def insert_into_mysql(conn, final_total):
    try:
        cursor = conn.cursor()
        sql = "INSERT INTO more_trading_node (final_total) VALUES (%s)"
        cursor.execute(sql, (final_total,))
        conn.commit()  # Commit the transaction
        cursor.close()
        print(f"Value {final_total} inserted successfully into MySQL.")
    except mysql.connector.Error as e:
        print(f"Error inserting into MySQL: {e}")
    except Exception as e:
        print(f"Error: {e}")

def run_continuously(conn):
    while True:
        final_total = find_total()
        if final_total is not None:
            insert_into_mysql(conn, final_total)
        time.sleep(3600)
    
def main():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='myDb',
            user='root',
            password=''
        )
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS more_trading_node (
                id INT AUTO_INCREMENT PRIMARY KEY,
                final_total FLOAT(10, 2) NOT NULL,
                insert_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cursor.close()
        continuous_thread = threading.Thread(target=run_continuously, args=(conn,))
        continuous_thread.start()
        continuous_thread.join()

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    main()