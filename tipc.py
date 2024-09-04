from datetime import datetime
import os
import pandas as pd
import mysql.connector

def find_total_tipc():
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
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[2])
                    second_df = pd.read_csv(second_file_path)
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[3])
                    third_df = pd.read_csv(third_file_path)
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[4])
                    fourth_df = pd.read_csv(fourth_file_path)
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[5])
                    fifth_df = pd.read_csv(fifth_file_path)
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[6])
                    sixth_df = pd.read_csv(sixth_file_path)
                   
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[7])
                    seventh_df = pd.read_csv(seventh_file_path)
                   
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[8])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[9])
                    ninth_df = pd.read_csv(ninth_file_path)
                   
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[10])
                    tenth_df = pd.read_csv(tenth_file_path)
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]
                    
                    eleventh_file_path = os.path.join(folder_path, files_in_folder[11])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[12])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total
                    botoca_g01_total = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total
                    calaca_g01_total = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total
                    calaca_g02_total = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total
                    kal_g01_total = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total
                    kal_g02_total = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total
                    kal_g03_total = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total
                    kal_g04_total = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total
                    leyte_a_total = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total
                    kspc_g01_total = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total
                    kspc_g02_total = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total
                    bantap_l01_total = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total
                    pedc_t1l1_total = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total
                    pedc_t1l2_total = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total
                    stbar_t1l1_total = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '02':
                    first_file_path = os.path.join(folder_path, files_in_folder[13])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[14])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[15])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[16])
                    fourth_df = pd.read_csv(fourth_file_path)

                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[17])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]
                    
                    sixth_file_path = os.path.join(folder_path, files_in_folder[18])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[19])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[20])
                    eighth_df = pd.read_csv(eighth_file_path)
                  
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[21])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[22])
                    tenth_df = pd.read_csv(tenth_file_path)
                  
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[23])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]


                    twelvth_file_path = os.path.join(folder_path, files_in_folder[24])
                    twelvth_df = pd.read_csv(twelvth_file_path)

                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_1
                    botoca_g01_total_1 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_1
                    calaca_g01_total_1 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_1
                    calaca_g02_total_1 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_1
                    kal_g01_total_1 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_1
                    kal_g02_total_1 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_1
                    kal_g03_total_1 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_1
                    kal_g04_total_1 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_1
                    leyte_a_total_1 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_1
                    kspc_g01_total_1 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_1
                    kspc_g02_total_1 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_1
                    bantap_l01_total_1 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_1
                    pedc_t1l1_total_1 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_1
                    pedc_t1l2_total_1 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_1
                    stbar_t1l1_total_1 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
         
                elif current_hour == '03':
                    first_file_path = os.path.join(folder_path, files_in_folder[25])
                    df = pd.read_csv(first_file_path)

                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[26])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[27])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[28])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[29])
                    fifth_df = pd.read_csv(fifth_file_path)
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]
                    
                    sixth_file_path = os.path.join(folder_path, files_in_folder[30])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[31])
                    seventh_df = pd.read_csv(seventh_file_path)

                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]
                    
                    eighth_file_path = os.path.join(folder_path, files_in_folder[32])
                    eighth_df = pd.read_csv(eighth_file_path)
                   
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[33])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[34])
                    tenth_df = pd.read_csv(tenth_file_path)

                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[35])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                   
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[36])

                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_2
                    botoca_g01_total_2 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_2
                    calaca_g01_total_2 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_2
                    calaca_g02_total_2 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_2
                    kal_g01_total_2 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_2
                    kal_g02_total_2 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_2
                    kal_g03_total_2 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_2
                    kal_g04_total_2 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_2
                    leyte_a_total_2 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_2
                    kspc_g01_total_2 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_2
                    kspc_g02_total_2 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_2
                    bantap_l01_total_2 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_2
                    pedc_t1l1_total_2 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_2
                    pedc_t1l2_total_2 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_2
                    stbar_t1l1_total_2 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '04':
                    first_file_path = os.path.join(folder_path, files_in_folder[37])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_df = pd.read_csv(second_file_path)
                    second_pedc_til1 = second_df.iloc[751,5]
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[39])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[40])
                    fourth_df = pd.read_csv(fourth_file_path)

                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[41])
                    fifth_df = pd.read_csv(fifth_file_path)

                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[42])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[43])
                    seventh_df = pd.read_csv(seventh_file_path)

                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]
                    
                    eighth_file_path = os.path.join(folder_path, files_in_folder[44])
                    eighth_df = pd.read_csv(eighth_file_path)

                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[45])
                    ninth_df = pd.read_csv(ninth_file_path)

                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[46])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[47])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[48])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_3
                    botoca_g01_total_3 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_3
                    calaca_g01_total_3 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_3
                    calaca_g02_total_3 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_3
                    kal_g01_total_3 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_3
                    kal_g02_total_3 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_3
                    kal_g03_total_3 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_3
                    kal_g04_total_3 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_3
                    leyte_a_total_3 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_3
                    kspc_g01_total_3 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_3
                    kspc_g02_total_3 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_3
                    bantap_l01_total_3 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_3
                    pedc_t1l1_total_3 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_3
                    pedc_t1l2_total_3 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_3
                    stbar_t1l1_total_3 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '05':
                    first_file_path = os.path.join(folder_path, files_in_folder[49])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]
                    
                    second_file_path = os.path.join(folder_path, files_in_folder[50])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[51])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[52])
                    fourth_df = pd.read_csv(fourth_file_path)

                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[53])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[54])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[55])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[56])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[57])
                    ninth_df = pd.read_csv(ninth_file_path)

                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[58])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[59])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]
                    
                    twelvth_file_path = os.path.join(folder_path, files_in_folder[60])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_4
                    botoca_g01_total_4 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_4
                    calaca_g01_total_4 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_4
                    calaca_g02_total_4 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_4
                    kal_g01_total_4 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_4
                    kal_g02_total_4 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_4
                    kal_g03_total_4 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_4
                    kal_g04_total_4 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_4
                    leyte_a_total_4 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_4
                    kspc_g01_total_4 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_4
                    kspc_g02_total_4 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_4
                    bantap_l01_total_4 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_4
                    pedc_t1l1_total_4 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_4
                    pedc_t1l2_total_4 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_4
                    stbar_t1l1_total_4 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '06':
                    first_file_path = os.path.join(folder_path, files_in_folder[61])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[62])
                    second_df = pd.read_csv(second_file_path)

                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[63])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[64])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[65])
                    fifth_df = pd.read_csv(fifth_file_path)

                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[66])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[68])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[69])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[70])
                    tenth_df = pd.read_csv(tenth_file_path)

                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[71])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]
                    
                    twelvth_file_path = os.path.join(folder_path, files_in_folder[72])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_5
                    botoca_g01_total_5 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_5
                    calaca_g01_total_5 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_5
                    calaca_g02_total_5 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_5
                    kal_g01_total_5 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_5
                    kal_g02_total_5 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_5
                    kal_g03_total_5 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_5
                    kal_g04_total_5 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_5
                    leyte_a_total_5 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_5
                    kspc_g01_total_5 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_5
                    kspc_g02_total_5 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_5
                    bantap_l01_total_5 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_5
                    pedc_t1l1_total_5 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_5
                    pedc_t1l2_total_5 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_5
                    stbar_t1l1_total_5 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '07':
                    first_file_path = os.path.join(folder_path, files_in_folder[73])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[74])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[75])
                    third_df = pd.read_csv(third_file_path)

                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[76])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[77])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[78])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[79])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[80])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[81])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[82])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[83])
                    eleventh_df = pd.read_csv(eleventh_file_path)

                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[84])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_6
                    botoca_g01_total_6 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_6
                    calaca_g01_total_6 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_6
                    calaca_g02_total_6 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_6
                    kal_g01_total_6 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_6
                    kal_g02_total_6 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_6
                    kal_g03_total_6 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_6
                    kal_g04_total_6 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_6
                    leyte_a_total_6 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_6
                    kspc_g01_total_6 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_6
                    kspc_g02_total_6 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_6
                    bantap_l01_total_6 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_6
                    pedc_t1l1_total_6 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_6
                    pedc_t1l2_total_6 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_6
                    stbar_t1l1_total_6 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '08':
                    first_file_path = os.path.join(folder_path, files_in_folder[85])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[86])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[87])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[88])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[89])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[90])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[91])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[92])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[93])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[94])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[95])
                    eleventh_df = pd.read_csv(eleventh_file_path)

                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[96])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_7
                    botoca_g01_total_7 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_7
                    calaca_g01_total_7 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_7
                    calaca_g02_total_7 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_7 
                    kal_g01_total_7 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_7
                    kal_g02_total_7 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_7
                    kal_g03_total_7 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_7
                    kal_g04_total_7 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_7
                    leyte_a_total_7 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_7
                    kspc_g01_total_7 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_7
                    kspc_g02_total_7 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_7
                    bantap_l01_total_7 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_7
                    pedc_t1l1_total_7 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_7
                    pedc_t1l2_total_7 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_7
                    stbar_t1l1_total_7 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '09':
                    first_file_path = os.path.join(folder_path, files_in_folder[97])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[98])
                    second_df = pd.read_csv(second_file_path)
                
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[99])
                    third_df = pd.read_csv(third_file_path)
                      
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[100])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[101])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[102])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[103])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]
                    
                    eighth_file_path = os.path.join(folder_path, files_in_folder[104])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[105])
                    ninth_df = pd.read_csv(ninth_file_path)

                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[106])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[107])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[108])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_8
                    botoca_g01_total_8 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_8
                    calaca_g01_total_8 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_8
                    calaca_g02_total_8 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_8
                    kal_g01_total_8 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_8
                    kal_g02_total_8 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_8
                    kal_g03_total_8 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_8
                    kal_g04_total_8 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_8
                    leyte_a_total_8 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_8
                    kspc_g01_total_8 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_8
                    kspc_g02_total_8 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_8
                    bantap_l01_total_8 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_8
                    pedc_t1l1_total_8 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_8
                    pedc_t1l2_total_8 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_8
                    stbar_t1l1_total_8 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '10':
                    first_file_path = os.path.join(folder_path, files_in_folder[109])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[110])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[111])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[112])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[113])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[114])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[115])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[116])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[117])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[118])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[119])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[120])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_9
                    botoca_g01_total_9 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_9
                    calaca_g01_total_9 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_9
                    calaca_g02_total_9 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_9
                    kal_g01_total_9 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_9
                    kal_g02_total_9 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_9
                    kal_g03_total_9 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_9
                    kal_g04_total_9 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_9
                    leyte_a_total_9 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_9
                    kspc_g01_total_9 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_9
                    kspc_g02_total_9 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_9
                    bantap_l01_total_9 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_9
                    pedc_t1l1_total_9 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_9
                    pedc_t1l2_total_9 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_9
                    stbar_t1l1_total_9 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '11':
                    first_file_path = os.path.join(folder_path, files_in_folder[121])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[122])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[123])
                    third_df = pd.read_csv(third_file_path)
                   
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[124])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[125])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[126])
                    sixth_df = pd.read_csv(sixth_file_path)

                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[127])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[128])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[129])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[130])
                    tenth_df = pd.read_csv(tenth_file_path)

                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[131])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[132])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_10
                    botoca_g01_total_10 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_10
                    calaca_g01_total_10 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_10
                    calaca_g02_total_10 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_10
                    kal_g01_total_10 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_10
                    kal_g02_total_10 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_10
                    kal_g03_total_10 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_10
                    kal_g04_total_10 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_10
                    leyte_a_total_10 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_10
                    kspc_g01_total_10 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_10
                    kspc_g02_total_10 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_10
                    bantap_l01_total_10 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_10
                    pedc_t1l1_total_10 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_10
                    pedc_t1l2_total_10 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_10
                    stbar_t1l1_total_10 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '12':
                    first_file_path = os.path.join(folder_path, files_in_folder[133])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[134])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[135])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]
                    
                    fourth_file_path = os.path.join(folder_path, files_in_folder[136])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[137])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[138])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[139])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[140])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[141])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[142])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[143])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[144])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_11
                    botoca_g01_total_11 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_11
                    calaca_g01_total_11 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_11
                    calaca_g02_total_11 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_11
                    kal_g01_total_11 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_11
                    kal_g02_total_11 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_11
                    kal_g03_total_11 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_11
                    kal_g04_total_11 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_11
                    leyte_a_total_11 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_11
                    kspc_g01_total_11 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_11
                    kspc_g02_total_11 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_11
                    bantap_l01_total_11 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_11
                    pedc_t1l1_total_11 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_11
                    pedc_t1l2_total_11 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_11
                    stbar_t1l1_total_11 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '13':
                    first_file_path = os.path.join(folder_path, files_in_folder[145])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[146])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[147])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[148])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[149])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[150])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[151])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[152])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[153])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[154])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[155])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[156])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]
                    
                    global botoca_g01_total_12
                    botoca_g01_total_12 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_12
                    calaca_g01_total_12 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_12
                    calaca_g02_total_12 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_12
                    kal_g01_total_12 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_12
                    kal_g02_total_12 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_12
                    kal_g03_total_12 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_12
                    kal_g04_total_12 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_12
                    leyte_a_total_12 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_12
                    kspc_g01_total_12 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_12
                    kspc_g02_total_12 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_12
                    bantap_l01_total_12 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_12
                    pedc_t1l1_total_12 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_12
                    pedc_t1l2_total_12 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_12
                    stbar_t1l1_total_12 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '14':
                    first_file_path = os.path.join(folder_path, files_in_folder[157])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]
                    
                    second_file_path = os.path.join(folder_path, files_in_folder[158])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[159])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[160])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[161])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[162])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[163])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]


                    eighth_file_path = os.path.join(folder_path, files_in_folder[164])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[165])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[166])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[167])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[168])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_13
                    botoca_g01_total_13 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_13
                    calaca_g01_total_13 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_13
                    calaca_g02_total_13 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_13
                    kal_g01_total_13 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_13
                    kal_g02_total_13 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_13
                    kal_g03_total_13 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_13
                    kal_g04_total_13 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_13
                    leyte_a_total_13 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_13
                    kspc_g01_total_13 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_13
                    kspc_g02_total_13 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_13
                    bantap_l01_total_13 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_13
                    pedc_t1l1_total_13 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_13
                    pedc_t1l2_total_13 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_13
                    stbar_t1l1_total_13 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '15':
                    first_file_path = os.path.join(folder_path, files_in_folder[169])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[170])
                    second_df = pd.read_csv(second_file_path)
                
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[171])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[172])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[173])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[174])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[175])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[176])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[177])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[178])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[179])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[180])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_14
                    botoca_g01_total_14 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_14
                    calaca_g01_total_14 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_14
                    calaca_g02_total_14 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_14
                    kal_g01_total_14 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_14
                    kal_g02_total_14 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_14
                    kal_g03_total_14 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_14
                    kal_g04_total_14 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_14
                    leyte_a_total_14 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_14
                    kspc_g01_total_14 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_14
                    kspc_g02_total_14 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_14
                    bantap_l01_total_14 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_14
                    pedc_t1l1_total_14 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_14
                    pedc_t1l2_total_14 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_14
                    stbar_t1l1_total_14 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '16':
                    first_file_path = os.path.join(folder_path, files_in_folder[181])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[182])
                    second_df = pd.read_csv(second_file_path)

                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[183])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[184])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[185])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[186])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[187])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[188])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[189])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]


                    tenth_file_path = os.path.join(folder_path, files_in_folder[190])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[191])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[192])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]
                    
                    global botoca_g01_total_15
                    botoca_g01_total_15 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_15
                    calaca_g01_total_15 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_15
                    calaca_g02_total_15 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_15
                    kal_g01_total_15 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_15
                    kal_g02_total_15 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_15
                    kal_g03_total_15 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_15
                    kal_g04_total_15 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_15
                    leyte_a_total_15 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_15
                    kspc_g01_total_15 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_15
                    kspc_g02_total_15 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_15
                    bantap_l01_total_15 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_15
                    pedc_t1l1_total_15 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_15
                    pedc_t1l2_total_15 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_15
                    stbar_t1l1_total_15 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '17':
                    first_file_path = os.path.join(folder_path, files_in_folder[193])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[194])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[195])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[196])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[197])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[198])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[199])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[200])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[201])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[202])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[203])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[204])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_16 
                    botoca_g01_total_16 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_16
                    calaca_g01_total_16 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_16
                    calaca_g02_total_16 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_16
                    kal_g01_total_16 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_16
                    kal_g02_total_16 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_16
                    kal_g03_total_16 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_16
                    kal_g04_total_16 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_16 
                    leyte_a_total_16 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_16
                    kspc_g01_total_16 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_16
                    kspc_g02_total_16 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_16
                    bantap_l01_total_16 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_16
                    pedc_t1l1_total_16 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_16
                    pedc_t1l2_total_16 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_16
                    stbar_t1l1_total_16 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '18':
                    first_file_path = os.path.join(folder_path, files_in_folder[205])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[206])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[207])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[208])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[209])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[210])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[211])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[212])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[213])
                    ninth_df = pd.read_csv(ninth_file_path)

                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[214])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[215])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[216])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_17
                    botoca_g01_total_17 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_17
                    calaca_g01_total_17 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_17
                    calaca_g02_total_17 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_17
                    kal_g01_total_17 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_17
                    kal_g02_total_17 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_17
                    kal_g03_total_17 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_17
                    kal_g04_total_17 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_17
                    leyte_a_total_17 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_17
                    kspc_g01_total_17 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_17
                    kspc_g02_total_17 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_17
                    bantap_l01_total_17 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_17
                    pedc_t1l1_total_17 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_17
                    pedc_t1l2_total_17 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_17
                    stbar_t1l1_total_17 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '19':
                    first_file_path = os.path.join(folder_path, files_in_folder[217])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[218])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[219])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[220])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[221])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[222])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[223])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[224])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[225])
                    ninth_df = pd.read_csv(ninth_file_path)
                
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[226])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[227])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[228])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_18
                    botoca_g01_total_18 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_18
                    calaca_g01_total_18 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_18
                    calaca_g02_total_18 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_18
                    kal_g01_total_18 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_18
                    kal_g02_total_18 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_18
                    kal_g03_total_18 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_18
                    kal_g04_total_18 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_18
                    leyte_a_total_18 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_18
                    kspc_g01_total_18 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_18
                    kspc_g02_total_18 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_18
                    bantap_l01_total_18 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_18
                    pedc_t1l1_total_18 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_18
                    pedc_t1l2_total_18 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_18 
                    stbar_t1l1_total_18 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '20':
                    first_file_path = os.path.join(folder_path, files_in_folder[229])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[230])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[231])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[232])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[233])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[234])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[235])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[236])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[237])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[238])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[239])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[240])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_19
                    botoca_g01_total_19 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_19
                    calaca_g01_total_19 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_19
                    calaca_g02_total_19 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_19
                    kal_g01_total_19 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_19
                    kal_g02_total_19 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_19
                    kal_g03_total_19 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_19
                    kal_g04_total_19 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_19
                    leyte_a_total_19 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_19
                    kspc_g01_total_19 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_19
                    kspc_g02_total_19 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_19
                    bantap_l01_total_19 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_19
                    pedc_t1l1_total_19 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_19
                    pedc_t1l2_total_19 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_19
                    stbar_t1l1_total_19 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '21':
                    first_file_path = os.path.join(folder_path, files_in_folder[241])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[242])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[243])
                    third_df = pd.read_csv(third_file_path)

                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[244])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[245])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[246])
                    sixth_df = pd.read_csv(sixth_file_path)
                   
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[247])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[248])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[249])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[250])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[251])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[252])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_20
                    botoca_g01_total_20 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_20
                    calaca_g01_total_20 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_20
                    calaca_g02_total_20 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_20
                    kal_g01_total_20 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_20
                    kal_g02_total_20 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_20
                    kal_g03_total_20 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_20
                    kal_g04_total_20 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_20
                    leyte_a_total_20 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_20
                    kspc_g01_total_20 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_20
                    kspc_g02_total_20 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_20 
                    bantap_l01_total_20 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_20
                    pedc_t1l1_total_20 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_20
                    pedc_t1l2_total_20 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_20
                    stbar_t1l1_total_20 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '22':
                    first_file_path = os.path.join(folder_path, files_in_folder[253])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[254])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[255])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[256])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[257])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[258])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[259])
                    seventh_df = pd.read_csv(seventh_file_path)

                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[260])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[261])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[262])
                    tenth_df = pd.read_csv(tenth_file_path)

                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[263])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[264])
                    twelvth_df = pd.read_csv(twelvth_file_path)

                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_21
                    botoca_g01_total_21 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_21
                    calaca_g01_total_21 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_21
                    calaca_g02_total_21 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_21
                    kal_g01_total_21 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_21
                    kal_g02_total_21 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_21 
                    kal_g03_total_21 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_21
                    kal_g04_total_21 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_21
                    leyte_a_total_21 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_21
                    kspc_g01_total_21 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_21
                    kspc_g02_total_21 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_21
                    bantap_l01_total_21 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_21
                    pedc_t1l1_total_21 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_21
                    pedc_t1l2_total_21 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_21
                    stbar_t1l1_total_21 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                elif current_hour == '23':
                    first_file_path = os.path.join(folder_path, files_in_folder[265])
                    df = pd.read_csv(first_file_path)

                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]

                    second_file_path = os.path.join(folder_path, files_in_folder[266])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[267])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[268])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[269])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[270])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[271])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[272])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[273])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[274])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[275])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[276])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global botoca_g01_total_22
                    botoca_g01_total_22 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_22
                    calaca_g01_total_22 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_22
                    calaca_g02_total_22 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_22
                    kal_g01_total_22 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_22
                    kal_g02_total_22 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_22
                    kal_g03_total_22 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_22
                    kal_g04_total_22 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_22
                    leyte_a_total_22 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_22
                    kspc_g01_total_22 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_22
                    kspc_g02_total_22 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_22
                    bantap_l01_total_22 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_22
                    pedc_t1l1_total_22 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_22
                    pedc_t1l2_total_22 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_22
                    stbar_t1l1_total_22 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

                else:
                    first_file_path = os.path.join(folder_path, files_in_folder[277])
                    df = pd.read_csv(first_file_path)
                    
                    file_03BOTOCA_G01 = df.iloc[364,5]
                    file_03CALACA_G01 = df.iloc[368,5]
                    file_03CALACA_G02 = df.iloc[369,5]
                    file_03KAL_G01 = df.iloc[417,5]
                    file_03KAL_G02 = df.iloc[418,5]
                    file_03KAL_G03 = df.iloc[419,5]
                    file_03KAL_G04 = df.iloc[420,5]
                    file_04LEYTE_A = df.iloc[532,5]
                    file_05KSPC_G01 = df.iloc[590,5]
                    file_05KSPC_G02 = df.iloc[591,5]
                    file_08BANTAP_L01 = df.iloc[717,5]
                    file_08PEDC_T1L1 = df.iloc[757,5]
                    file_08PEDC_T1L2 = df.iloc[758,5]
                    file_08STBAR_T1L1 = df.iloc[772,5]                  

                    second_file_path = os.path.join(folder_path, files_in_folder[278])
                    second_df = pd.read_csv(second_file_path)
                    
                    second_file_03BOTOCA_G01 = second_df.iloc[364,5]
                    second_file_03CALACA_G01 = second_df.iloc[368,5]
                    second_file_03CALACA_G02 = second_df.iloc[369,5]
                    second_file_03KAL_G01 = second_df.iloc[417,5]
                    second_file_03KAL_G02 = second_df.iloc[418,5]
                    second_file_03KAL_G03 = second_df.iloc[419,5]
                    second_file_03KAL_G04 = second_df.iloc[420,5]
                    second_file_04LEYTE_A = second_df.iloc[532,5]
                    second_file_05KSPC_G01 = second_df.iloc[590,5]
                    second_file_05KSPC_G02 = second_df.iloc[591,5]
                    second_file_08BANTAP_L01 = second_df.iloc[717,5]
                    second_file_08PEDC_T1L1 = second_df.iloc[757,5]
                    second_file_08PEDC_T1L2 = second_df.iloc[758,5]
                    second_file_08STBAR_T1L1 = second_df.iloc[772,5]

                    third_file_path = os.path.join(folder_path, files_in_folder[279])
                    third_df = pd.read_csv(third_file_path)
                    
                    third_file_03BOTOCA_G01 = third_df.iloc[364,5]
                    third_file_03CALACA_G01 = third_df.iloc[368,5]
                    third_file_03CALACA_G02 = third_df.iloc[369,5]
                    third_file_03KAL_G01 = third_df.iloc[417,5]
                    third_file_03KAL_G02 = third_df.iloc[418,5]
                    third_file_03KAL_G03 = third_df.iloc[419,5]
                    third_file_03KAL_G04 = third_df.iloc[420,5]
                    third_file_04LEYTE_A = third_df.iloc[532,5]
                    third_file_05KSPC_G01 = third_df.iloc[590,5]
                    third_file_05KSPC_G02 = third_df.iloc[591,5]
                    third_file_08BANTAP_L01 = third_df.iloc[717,5]
                    third_file_08PEDC_T1L1 = third_df.iloc[757,5]
                    third_file_08PEDC_T1L2 = third_df.iloc[758,5]
                    third_file_08STBAR_T1L1 = third_df.iloc[772,5]

                    fourth_file_path = os.path.join(folder_path, files_in_folder[280])
                    fourth_df = pd.read_csv(fourth_file_path)
                    
                    fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
                    fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
                    fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
                    fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
                    fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
                    fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
                    fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
                    fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
                    fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
                    fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
                    fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
                    fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
                    fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
                    fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

                    fifth_file_path = os.path.join(folder_path, files_in_folder[281])
                    fifth_df = pd.read_csv(fifth_file_path)
                    
                    fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
                    fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
                    fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
                    fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
                    fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
                    fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
                    fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
                    fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
                    fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
                    fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
                    fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
                    fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
                    fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
                    fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

                    sixth_file_path = os.path.join(folder_path, files_in_folder[282])
                    sixth_df = pd.read_csv(sixth_file_path)
                    
                    sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
                    sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
                    sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
                    sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
                    sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
                    sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
                    sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
                    sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
                    sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
                    sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
                    sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
                    sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
                    sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
                    sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

                    seventh_file_path = os.path.join(folder_path, files_in_folder[283])
                    seventh_df = pd.read_csv(seventh_file_path)
                    
                    seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
                    seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
                    seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
                    seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
                    seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
                    seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
                    seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
                    seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
                    seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
                    seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
                    seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
                    seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
                    seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
                    seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

                    eighth_file_path = os.path.join(folder_path, files_in_folder[284])
                    eighth_df = pd.read_csv(eighth_file_path)
                    
                    eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
                    eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
                    eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
                    eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
                    eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
                    eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
                    eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
                    eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
                    eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
                    eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
                    eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
                    eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
                    eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
                    eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

                    ninth_file_path = os.path.join(folder_path, files_in_folder[285])
                    ninth_df = pd.read_csv(ninth_file_path)
                    
                    ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
                    ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
                    ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
                    ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
                    ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
                    ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
                    ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
                    ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
                    ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
                    ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
                    ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
                    ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
                    ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
                    ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

                    tenth_file_path = os.path.join(folder_path, files_in_folder[286])
                    tenth_df = pd.read_csv(tenth_file_path)
                    
                    tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
                    tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
                    tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
                    tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
                    tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
                    tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
                    tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
                    tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
                    tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
                    tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
                    tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
                    tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
                    tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
                    tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

                    eleventh_file_path = os.path.join(folder_path, files_in_folder[287])
                    eleventh_df = pd.read_csv(eleventh_file_path)
                    
                    eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
                    eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
                    eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
                    eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
                    eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
                    eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
                    eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
                    eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
                    eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
                    eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
                    eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
                    eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
                    eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
                    eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

                    twelvth_file_path = os.path.join(folder_path, files_in_folder[0])
                    twelvth_df = pd.read_csv(twelvth_file_path)
                    
                    twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
                    twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
                    twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
                    twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
                    twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
                    twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
                    twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
                    twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
                    twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
                    twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
                    twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
                    twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
                    twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
                    twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    global  botoca_g01_total_23
                    botoca_g01_total_23 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
                    global calaca_g01_total_23
                    calaca_g01_total_23 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
                    global calaca_g02_total_23
                    calaca_g02_total_23 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
                    global kal_g01_total_23
                    kal_g01_total_23 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
                    global kal_g02_total_23
                    kal_g02_total_23 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
                    global kal_g03_total_23
                    kal_g03_total_23 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
                    global kal_g04_total_23
                    kal_g04_total_23 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
                    global leyte_a_total_23
                    leyte_a_total_23 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
                    global kspc_g01_total_23
                    kspc_g01_total_23 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
                    global kspc_g02_total_23
                    kspc_g02_total_23 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
                    global bantap_l01_total_23
                    bantap_l01_total_23 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
                    global pedc_t1l1_total_23 
                    pedc_t1l1_total_23 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
                    global pedc_t1l2_total_23
                    pedc_t1l2_total_23 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
                    global stbar_t1l1_total_23
                    stbar_t1l1_total_23 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime as dt

