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

                    try: 
                        first_file_path = os.path.join(folder_path, files_in_folder[1])
                        second_file_path = os.path.join(folder_path, files_in_folder[2])
                        third_file_path = os.path.join(folder_path, files_in_folder[3])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[4])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[5])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[6])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[7])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[8])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[9])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[10])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[11])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[12])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                    
                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                    
                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        
                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        
                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        
                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        
                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        
                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        
                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                    
                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                    except:
                        return None
                
                elif current_hour == '02':

                    try:

                        first_file_path = os.path.join(folder_path, files_in_folder[13])
                        second_file_path = os.path.join(folder_path, files_in_folder[14])
                        third_file_path = os.path.join(folder_path, files_in_folder[15])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[16])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[17])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[18])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[19])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[20])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[21])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[22])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[23])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[24])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3


                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                        
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:
                            
                        first_file_path = os.path.join(folder_path, files_in_folder[1])
                        second_file_path = os.path.join(folder_path, files_in_folder[2])
                        third_file_path = os.path.join(folder_path, files_in_folder[3])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[4])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[5])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[6])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[7])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[8])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[9])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[10])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[11])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[12])
                        
                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                    
                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                    
                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        
                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        
                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        
                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        
                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        
                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        
                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                    
                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '03':
                    try: 
                        first_file_path = os.path.join(folder_path, files_in_folder[25])
                        second_file_path = os.path.join(folder_path, files_in_folder[26])
                        third_file_path = os.path.join(folder_path, files_in_folder[27])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[28])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[29])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[30])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[31])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[32])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[33])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[34])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[35])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[36])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3


                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_file_path = os.path.join(folder_path, files_in_folder[28])
                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                        
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[13])
                        second_file_path = os.path.join(folder_path, files_in_folder[14])
                        third_file_path = os.path.join(folder_path, files_in_folder[15])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[16])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[17])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[18])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[19])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[20])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[21])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[22])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[23])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[24])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3


                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                        
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                elif current_hour == '04':
                    try: 
                        first_file_path = os.path.join(folder_path, files_in_folder[37])
                        second_file_path = os.path.join(folder_path, files_in_folder[38])
                        third_file_path = os.path.join(folder_path, files_in_folder[39])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[40])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[41])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[42])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[43])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[44])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[45])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[46])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[47])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[48])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                    except:

                        first_file_path = os.path.join(folder_path, files_in_folder[25])
                        second_file_path = os.path.join(folder_path, files_in_folder[26])
                        third_file_path = os.path.join(folder_path, files_in_folder[27])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[28])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[29])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[30])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[31])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[32])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[33])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[34])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[35])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[36])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3


                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_file_path = os.path.join(folder_path, files_in_folder[28])
                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                        
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '05':

                    try: 
                        first_file_path = os.path.join(folder_path, files_in_folder[49])
                        second_file_path = os.path.join(folder_path, files_in_folder[50])
                        third_file_path = os.path.join(folder_path, files_in_folder[51])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[52])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[53])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[54])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[55])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[56])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[57])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[58])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[59])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[60])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                    except:

                        first_file_path = os.path.join(folder_path, files_in_folder[37])
                        second_file_path = os.path.join(folder_path, files_in_folder[38])
                        third_file_path = os.path.join(folder_path, files_in_folder[39])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[40])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[41])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[42])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[43])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[44])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[45])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[46])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[47])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[48])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '06':

                    try:
                        first_file_path = os.path.join(folder_path, files_in_folder[61])
                        second_file_path = os.path.join(folder_path, files_in_folder[62])
                        third_file_path = os.path.join(folder_path, files_in_folder[63])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[64])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[65])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[66])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[67])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[68])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[69])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[70])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[71])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[72])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[49])
                        second_file_path = os.path.join(folder_path, files_in_folder[50])
                        third_file_path = os.path.join(folder_path, files_in_folder[51])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[52])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[53])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[54])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[55])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[56])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[57])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[58])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[59])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[60])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '07':

                    try: 

                        first_file_path = os.path.join(folder_path, files_in_folder[73])
                        second_file_path = os.path.join(folder_path, files_in_folder[74])
                        third_file_path = os.path.join(folder_path, files_in_folder[75])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[76])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[77])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[78])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[79])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[80])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[81])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[82])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[83])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[84])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[61])
                        second_file_path = os.path.join(folder_path, files_in_folder[62])
                        third_file_path = os.path.join(folder_path, files_in_folder[63])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[64])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[65])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[66])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[67])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[68])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[69])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[70])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[71])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[72])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '08':

                    try: 

                        first_file_path = os.path.join(folder_path, files_in_folder[85])
                        second_file_path = os.path.join(folder_path, files_in_folder[86])
                        third_file_path = os.path.join(folder_path, files_in_folder[87])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[88])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[89])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[90])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[91])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[92])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[93])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[94])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[95])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[96])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:

                        first_file_path = os.path.join(folder_path, files_in_folder[73])
                        second_file_path = os.path.join(folder_path, files_in_folder[74])
                        third_file_path = os.path.join(folder_path, files_in_folder[75])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[76])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[77])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[78])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[79])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[80])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[81])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[82])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[83])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[84])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '09':

                    try: 
                        first_file_path = os.path.join(folder_path, files_in_folder[97])
                        second_file_path = os.path.join(folder_path, files_in_folder[98])
                        third_file_path = os.path.join(folder_path, files_in_folder[99])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[100])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[101])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[102])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[103])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[104])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[105])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[106])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[107])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[108])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:

                        first_file_path = os.path.join(folder_path, files_in_folder[85])
                        second_file_path = os.path.join(folder_path, files_in_folder[86])
                        third_file_path = os.path.join(folder_path, files_in_folder[87])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[88])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[89])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[90])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[91])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[92])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[93])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[94])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[95])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[96])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '10':

                    try:
                        first_file_path = os.path.join(folder_path, files_in_folder[109])
                        second_file_path = os.path.join(folder_path, files_in_folder[110])
                        third_file_path = os.path.join(folder_path, files_in_folder[111])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[112])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[113])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[114])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[115])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[116])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[117])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[118])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[119])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[120])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                    
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_file_path = os.path.join(folder_path, files_in_folder[114])
                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[97])
                        second_file_path = os.path.join(folder_path, files_in_folder[98])
                        third_file_path = os.path.join(folder_path, files_in_folder[99])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[100])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[101])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[102])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[103])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[104])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[105])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[106])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[107])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[108])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                elif current_hour == '11':
                    try: 
                        first_file_path = os.path.join(folder_path, files_in_folder[121])
                        second_file_path = os.path.join(folder_path, files_in_folder[122])
                        third_file_path = os.path.join(folder_path, files_in_folder[123])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[124])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[125])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[126])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[127])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[128])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[129])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[130])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[131])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[132])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                
                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[109])
                        second_file_path = os.path.join(folder_path, files_in_folder[110])
                        third_file_path = os.path.join(folder_path, files_in_folder[111])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[112])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[113])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[114])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[115])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[116])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[117])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[118])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[119])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[120])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                    
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_file_path = os.path.join(folder_path, files_in_folder[114])
                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '12':
                    try: 
                        first_file_path = os.path.join(folder_path, files_in_folder[133])
                        second_file_path = os.path.join(folder_path, files_in_folder[134])
                        third_file_path = os.path.join(folder_path, files_in_folder[135])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[136])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[137])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[138])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[139])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[140])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[141])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[142])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[143])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[144])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[121])
                        second_file_path = os.path.join(folder_path, files_in_folder[122])
                        third_file_path = os.path.join(folder_path, files_in_folder[123])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[124])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[125])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[126])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[127])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[128])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[129])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[130])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[131])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[132])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '13':

                    try: 

                        first_file_path = os.path.join(folder_path, files_in_folder[145])
                        second_file_path = os.path.join(folder_path, files_in_folder[146])
                        third_file_path = os.path.join(folder_path, files_in_folder[147])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[148])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[149])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[150])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[151])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[152])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[153])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[154])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[155])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[156])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                    
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[121])
                        second_file_path = os.path.join(folder_path, files_in_folder[122])
                        third_file_path = os.path.join(folder_path, files_in_folder[123])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[124])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[125])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[126])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[127])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[128])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[129])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[130])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[131])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[132])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '14':
                    try:
                        first_file_path = os.path.join(folder_path, files_in_folder[157])
                        second_file_path = os.path.join(folder_path, files_in_folder[158])
                        third_file_path = os.path.join(folder_path, files_in_folder[159])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[160])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[161])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[162])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[163])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[164])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[165])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[166])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[167])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[168])
                    
                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_file_path = os.path.join(folder_path, files_in_folder[168])
                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[145])
                        second_file_path = os.path.join(folder_path, files_in_folder[146])
                        third_file_path = os.path.join(folder_path, files_in_folder[147])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[148])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[149])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[150])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[151])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[152])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[153])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[154])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[155])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[156])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                    
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '15':

                    try:
                        first_file_path = os.path.join(folder_path, files_in_folder[169])
                        second_file_path = os.path.join(folder_path, files_in_folder[170])
                        third_file_path = os.path.join(folder_path, files_in_folder[171])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[172])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[173])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[174])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[175])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[176])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[177])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[178])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[179])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[180])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                    
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:

                        first_file_path = os.path.join(folder_path, files_in_folder[157])
                        second_file_path = os.path.join(folder_path, files_in_folder[158])
                        third_file_path = os.path.join(folder_path, files_in_folder[159])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[160])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[161])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[162])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[163])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[164])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[165])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[166])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[167])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[168])
                    
                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_file_path = os.path.join(folder_path, files_in_folder[168])
                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
            
                elif current_hour == '16':
                    try:
                        first_file_path = os.path.join(folder_path, files_in_folder[181])
                        second_file_path = os.path.join(folder_path, files_in_folder[182])
                        third_file_path = os.path.join(folder_path, files_in_folder[183])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[184])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[185])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[186])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[187])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[188])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[189])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[190])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[191])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[192])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[169])
                        second_file_path = os.path.join(folder_path, files_in_folder[170])
                        third_file_path = os.path.join(folder_path, files_in_folder[171])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[172])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[173])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[174])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[175])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[176])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[177])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[178])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[179])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[180])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                    
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '17':
                    try:
                        first_file_path = os.path.join(folder_path, files_in_folder[193])
                        second_file_path = os.path.join(folder_path, files_in_folder[194])
                        third_file_path = os.path.join(folder_path, files_in_folder[195])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[196])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[197])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[198])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[199])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[200])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[201])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[202])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[203])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[204])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[181])
                        second_file_path = os.path.join(folder_path, files_in_folder[182])
                        third_file_path = os.path.join(folder_path, files_in_folder[183])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[184])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[185])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[186])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[187])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[188])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[189])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[190])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[191])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[192])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                
                elif current_hour == '18':
                    try:
                        first_file_path = os.path.join(folder_path, files_in_folder[205])
                        second_file_path = os.path.join(folder_path, files_in_folder[206])
                        third_file_path = os.path.join(folder_path, files_in_folder[207])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[208])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[209])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[210])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[211])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[212])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[213])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[214])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[215])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[216])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                    
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                    
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[193])
                        second_file_path = os.path.join(folder_path, files_in_folder[194])
                        third_file_path = os.path.join(folder_path, files_in_folder[195])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[196])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[197])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[198])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[199])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[200])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[201])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[202])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[203])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[204])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '19':
                    try:
                        first_file_path = os.path.join(folder_path, files_in_folder[217])
                        second_file_path = os.path.join(folder_path, files_in_folder[218])
                        third_file_path = os.path.join(folder_path, files_in_folder[219])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[220])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[221])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[222])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[223])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[224])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[225])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[226])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[227])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[228])
                    
                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:

                        first_file_path = os.path.join(folder_path, files_in_folder[205])
                        second_file_path = os.path.join(folder_path, files_in_folder[206])
                        third_file_path = os.path.join(folder_path, files_in_folder[207])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[208])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[209])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[210])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[211])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[212])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[213])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[214])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[215])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[216])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                    
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                    
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '20':

                    try:
                        first_file_path = os.path.join(folder_path, files_in_folder[229])
                        second_file_path = os.path.join(folder_path, files_in_folder[230])
                        third_file_path = os.path.join(folder_path, files_in_folder[231])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[232])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[233])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[234])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[235])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[236])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[237])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[238])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[239])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[240])
                    
                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[217])
                        second_file_path = os.path.join(folder_path, files_in_folder[218])
                        third_file_path = os.path.join(folder_path, files_in_folder[219])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[220])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[221])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[222])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[223])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[224])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[225])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[226])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[227])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[228])
                    
                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '21': 
                    try:
                        first_file_path = os.path.join(folder_path, files_in_folder[241])
                        second_file_path = os.path.join(folder_path, files_in_folder[242])
                        third_file_path = os.path.join(folder_path, files_in_folder[243])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[244])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[245])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[246])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[247])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[248])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[249])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[250])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[251])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[252])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[229])
                        second_file_path = os.path.join(folder_path, files_in_folder[230])
                        third_file_path = os.path.join(folder_path, files_in_folder[231])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[232])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[233])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[234])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[235])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[236])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[237])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[238])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[239])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[240])
                    
                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                elif current_hour == '22':
                    try:
                        first_file_path = os.path.join(folder_path, files_in_folder[253])
                        second_file_path = os.path.join(folder_path, files_in_folder[254])
                        third_file_path = os.path.join(folder_path, files_in_folder[255])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[256])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[257])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[258])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[259])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[260])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[261])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[262])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[263])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[264])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:

                        first_file_path = os.path.join(folder_path, files_in_folder[241])
                        second_file_path = os.path.join(folder_path, files_in_folder[242])
                        third_file_path = os.path.join(folder_path, files_in_folder[243])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[244])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[245])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[246])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[247])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[248])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[249])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[250])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[251])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[252])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '23':
                    try:
                        first_file_path = os.path.join(folder_path, files_in_folder[265])
                        second_file_path = os.path.join(folder_path, files_in_folder[266])
                        third_file_path = os.path.join(folder_path, files_in_folder[267])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[268])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[269])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[270])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[271])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[272])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[273])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[274])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[275])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[276])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)
                    
                    except:
                        
                        first_file_path = os.path.join(folder_path, files_in_folder[253])
                        second_file_path = os.path.join(folder_path, files_in_folder[254])
                        third_file_path = os.path.join(folder_path, files_in_folder[255])
                        fourth_file_path = os.path.join(folder_path, files_in_folder[256])
                        fifth_file_path = os.path.join(folder_path, files_in_folder[257])
                        sixth_file_path = os.path.join(folder_path, files_in_folder[258])
                        seventh_file_path = os.path.join(folder_path, files_in_folder[259])
                        eighth_file_path = os.path.join(folder_path, files_in_folder[260])
                        ninth_file_path = os.path.join(folder_path, files_in_folder[261])
                        tenth_file_path = os.path.join(folder_path, files_in_folder[262])
                        eleventh_file_path = os.path.join(folder_path, files_in_folder[263])
                        twelvth_file_path = os.path.join(folder_path, files_in_folder[264])

                        df = pd.read_csv(first_file_path)

                        search_value_1 = '08PEDC_T1L1'
                        matching_row_1 = df[df['RESOURCE_NAME'] == search_value_1]
                        file_08PEDC_T1L1_1 = matching_row_1['DIPC_PRICE'].values[0]

                        search_value_2 = '08PEDC_T1L2'
                        matching_row_2 = df[df['RESOURCE_NAME'] == search_value_2]
                        file_08PEDC_T1L2_1 = matching_row_2['DIPC_PRICE'].values[0]

                        search_value_3 = '08STBAR_T1L1'
                        matching_row_3 = df[df['RESOURCE_NAME'] == search_value_3]
                        file_08STBAR_T1L1_1 = matching_row_3['DIPC_PRICE'].values[0]

                        average_1 = (file_08PEDC_T1L1_1 + file_08PEDC_T1L2_1 + file_08STBAR_T1L1_1)/3

                        second_df = pd.read_csv(second_file_path)

                        search_value_4 = '08PEDC_T1L1'
                        matching_row_4 = second_df[second_df['RESOURCE_NAME'] == search_value_4]
                        file_08PEDC_T1L1_4 = matching_row_4['DIPC_PRICE'].values[0]
                        
                        search_value_5 = '08PEDC_T1L2'
                        matching_row_5 = second_df[second_df['RESOURCE_NAME'] == search_value_5]
                        file_08PEDC_T1L2_5 = matching_row_5['DIPC_PRICE'].values[0]

                        search_value_6 = '08STBAR_T1L1'
                        matching_row_6 = df[df['RESOURCE_NAME'] == search_value_6]
                        file_08STBAR_T1L1_6 = matching_row_6['DIPC_PRICE'].values[0]

                        average_2 = (file_08PEDC_T1L1_4 + file_08PEDC_T1L2_5 + file_08STBAR_T1L1_6)/3

                        third_df = pd.read_csv(third_file_path)

                        search_value_7 = '08PEDC_T1L1'
                        matching_row_7 = third_df[third_df['RESOURCE_NAME'] == search_value_7]
                        file_08PEDC_T1L1_7 = matching_row_7['DIPC_PRICE'].values[0]

                        search_value_8 = '08PEDC_T1L2'
                        matching_row_8 = third_df[third_df['RESOURCE_NAME'] == search_value_8]
                        file_08PEDC_T1L2_8 = matching_row_8['DIPC_PRICE'].values[0]

                        search_value_9 = '08STBAR_T1L1'
                        matching_row_9 = third_df[third_df['RESOURCE_NAME'] == search_value_9]
                        file_08STBAR_T1L1_9 = matching_row_9['DIPC_PRICE'].values[0]

                        average_3 = (file_08PEDC_T1L1_7 + file_08PEDC_T1L2_8 + file_08STBAR_T1L1_9)/3

                        fourth_df = pd.read_csv(fourth_file_path)

                        search_value_10 = '08PEDC_T1L1'
                        matching_row_10 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_10]
                        file_08PEDC_T1L1_10 = matching_row_10['DIPC_PRICE'].values[0]

                        search_value_11 = '08PEDC_T1L2'
                        matching_row_11 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_11]
                        file_08PEDC_T1L2_11 = matching_row_11['DIPC_PRICE'].values[0]

                        search_value_12 = '08STBAR_T1L1'
                        matching_row_12 = fourth_df[fourth_df['RESOURCE_NAME'] == search_value_12]
                        file_08STBAR_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

                        average_4 = (file_08PEDC_T1L1_10 + file_08PEDC_T1L2_11 + file_08STBAR_T1L1_12)/3

                        fifth_df = pd.read_csv(fifth_file_path)

                        search_value_13 = '08PEDC_T1L1'
                        matching_row_13 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_13]
                        file_08PEDC_T1L1_13 = matching_row_13['DIPC_PRICE'].values[0]

                        search_value_14 = '08PEDC_T1L2'
                        matching_row_14 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_14]
                        file_08PEDC_T1L2_14 = matching_row_14['DIPC_PRICE'].values[0]

                        search_value_15 = '08STBAR_T1L1'
                        matching_row_15 = fifth_df[fifth_df['RESOURCE_NAME'] == search_value_15]
                        file_08STBAR_T1L1_15 = matching_row_15['DIPC_PRICE'].values[0]

                        average_5 = (file_08PEDC_T1L1_13 + file_08PEDC_T1L2_14 + file_08STBAR_T1L1_15)/3

                        sixth_df = pd.read_csv(sixth_file_path)

                        search_value_16 = '08PEDC_T1L1'
                        matching_row_16 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_16]
                        file_08PEDC_T1L1_16 = matching_row_16['DIPC_PRICE'].values[0]

                        search_value_17 = '08PEDC_T1L2'
                        matching_row_17 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_17]
                        file_08PEDC_T1L2_17 = matching_row_17['DIPC_PRICE'].values[0]

                        search_value_18 = '08STBAR_T1L1'
                        matching_row_18 = sixth_df[sixth_df['RESOURCE_NAME'] == search_value_18]
                        file_08STBAR_T1L1_18 = matching_row_18['DIPC_PRICE'].values[0]

                        average_6 = (file_08PEDC_T1L1_16 + file_08PEDC_T1L2_17 + file_08STBAR_T1L1_18)/3

                        seventh_df = pd.read_csv(seventh_file_path)

                        search_value_19 = '08PEDC_T1L1'
                        matching_row_19 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_19]
                        file_08PEDC_T1L1_19 = matching_row_19['DIPC_PRICE'].values[0]

                        search_value_20 = '08PEDC_T1L2'
                        matching_row_20 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_20]
                        file_08PEDC_T1L2_20 = matching_row_20['DIPC_PRICE'].values[0]

                        search_value_21 = '08STBAR_T1L1'
                        matching_row_21 = seventh_df[seventh_df['RESOURCE_NAME'] == search_value_21]
                        file_08STBAR_T1L1_21 = matching_row_21['DIPC_PRICE'].values[0]

                        average_7 = (file_08PEDC_T1L1_19 + file_08PEDC_T1L2_20 + file_08STBAR_T1L1_21)/3

                        eighth_df = pd.read_csv(eighth_file_path)

                        search_value_22 = '08PEDC_T1L1'
                        matching_row_22 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_22]
                        file_08PEDC_T1L1_22 = matching_row_22['DIPC_PRICE'].values[0]

                        search_value_23 = '08PEDC_T1L2'
                        matching_row_23 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_23]
                        file_08PEDC_T1L2_23 = matching_row_23['DIPC_PRICE'].values[0]

                        search_value_24 = '08STBAR_T1L1'
                        matching_row_24 = eighth_df[eighth_df['RESOURCE_NAME'] == search_value_24]
                        file_08STBAR_T1L1_24 = matching_row_24['DIPC_PRICE'].values[0]

                        average_8 = (file_08PEDC_T1L1_22 + file_08PEDC_T1L2_23 + file_08STBAR_T1L1_24)/3
                            
                        ninth_df = pd.read_csv(ninth_file_path)

                        search_value_25 = '08PEDC_T1L1'
                        matching_row_25 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_25]
                        file_08PEDC_T1L1_25 = matching_row_25['DIPC_PRICE'].values[0]

                        search_value_26 = '08PEDC_T1L2'
                        matching_row_26 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_26]
                        file_08PEDC_T1L2_26 = matching_row_26['DIPC_PRICE'].values[0]

                        search_value_27 = '08STBAR_T1L1'
                        matching_row_27 = ninth_df[ninth_df['RESOURCE_NAME'] == search_value_27]
                        file_08STBAR_T1L1_27 = matching_row_27['DIPC_PRICE'].values[0]

                        average_9 = (file_08PEDC_T1L1_25 + file_08PEDC_T1L2_26 + file_08STBAR_T1L1_27)/3

                        tenth_df = pd.read_csv(tenth_file_path)

                        search_value_28 = '08PEDC_T1L1'
                        matching_row_28 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_28]
                        file_08PEDC_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

                        search_value_29 = '08PEDC_T1L2'
                        matching_row_29 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_29]
                        file_08PEDC_T1L2_29 = matching_row_29['DIPC_PRICE'].values[0]

                        search_value_30 = '08STBAR_T1L1'
                        matching_row_30 = tenth_df[tenth_df['RESOURCE_NAME'] == search_value_30]
                        file_08STBAR_T1L1_30 = matching_row_30['DIPC_PRICE'].values[0]

                        average_10 = (file_08PEDC_T1L1_28 + file_08PEDC_T1L2_29 + file_08STBAR_T1L1_30)/3

                        eleventh_df = pd.read_csv(eleventh_file_path)

                        search_value_31 = '08PEDC_T1L1'
                        matching_row_31 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_31]
                        file_08PEDC_T1L1_31 = matching_row_31['DIPC_PRICE'].values[0]

                        search_value_32 = '08PEDC_T1L2'
                        matching_row_32 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_32]
                        file_08PEDC_T1L2_32 = matching_row_32['DIPC_PRICE'].values[0]

                        search_value_33 = '08STBAR_T1L1'
                        matching_row_33 = eleventh_df[eleventh_df['RESOURCE_NAME'] == search_value_33]
                        file_08STBAR_T1L1_33 = matching_row_33['DIPC_PRICE'].values[0]

                        average_11 = (file_08PEDC_T1L1_31 + file_08PEDC_T1L2_32 + file_08STBAR_T1L1_33)/3

                        twelvth_df = pd.read_csv(twelvth_file_path)

                        search_value_34 = '08PEDC_T1L1'
                        matching_row_34 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_34]
                        file_08PEDC_T1L1_34 = matching_row_34['DIPC_PRICE'].values[0]
                        
                        search_value_35 = '08PEDC_T1L2'
                        matching_row_35 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_35]
                        file_08PEDC_T1L2_35 = matching_row_35['DIPC_PRICE'].values[0]

                        search_value_36 = '08STBAR_T1L1'
                        matching_row_36 = twelvth_df[twelvth_df['RESOURCE_NAME'] == search_value_36]
                        file_08STBAR_T1L1_36 = matching_row_36['DIPC_PRICE'].values[0]

                        average_12 = (file_08PEDC_T1L1_34 + file_08PEDC_T1L2_35 + file_08STBAR_T1L1_36)/3

                        final_total = (average_1 + average_2 + average_3 + average_4 + average_5 + average_6 + average_7 + average_8 + average_9 + average_10 + average_11 + average_12)/12
                        
                        return float(final_total)

                elif current_hour == '00':
                        return None

# MORE Nodes (RESOURCE_NAME) - 08PEDC_T1L1, 08PEDC_T1L2, 08STBAR_T1L1 

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
        time.sleep(60)
    
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