s = dt.now()

first_hour = s.strftime("%d/%m/%Y 01:00:00")
second_hour = s.strftime("%d/%m/%Y 02:00:00")
third_hour = s.strftime("%d/%m/%Y 03:00:00")
fourth_hour = s.strftime("%d/%m/%Y 04:00:00")
fifth_hour = s.strftime("%d/%m/%Y 05:00:00")
sixth_hour = s.strftime("%d/%m/%Y 06:00:00")
seventh_hour = s.strftime("%d/%m/%Y 07:00:00")
eighth_hour = s.strftime("%d/%m/%Y 08:00:00")
ninth_hour = s.strftime("%d/%m/%Y 09:00:00")
tenth_hour = s.strftime("%d/%m/%Y 10:00:00")
eleventh_hour = s.strftime("%d/%m/%Y 11:00:00")
twelvth_hour = s.strftime("%d/%m/%Y 12:00:00")
thirteenth_hour = s.strftime("%d/%m/%Y 13:00:00")
fourteenth_hour = s.strftime("%d/%m/%Y 14:00:00")
fifteenth_hour = s.strftime("%d/%m/%Y 15:00:00")
sixteenth_hour = s.strftime("%d/%m/%Y 16:00:00")
seventeenth_hour = s.strftime("%d/%m/%Y 17:00:00")
eighteenth_hour = s.strftime("%d/%m/%Y 18:00:00")
nineteenth_hour = s.strftime("%d/%m/%Y 19:00:00")
twentieth_hour = s.strftime("%d/%m/%Y 20:00:00")
twenty_first_hour = s.strftime("%d/%m/%Y 21:00:00")
twenty_second_hour = s.strftime("%d/%m/%Y 22:00:00")
twenty_third_hour = s.strftime("%d/%m/%Y 23:00:00")
twenty_fourth_hour = s.strftime("%d/%m/%Y 24:00:00")

# DATA
tipc_data = {
    'HOUR': [first_hour, second_hour, third_hour, fourth_hour, fifth_hour, sixth_hour, seventh_hour, eighth_hour, ninth_hour, tenth_hour, eleventh_hour, twelvth_hour, thirteenth_hour, fourteenth_hour, fifteenth_hour, sixteenth_hour, seventeenth_hour, eighteenth_hour, nineteenth_hour, twentieth_hour, twenty_first_hour, twenty_second_hour, twenty_third_hour, twenty_fourth_hour],
    '03BOTOCA_G01': [botoca_g01_total, botoca_g01_total_1, botoca_g01_total_2, botoca_g01_total_3, botoca_g01_total_4, botoca_g01_total_5, botoca_g01_total_6, botoca_g01_total_7, botoca_g01_total_8, botoca_g01_total_9, botoca_g01_total_10, botoca_g01_total_11, botoca_g01_total_12, botoca_g01_total_13, botoca_g01_total_14, botoca_g01_total_15, botoca_g01_total_16, botoca_g01_total_17, botoca_g01_total_18, botoca_g01_total_19, botoca_g01_total_20, botoca_g01_total_21, botoca_g01_total_22, botoca_g01_total_23],
    '03CALACA_G01': [calaca_g01_total, calaca_g01_total_1, calaca_g01_total_2, calaca_g01_total_3, calaca_g01_total_4, calaca_g01_total_5, calaca_g01_total_6, calaca_g01_total_7, calaca_g01_total_8, calaca_g01_total_9, calaca_g01_total_10, calaca_g01_total_11, calaca_g01_total_12, calaca_g01_total_13, calaca_g01_total_14, calaca_g01_total_15, calaca_g01_total_16, calaca_g01_total_17, calaca_g01_total_18, calaca_g01_total_19, calaca_g01_total_20, calaca_g01_total_21, calaca_g01_total_22, calaca_g01_total_23],
    '03CALACA_G02': [calaca_g02_total, calaca_g02_total_1, calaca_g02_total_2, calaca_g02_total_3, calaca_g02_total_4, calaca_g02_total_5, calaca_g02_total_6, calaca_g02_total_7, calaca_g02_total_8, calaca_g02_total_9, calaca_g02_total_10, calaca_g02_total_11, calaca_g02_total_12, calaca_g02_total_13, calaca_g02_total_14, calaca_g02_total_15, calaca_g02_total_16, calaca_g02_total_17, calaca_g02_total_18, calaca_g02_total_19, calaca_g02_total_20, calaca_g02_total_21, calaca_g02_total_22, calaca_g02_total_23],
    '03KAL_G01': [kal_g01_total, kal_g01_total_1, kal_g01_total_2, kal_g01_total_3, kal_g01_total_4, kal_g01_total_5, kal_g01_total_6, kal_g01_total_7, kal_g01_total_8, kal_g01_total_9, kal_g01_total_10, kal_g01_total_11, kal_g01_total_12, kal_g01_total_13, kal_g01_total_14, kal_g01_total_15, kal_g01_total_16, kal_g01_total_17, kal_g01_total_18, kal_g01_total_19, kal_g01_total_20, kal_g01_total_21, kal_g01_total_22, kal_g01_total_23],
    '03KAL_G02': [kal_g02_total, kal_g02_total_1, kal_g02_total_2, kal_g02_total_3, kal_g02_total_4, kal_g02_total_5, kal_g02_total_6, kal_g02_total_7, kal_g02_total_8, kal_g02_total_9, kal_g02_total_10, kal_g02_total_11, kal_g02_total_12, kal_g02_total_13, kal_g02_total_14, kal_g02_total_15, kal_g02_total_16, kal_g02_total_17, kal_g02_total_18, kal_g02_total_19, kal_g02_total_20, kal_g02_total_21, kal_g02_total_22, kal_g02_total_23],
    '03KAL_G03': [kal_g03_total, kal_g03_total_1, kal_g03_total_2, kal_g03_total_3, kal_g03_total_4, kal_g03_total_5, kal_g03_total_6, kal_g03_total_7, kal_g03_total_8, kal_g03_total_9, kal_g03_total_10, kal_g03_total_11, kal_g03_total_12, kal_g03_total_13, kal_g03_total_14, kal_g03_total_15, kal_g03_total_16, kal_g03_total_17, kal_g03_total_18, kal_g03_total_19, kal_g03_total_20, kal_g03_total_21, kal_g03_total_22, kal_g03_total_23],
    '03KAL_G04': [kal_g04_total, kal_g04_total_1, kal_g04_total_2, kal_g04_total_3, kal_g04_total_4, kal_g04_total_5, kal_g04_total_6, kal_g04_total_7, kal_g04_total_8, kal_g04_total_9, kal_g04_total_10, kal_g04_total_11, kal_g04_total_12, kal_g04_total_13, kal_g04_total_14, kal_g04_total_15, kal_g04_total_16, kal_g04_total_17, kal_g04_total_18, kal_g04_total_19, kal_g04_total_20, kal_g04_total_21, kal_g04_total_22, kal_g04_total_23],
    '04LEYTE_A': [leyte_a_total, leyte_a_total_1, leyte_a_total_2, leyte_a_total_3, leyte_a_total_4, leyte_a_total_5, leyte_a_total_6, leyte_a_total_7, leyte_a_total_8, leyte_a_total_9, leyte_a_total_10, leyte_a_total_11, leyte_a_total_12, leyte_a_total_13, leyte_a_total_14, leyte_a_total_15, leyte_a_total_16, leyte_a_total_17, leyte_a_total_18, leyte_a_total_19, leyte_a_total_20, leyte_a_total_21, leyte_a_total_22, leyte_a_total_23],
    '05KSPC_G01': [kspc_g01_total, kspc_g01_total_1, kspc_g01_total_2, kspc_g01_total_3, kspc_g01_total_4, kspc_g01_total_5, kspc_g01_total_6, kspc_g01_total_7, kspc_g01_total_8, kspc_g01_total_9, kspc_g01_total_10, kspc_g01_total_11, kspc_g01_total_12, kspc_g01_total_13, kspc_g01_total_14, kspc_g01_total_15, kspc_g01_total_16, kspc_g01_total_17, kspc_g01_total_18, kspc_g01_total_19, kspc_g01_total_20, kspc_g01_total_21, kspc_g01_total_22, kspc_g01_total_23],
    '05KSPC_G02': [kspc_g02_total, kspc_g02_total_1, kspc_g02_total_2, kspc_g02_total_3, kspc_g02_total_4, kspc_g02_total_5, kspc_g02_total_6, kspc_g02_total_7, kspc_g02_total_8, kspc_g02_total_9, kspc_g02_total_10, kspc_g02_total_11, kspc_g02_total_12, kspc_g02_total_13, kspc_g02_total_14, kspc_g02_total_15, kspc_g02_total_16, kspc_g02_total_17, kspc_g02_total_18, kspc_g02_total_19, kspc_g02_total_20, kspc_g02_total_21, kspc_g02_total_22, kspc_g02_total_23], 
    '08BANTAP_L01': [bantap_l01_total, bantap_l01_total_1, bantap_l01_total_2, bantap_l01_total_3, bantap_l01_total_4, bantap_l01_total_5, bantap_l01_total_6, bantap_l01_total_7, bantap_l01_total_8, bantap_l01_total_9, bantap_l01_total_10, bantap_l01_total_11, bantap_l01_total_12, bantap_l01_total_13, bantap_l01_total_14, bantap_l01_total_15, bantap_l01_total_16, bantap_l01_total_17, bantap_l01_total_18, bantap_l01_total_19, bantap_l01_total_20, bantap_l01_total_21, bantap_l01_total_22, bantap_l01_total_23], 
    '08PEDC_T1L1': [pedc_t1l1_total, pedc_t1l1_total_1, pedc_t1l1_total_2, pedc_t1l1_total_3, pedc_t1l1_total_4, pedc_t1l1_total_5, pedc_t1l1_total_6, pedc_t1l1_total_7, pedc_t1l1_total_8, pedc_t1l1_total_9, pedc_t1l1_total_10, pedc_t1l1_total_11, pedc_t1l1_total_12, pedc_t1l1_total_13, pedc_t1l1_total_14, pedc_t1l1_total_15, pedc_t1l1_total_16, pedc_t1l1_total_17, pedc_t1l1_total_18, pedc_t1l1_total_19, pedc_t1l1_total_20, pedc_t1l1_total_21, pedc_t1l1_total_22, pedc_t1l1_total_23], 
    '08PEDC_T1L2': [pedc_t1l2_total, pedc_t1l2_total_1, pedc_t1l2_total_2, pedc_t1l2_total_3, pedc_t1l2_total_4, pedc_t1l2_total_5, pedc_t1l2_total_6, pedc_t1l2_total_7, pedc_t1l2_total_8, pedc_t1l2_total_9, pedc_t1l2_total_10, pedc_t1l2_total_11, pedc_t1l2_total_12, pedc_t1l2_total_13, pedc_t1l2_total_14, pedc_t1l2_total_15, pedc_t1l2_total_16, pedc_t1l2_total_17, pedc_t1l2_total_18, pedc_t1l2_total_19, pedc_t1l2_total_20, pedc_t1l2_total_21, pedc_t1l2_total_22, pedc_t1l2_total_23],
    '08STBAR_T1L1': [stbar_t1l1_total, stbar_t1l1_total_1, stbar_t1l1_total_2, stbar_t1l1_total_3, stbar_t1l1_total_4, stbar_t1l1_total_5, stbar_t1l1_total_6, stbar_t1l1_total_7, stbar_t1l1_total_8, stbar_t1l1_total_9, stbar_t1l1_total_10, stbar_t1l1_total_11, stbar_t1l1_total_12, stbar_t1l1_total_13, stbar_t1l1_total_14, stbar_t1l1_total_15, stbar_t1l1_total_16, stbar_t1l1_total_17, stbar_t1l1_total_18, stbar_t1l1_total_19, stbar_t1l1_total_20, stbar_t1l1_total_21, stbar_t1l1_total_22, stbar_t1l1_total_23], 
}

tipc_df = pd.DataFrame(tipc_data)

# Melt the DataFrame to have a long format
tipc_df_melted = tipc_df.melt(id_vars='hour', var_name='variable', value_name='value')

# Create a Plotly line chart
tipc_fig = px.line(tipc_df_melted, x='hour', y='value', color='variable', markers=True,
              title='Line Chart with Different Values per Hour',
              labels={'hour': 'Hour of the Day', 'value': 'Value', 'variable': 'Variable'})

# Customize the layout
tipc_fig.update_layout(
    xaxis_title='Hour of the Day',
    yaxis_title='Value',
    legend_title='Variable'
)

# Display the chart in Streamlit
st.plotly_chart(tipc_fig)

# -- END OF TRADING INTERVAL PRICE CALCULATION LINE CHART --