# 03BOTOCA_G01
# O3CALACA_G01
# 03CALACA_G02
# 03KAL_G01
# 03KAL_G02
# 03KAL_G03
# 03KAL_G04
# 04LEYTE_A
# 05KSPC_G01
# 05KSPC_G02
# 08BANTAP_L01
# 08PEDC_TIL1
# O8PEDC_TIL2
# O8STBAR_TIL1

# from datetime import datetime
# import os
# import pandas as pd
# import mysql.connector

# directory = r'C:\Users\aslee\OneDrive - MORE ELECTRIC AND POWER CORPORATION\Desktop\DASHBOARD_FINAL\MORE Trading Node'
# now = datetime.now()
# date_today = now.strftime("%Y%m%d")
# contents = os.listdir(directory)
# for item in contents:
#     if item == date_today:
#         folder_path = os.path.join(directory, item) 
#         if os.path.isdir(folder_path):
#             files_in_folder = os.listdir(folder_path) # MPI_LMP_DIPC_202407110000, etc.

#             filepath_1 = os.path.join(folder_path, files_in_folder[1]) 
#             df_1 = pd.read_csv(filepath_1)

#             search_value_1 = '03BOTOCA_G01'
#             matching_row_1 = df_1[df_1['RESOURCE_NAME'] == search_value_1]
#             file_03BOTOCA_G01_1 = matching_row_1['DIPC_PRICE'].values[0]

#             search_value_2 = '03CALACA_G01'
#             matching_row_2 = df_1[df_1['RESOURCE_NAME'] == search_value_2]
#             file_03CALACA_G01_2 = matching_row_2['DIPC_PRICE'].values[0]
            
#             search_value_3 = '03CALACA_G02'
#             matching_row_3 = df_1[df_1['RESOURCE_NAME'] == search_value_3]
#             file_03CALACA_G02_3 = matching_row_3['DIPC_PRICE'].values[0]
            
#             search_value_4 = '03KAL_G01'
#             matching_row_4 = df_1[df_1['RESOURCE_NAME'] == search_value_4]
#             file_03KAL_G01_4 = matching_row_4['DIPC_PRICE'].values[0]

#             search_value_5 = '03KAL_G02'
#             matching_row_5 = df_1[df_1['RESOURCE_NAME'] == search_value_5]
#             file_03KAL_G02_5 = matching_row_5['DIPC_PRICE'].values[0]
            
#             search_value_6 = '03KAL_G03'
#             matching_row_6 = df_1[df_1['RESOURCE_NAME'] == search_value_6]
#             file_03KAL_G03_6 = matching_row_6['DIPC_PRICE'].values[0]

#             search_value_7 = '03KAL_G04'
#             matching_row_7 = df_1[df_1['RESOURCE_NAME'] == search_value_7]
#             file_03KAL_G04_7 = matching_row_7['DIPC_PRICE'].values[0]

#             search_value_8 = '04LEYTE_A'
#             matching_row_8 = df_1[df_1['RESOURCE_NAME'] == search_value_8]
#             file_04LEYTE_A_8 = matching_row_8['DIPC_PRICE'].values[0]

#             search_value_9 = '05KSPC_G01'
#             matching_row_9 = df_1[df_1['RESOURCE_NAME'] == search_value_9]
#             file_05KSPC_G01_9 = matching_row_9['DIPC_PRICE'].values[0]

#             search_value_10 = '05KSPC_G02'
#             matching_row_10 = df_1[df_1['RESOURCE_NAME'] == search_value_10]
#             file_05KSPC_G02_10 = matching_row_10['DIPC_PRICE'].values[0]

#             search_value_11 = '08BANTAP_L01'
#             matching_row_11 = df_1[df_1['RESOURCE_NAME'] == search_value_11]
#             file_08BANTAP_L01_11 = matching_row_11['DIPC_PRICE'].values[0]

#             search_value_12 = '08PEDC_T1L1'
#             matching_row_12 = df_1[df_1['RESOURCE_NAME'] == search_value_12]
#             file_08PEDC_T1L1_12 = matching_row_12['DIPC_PRICE'].values[0]

#             search_value_13 = '08PEDC_T1L2'
#             matching_row_13 = df_1[df_1['RESOURCE_NAME'] ==  search_value_13]
#             file_08PEDC_T1L2_13 = matching_row_13['DIPC_PRICE'].values[0]

#             search_value_14 = '08STBAR_T1L1'
#             matching_row_14 = df_1[df_1['RESOURCE_NAME'] ==  search_value_14]
#             file_08STBAR_T1L1_14 = matching_row_14['DIPC_PRICE'].values[0]
            
#             # 2nd Folder
#             filepath_2 = os.path.join(folder_path, files_in_folder[2]) 
#             df_2 = pd.read_csv(filepath_2)

#             search_value_15 = '03BOTOCA_G01'
#             matching_row_15 = df_2[df_2['RESOURCE_NAME'] == search_value_15]
#             file_03BOTOCA_G01_15 = matching_row_15['DIPC_PRICE'].values[0]

#             search_value_16 = '03CALACA_G01'
#             matching_row_16 = df_2[df_2['RESOURCE_NAME'] == search_value_16]
#             file_03CALACA_G01_16 = matching_row_16['DIPC_PRICE'].values[0]

#             search_value_17 = '03CALACA_G02'
#             matching_row_17 = df_2[df_2['RESOURCE_NAME'] == search_value_17]
#             file_03CALACA_G02_17 = matching_row_17['DIPC_PRICE'].values[0]

#             search_value_18 = '03KAL_G01'
#             matching_row_18 = df_2[df_2['RESOURCE_NAME'] == search_value_18]
#             file_03KAL_G01_18 = matching_row_18['DIPC_PRICE'].values[0]

#             search_value_19 = '03KAL_G02'
#             matching_row_19 = df_2[df_2['RESOURCE_NAME'] == search_value_19]
#             file_03KAL_G02_19 = matching_row_19['DIPC_PRICE'].values[0]

#             search_value_20 = '03KAL_G03'
#             matching_row_20 = df_2[df_2['RESOURCE_NAME'] == search_value_20]
#             file_03KAL_G03_20 =  matching_row_20['DIPC_PRICE'].values[0]

#             search_value_21 = '03KAL_G04'
#             matching_row_21 = df_2[df_2['RESOURCE_NAME'] == search_value_21]
#             file_03KAL_G04_21 = matching_row_21['DIPC_PRICE'].values[0]

#             search_value_22 = '04LEYTE_A'
#             matching_row_22 = df_2[df_2['RESOURCE_NAME'] == search_value_22]
#             file_04LEYTE_A_22 = matching_row_22['DIPC_PRICE'].values[0]

#             search_value_23 = '05KSPC_G01'
#             matching_row_23 = df_2[df_2['RESOURCE_NAME'] == search_value_23]
#             file_05KSPC_G01_23 = matching_row_23['DIPC_PRICE'].values[0]

#             search_value_24 = '05KSPC_G02'
#             matching_row_24 = df_2[df_2['RESOURCE_NAME'] == search_value_24]
#             file_05KSPC_G02_24 = matching_row_24['DIPC_PRICE'].values[0]

#             search_value_25 = '08BANTAP_L01'
#             matching_row_25 = df_2[df_2['RESOURCE_NAME'] == search_value_25]
#             file_08BANTAP_L01_25 = matching_row_25['DIPC_PRICE'].values[0]

#             search_value_26 = '08PEDC_T1L1'
#             matching_row_26 = df_2[df_2['RESOURCE_NAME'] == search_value_26]
#             file_08PEDC_T1L1_26 = matching_row_26['DIPC_PRICE'].values[0]

#             search_value_27 = '08PEDC_T1L2'
#             matching_row_27 = df_2[df_2['RESOURCE_NAME'] == search_value_27]
#             file_08PEDC_T1L2_27 = matching_row_27['DIPC_PRICE'].values[0]

#             search_value_28 = '08STBAR_T1L1'
#             matching_row_28 = df_2[df_2['RESOURCE_NAME'] == search_value_28]
#             file_08STBAR_T1L1_28 = matching_row_28['DIPC_PRICE'].values[0]

#             # Third Folder
#             filepath_3 = os.path.join(folder_path, files_in_folder[3]) 
#             df_3 = pd.read_csv(filepath_3)

#             search_value_29 = '03BOTOCA_G01'
#             matching_row_29 = df_3[df_3['RESOURCE_NAME'] == search_value_29]
#             file_03BOTOCA_G01_29 = matching_row_29['DIPC_PRICE'].values[0]

#             search_value_30 = '03CALACA_G01'
#             matching_row_30 = df_3[df_3['RESOURCE_NAME'] == search_value_30]
#             file_03CALACA_G01_30 = matching_row_30['DIPC_PRICE'].values[0]

#             search_value_31 = '03CALACA_G02'
#             matching_row_31 = df_3[df_3['RESOURCE_NAME'] == search_value_31]
#             file_03CALACA_G02_31 = matching_row_31['DIPC_PRICE'].values[0]

#             search_value_32 = '03KAL_G01'
#             matching_row_32 = df_3[df_3['RESOURCE_NAME'] == search_value_32]
#             file_03KAL_G01_32 = matching_row_32['DIPC_PRICE'].values[0]

#             search_value_33 = '03KAL_G02'
#             matching_row_33 = df_3[df_3['RESOURCE_NAME'] == search_value_33]
#             file_03KAL_G02_33 = matching_row_33['DIPC_PRICE'].values[0]

#             search_value_34 = '03KAL_G03'
#             matching_row_34 = df_3[df_3['RESOURCE_NAME'] == search_value_34]
#             file_03KAL_G03_34 = matching_row_34['DIPC_PRICE'].values[0]

#             search_value_35 = '03KAL_G04'
#             matching_row_35 = df_3[df_3['RESOURCE_NAME'] == search_value_35]
#             file_03KAL_G04_35 = matching_row_35['DIPC_PRICE'].values[0]

#             search_value_36 = '04LEYTE_A'
#             matching_row_36 = df_3[df_3['RESOURCE_NAME'] == search_value_36]
#             file_04LEYTE_A_36 = matching_row_36['DIPC_PRICE'].values[0]

#             search_value_37 = '05KSPC_G01'
#             matching_row_37 = df_3[df_3['RESOURCE_NAME'] == search_value_37]
#             file_05KSPC_G01_37 = matching_row_37['DIPC_PRICE'].values[0]

#             search_value_38 = '05KSPC_G02'
#             matching_row_38 = df_3[df_3['RESOURCE_NAME'] == search_value_38]
#             file_05KSPC_G02_38 = matching_row_38['DIPC_PRICE'].values[0]

#             search_value_39 = '08BANTAP_L01'
#             matching_row_39 = df_3[df_3['RESOURCE_NAME'] == search_value_39]
#             file_08BANTAP_L01_39 = matching_row_39['DIPC_PRICE'].values[0]

#             search_value_40 = '08PEDC_T1L1'
#             matching_row_40 = df_3[df_3['RESOURCE_NAME'] == search_value_40]
#             file_08PEDC_T1L1_40 = matching_row_40['DIPC_PRICE'].values[0]

#             search_value_41 = '08PEDC_T1L2'
#             matching_row_41 = df_3[df_3['RESOURCE_NAME'] == search_value_41]
#             file_08PEDC_T1L2_41 = matching_row_41['DIPC_PRICE'].values[0]

#             search_value_42 = '08STBAR_T1L1'
#             matching_row_42 = df_3[df_3['RESOURCE_NAME'] == search_value_42]
#             file_08STBAR_T1L1_42 = matching_row_42['DIPC_PRICE'].values[0]

#             # Fourth Folder
#             filepath_4 = os.path.join(folder_path, files_in_folder[4]) 
#             df_4 = pd.read_csv(filepath_4)

#             search_value_43 = '03BOTOCA_G01'
#             matching_row_43 = df_4[df_4['RESOURCE_NAME'] == search_value_43]
#             file_03BOTOCA_G01_43 = matching_row_43['DIPC_PRICE'].values[0]

#             search_value_44 = '03CALACA_G01'
#             matching_row_44 = df_4[df_4['RESOURCE_NAME'] == search_value_44]
#             file_03CALACA_G01_44 = matching_row_44['DIPC_PRICE'].values[0]

#             search_value_45 = '03CALACA_G02'
#             matching_row_45 = df_4[df_4['RESOURCE_NAME'] == search_value_45]
#             file_03CALACA_G02_45 = matching_row_45['DIPC_PRICE'].values[0]

#             search_value_46 = '03KAL_G01'
#             matching_row_46 = df_4[df_4['RESOURCE_NAME'] == search_value_46]
#             file_03KAL_G01_46 = matching_row_46['DIPC_PRICE'].values[0]

#             search_value_47 = '03KAL_G02'
#             matching_row_47 = df_4[df_4['RESOURCE_NAME'] == search_value_47]
#             file_03KAL_G02_47 = matching_row_47['DIPC_PRICE'].values[0]

#             search_value_48 = '03KAL_G03'
#             matching_row_48 = df_4[df_4['RESOURCE_NAME'] == search_value_48]
#             file_03KAL_G03_48 = matching_row_48['DIPC_PRICE'].values[0]

#             search_value_49 = '03KAL_G04'
#             matching_row_49 = df_4[df_4['RESOURCE_NAME'] == search_value_49]
#             file_03KAL_G04_49 = matching_row_49['DIPC_PRICE'].values[0]

#             search_value_50 = '04LEYTE_A'
#             matching_row_50 = df_4[df_4['RESOURCE_NAME'] == search_value_50]
#             file_04LEYTE_A_50 = matching_row_50['DIPC_PRICE'].values[0]

#             search_value_51 = '05KSPC_G01'
#             matching_row_51 = df_4[df_4['RESOURCE_NAME'] == search_value_51]
#             file_05KSPC_G01_51 = matching_row_51['DIPC_PRICE'].values[0]

#             search_value_52 = '05KSPC_G02'
#             matching_row_52 = df_4[df_4['RESOURCE_NAME'] == search_value_52]
#             file_05KSPC_G02_52 = matching_row_52['DIPC_PRICE'].values[0]

#             search_value_53 = '08BANTAP_L01'
#             matching_row_53 = df_4[df_4['RESOURCE_NAME'] == search_value_53]
#             file_08BANTAP_L01_53 = matching_row_53['DIPC_PRICE'].values[0]

#             search_value_54 = '08PEDC_T1L1'
#             matching_row_54 = df_4[df_4['RESOURCE_NAME'] == search_value_54]
#             file_08PEDC_T1L1_54 = matching_row_54['DIPC_PRICE'].values[0]

#             search_value_55 = '08PEDC_T1L2'
#             matching_row_55 = df_4[df_4['RESOURCE_NAME'] == search_value_55]
#             file_08PEDC_T1L2_55 = matching_row_55['DIPC_PRICE'].values[0]

#             search_value_56 = '08STBAR_T1L1'
#             matching_row_56 = df_4[df_4['RESOURCE_NAME'] == search_value_56]
#             file_08STBAR_T1L1_56 = matching_row_56['DIPC_PRICE'].values[0]

#             # Fifth Folder
#             filepath_5 = os.path.join(folder_path, files_in_folder[5]) 
#             df_5 = pd.read_csv(filepath_5)

#             search_value_57 = '03BOTOCA_G01'
#             matching_row_57 = df_5[df_5['RESOURCE_NAME'] == search_value_57]
#             file_03BOTOCA_G01_57 = matching_row_57['DIPC_PRICE'].values[0]

#             search_value_58 = '03CALACA_G01'
#             matching_row_58 = df_5[df_5['RESOURCE_NAME'] == search_value_58]
#             file_03CALACA_G01_58 = matching_row_58['DIPC_PRICE'].values[0]

#             search_value_59 = '03CALACA_G02'
#             matching_row_59 = df_5[df_5['RESOURCE_NAME'] == search_value_59]
#             file_03CALACA_G02_59 = matching_row_59['DIPC_PRICE'].values[0]

#             search_value_60 = '03KAL_G01'
#             matching_row_60 = df_5[df_5['RESOURCE_NAME'] == search_value_60]
#             file_03KAL_G01_60 = matching_row_60['DIPC_PRICE'].values[0]

#             search_value_61 = '03KAL_G02'
#             matching_row_61 = df_5[df_5['RESOURCE_NAME'] == search_value_61]
#             file_03KAL_G02_61 = matching_row_61['DIPC_PRICE'].values[0]

#             search_value_62 = '03KAL_G03'
#             matching_row_62 = df_5[df_5['RESOURCE_NAME'] == search_value_62]
#             file_03KAL_G03_62 = matching_row_62['DIPC_PRICE'].values[0]

#             search_value_63 = '03KAL_G04'
#             matching_row_63 = df_5[df_5['RESOURCE_NAME'] == search_value_63]
#             file_03KAL_G04_63 = matching_row_63['DIPC_PRICE'].values[0]

#             search_value_64 = '04LEYTE_A'
#             matching_row_64 = df_5[df_5['RESOURCE_NAME'] == search_value_64]
#             file_04LEYTE_A_64 = matching_row_64['DIPC_PRICE'].values[0]

#             search_value_65 = '05KSPC_G01'
#             matching_row_65 = df_5[df_5['RESOURCE_NAME'] == search_value_65]
#             file_05KSPC_G01_65 = matching_row_65['DIPC_PRICE'].values[0]

#             search_value_66 = '05KSPC_G02'
#             matching_row_66 = df_5[df_5['RESOURCE_NAME'] == search_value_66]
#             file_05KSPC_G02_66 = matching_row_66['DIPC_PRICE'].values[0]

#             search_value_67 = '08BANTAP_L01'
#             matching_row_67 = df_5[df_5['RESOURCE_NAME'] == search_value_67]
#             file_08BANTAP_L01_67 = matching_row_67['DIPC_PRICE'].values[0]

#             search_value_68 = '08PEDC_T1L1'
#             matching_row_68 = df_5[df_5['RESOURCE_NAME'] == search_value_68]
#             file_08PEDC_T1L1_68 = matching_row_68['DIPC_PRICE'].values[0]

#             search_value_69 = '08PEDC_T1L2'
#             matching_row_69 = df_5[df_5['RESOURCE_NAME'] == search_value_69]
#             file_08PEDC_T1L2_69 = matching_row_69['DIPC_PRICE'].values[0]

#             search_value_70 = '08STBAR_T1L1'
#             matching_row_70 = df_5[df_5['RESOURCE_NAME'] == search_value_70]
#             file_08STBAR_T1L1_70 = matching_row_70['DIPC_PRICE'].values[0]
                 
#             # Sixth Folder
#             filepath_6 = os.path.join(folder_path, files_in_folder[6]) 
#             df_6 = pd.read_csv(filepath_6)

#             search_value_71 = '03BOTOCA_G01'
#             matching_row_71 = df_6[df_6['RESOURCE_NAME'] == search_value_71]
#             file_03BOTOCA_G01_71 = matching_row_71['DIPC_PRICE'].values[0]

#             search_value_72 = '03CALACA_G01'
#             matching_row_72 = df_6[df_6['RESOURCE_NAME'] == search_value_72]
#             file_03CALACA_G01_72 = matching_row_72['DIPC_PRICE'].values[0]

#             search_value_73 = '03CALACA_G02'
#             matching_row_73 = df_6[df_6['RESOURCE_NAME'] == search_value_73]
#             file_03CALACA_G02_73 = matching_row_73['DIPC_PRICE'].values[0]

#             search_value_74 = '03KAL_G01'
#             matching_row_74 = df_6[df_6['RESOURCE_NAME'] == search_value_74]
#             file_03KAL_G01_74 = matching_row_74['DIPC_PRICE'].values[0]

#             search_value_75 = '03KAL_G02'
#             matching_row_75 = df_6[df_6['RESOURCE_NAME'] == search_value_75]
#             file_03KAL_G02_75 = matching_row_75['DIPC_PRICE'].values[0]

#             search_value_76 = '03KAL_G03'
#             matching_row_76 = df_6[df_6['RESOURCE_NAME'] == search_value_76]
#             file_03KAL_G03_76 = matching_row_76['DIPC_PRICE'].values[0]

#             search_value_77 = '03KAL_G04'
#             matching_row_77 = df_6[df_6['RESOURCE_NAME'] == search_value_77]
#             file_03KAL_G04_77 = matching_row_77['DIPC_PRICE'].values[0]

#             search_value_78 = '04LEYTE_A'
#             matching_row_78 = df_6[df_6['RESOURCE_NAME'] == search_value_78]
#             file_04LEYTE_A_78 = matching_row_78['DIPC_PRICE'].values[0]

#             search_value_79 = '05KSPC_G01'
#             matching_row_79 = df_6[df_6['RESOURCE_NAME'] == search_value_79]
#             file_05KSPC_G01_79 = matching_row_79['DIPC_PRICE'].values[0]

#             search_value_80 = '05KSPC_G02'
#             matching_row_80 = df_6[df_6['RESOURCE_NAME'] == search_value_80]
#             file_05KSPC_G02_80 = matching_row_80['DIPC_PRICE'].values[0]

#             search_value_81 = '08BANTAP_L01'
#             matching_row_81 = df_6[df_6['RESOURCE_NAME'] == search_value_81]
#             file_08BANTAP_L01_81 = matching_row_81['DIPC_PRICE'].values[0]

#             search_value_82 = '08PEDC_T1L1'
#             matching_row_82 = df_6[df_6['RESOURCE_NAME'] == search_value_82]
#             file_08PEDC_T1L1_82 = matching_row_82['DIPC_PRICE'].values[0]

#             search_value_83 = '08PEDC_T1L2'
#             matching_row_83 = df_6[df_6['RESOURCE_NAME'] == search_value_83]
#             file_08PEDC_T1L2_83 = matching_row_83['DIPC_PRICE'].values[0]

#             search_value_84 = '08STBAR_T1L1'
#             matching_row_84 = df_6[df_6['RESOURCE_NAME'] == search_value_84]
#             file_08STBAR_T1L1_84 = matching_row_84['DIPC_PRICE'].values[0]

#             # Seventh Folder
#             filepath_7 = os.path.join(folder_path, files_in_folder[7]) 
#             df_7 = pd.read_csv(filepath_7)

#             search_value_85 = '03BOTOCA_G01'
#             matching_row_85 = df_7[df_7['RESOURCE_NAME'] == search_value_85]
#             file_03BOTOCA_G01_85 = matching_row_85['DIPC_PRICE'].values[0]

#             search_value_86 = '03CALACA_G01'
#             matching_row_86 = df_7[df_7['RESOURCE_NAME'] == search_value_86]
#             file_03CALACA_G01_86 = matching_row_86['DIPC_PRICE'].values[0]

#             search_value_87 = '03CALACA_G02'
#             matching_row_87 = df_7[df_7['RESOURCE_NAME'] == search_value_87]
#             file_03CALACA_G02_87 = matching_row_87['DIPC_PRICE'].values[0]

#             search_value_88 = '03KAL_G01'
#             matching_row_88 = df_7[df_7['RESOURCE_NAME'] == search_value_88]
#             file_03KAL_G01_88 = matching_row_88['DIPC_PRICE'].values[0]

#             search_value_89 = '03KAL_G02'
#             matching_row_89 = df_7[df_7['RESOURCE_NAME'] == search_value_89]
#             file_03KAL_G02_89 = matching_row_89['DIPC_PRICE'].values[0]

#             search_value_90 = '03KAL_G03'
#             matching_row_90 = df_7[df_7['RESOURCE_NAME'] == search_value_90]
#             file_03KAL_G03_90 = matching_row_90['DIPC_PRICE'].values[0]

#             search_value_91 = '03KAL_G04'
#             matching_row_91 = df_7[df_7['RESOURCE_NAME'] == search_value_91]
#             file_03KAL_G04_91 = matching_row_91['DIPC_PRICE'].values[0]

#             search_value_92 = '04LEYTE_A'
#             matching_row_92 = df_7[df_7['RESOURCE_NAME'] == search_value_92]
#             file_04LEYTE_A_92 = matching_row_92['DIPC_PRICE'].values[0]

#             search_value_93 = '05KSPC_G01'
#             matching_row_93 = df_7[df_7['RESOURCE_NAME'] == search_value_93]
#             file_05KSPC_G01_93 = matching_row_93['DIPC_PRICE'].values[0]

#             search_value_94 = '05KSPC_G02'
#             matching_row_94 = df_7[df_7['RESOURCE_NAME'] == search_value_94]
#             file_05KSPC_G02_94 = matching_row_94['DIPC_PRICE'].values[0]

#             search_value_95 = '08BANTAP_L01'
#             matching_row_95 = df_7[df_7['RESOURCE_NAME'] == search_value_95]
#             file_08BANTAP_L01_95 = matching_row_95['DIPC_PRICE'].values[0]

#             search_value_96 = '08PEDC_T1L1'
#             matching_row_96 = df_7[df_7['RESOURCE_NAME'] == search_value_96]
#             file_08PEDC_T1L1_96 = matching_row_96['DIPC_PRICE'].values[0]

#             search_value_97 = '08PEDC_T1L2'
#             matching_row_97 = df_7[df_7['RESOURCE_NAME'] == search_value_97]
#             file_08PEDC_T1L2_97 = matching_row_97['DIPC_PRICE'].values[0]

#             search_value_98 = '08STBAR_T1L1'
#             matching_row_98 = df_7[df_7['RESOURCE_NAME'] == search_value_98]
#             file_08STBAR_T1L1_98 = matching_row_98['DIPC_PRICE'].values[0]

#             # Eighth Folder
#             filepath_8 = os.path.join(folder_path, files_in_folder[8]) 
#             df_8 = pd.read_csv(filepath_8)

#             search_value_99 = '03BOTOCA_G01'
#             matching_row_99 = df_8[df_8['RESOURCE_NAME'] == search_value_99]
#             file_03BOTOCA_G01_99 = matching_row_99['DIPC_PRICE'].values[0]

#             search_value_100 = '03CALACA_G01'
#             matching_row_100 = df_8[df_8['RESOURCE_NAME'] == search_value_100]
#             file_03CALACA_G01_100 = matching_row_100['DIPC_PRICE'].values[0]

#             search_value_101 = '03CALACA_G02'
#             matching_row_101 = df_8[df_8['RESOURCE_NAME'] == search_value_101]
#             file_03CALACA_G02_101 = matching_row_101['DIPC_PRICE'].values[0]

#             search_value_102 = '03KAL_G01'
#             matching_row_102 = df_8[df_8['RESOURCE_NAME'] == search_value_102]
#             file_03KAL_G01_102 = matching_row_102['DIPC_PRICE'].values[0]

#             search_value_103 = '03KAL_G02'
#             matching_row_103 = df_8[df_8['RESOURCE_NAME'] == search_value_103]
#             file_03KAL_G02_103 = matching_row_103['DIPC_PRICE'].values[0]

#             search_value_104 = '03KAL_G03'
#             matching_row_104 = df_8[df_8['RESOURCE_NAME'] == search_value_104]
#             file_03KAL_G03_104 = matching_row_104['DIPC_PRICE'].values[0]

#             search_value_105 = '03KAL_G04'
#             matching_row_105 = df_8[df_8['RESOURCE_NAME'] == search_value_105]
#             file_03KAL_G04_105 = matching_row_105['DIPC_PRICE'].values[0]

#             search_value_106 = '04LEYTE_A'
#             matching_row_106 = df_8[df_8['RESOURCE_NAME'] == search_value_106]
#             file_04LEYTE_A_106 = matching_row_106['DIPC_PRICE'].values[0]

#             search_value_107 = '05KSPC_G01'
#             matching_row_107 = df_8[df_8['RESOURCE_NAME'] == search_value_107]
#             file_05KSPC_G01_107 = matching_row_107['DIPC_PRICE'].values[0]

#             search_value_108 = '05KSPC_G02'
#             matching_row_108 = df_8[df_8['RESOURCE_NAME'] == search_value_108]
#             file_05KSPC_G02_108 = matching_row_108['DIPC_PRICE'].values[0]

#             search_value_109 = '08BANTAP_L01'
#             matching_row_109 = df_8[df_8['RESOURCE_NAME'] == search_value_109]
#             file_08BANTAP_L01_109 = matching_row_109['DIPC_PRICE'].values[0]

#             search_value_110 = '08PEDC_T1L1'
#             matching_row_110 = df_8[df_8['RESOURCE_NAME'] == search_value_110]
#             file_08PEDC_T1L1_110 = matching_row_110['DIPC_PRICE'].values[0]

#             search_value_111 = '08PEDC_T1L2'
#             matching_row_111 = df_8[df_8['RESOURCE_NAME'] == search_value_111]
#             file_08PEDC_T1L2_111 = matching_row_111['DIPC_PRICE'].values[0]

#             search_value_112 = '08STBAR_T1L1'
#             matching_row_112 = df_8[df_8['RESOURCE_NAME'] == search_value_112]
#             file_08STBAR_T1L1_112 = matching_row_112['DIPC_PRICE'].values[0]

#             # Ninth Folder
#             filepath_9 = os.path.join(folder_path, files_in_folder[9]) 
#             df_9 = pd.read_csv(filepath_9)

#             search_value_113 = '03BOTOCA_G01'
#             matching_row_113 = df_9[df_9['RESOURCE_NAME'] == search_value_113]
#             file_03BOTOCA_G01_113 = matching_row_113['DIPC_PRICE'].values[0]

#             search_value_114 = '03CALACA_G01'
#             matching_row_114 = df_9[df_9['RESOURCE_NAME'] == search_value_114]
#             file_03CALACA_G01_114 = matching_row_114['DIPC_PRICE'].values[0]

#             search_value_115 = '03CALACA_G02'
#             matching_row_115 = df_9[df_9['RESOURCE_NAME'] == search_value_115]
#             file_03CALACA_G02_115 = matching_row_115['DIPC_PRICE'].values[0]

#             search_value_116 = '03KAL_G01'
#             matching_row_116 = df_9[df_9['RESOURCE_NAME'] == search_value_116]
#             file_03KAL_G01_116 = matching_row_116['DIPC_PRICE'].values[0]

#             search_value_117 = '03KAL_G02'
#             matching_row_117 = df_9[df_9['RESOURCE_NAME'] == search_value_117]
#             file_03KAL_G02_117 = matching_row_117['DIPC_PRICE'].values[0]

#             search_value_118 = '03KAL_G03'
#             matching_row_118 = df_9[df_9['RESOURCE_NAME'] == search_value_118]
#             file_03KAL_G03_118 = matching_row_118['DIPC_PRICE'].values[0]

#             search_value_119 = '03KAL_G04'
#             matching_row_119 = df_9[df_9['RESOURCE_NAME'] == search_value_119]
#             file_03KAL_G04_119 = matching_row_119['DIPC_PRICE'].values[0]

#             search_value_120 = '04LEYTE_A'
#             matching_row_120 = df_9[df_9['RESOURCE_NAME'] == search_value_120]
#             file_04LEYTE_A_120 = matching_row_120['DIPC_PRICE'].values[0]

#             search_value_121 = '05KSPC_G01'
#             matching_row_121 = df_9[df_9['RESOURCE_NAME'] == search_value_121]
#             file_05KSPC_G01_121 = matching_row_121['DIPC_PRICE'].values[0]

#             search_value_122 = '05KSPC_G02'
#             matching_row_122 = df_9[df_9['RESOURCE_NAME'] == search_value_122]
#             file_05KSPC_G02_122 = matching_row_122['DIPC_PRICE'].values[0]

#             search_value_123 = '08BANTAP_L01'
#             matching_row_123 = df_9[df_9['RESOURCE_NAME'] == search_value_123]
#             file_08BANTAP_L01_123 = matching_row_123['DIPC_PRICE'].values[0]

#             search_value_124 = '08PEDC_T1L1'
#             matching_row_124 = df_9[df_9['RESOURCE_NAME'] == search_value_124]
#             file_08PEDC_T1L1_124 = matching_row_124['DIPC_PRICE'].values[0]

#             search_value_125 = '08PEDC_T1L2'
#             matching_row_125 = df_9[df_9['RESOURCE_NAME'] == search_value_125]
#             file_08PEDC_T1L2_125 = matching_row_125['DIPC_PRICE'].values[0]

#             search_value_126 = '08STBAR_T1L1'
#             matching_row_126 = df_9[df_9['RESOURCE_NAME'] == search_value_126]
#             file_08STBAR_T1L1_126 = matching_row_126['DIPC_PRICE'].values[0]

#             # Tenth Folder
#             filepath_10 = os.path.join(folder_path, files_in_folder[10]) 
#             df_10 = pd.read_csv(filepath_10)

#             search_value_127 = '03BOTOCA_G01'
#             matching_row_127 = df_10[df_10['RESOURCE_NAME'] == search_value_127]
#             file_03BOTOCA_G01_127 = matching_row_127['DIPC_PRICE'].values[0]

#             search_value_128 = '03CALACA_G01'
#             matching_row_128 = df_10[df_10['RESOURCE_NAME'] == search_value_128]
#             file_03CALACA_G01_128 = matching_row_128['DIPC_PRICE'].values[0]

#             search_value_129 = '03CALACA_G02'
#             matching_row_129 = df_10[df_10['RESOURCE_NAME'] == search_value_129]
#             file_03CALACA_G02_129 = matching_row_129['DIPC_PRICE'].values[0]

#             search_value_130 = '03KAL_G01'
#             matching_row_130 = df_10[df_10['RESOURCE_NAME'] == search_value_130]
#             file_03KAL_G01_130 = matching_row_130['DIPC_PRICE'].values[0]

#             search_value_131 = '03KAL_G02'
#             matching_row_131 = df_10[df_10['RESOURCE_NAME'] == search_value_131]
#             file_03KAL_G02_131 = matching_row_131['DIPC_PRICE'].values[0]

#             search_value_132 = '03KAL_G03'
#             matching_row_132 = df_10[df_10['RESOURCE_NAME'] == search_value_132]
#             file_03KAL_G03_132 = matching_row_132['DIPC_PRICE'].values[0]

#             search_value_133 = '03KAL_G04'
#             matching_row_133 = df_10[df_10['RESOURCE_NAME'] == search_value_133]
#             file_03KAL_G04_133 = matching_row_133['DIPC_PRICE'].values[0]

#             search_value_134 = '04LEYTE_A'
#             matching_row_134 = df_10[df_10['RESOURCE_NAME'] == search_value_134]
#             file_04LEYTE_A_134 = matching_row_134['DIPC_PRICE'].values[0]

#             search_value_135 = '05KSPC_G01'
#             matching_row_135 = df_10[df_10['RESOURCE_NAME'] == search_value_135]
#             file_05KSPC_G01_135 = matching_row_135['DIPC_PRICE'].values[0]

#             search_value_136 = '05KSPC_G02'
#             matching_row_136 = df_10[df_10['RESOURCE_NAME'] == search_value_136]
#             file_05KSPC_G02_136 = matching_row_136['DIPC_PRICE'].values[0]

#             search_value_137 = '08BANTAP_L01'
#             matching_row_137 = df_10[df_10['RESOURCE_NAME'] == search_value_137]
#             file_08BANTAP_L01_137 = matching_row_137['DIPC_PRICE'].values[0]

#             search_value_138 = '08PEDC_T1L1'
#             matching_row_138 = df_10[df_10['RESOURCE_NAME'] == search_value_138]
#             file_08PEDC_T1L1_138 = matching_row_138['DIPC_PRICE'].values[0]

#             search_value_139 = '08PEDC_T1L2'
#             matching_row_139 = df_10[df_10['RESOURCE_NAME'] == search_value_139]
#             file_08PEDC_T1L2_139 = matching_row_139['DIPC_PRICE'].values[0]

#             search_value_140 = '08STBAR_T1L1'
#             matching_row_140 = df_10[df_10['RESOURCE_NAME'] == search_value_140]
#             file_08STBAR_T1L1_140 = matching_row_140['DIPC_PRICE'].values[0]

#             # Eleventh Folder
#             filepath_11 = os.path.join(folder_path, files_in_folder[11]) 
#             df_11 = pd.read_csv(filepath_11)

#             search_value_141 = '03BOTOCA_G01'
#             matching_row_141 = df_11[df_11['RESOURCE_NAME'] == search_value_141]
#             file_03BOTOCA_G01_141 = matching_row_141['DIPC_PRICE'].values[0]

#             search_value_142 = '03CALACA_G01'
#             matching_row_142 = df_11[df_11['RESOURCE_NAME'] == search_value_142]
#             file_03CALACA_G01_142 = matching_row_142['DIPC_PRICE'].values[0]

#             search_value_143 = '03CALACA_G02'
#             matching_row_143 = df_11[df_11['RESOURCE_NAME'] == search_value_143]
#             file_03CALACA_G02_143 = matching_row_143['DIPC_PRICE'].values[0]

#             search_value_144 = '03KAL_G01'
#             matching_row_144 = df_11[df_11['RESOURCE_NAME'] == search_value_144]
#             file_03KAL_G01_144 = matching_row_144['DIPC_PRICE'].values[0]

#             search_value_145 = '03KAL_G02'
#             matching_row_145 = df_11[df_11['RESOURCE_NAME'] == search_value_145]
#             file_03KAL_G02_145 = matching_row_145['DIPC_PRICE'].values[0]

#             search_value_146 = '03KAL_G03'
#             matching_row_146 = df_11[df_11['RESOURCE_NAME'] == search_value_146]
#             file_03KAL_G03_146 = matching_row_146['DIPC_PRICE'].values[0]

#             search_value_147 = '03KAL_G04'
#             matching_row_147 = df_11[df_11['RESOURCE_NAME'] == search_value_147]
#             file_03KAL_G04_147 = matching_row_147['DIPC_PRICE'].values[0]

#             search_value_148 = '04LEYTE_A'
#             matching_row_148 = df_11[df_11['RESOURCE_NAME'] == search_value_148]
#             file_04LEYTE_A_148 = matching_row_148['DIPC_PRICE'].values[0]

#             search_value_149 = '05KSPC_G01'
#             matching_row_149 = df_11[df_11['RESOURCE_NAME'] == search_value_149]
#             file_05KSPC_G01_149 = matching_row_149['DIPC_PRICE'].values[0]

#             search_value_150 = '05KSPC_G02'
#             matching_row_150 = df_11[df_11['RESOURCE_NAME'] == search_value_150]
#             file_05KSPC_G02_150 = matching_row_150['DIPC_PRICE'].values[0]

#             search_value_151 = '08BANTAP_L01'
#             matching_row_151 = df_11[df_11['RESOURCE_NAME'] == search_value_151]
#             file_08BANTAP_L01_151 = matching_row_151['DIPC_PRICE'].values[0]

#             search_value_152 = '08PEDC_T1L1'
#             matching_row_152 = df_11[df_11['RESOURCE_NAME'] == search_value_152]
#             file_08PEDC_T1L1_152 = matching_row_152['DIPC_PRICE'].values[0]

#             search_value_153 = '08PEDC_T1L2'
#             matching_row_153 = df_11[df_11['RESOURCE_NAME'] == search_value_153]
#             file_08PEDC_T1L2_153 = matching_row_153['DIPC_PRICE'].values[0]

#             search_value_154 = '08STBAR_T1L1'
#             matching_row_154 = df_11[df_11['RESOURCE_NAME'] == search_value_154]
#             file_08STBAR_T1L1_154 = matching_row_154['DIPC_PRICE'].values[0]

#             # Twelvth Folder
#             filepath_12 = os.path.join(folder_path, files_in_folder[12]) 
#             df_12 = pd.read_csv(filepath_12)

#             search_value_155 = '03BOTOCA_G01'
#             matching_row_155 = df_12[df_12['RESOURCE_NAME'] == search_value_155]
#             file_03BOTOCA_G01_155 = matching_row_155['DIPC_PRICE'].values[0]

#             search_value_156 = '03CALACA_G01'
#             matching_row_156 = df_12[df_12['RESOURCE_NAME'] == search_value_156]
#             file_03CALACA_G01_156 = matching_row_156['DIPC_PRICE'].values[0]

#             search_value_157 = '03CALACA_G02'
#             matching_row_157 = df_12[df_12['RESOURCE_NAME'] == search_value_157]
#             file_03CALACA_G02_157 = matching_row_157['DIPC_PRICE'].values[0]

#             search_value_158 = '03KAL_G01'
#             matching_row_158 = df_12[df_12['RESOURCE_NAME'] == search_value_158]
#             file_03KAL_G01_158 = matching_row_158['DIPC_PRICE'].values[0]

#             search_value_159 = '03KAL_G02'
#             matching_row_159 = df_12[df_12['RESOURCE_NAME'] == search_value_159]
#             file_03KAL_G02_159 = matching_row_159['DIPC_PRICE'].values[0]

#             search_value_160 = '03KAL_G03'
#             matching_row_160 = df_12[df_12['RESOURCE_NAME'] == search_value_160]
#             file_03KAL_G03_160 = matching_row_160['DIPC_PRICE'].values[0]

#             search_value_161 = '03KAL_G04'
#             matching_row_161 = df_12[df_12['RESOURCE_NAME'] == search_value_161]
#             file_03KAL_G04_161 = matching_row_161['DIPC_PRICE'].values[0]

#             search_value_162 = '04LEYTE_A'
#             matching_row_162 = df_12[df_12['RESOURCE_NAME'] == search_value_162]
#             file_04LEYTE_A_162 = matching_row_162['DIPC_PRICE'].values[0]

#             search_value_163 = '05KSPC_G01'
#             matching_row_163 = df_12[df_12['RESOURCE_NAME'] == search_value_163]
#             file_05KSPC_G01_163 = matching_row_163['DIPC_PRICE'].values[0]

#             search_value_164 = '05KSPC_G02'
#             matching_row_164 = df_12[df_12['RESOURCE_NAME'] == search_value_164]
#             file_05KSPC_G02_164 = matching_row_164['DIPC_PRICE'].values[0]

#             search_value_165 = '08BANTAP_L01'
#             matching_row_165 = df_12[df_12['RESOURCE_NAME'] == search_value_165]
#             file_08BANTAP_L01_165 = matching_row_165['DIPC_PRICE'].values[0]

#             search_value_166 = '08PEDC_T1L1'
#             matching_row_166 = df_12[df_12['RESOURCE_NAME'] == search_value_166]
#             file_08PEDC_T1L1_166 = matching_row_166['DIPC_PRICE'].values[0]

#             search_value_167 = '08PEDC_T1L2'
#             matching_row_167 = df_12[df_12['RESOURCE_NAME'] == search_value_167]
#             file_08PEDC_T1L2_167 = matching_row_167['DIPC_PRICE'].values[0]

#             search_value_168 = '08STBAR_T1L1'
#             matching_row_168 = df_12[df_12['RESOURCE_NAME'] == search_value_168]
#             file_08STBAR_T1L1_168 = matching_row_168['DIPC_PRICE'].values[0]
                    
#             botoca_g01_total_1 = (file_03BOTOCA_G01_1 + file_03BOTOCA_G01_15 + file_03BOTOCA_G01_29 + file_03BOTOCA_G01_43 + file_03BOTOCA_G01_57 + file_03BOTOCA_G01_71 + file_03BOTOCA_G01_85 + file_03BOTOCA_G01_99 + file_03BOTOCA_G01_113 + file_03BOTOCA_G01_127 + file_03BOTOCA_G01_141 + file_03BOTOCA_G01_155)/12
#             calaca_g01_total_2 = (file_03CALACA_G01_2 + file_03CALACA_G01_16 + file_03CALACA_G01_30 + file_03CALACA_G01_44 + file_03CALACA_G01_58 + file_03CALACA_G01_72 + file_03CALACA_G01_86 + file_03CALACA_G01_100 + file_03CALACA_G01_114 + file_03CALACA_G01_128 + file_03CALACA_G01_142 + file_03CALACA_G01_156)/12
#             calaca_g02_total_3 = (file_03CALACA_G02_3 + file_03CALACA_G02_17 + file_03CALACA_G02_31 + file_03CALACA_G02_45 + file_03CALACA_G02_59 + file_03CALACA_G02_73 + file_03CALACA_G02_87 + file_03CALACA_G02_101 + file_03CALACA_G02_115 + file_03CALACA_G02_129 + file_03CALACA_G02_143 + file_03CALACA_G02_157)/12
#             kal_g01_total_4 = (file_03KAL_G01_4 + file_03KAL_G01_18 + file_03KAL_G01_32 + file_03KAL_G01_46 + file_03KAL_G01_60 + file_03KAL_G01_74 + file_03KAL_G01_88 + file_03KAL_G01_102 + file_03KAL_G01_116 + file_03KAL_G01_130 + file_03KAL_G01_144 + file_03KAL_G01_158)/12
#             kal_g02_total_5 = (file_03KAL_G02_5 + file_03KAL_G02_19 + file_03KAL_G02_33 + file_03KAL_G02_47 + file_03KAL_G02_61 + file_03KAL_G02_75 + file_03KAL_G02_89 + file_03KAL_G02_103 + file_03KAL_G02_117 + file_03KAL_G02_131 + file_03KAL_G02_145 + file_03KAL_G02_159)/12
#             kal_g03_total_6 = (file_03KAL_G03_6 + file_03KAL_G03_20 + file_03KAL_G03_34 + file_03KAL_G03_48 + file_03KAL_G03_62 + file_03KAL_G03_76 + file_03KAL_G03_90 + file_03KAL_G03_104 + file_03KAL_G03_118 + file_03KAL_G03_132 + file_03KAL_G03_146 + file_03KAL_G03_160)/12
#             kal_g04_total_7 = (file_03KAL_G04_7 + file_03KAL_G04_21 + file_03KAL_G04_35 + file_03KAL_G04_49 + file_03KAL_G04_63 + file_03KAL_G04_77 + file_03KAL_G04_91 + file_03KAL_G04_105 + file_03KAL_G04_119 + file_03KAL_G04_133 + file_03KAL_G04_147 + file_03KAL_G04_161)/12
#             leyte_a_total_8 = (file_04LEYTE_A_8 + file_04LEYTE_A_22 + file_04LEYTE_A_36 + file_04LEYTE_A_50 + file_04LEYTE_A_64 + file_04LEYTE_A_78 + file_04LEYTE_A_92 + file_04LEYTE_A_106 + file_04LEYTE_A_120 + file_04LEYTE_A_134 + file_04LEYTE_A_148 + file_04LEYTE_A_162)/12
#             kspc_g01_total_9 = (file_05KSPC_G01_9 + file_05KSPC_G01_23 + file_05KSPC_G01_37 + file_05KSPC_G01_51 + file_05KSPC_G01_65 + file_05KSPC_G01_79 + file_05KSPC_G01_93 + file_05KSPC_G01_107 + file_05KSPC_G01_121 + file_05KSPC_G01_135 + file_05KSPC_G01_149 + file_05KSPC_G01_163)/12
#             kspc_g02_total_10 = (file_05KSPC_G02_10 + file_05KSPC_G02_24 + file_05KSPC_G02_38 + file_05KSPC_G02_52 + file_05KSPC_G02_66 + file_05KSPC_G02_80 + file_05KSPC_G02_94 + file_05KSPC_G02_108 + file_05KSPC_G02_122 + file_05KSPC_G02_136 + file_05KSPC_G02_150 + file_05KSPC_G02_164)/12
#             bantap_l01_total_11 = (file_08BANTAP_L01_11 + file_08BANTAP_L01_25 + file_08BANTAP_L01_39 + file_08BANTAP_L01_53 + file_08BANTAP_L01_67 + file_08BANTAP_L01_81 + file_08BANTAP_L01_95 + file_08BANTAP_L01_109 + file_08BANTAP_L01_123 + file_08BANTAP_L01_137 + file_08BANTAP_L01_151 + file_08BANTAP_L01_165)/12
#             pedc_t1l1_total_12 = (file_08PEDC_T1L1_12 + file_08PEDC_T1L1_26 + file_08PEDC_T1L1_40 + file_08PEDC_T1L1_54 + file_08PEDC_T1L1_68 + file_08PEDC_T1L1_82 + file_08PEDC_T1L1_96 + file_08PEDC_T1L1_110 + file_08PEDC_T1L1_124 + file_08PEDC_T1L1_138 + file_08PEDC_T1L1_152 + file_08PEDC_T1L1_166)/12
#             pedc_t1l2_total_13 = (file_08PEDC_T1L2_13 + file_08PEDC_T1L2_27 + file_08PEDC_T1L2_41 + file_08PEDC_T1L2_55 + file_08PEDC_T1L2_69 + file_08PEDC_T1L2_83 + file_08PEDC_T1L2_97 + file_08PEDC_T1L2_111 + file_08PEDC_T1L2_125 + file_08PEDC_T1L2_139 + file_08PEDC_T1L2_153 + file_08PEDC_T1L2_167)/12
#             stbar_t1l1_total_14 = (file_08STBAR_T1L1_14 + file_08STBAR_T1L1_28 + file_08STBAR_T1L1_42 + file_08STBAR_T1L1_56 + file_08STBAR_T1L1_70 + file_08STBAR_T1L1_84 + file_08STBAR_T1L1_98 + file_08STBAR_T1L1_112 + file_08STBAR_T1L1_126 + file_08STBAR_T1L1_140 + file_08STBAR_T1L1_154 + file_08STBAR_T1L1_168)/12
            
#             filepath_13 = os.path.join(folder_path, files_in_folder[13]) 
#             df_13 = pd.read_csv(filepath_13)

#             search_value_169 = '03BOTOCA_G01'
#             matching_row_169 = df_13[df_13['RESOURCE_NAME'] == search_value_169]
#             file_03BOTOCA_G01_169 = matching_row_169['DIPC_PRICE'].values[0]

#             search_value_170 = '03CALACA_G01'
#             matching_row_170 = df_13[df_13['RESOURCE_NAME'] == search_value_170]
#             file_03CALACA_G01_170 = matching_row_170['DIPC_PRICE'].values[0]
            
#             search_value_171 = '03CALACA_G02'
#             matching_row_171 = df_13[df_13['RESOURCE_NAME'] == search_value_171]
#             file_03CALACA_G02_171 = matching_row_171['DIPC_PRICE'].values[0]
            
#             search_value_172 = '03KAL_G01'
#             matching_row_172 = df_13[df_13['RESOURCE_NAME'] == search_value_172]
#             file_03KAL_G01_172 = matching_row_172['DIPC_PRICE'].values[0]

#             search_value_173 = '03KAL_G02'
#             matching_row_173 = df_13[df_13['RESOURCE_NAME'] == search_value_173]
#             file_03KAL_G02_173 = matching_row_173['DIPC_PRICE'].values[0]

#             search_value_174 = '03KAL_G03'
#             matching_row_174 = df_13[df_13['RESOURCE_NAME'] == search_value_174]
#             file_03KAL_G03_174 = matching_row_174['DIPC_PRICE'].values[0]

#             search_value_175 = '03KAL_G04'
#             matching_row_175 = df_13[df_13['RESOURCE_NAME'] == search_value_175]
#             file_03KAL_G04_175 = matching_row_175['DIPC_PRICE'].values[0]

#             search_value_176 = '04LEYTE_A'
#             matching_row_176 = df_13[df_13['RESOURCE_NAME'] == search_value_176]
#             file_04LEYTE_A_176 = matching_row_176['DIPC_PRICE'].values[0]

#             search_value_177 = '05KSPC_G01'
#             matching_row_177 = df_13[df_13['RESOURCE_NAME'] == search_value_177]
#             file_05KSPC_G01_177 = matching_row_177['DIPC_PRICE'].values[0]

#             search_value_178 = '05KSPC_G02'
#             matching_row_178 = df_13[df_13['RESOURCE_NAME'] == search_value_178]
#             file_05KSPC_G02_178 = matching_row_178['DIPC_PRICE'].values[0]

#             search_value_179 = '08BANTAP_L01'
#             matching_row_179 = df_13[df_13['RESOURCE_NAME'] == search_value_179]
#             file_08BANTAP_L01_179 = matching_row_179['DIPC_PRICE'].values[0]

#             search_value_180 = '08PEDC_T1L1'
#             matching_row_180 = df_13[df_13['RESOURCE_NAME'] == search_value_180]
#             file_08PEDC_T1L1_180 = matching_row_180['DIPC_PRICE'].values[0]

#             search_value_181 = '08PEDC_T1L2'
#             matching_row_181 = df_13[df_13['RESOURCE_NAME'] ==  search_value_181]
#             file_08PEDC_T1L2_181 = matching_row_181['DIPC_PRICE'].values[0]

#             search_value_182 = '08STBAR_T1L1'
#             matching_row_182 = df_13[df_13['RESOURCE_NAME'] ==  search_value_182]
#             file_08STBAR_T1L1_182 = matching_row_182['DIPC_PRICE'].values[0]
            
#             # 2nd Folder
#             filepath_14 = os.path.join(folder_path, files_in_folder[14]) 
#             df_14 = pd.read_csv(filepath_14)

#             search_value_183 = '03BOTOCA_G01'
#             matching_row_183 = df_14[df_14['RESOURCE_NAME'] == search_value_183]
#             file_03BOTOCA_G01_183 = matching_row_183['DIPC_PRICE'].values[0]

#             search_value_184 = '03CALACA_G01'
#             matching_row_184 = df_14[df_14['RESOURCE_NAME'] == search_value_184]
#             file_03CALACA_G01_184 = matching_row_184['DIPC_PRICE'].values[0]
            
#             search_value_185 = '03CALACA_G02'
#             matching_row_185 = df_14[df_14['RESOURCE_NAME'] == search_value_185]
#             file_03CALACA_G02_185 = matching_row_185['DIPC_PRICE'].values[0]

#             search_value_186 = '03KAL_G01'
#             matching_row_186 = df_14[df_14['RESOURCE_NAME'] == search_value_186]
#             file_03KAL_G01_186 = matching_row_186['DIPC_PRICE'].values[0]

#             search_value_187 = '03KAL_G02'
#             matching_row_187 = df_14[df_14['RESOURCE_NAME'] == search_value_187]
#             file_03KAL_G02_187 = matching_row_187['DIPC_PRICE'].values[0]

#             search_value_188 = '03KAL_G03'
#             matching_row_188 = df_14[df_14['RESOURCE_NAME'] == search_value_188]
#             file_03KAL_G03_188 =  matching_row_188['DIPC_PRICE'].values[0]

#             search_value_189 = '03KAL_G04'
#             matching_row_189 = df_14[df_14['RESOURCE_NAME'] == search_value_189]
#             file_03KAL_G04_189 = matching_row_189['DIPC_PRICE'].values[0]

#             search_value_190 = '04LEYTE_A'
#             matching_row_190 = df_14[df_14['RESOURCE_NAME'] == search_value_190]
#             file_04LEYTE_A_190 = matching_row_190['DIPC_PRICE'].values[0]

#             search_value_191 = '05KSPC_G01'
#             matching_row_191 = df_14[df_14['RESOURCE_NAME'] == search_value_191]
#             file_05KSPC_G01_191 = matching_row_191['DIPC_PRICE'].values[0]

#             search_value_192 = '05KSPC_G02'
#             matching_row_192 = df_14[df_14['RESOURCE_NAME'] == search_value_192]
#             file_05KSPC_G02_192 = matching_row_192['DIPC_PRICE'].values[0]

#             search_value_193 = '08BANTAP_L01'
#             matching_row_193 = df_14[df_14['RESOURCE_NAME'] == search_value_193]
#             file_08BANTAP_L01_193 = matching_row_193['DIPC_PRICE'].values[0]

#             search_value_194 = '08PEDC_T1L1'
#             matching_row_194 = df_14[df_14['RESOURCE_NAME'] == search_value_194]
#             file_08PEDC_T1L1_194 = matching_row_194['DIPC_PRICE'].values[0]

#             search_value_195 = '08PEDC_T1L2'
#             matching_row_195 = df_14[df_14['RESOURCE_NAME'] == search_value_195]
#             file_08PEDC_T1L2_195 = matching_row_195['DIPC_PRICE'].values[0]

#             search_value_196 = '08STBAR_T1L1'
#             matching_row_196 = df_14[df_14['RESOURCE_NAME'] == search_value_196]
#             file_08STBAR_T1L1_196 = matching_row_196['DIPC_PRICE'].values[0]

#             # Third Folder
#             filepath_15 = os.path.join(folder_path, files_in_folder[15]) 
#             df_15 = pd.read_csv(filepath_15)

#             search_value_197 = '03BOTOCA_G01'
#             matching_row_197 = df_15[df_15['RESOURCE_NAME'] == search_value_197]
#             file_03BOTOCA_G01_197 = matching_row_197['DIPC_PRICE'].values[0]

#             search_value_198 = '03CALACA_G01'
#             matching_row_198 = df_15[df_15['RESOURCE_NAME'] == search_value_198]
#             file_03CALACA_G01_198 = matching_row_198['DIPC_PRICE'].values[0]

#             search_value_199 = '03CALACA_G02'
#             matching_row_199 = df_15[df_15['RESOURCE_NAME'] == search_value_199]
#             file_03CALACA_G02_199 = matching_row_199['DIPC_PRICE'].values[0]

#             search_value_200 = '03KAL_G01'
#             matching_row_200 = df_15[df_15['RESOURCE_NAME'] == search_value_200]
#             file_03KAL_G01_200 = matching_row_200['DIPC_PRICE'].values[0]

#             search_value_201 = '03KAL_G02'
#             matching_row_201 = df_15[df_15['RESOURCE_NAME'] == search_value_201]
#             file_03KAL_G02_201 = matching_row_201['DIPC_PRICE'].values[0]

#             search_value_202 = '03KAL_G03'
#             matching_row_202 = df_15[df_15['RESOURCE_NAME'] == search_value_202]
#             file_03KAL_G03_202 = matching_row_202['DIPC_PRICE'].values[0]

#             search_value_203 = '03KAL_G04'
#             matching_row_203 = df_15[df_15['RESOURCE_NAME'] == search_value_203]
#             file_03KAL_G04_203 = matching_row_203['DIPC_PRICE'].values[0]
            
#             search_value_204 = '04LEYTE_A'
#             matching_row_204 = df_15[df_15['RESOURCE_NAME'] == search_value_204]
#             file_04LEYTE_A_204 = matching_row_204['DIPC_PRICE'].values[0]

#             search_value_205 = '05KSPC_G01'
#             matching_row_205 = df_15[df_15['RESOURCE_NAME'] == search_value_205]
#             file_05KSPC_G01_205 = matching_row_205['DIPC_PRICE'].values[0]

#             search_value_206 = '05KSPC_G02'
#             matching_row_206 = df_15[df_15['RESOURCE_NAME'] == search_value_206]
#             file_05KSPC_G02_206 = matching_row_206['DIPC_PRICE'].values[0]

#             search_value_207 = '08BANTAP_L01'
#             matching_row_207 = df_15[df_15['RESOURCE_NAME'] == search_value_207]
#             file_08BANTAP_L01_207 = matching_row_207['DIPC_PRICE'].values[0]

#             search_value_208 = '08PEDC_T1L1'
#             matching_row_208 = df_15[df_15['RESOURCE_NAME'] == search_value_208]
#             file_08PEDC_T1L1_208 = matching_row_208['DIPC_PRICE'].values[0]

#             search_value_209 = '08PEDC_T1L2'
#             matching_row_209 = df_15[df_15['RESOURCE_NAME'] == search_value_209]
#             file_08PEDC_T1L2_209 = matching_row_209['DIPC_PRICE'].values[0]

#             search_value_210 = '08STBAR_T1L1'
#             matching_row_210 = df_15[df_15['RESOURCE_NAME'] == search_value_210]
#             file_08STBAR_T1L1_210 = matching_row_210['DIPC_PRICE'].values[0]

#             # Fourth Folder
#             filepath_16 = os.path.join(folder_path, files_in_folder[16]) 
#             df_16 = pd.read_csv(filepath_16)

#             search_value_211 = '03BOTOCA_G01'
#             matching_row_211 = df_16[df_16['RESOURCE_NAME'] == search_value_211]
#             file_03BOTOCA_G01_211 = matching_row_211['DIPC_PRICE'].values[0]

#             search_value_212 = '03CALACA_G01'
#             matching_row_212 = df_16[df_16['RESOURCE_NAME'] == search_value_212]
#             file_03CALACA_G01_212 = matching_row_212['DIPC_PRICE'].values[0]

#             search_value_213 = '03CALACA_G02'
#             matching_row_213 = df_16[df_16['RESOURCE_NAME'] == search_value_213]
#             file_03CALACA_G02_213 = matching_row_213['DIPC_PRICE'].values[0]

#             search_value_214 = '03KAL_G01'
#             matching_row_214 = df_16[df_16['RESOURCE_NAME'] == search_value_214]
#             file_03KAL_G01_214 = matching_row_214['DIPC_PRICE'].values[0]

#             search_value_215 = '03KAL_G02'
#             matching_row_215 = df_16[df_16['RESOURCE_NAME'] == search_value_215]
#             file_03KAL_G02_215 = matching_row_215['DIPC_PRICE'].values[0]

#             search_value_216 = '03KAL_G03'
#             matching_row_216 = df_16[df_16['RESOURCE_NAME'] == search_value_216]
#             file_03KAL_G03_216 = matching_row_216['DIPC_PRICE'].values[0]

#             search_value_217 = '03KAL_G04'
#             matching_row_217 = df_16[df_16['RESOURCE_NAME'] == search_value_217]
#             file_03KAL_G04_217 = matching_row_217['DIPC_PRICE'].values[0]
            
#             search_value_218 = '04LEYTE_A'
#             matching_row_218 = df_16[df_16['RESOURCE_NAME'] == search_value_218]
#             file_04LEYTE_A_218 = matching_row_218['DIPC_PRICE'].values[0]

#             search_value_219 = '05KSPC_G01'
#             matching_row_219 = df_16[df_16['RESOURCE_NAME'] == search_value_219]
#             file_05KSPC_G01_219 = matching_row_219['DIPC_PRICE'].values[0]

#             search_value_220 = '05KSPC_G02'
#             matching_row_220 = df_16[df_16['RESOURCE_NAME'] == search_value_220]
#             file_05KSPC_G02_220 = matching_row_220['DIPC_PRICE'].values[0]

#             search_value_221 = '08BANTAP_L01'
#             matching_row_221 = df_16[df_16['RESOURCE_NAME'] == search_value_221]
#             file_08BANTAP_L01_221 = matching_row_221['DIPC_PRICE'].values[0]

#             search_value_222 = '08PEDC_T1L1'
#             matching_row_222 = df_16[df_16['RESOURCE_NAME'] == search_value_222]
#             file_08PEDC_T1L1_222 = matching_row_222['DIPC_PRICE'].values[0]

#             search_value_223 = '08PEDC_T1L2'
#             matching_row_223 = df_16[df_16['RESOURCE_NAME'] == search_value_223]
#             file_08PEDC_T1L2_223 = matching_row_223['DIPC_PRICE'].values[0]

#             search_value_224 = '08STBAR_T1L1'
#             matching_row_224 = df_16[df_16['RESOURCE_NAME'] == search_value_224]
#             file_08STBAR_T1L1_224 = matching_row_224['DIPC_PRICE'].values[0]

#             # Fifth Folder
#             filepath_17 = os.path.join(folder_path, files_in_folder[17]) 
#             df_17 = pd.read_csv(filepath_17)

#             search_value_225 = '03BOTOCA_G01'
#             matching_row_225 = df_17[df_17['RESOURCE_NAME'] == search_value_225]
#             file_03BOTOCA_G01_225 = matching_row_225['DIPC_PRICE'].values[0]

#             search_value_226 = '03CALACA_G01'
#             matching_row_226 = df_17[df_17['RESOURCE_NAME'] == search_value_226]
#             file_03CALACA_G01_226 = matching_row_226['DIPC_PRICE'].values[0]

#             search_value_227 = '03CALACA_G02'
#             matching_row_227 = df_17[df_17['RESOURCE_NAME'] == search_value_227]
#             file_03CALACA_G02_227 = matching_row_227['DIPC_PRICE'].values[0]

#             search_value_228 = '03KAL_G01'
#             matching_row_228 = df_17[df_17['RESOURCE_NAME'] == search_value_228]
#             file_03KAL_G01_228 = matching_row_228['DIPC_PRICE'].values[0]

#             search_value_229 = '03KAL_G02'
#             matching_row_229 = df_17[df_17['RESOURCE_NAME'] == search_value_229]
#             file_03KAL_G02_229 = matching_row_229['DIPC_PRICE'].values[0]

#             search_value_230 = '03KAL_G03'
#             matching_row_230 = df_17[df_17['RESOURCE_NAME'] == search_value_230]
#             file_03KAL_G03_230 = matching_row_230['DIPC_PRICE'].values[0]

#             search_value_231 = '03KAL_G04'
#             matching_row_231 = df_17[df_17['RESOURCE_NAME'] == search_value_231]
#             file_03KAL_G04_231 = matching_row_231['DIPC_PRICE'].values[0]

#             search_value_232 = '04LEYTE_A'
#             matching_row_232 = df_17[df_17['RESOURCE_NAME'] == search_value_232]
#             file_04LEYTE_A_232 = matching_row_232['DIPC_PRICE'].values[0]

#             search_value_233 = '05KSPC_G01'
#             matching_row_233 = df_17[df_17['RESOURCE_NAME'] == search_value_233]
#             file_05KSPC_G01_233 = matching_row_233['DIPC_PRICE'].values[0]

#             search_value_234 = '05KSPC_G02'
#             matching_row_234 = df_17[df_17['RESOURCE_NAME'] == search_value_234]
#             file_05KSPC_G02_234 = matching_row_234['DIPC_PRICE'].values[0]

#             search_value_235 = '08BANTAP_L01'
#             matching_row_235 = df_17[df_17['RESOURCE_NAME'] == search_value_235]
#             file_08BANTAP_L01_235 = matching_row_235['DIPC_PRICE'].values[0]

#             search_value_236 = '08PEDC_T1L1'
#             matching_row_236 = df_17[df_17['RESOURCE_NAME'] == search_value_236]
#             file_08PEDC_T1L1_236 = matching_row_236['DIPC_PRICE'].values[0]

#             search_value_237 = '08PEDC_T1L2'
#             matching_row_237 = df_17[df_17['RESOURCE_NAME'] == search_value_237]
#             file_08PEDC_T1L2_237 = matching_row_237['DIPC_PRICE'].values[0]

#             search_value_238 = '08STBAR_T1L1'
#             matching_row_238 = df_17[df_17['RESOURCE_NAME'] == search_value_238]
#             file_08STBAR_T1L1_238 = matching_row_238['DIPC_PRICE'].values[0]
                 
#             # Sixth Folder
#             filepath_18 = os.path.join(folder_path, files_in_folder[18]) 
#             df_18 = pd.read_csv(filepath_18)

#             search_value_239 = '03BOTOCA_G01'
#             matching_row_239 = df_18[df_18['RESOURCE_NAME'] == search_value_239]
#             file_03BOTOCA_G01_239 = matching_row_239['DIPC_PRICE'].values[0]

#             search_value_240 = '03CALACA_G01'
#             matching_row_240 = df_18[df_18['RESOURCE_NAME'] == search_value_240]
#             file_03CALACA_G01_240 = matching_row_240['DIPC_PRICE'].values[0]

#             search_value_241 = '03CALACA_G02'
#             matching_row_241 = df_18[df_18['RESOURCE_NAME'] == search_value_241]
#             file_03CALACA_G02_241 = matching_row_241['DIPC_PRICE'].values[0]

#             search_value_242 = '03KAL_G01'
#             matching_row_242 = df_18[df_18['RESOURCE_NAME'] == search_value_242]
#             file_03KAL_G01_242 = matching_row_242['DIPC_PRICE'].values[0]

#             search_value_243 = '03KAL_G02'
#             matching_row_243 = df_18[df_18['RESOURCE_NAME'] == search_value_243]
#             file_03KAL_G02_243 = matching_row_243['DIPC_PRICE'].values[0]

#             search_value_244 = '03KAL_G03'
#             matching_row_244 = df_18[df_18['RESOURCE_NAME'] == search_value_244]
#             file_03KAL_G03_244 = matching_row_244['DIPC_PRICE'].values[0]

#             search_value_245 = '03KAL_G04'
#             matching_row_245 = df_18[df_18['RESOURCE_NAME'] == search_value_245]
#             file_03KAL_G04_245 = matching_row_245['DIPC_PRICE'].values[0]

#             search_value_246 = '04LEYTE_A'
#             matching_row_246 = df_18[df_18['RESOURCE_NAME'] == search_value_246]
#             file_04LEYTE_A_246 = matching_row_246['DIPC_PRICE'].values[0]

#             search_value_247 = '05KSPC_G01'
#             matching_row_247 = df_18[df_18['RESOURCE_NAME'] == search_value_247]
#             file_05KSPC_G01_247 = matching_row_247['DIPC_PRICE'].values[0]

#             search_value_248 = '05KSPC_G02'
#             matching_row_248 = df_18[df_18['RESOURCE_NAME'] == search_value_248]
#             file_05KSPC_G02_248 = matching_row_248['DIPC_PRICE'].values[0]

#             search_value_249 = '08BANTAP_L01'
#             matching_row_249 = df_18[df_18['RESOURCE_NAME'] == search_value_249]
#             file_08BANTAP_L01_249 = matching_row_249['DIPC_PRICE'].values[0]

#             search_value_250 = '08PEDC_T1L1'
#             matching_row_250 = df_18[df_18['RESOURCE_NAME'] == search_value_250]
#             file_08PEDC_T1L1_250 = matching_row_250['DIPC_PRICE'].values[0]

#             search_value_251 = '08PEDC_T1L2'
#             matching_row_251 = df_18[df_18['RESOURCE_NAME'] == search_value_251]
#             file_08PEDC_T1L2_251 = matching_row_251['DIPC_PRICE'].values[0]

#             search_value_252 = '08STBAR_T1L1'
#             matching_row_252 = df_18[df_18['RESOURCE_NAME'] == search_value_252]
#             file_08STBAR_T1L1_252 = matching_row_252['DIPC_PRICE'].values[0]

#             # Seventh Folder
#             filepath_19 = os.path.join(folder_path, files_in_folder[19]) 
#             df_19 = pd.read_csv(filepath_19)

#             search_value_253 = '03BOTOCA_G01'
#             matching_row_253 = df_19[df_19['RESOURCE_NAME'] == search_value_253]
#             file_03BOTOCA_G01_253 = matching_row_253['DIPC_PRICE'].values[0]

#             search_value_254 = '03CALACA_G01'
#             matching_row_254 = df_19[df_19['RESOURCE_NAME'] == search_value_254]
#             file_03CALACA_G01_254 = matching_row_254['DIPC_PRICE'].values[0]

#             search_value_255 = '03CALACA_G02'
#             matching_row_255 = df_19[df_19['RESOURCE_NAME'] == search_value_255]
#             file_03CALACA_G02_255 = matching_row_255['DIPC_PRICE'].values[0]

#             search_value_256 = '03KAL_G01'
#             matching_row_256 = df_19[df_19['RESOURCE_NAME'] == search_value_256]
#             file_03KAL_G01_256 = matching_row_256['DIPC_PRICE'].values[0]

#             search_value_257 = '03KAL_G02'
#             matching_row_257 = df_19[df_19['RESOURCE_NAME'] == search_value_257]
#             file_03KAL_G02_257 = matching_row_257['DIPC_PRICE'].values[0]

#             search_value_258 = '03KAL_G03'
#             matching_row_258 = df_19[df_19['RESOURCE_NAME'] == search_value_258]
#             file_03KAL_G03_258 = matching_row_258['DIPC_PRICE'].values[0]

#             search_value_259 = '03KAL_G04'
#             matching_row_259 = df_19[df_19['RESOURCE_NAME'] == search_value_259]
#             file_03KAL_G04_259 = matching_row_259['DIPC_PRICE'].values[0]

#             search_value_260 = '04LEYTE_A'
#             matching_row_260 = df_19[df_19['RESOURCE_NAME'] == search_value_260]
#             file_04LEYTE_A_260 = matching_row_260['DIPC_PRICE'].values[0]

#             search_value_261 = '05KSPC_G01'
#             matching_row_261 = df_19[df_19['RESOURCE_NAME'] == search_value_261]
#             file_05KSPC_G01_261 = matching_row_261['DIPC_PRICE'].values[0]

#             search_value_262 = '05KSPC_G02'
#             matching_row_262 = df_19[df_19['RESOURCE_NAME'] == search_value_262]
#             file_05KSPC_G02_262 = matching_row_262['DIPC_PRICE'].values[0]

#             search_value_263 = '08BANTAP_L01'
#             matching_row_263 = df_19[df_19['RESOURCE_NAME'] == search_value_263]
#             file_08BANTAP_L01_263 = matching_row_263['DIPC_PRICE'].values[0]

#             search_value_264 = '08PEDC_T1L1'
#             matching_row_264 = df_19[df_19['RESOURCE_NAME'] == search_value_264]
#             file_08PEDC_T1L1_264 = matching_row_264['DIPC_PRICE'].values[0]

#             search_value_265 = '08PEDC_T1L2'
#             matching_row_265 = df_19[df_19['RESOURCE_NAME'] == search_value_265]
#             file_08PEDC_T1L2_265 = matching_row_265['DIPC_PRICE'].values[0]

#             search_value_266 = '08STBAR_T1L1'
#             matching_row_266 = df_19[df_19['RESOURCE_NAME'] == search_value_266]
#             file_08STBAR_T1L1_266 = matching_row_266['DIPC_PRICE'].values[0]

#             # Eighth Folder
#             filepath_20 = os.path.join(folder_path, files_in_folder[20]) 
#             df_20 = pd.read_csv(filepath_20)

#             search_value_267 = '03BOTOCA_G01'
#             matching_row_267 = df_20[df_20['RESOURCE_NAME'] == search_value_267]
#             file_03BOTOCA_G01_267 = matching_row_267['DIPC_PRICE'].values[0]

#             search_value_268 = '03CALACA_G01'
#             matching_row_268 = df_20[df_20['RESOURCE_NAME'] == search_value_268]
#             file_03CALACA_G01_268 = matching_row_268['DIPC_PRICE'].values[0]

#             search_value_269 = '03CALACA_G02'
#             matching_row_269 = df_20[df_20['RESOURCE_NAME'] == search_value_269]
#             file_03CALACA_G02_269 = matching_row_269['DIPC_PRICE'].values[0]

#             search_value_270 = '03KAL_G01'
#             matching_row_270 = df_20[df_20['RESOURCE_NAME'] == search_value_270]
#             file_03KAL_G01_270 = matching_row_270['DIPC_PRICE'].values[0]

#             search_value_271 = '03KAL_G02'
#             matching_row_271 = df_20[df_20['RESOURCE_NAME'] == search_value_271]
#             file_03KAL_G02_271 = matching_row_271['DIPC_PRICE'].values[0]

#             search_value_272 = '03KAL_G03'
#             matching_row_272 = df_20[df_20['RESOURCE_NAME'] == search_value_272]
#             file_03KAL_G03_272 = matching_row_272['DIPC_PRICE'].values[0]

#             search_value_273 = '03KAL_G04'
#             matching_row_273 = df_20[df_20['RESOURCE_NAME'] == search_value_273]
#             file_03KAL_G04_273 = matching_row_273['DIPC_PRICE'].values[0]

#             search_value_274 = '04LEYTE_A'
#             matching_row_274 = df_20[df_20['RESOURCE_NAME'] == search_value_274]
#             file_04LEYTE_A_274 = matching_row_274['DIPC_PRICE'].values[0]

#             search_value_275 = '05KSPC_G01'
#             matching_row_275 = df_20[df_20['RESOURCE_NAME'] == search_value_275]
#             file_05KSPC_G01_275 = matching_row_275['DIPC_PRICE'].values[0]

#             search_value_276 = '05KSPC_G02'
#             matching_row_276 = df_20[df_20['RESOURCE_NAME'] == search_value_276]
#             file_05KSPC_G02_276 = matching_row_276['DIPC_PRICE'].values[0]

#             search_value_277 = '08BANTAP_L01'
#             matching_row_277 = df_20[df_20['RESOURCE_NAME'] == search_value_277]
#             file_08BANTAP_L01_277 = matching_row_277['DIPC_PRICE'].values[0]

#             search_value_278 = '08PEDC_T1L1'
#             matching_row_278 = df_20[df_20['RESOURCE_NAME'] == search_value_278]
#             file_08PEDC_T1L1_278 = matching_row_278['DIPC_PRICE'].values[0]

#             search_value_279 = '08PEDC_T1L2'
#             matching_row_279 = df_20[df_20['RESOURCE_NAME'] == search_value_279]
#             file_08PEDC_T1L2_279 = matching_row_279['DIPC_PRICE'].values[0]

#             search_value_280 = '08STBAR_T1L1'
#             matching_row_280 = df_20[df_20['RESOURCE_NAME'] == search_value_280]
#             file_08STBAR_T1L1_280 = matching_row_280['DIPC_PRICE'].values[0]

#             # Ninth Folder
#             filepath_21 = os.path.join(folder_path, files_in_folder[21]) 
#             df_21 = pd.read_csv(filepath_21)

#             search_value_281 = '03BOTOCA_G01'
#             matching_row_281 = df_21[df_21['RESOURCE_NAME'] == search_value_281]
#             file_03BOTOCA_G01_281 = matching_row_281['DIPC_PRICE'].values[0]

#             search_value_282 = '03CALACA_G01'
#             matching_row_282 = df_21[df_21['RESOURCE_NAME'] == search_value_282]
#             file_03CALACA_G01_282 = matching_row_282['DIPC_PRICE'].values[0]

#             search_value_283 = '03CALACA_G02'
#             matching_row_283 = df_21[df_21['RESOURCE_NAME'] == search_value_283]
#             file_03CALACA_G02_283 = matching_row_283['DIPC_PRICE'].values[0]

#             search_value_284 = '03KAL_G01'
#             matching_row_284 = df_21[df_21['RESOURCE_NAME'] == search_value_284]
#             file_03KAL_G01_284 = matching_row_284['DIPC_PRICE'].values[0]

#             search_value_285 = '03KAL_G02'
#             matching_row_285 = df_21[df_21['RESOURCE_NAME'] == search_value_285]
#             file_03KAL_G02_285 = matching_row_285['DIPC_PRICE'].values[0]

#             search_value_286 = '03KAL_G03'
#             matching_row_286 = df_21[df_21['RESOURCE_NAME'] == search_value_286]
#             file_03KAL_G03_286 = matching_row_286['DIPC_PRICE'].values[0]

#             search_value_287 = '03KAL_G04'
#             matching_row_287 = df_21[df_21['RESOURCE_NAME'] == search_value_287]
#             file_03KAL_G04_287 = matching_row_287['DIPC_PRICE'].values[0]

#             search_value_288 = '04LEYTE_A'
#             matching_row_288 = df_21[df_21['RESOURCE_NAME'] == search_value_288]
#             file_04LEYTE_A_288 = matching_row_288['DIPC_PRICE'].values[0]

#             search_value_289 = '05KSPC_G01'
#             matching_row_289 = df_21[df_21['RESOURCE_NAME'] == search_value_289]
#             file_05KSPC_G01_289 = matching_row_289['DIPC_PRICE'].values[0]

#             search_value_290 = '05KSPC_G02'
#             matching_row_290 = df_21[df_21['RESOURCE_NAME'] == search_value_290]
#             file_05KSPC_G02_290 = matching_row_290['DIPC_PRICE'].values[0]

#             search_value_291 = '08BANTAP_L01'
#             matching_row_291 = df_21[df_21['RESOURCE_NAME'] == search_value_291]
#             file_08BANTAP_L01_291 = matching_row_291['DIPC_PRICE'].values[0]

#             search_value_292 = '08PEDC_T1L1'
#             matching_row_292 = df_21[df_21['RESOURCE_NAME'] == search_value_292]
#             file_08PEDC_T1L1_292 = matching_row_292['DIPC_PRICE'].values[0]

#             search_value_293 = '08PEDC_T1L2'
#             matching_row_293 = df_21[df_21['RESOURCE_NAME'] == search_value_293]
#             file_08PEDC_T1L2_293 = matching_row_293['DIPC_PRICE'].values[0]

#             search_value_294 = '08STBAR_T1L1'
#             matching_row_294 = df_21[df_21['RESOURCE_NAME'] == search_value_294]
#             file_08STBAR_T1L1_294 = matching_row_294['DIPC_PRICE'].values[0]

#             # Tenth Folder
#             filepath_22 = os.path.join(folder_path, files_in_folder[22]) 
#             df_22 = pd.read_csv(filepath_22)

#             search_value_295 = '03BOTOCA_G01'
#             matching_row_295 = df_22[df_22['RESOURCE_NAME'] == search_value_295]
#             file_03BOTOCA_G01_295 = matching_row_295['DIPC_PRICE'].values[0]

#             search_value_296 = '03CALACA_G01'
#             matching_row_296 = df_22[df_22['RESOURCE_NAME'] == search_value_296]
#             file_03CALACA_G01_296 = matching_row_296['DIPC_PRICE'].values[0]

#             search_value_297 = '03CALACA_G02'
#             matching_row_297 = df_22[df_22['RESOURCE_NAME'] == search_value_297]
#             file_03CALACA_G02_297 = matching_row_297['DIPC_PRICE'].values[0]

#             search_value_298 = '03KAL_G01'
#             matching_row_298 = df_22[df_22['RESOURCE_NAME'] == search_value_298]
#             file_03KAL_G01_298 = matching_row_298['DIPC_PRICE'].values[0]

#             search_value_299 = '03KAL_G02'
#             matching_row_299 = df_22[df_22['RESOURCE_NAME'] == search_value_299]
#             file_03KAL_G02_299 = matching_row_299['DIPC_PRICE'].values[0]

#             search_value_300 = '03KAL_G03'
#             matching_row_300 = df_22[df_22['RESOURCE_NAME'] == search_value_300]
#             file_03KAL_G03_300 = matching_row_300['DIPC_PRICE'].values[0]

#             search_value_301 = '03KAL_G04'
#             matching_row_301 = df_22[df_22['RESOURCE_NAME'] == search_value_301]
#             file_03KAL_G04_301 = matching_row_301['DIPC_PRICE'].values[0]

#             search_value_302 = '04LEYTE_A'
#             matching_row_302 = df_22[df_22['RESOURCE_NAME'] == search_value_302]
#             file_04LEYTE_A_302 = matching_row_302['DIPC_PRICE'].values[0]

#             search_value_303 = '05KSPC_G01'
#             matching_row_303 = df_22[df_22['RESOURCE_NAME'] == search_value_303]
#             file_05KSPC_G01_303 = matching_row_303['DIPC_PRICE'].values[0]

#             search_value_304 = '05KSPC_G02'
#             matching_row_304 = df_22[df_22['RESOURCE_NAME'] == search_value_304]
#             file_05KSPC_G02_304 = matching_row_304['DIPC_PRICE'].values[0]

#             search_value_305 = '08BANTAP_L01'
#             matching_row_305 = df_22[df_22['RESOURCE_NAME'] == search_value_305]
#             file_08BANTAP_L01_305 = matching_row_305['DIPC_PRICE'].values[0]

#             search_value_306 = '08PEDC_T1L1'
#             matching_row_306 = df_22[df_22['RESOURCE_NAME'] == search_value_306]
#             file_08PEDC_T1L1_306 = matching_row_306['DIPC_PRICE'].values[0]

#             search_value_307 = '08PEDC_T1L2'
#             matching_row_307 = df_22[df_22['RESOURCE_NAME'] == search_value_307]
#             file_08PEDC_T1L2_307 = matching_row_307['DIPC_PRICE'].values[0]

#             search_value_308 = '08STBAR_T1L1'
#             matching_row_308 = df_22[df_22['RESOURCE_NAME'] == search_value_308]
#             file_08STBAR_T1L1_308 = matching_row_308['DIPC_PRICE'].values[0]

#             # Eleventh Folder
#             filepath_23 = os.path.join(folder_path, files_in_folder[23]) 
#             df_23 = pd.read_csv(filepath_23)

#             search_value_309 = '03BOTOCA_G01'
#             matching_row_309 = df_23[df_23['RESOURCE_NAME'] == search_value_309]
#             file_03BOTOCA_G01_309 = matching_row_309['DIPC_PRICE'].values[0]

#             search_value_310 = '03CALACA_G01'
#             matching_row_310 = df_23[df_23['RESOURCE_NAME'] == search_value_310]
#             file_03CALACA_G01_310 = matching_row_310['DIPC_PRICE'].values[0]

#             search_value_311 = '03CALACA_G02'
#             matching_row_311 = df_23[df_23['RESOURCE_NAME'] == search_value_311]
#             file_03CALACA_G02_311 = matching_row_311['DIPC_PRICE'].values[0]

#             search_value_312 = '03KAL_G01'
#             matching_row_312 = df_23[df_23['RESOURCE_NAME'] == search_value_312]
#             file_03KAL_G01_312 = matching_row_312['DIPC_PRICE'].values[0]

#             search_value_313 = '03KAL_G02'
#             matching_row_313 = df_23[df_23['RESOURCE_NAME'] == search_value_313]
#             file_03KAL_G02_313 = matching_row_313['DIPC_PRICE'].values[0]

#             search_value_314 = '03KAL_G03'
#             matching_row_314 = df_23[df_23['RESOURCE_NAME'] == search_value_314]
#             file_03KAL_G03_314 = matching_row_314['DIPC_PRICE'].values[0]

#             search_value_315 = '03KAL_G04'
#             matching_row_315 = df_23[df_23['RESOURCE_NAME'] == search_value_315]
#             file_03KAL_G04_315 = matching_row_315['DIPC_PRICE'].values[0]

#             search_value_316 = '04LEYTE_A'
#             matching_row_316 = df_23[df_23['RESOURCE_NAME'] == search_value_316]
#             file_04LEYTE_A_316 = matching_row_316['DIPC_PRICE'].values[0]

#             search_value_317 = '05KSPC_G01'
#             matching_row_317 = df_23[df_23['RESOURCE_NAME'] == search_value_317]
#             file_05KSPC_G01_317 = matching_row_317['DIPC_PRICE'].values[0]

#             search_value_318 = '05KSPC_G02'
#             matching_row_318 = df_23[df_23['RESOURCE_NAME'] == search_value_318]
#             file_05KSPC_G02_318 = matching_row_318['DIPC_PRICE'].values[0]

#             search_value_319 = '08BANTAP_L01'
#             matching_row_319 = df_23[df_23['RESOURCE_NAME'] == search_value_319]
#             file_08BANTAP_L01_319 = matching_row_319['DIPC_PRICE'].values[0]

#             search_value_320 = '08PEDC_T1L1'
#             matching_row_320 = df_23[df_23['RESOURCE_NAME'] == search_value_320]
#             file_08PEDC_T1L1_320 = matching_row_320['DIPC_PRICE'].values[0]

#             search_value_321 = '08PEDC_T1L2'
#             matching_row_321 = df_23[df_23['RESOURCE_NAME'] == search_value_321]
#             file_08PEDC_T1L2_321 = matching_row_321['DIPC_PRICE'].values[0]

#             search_value_322 = '08STBAR_T1L1'
#             matching_row_322 = df_23[df_23['RESOURCE_NAME'] == search_value_322]
#             file_08STBAR_T1L1_322 = matching_row_322['DIPC_PRICE'].values[0]

#             # Twelvth Folder
#             filepath_24 = os.path.join(folder_path, files_in_folder[24]) 
#             df_24 = pd.read_csv(filepath_24)

#             search_value_323 = '03BOTOCA_G01'
#             matching_row_323 = df_24[df_24['RESOURCE_NAME'] == search_value_323]
#             file_03BOTOCA_G01_323 = matching_row_323['DIPC_PRICE'].values[0]

#             search_value_324 = '03CALACA_G01'
#             matching_row_324 = df_24[df_24['RESOURCE_NAME'] == search_value_324]
#             file_03CALACA_G01_324 = matching_row_324['DIPC_PRICE'].values[0]

#             search_value_325 = '03CALACA_G02'
#             matching_row_325 = df_24[df_24['RESOURCE_NAME'] == search_value_325]
#             file_03CALACA_G02_325 = matching_row_325['DIPC_PRICE'].values[0]

#             search_value_326 = '03KAL_G01'
#             matching_row_326 = df_24[df_24['RESOURCE_NAME'] == search_value_326]
#             file_03KAL_G01_326 = matching_row_326['DIPC_PRICE'].values[0]

#             search_value_327 = '03KAL_G02'
#             matching_row_327 = df_24[df_24['RESOURCE_NAME'] == search_value_327]
#             file_03KAL_G02_327 = matching_row_327['DIPC_PRICE'].values[0]

#             search_value_328 = '03KAL_G03'
#             matching_row_328 = df_24[df_24['RESOURCE_NAME'] == search_value_328]
#             file_03KAL_G03_328 = matching_row_328['DIPC_PRICE'].values[0]

#             search_value_329 = '03KAL_G04'
#             matching_row_329 = df_24[df_24['RESOURCE_NAME'] == search_value_329]
#             file_03KAL_G04_329 = matching_row_329['DIPC_PRICE'].values[0]

#             search_value_330 = '04LEYTE_A'
#             matching_row_330 = df_24[df_24['RESOURCE_NAME'] == search_value_330]
#             file_04LEYTE_A_330 = matching_row_330['DIPC_PRICE'].values[0]

#             search_value_331 = '05KSPC_G01'
#             matching_row_331 = df_24[df_24['RESOURCE_NAME'] == search_value_331]
#             file_05KSPC_G01_331 = matching_row_331['DIPC_PRICE'].values[0]

#             search_value_332 = '05KSPC_G02'
#             matching_row_332 = df_24[df_24['RESOURCE_NAME'] == search_value_332]
#             file_05KSPC_G02_332 = matching_row_332['DIPC_PRICE'].values[0]

#             search_value_333 = '08BANTAP_L01'
#             matching_row_333 = df_24[df_24['RESOURCE_NAME'] == search_value_333]
#             file_08BANTAP_L01_333 = matching_row_333['DIPC_PRICE'].values[0]

#             search_value_334 = '08PEDC_T1L1'
#             matching_row_334 = df_24[df_24['RESOURCE_NAME'] == search_value_334]
#             file_08PEDC_T1L1_334 = matching_row_334['DIPC_PRICE'].values[0]

#             search_value_335 = '08PEDC_T1L2'
#             matching_row_335 = df_24[df_24['RESOURCE_NAME'] == search_value_335]
#             file_08PEDC_T1L2_335 = matching_row_335['DIPC_PRICE'].values[0]

#             search_value_336 = '08STBAR_T1L1'
#             matching_row_336 = df_24[df_24['RESOURCE_NAME'] == search_value_336]
#             file_08STBAR_T1L1_336 = matching_row_336['DIPC_PRICE'].values[0]
                    
#             botoca_g01_total_15 = (file_03BOTOCA_G01_169 + file_03BOTOCA_G01_183 + file_03BOTOCA_G01_197 + file_03BOTOCA_G01_211 + file_03BOTOCA_G01_225 + file_03BOTOCA_G01_239 + file_03BOTOCA_G01_253 + file_03BOTOCA_G01_267 + file_03BOTOCA_G01_281 + file_03BOTOCA_G01_295 + file_03BOTOCA_G01_309 + file_03BOTOCA_G01_323)/12
#             calaca_g01_total_16 = (file_03CALACA_G01_170 + file_03CALACA_G01_184 + file_03CALACA_G01_198 + file_03CALACA_G01_212 + file_03CALACA_G01_226 + file_03CALACA_G01_240 + file_03CALACA_G01_254 + file_03CALACA_G01_268 + file_03CALACA_G01_282 + file_03CALACA_G01_296 + file_03CALACA_G01_310 + file_03CALACA_G01_324)/12
#             calaca_g02_total_17 = (file_03CALACA_G02_171 + file_03CALACA_G02_185 + file_03CALACA_G02_199 + file_03CALACA_G02_213 + file_03CALACA_G02_227 + file_03CALACA_G02_241 + file_03CALACA_G02_255 + file_03CALACA_G02_269 + file_03CALACA_G02_283 + file_03CALACA_G02_297 + file_03CALACA_G02_311 + file_03CALACA_G02_325)/12
#             kal_g01_total_18 = (file_03KAL_G01_172 + file_03KAL_G01_186 + file_03KAL_G01_200 + file_03KAL_G01_214 + file_03KAL_G01_228 + file_03KAL_G01_242 + file_03KAL_G01_256 + file_03KAL_G01_270 + file_03KAL_G01_284 + file_03KAL_G01_298 + file_03KAL_G01_312 + file_03KAL_G01_326)/12
#             kal_g02_total_19 = (file_03KAL_G02_173 + file_03KAL_G02_187 + file_03KAL_G02_201 + file_03KAL_G02_215 + file_03KAL_G02_229 + file_03KAL_G02_243 + file_03KAL_G02_257 + file_03KAL_G02_271 + file_03KAL_G02_285 + file_03KAL_G02_299 + file_03KAL_G02_313 + file_03KAL_G02_327)/12
#             kal_g03_total_20 = (file_03KAL_G03_174 + file_03KAL_G03_188 + file_03KAL_G03_202 + file_03KAL_G03_216 + file_03KAL_G03_230 + file_03KAL_G03_244 + file_03KAL_G03_258 + file_03KAL_G03_272 + file_03KAL_G03_286 + file_03KAL_G03_300 + file_03KAL_G03_314 + file_03KAL_G03_328)/12
#             kal_g04_total_21 = (file_03KAL_G04_175 + file_03KAL_G04_189 + file_03KAL_G04_203 + file_03KAL_G04_217 + file_03KAL_G04_231 + file_03KAL_G04_245 + file_03KAL_G04_259 + file_03KAL_G04_273 + file_03KAL_G04_287 + file_03KAL_G04_301 + file_03KAL_G04_315 + file_03KAL_G04_329)/12
#             leyte_a_total_22 = (file_04LEYTE_A_176 + file_04LEYTE_A_190 + file_04LEYTE_A_204 + file_04LEYTE_A_218 + file_04LEYTE_A_232 + file_04LEYTE_A_246 + file_04LEYTE_A_260 + file_04LEYTE_A_274 + file_04LEYTE_A_288 + file_04LEYTE_A_302 + file_04LEYTE_A_316 + file_04LEYTE_A_330)/12
#             kspc_g01_total_23 = (file_05KSPC_G01_177 + file_05KSPC_G01_191 + file_05KSPC_G01_205 + file_05KSPC_G01_219 + file_05KSPC_G01_233 + file_05KSPC_G01_247 + file_05KSPC_G01_261 + file_05KSPC_G01_275 + file_05KSPC_G01_289 + file_05KSPC_G01_303 + file_05KSPC_G01_317 + file_05KSPC_G01_331)/12
#             kspc_g02_total_24 = (file_05KSPC_G02_178 + file_05KSPC_G02_192 + file_05KSPC_G02_206 + file_05KSPC_G02_220 + file_05KSPC_G02_234 + file_05KSPC_G02_248 + file_05KSPC_G02_262 + file_05KSPC_G02_276 + file_05KSPC_G02_290 + file_05KSPC_G02_304 + file_05KSPC_G02_318 + file_05KSPC_G02_332)/12
#             bantap_l01_total_25 = (file_08BANTAP_L01_179 + file_08BANTAP_L01_193 + file_08BANTAP_L01_207 + file_08BANTAP_L01_221 + file_08BANTAP_L01_235 + file_08BANTAP_L01_249 + file_08BANTAP_L01_263 + file_08BANTAP_L01_277 + file_08BANTAP_L01_291 + file_08BANTAP_L01_305 + file_08BANTAP_L01_319 + file_08BANTAP_L01_333)/12
#             pedc_t1l1_total_26 = (file_08PEDC_T1L1_180 + file_08PEDC_T1L1_194 + file_08PEDC_T1L1_208 + file_08PEDC_T1L1_222 + file_08PEDC_T1L1_236 + file_08PEDC_T1L1_250 + file_08PEDC_T1L1_264 + file_08PEDC_T1L1_278 + file_08PEDC_T1L1_292 + file_08PEDC_T1L1_306 + file_08PEDC_T1L1_320 + file_08PEDC_T1L1_334)/12
#             pedc_t1l2_total_27 = (file_08PEDC_T1L2_181 + file_08PEDC_T1L2_195 + file_08PEDC_T1L2_209 + file_08PEDC_T1L2_223 + file_08PEDC_T1L2_237 + file_08PEDC_T1L2_251 + file_08PEDC_T1L2_265 + file_08PEDC_T1L2_279 + file_08PEDC_T1L2_293 + file_08PEDC_T1L2_307 + file_08PEDC_T1L2_321 + file_08PEDC_T1L2_335)/12
#             stbar_t1l1_total_28 = (file_08STBAR_T1L1_182 + file_08STBAR_T1L1_196 + file_08STBAR_T1L1_210 + file_08STBAR_T1L1_224 + file_08STBAR_T1L1_238 + file_08STBAR_T1L1_252 + file_08STBAR_T1L1_266 + file_08STBAR_T1L1_280 + file_08STBAR_T1L1_294 + file_08STBAR_T1L1_308 + file_08PEDC_T1L2_322 + file_08PEDC_T1L2_336)/12

#             filepath_25 = os.path.join(folder_path, files_in_folder[25]) 
#             df_25 = pd.read_csv(filepath_25)

#             search_value_337 = '03BOTOCA_G01'
#             matching_row_337 = df_25[df_25['RESOURCE_NAME'] == search_value_337]
#             file_03BOTOCA_G01_337 = matching_row_337['DIPC_PRICE'].values[0]

#             search_value_338 = '03CALACA_G01'
#             matching_row_338 = df_25[df_25['RESOURCE_NAME'] == search_value_338]
#             file_03CALACA_G01_338 = matching_row_338['DIPC_PRICE'].values[0]
            
#             search_value_339 = '03CALACA_G02'
#             matching_row_339 = df_25[df_25['RESOURCE_NAME'] == search_value_339]
#             file_03CALACA_G02_339 = matching_row_339['DIPC_PRICE'].values[0]
            
#             search_value_340 = '03KAL_G01'
#             matching_row_340 = df_25[df_25['RESOURCE_NAME'] == search_value_340]
#             file_03KAL_G01_340 = matching_row_340['DIPC_PRICE'].values[0]

#             search_value_341 = '03KAL_G02'
#             matching_row_341 = df_25[df_25['RESOURCE_NAME'] == search_value_341]
#             file_03KAL_G02_341 = matching_row_341['DIPC_PRICE'].values[0]
            
#             search_value_342 = '03KAL_G03'
#             matching_row_342 = df_25[df_25['RESOURCE_NAME'] == search_value_342]
#             file_03KAL_G03_342 = matching_row_342['DIPC_PRICE'].values[0]

#             search_value_343 = '03KAL_G04'
#             matching_row_343 = df_25[df_25['RESOURCE_NAME'] == search_value_343]
#             file_03KAL_G04_343 = matching_row_343['DIPC_PRICE'].values[0]

#             search_value_344 = '04LEYTE_A'
#             matching_row_344 = df_25[df_25['RESOURCE_NAME'] == search_value_344]
#             file_04LEYTE_A_344 = matching_row_344['DIPC_PRICE'].values[0]

#             search_value_345 = '05KSPC_G01'
#             matching_row_345 = df_25[df_25['RESOURCE_NAME'] == search_value_345]
#             file_05KSPC_G01_345 = matching_row_345['DIPC_PRICE'].values[0]

#             search_value_346 = '05KSPC_G02'
#             matching_row_346 = df_25[df_25['RESOURCE_NAME'] == search_value_346]
#             file_05KSPC_G02_346 = matching_row_346['DIPC_PRICE'].values[0]

#             search_value_347 = '08BANTAP_L01'
#             matching_row_347 = df_25[df_25['RESOURCE_NAME'] == search_value_347]
#             file_08BANTAP_L01_347 = matching_row_347['DIPC_PRICE'].values[0]

#             search_value_348 = '08PEDC_T1L1'
#             matching_row_348 = df_25[df_25['RESOURCE_NAME'] == search_value_348]
#             file_08PEDC_T1L1_348 = matching_row_348['DIPC_PRICE'].values[0]

#             search_value_349 = '08PEDC_T1L2'
#             matching_row_349 = df_25[df_25['RESOURCE_NAME'] ==  search_value_349]
#             file_08PEDC_T1L2_349 = matching_row_349['DIPC_PRICE'].values[0]

#             search_value_350 = '08STBAR_T1L1'
#             matching_row_350 = df_25[df_25['RESOURCE_NAME'] ==  search_value_350]
#             file_08STBAR_T1L1_350 = matching_row_350['DIPC_PRICE'].values[0]
            
#             # 2nd Folder
#             filepath_26 = os.path.join(folder_path, files_in_folder[26]) 
#             df_26 = pd.read_csv(filepath_26)

#             search_value_351 = '03BOTOCA_G01'
#             matching_row_351 = df_26[df_26['RESOURCE_NAME'] == search_value_351]
#             file_03BOTOCA_G01_351 = matching_row_351['DIPC_PRICE'].values[0]

#             search_value_352 = '03CALACA_G01'
#             matching_row_352 = df_26[df_26['RESOURCE_NAME'] == search_value_352]
#             file_03CALACA_G01_352 = matching_row_352['DIPC_PRICE'].values[0]

#             search_value_353 = '03CALACA_G02'
#             matching_row_353 = df_26[df_26['RESOURCE_NAME'] == search_value_353]
#             file_03CALACA_G02_353 = matching_row_353['DIPC_PRICE'].values[0]

#             search_value_354 = '03KAL_G01'
#             matching_row_354 = df_26[df_26['RESOURCE_NAME'] == search_value_354]
#             file_03KAL_G01_354 = matching_row_354['DIPC_PRICE'].values[0]

#             search_value_355 = '03KAL_G02'
#             matching_row_355 = df_26[df_26['RESOURCE_NAME'] == search_value_355]
#             file_03KAL_G02_355 = matching_row_355['DIPC_PRICE'].values[0]

#             search_value_356 = '03KAL_G03'
#             matching_row_356 = df_26[df_26['RESOURCE_NAME'] == search_value_20]
#             file_03KAL_G03_20 =  matching_row_20['DIPC_PRICE'].values[0]

#             search_value_357 = '03KAL_G04'
#             matching_row_357 = df_26[df_26['RESOURCE_NAME'] == search_value_357]
#             file_03KAL_G04_357 = matching_row_357['DIPC_PRICE'].values[0]

#             search_value_358 = '04LEYTE_A'
#             matching_row_358 = df_26[df_26['RESOURCE_NAME'] == search_value_358]
#             file_04LEYTE_A_358 = matching_row_358['DIPC_PRICE'].values[0]

#             search_value_359 = '05KSPC_G01'
#             matching_row_359 = df_26[df_26['RESOURCE_NAME'] == search_value_359]
#             file_05KSPC_G01_359 = matching_row_359['DIPC_PRICE'].values[0]

#             search_value_360 = '05KSPC_G02'
#             matching_row_360 = df_26[df_26['RESOURCE_NAME'] == search_value_360]
#             file_05KSPC_G02_360 = matching_row_360['DIPC_PRICE'].values[0]

#             search_value_361 = '08BANTAP_L01'
#             matching_row_361 = df_26[df_26['RESOURCE_NAME'] == search_value_361]
#             file_08BANTAP_L01_361 = matching_row_361['DIPC_PRICE'].values[0]

#             search_value_362 = '08PEDC_T1L1'
#             matching_row_362 = df_26[df_26['RESOURCE_NAME'] == search_value_362]
#             file_08PEDC_T1L1_362 = matching_row_362['DIPC_PRICE'].values[0]

#             search_value_363 = '08PEDC_T1L2'
#             matching_row_363 = df_26[df_26['RESOURCE_NAME'] == search_value_363]
#             file_08PEDC_T1L2_363 = matching_row_363['DIPC_PRICE'].values[0]

#             search_value_364 = '08STBAR_T1L1'
#             matching_row_364 = df_26[df_26['RESOURCE_NAME'] == search_value_364]
#             file_08STBAR_T1L1_364 = matching_row_364['DIPC_PRICE'].values[0]

#             # Third Folder
#             filepath_27 = os.path.join(folder_path, files_in_folder[27]) 
#             df_27 = pd.read_csv(filepath_27)

#             search_value_365 = '03BOTOCA_G01'
#             matching_row_365 = df_27[df_27['RESOURCE_NAME'] == search_value_365]
#             file_03BOTOCA_G01_365 = matching_row_365['DIPC_PRICE'].values[0]

#             search_value_366 = '03CALACA_G01'
#             matching_row_366 = df_27[df_27['RESOURCE_NAME'] == search_value_366]
#             file_03CALACA_G01_366 = matching_row_366['DIPC_PRICE'].values[0]

#             search_value_367 = '03CALACA_G02'
#             matching_row_367 = df_27[df_27['RESOURCE_NAME'] == search_value_367]
#             file_03CALACA_G02_367 = matching_row_367['DIPC_PRICE'].values[0]

#             search_value_368 = '03KAL_G01'
#             matching_row_368 = df_27[df_27['RESOURCE_NAME'] == search_value_368]
#             file_03KAL_G01_368 = matching_row_368['DIPC_PRICE'].values[0]

#             search_value_369 = '03KAL_G02'
#             matching_row_369 = df_27[df_27['RESOURCE_NAME'] == search_value_369]
#             file_03KAL_G02_369 = matching_row_369['DIPC_PRICE'].values[0]

#             search_value_370 = '03KAL_G03'
#             matching_row_370 = df_27[df_27['RESOURCE_NAME'] == search_value_370]
#             file_03KAL_G03_370 = matching_row_370['DIPC_PRICE'].values[0]

#             search_value_371 = '03KAL_G04'
#             matching_row_371 = df_27[df_27['RESOURCE_NAME'] == search_value_371]
#             file_03KAL_G04_371 = matching_row_371['DIPC_PRICE'].values[0]

#             search_value_372 = '04LEYTE_A'
#             matching_row_372 = df_27[df_27['RESOURCE_NAME'] == search_value_372]
#             file_04LEYTE_A_372 = matching_row_372['DIPC_PRICE'].values[0]

#             search_value_373 = '05KSPC_G01'
#             matching_row_373 = df_27[df_27['RESOURCE_NAME'] == search_value_373]
#             file_05KSPC_G01_373 = matching_row_373['DIPC_PRICE'].values[0]

#             search_value_374 = '05KSPC_G02'
#             matching_row_374 = df_27[df_27['RESOURCE_NAME'] == search_value_374]
#             file_05KSPC_G02_374 = matching_row_374['DIPC_PRICE'].values[0]

#             search_value_375 = '08BANTAP_L01'
#             matching_row_375 = df_27[df_27['RESOURCE_NAME'] == search_value_375]
#             file_08BANTAP_L01_375 = matching_row_375['DIPC_PRICE'].values[0]

#             search_value_376 = '08PEDC_T1L1'
#             matching_row_376 = df_27[df_27['RESOURCE_NAME'] == search_value_376]
#             file_08PEDC_T1L1_376 = matching_row_376['DIPC_PRICE'].values[0]

#             search_value_377 = '08PEDC_T1L2'
#             matching_row_377 = df_27[df_27['RESOURCE_NAME'] == search_value_377]
#             file_08PEDC_T1L2_377 = matching_row_377['DIPC_PRICE'].values[0]

#             search_value_378 = '08STBAR_T1L1'
#             matching_row_378 = df_27[df_27['RESOURCE_NAME'] == search_value_378]
#             file_08STBAR_T1L1_378 = matching_row_378['DIPC_PRICE'].values[0]

#             # Fourth Folder
#             filepath_28 = os.path.join(folder_path, files_in_folder[28]) 
#             df_28 = pd.read_csv(filepath_28)

#             search_value_379 = '03BOTOCA_G01'
#             matching_row_379 = df_28[df_28['RESOURCE_NAME'] == search_value_379]
#             file_03BOTOCA_G01_379 = matching_row_379['DIPC_PRICE'].values[0]

#             search_value_380 = '03CALACA_G01'
#             matching_row_380 = df_28[df_28['RESOURCE_NAME'] == search_value_380]
#             file_03CALACA_G01_380 = matching_row_380['DIPC_PRICE'].values[0]

#             search_value_381 = '03CALACA_G02'
#             matching_row_381 = df_28[df_28['RESOURCE_NAME'] == search_value_381]
#             file_03CALACA_G02_381 = matching_row_381['DIPC_PRICE'].values[0]

#             search_value_382 = '03KAL_G01'
#             matching_row_382 = df_28[df_28['RESOURCE_NAME'] == search_value_382]
#             file_03KAL_G01_382 = matching_row_382['DIPC_PRICE'].values[0]

#             search_value_383 = '03KAL_G02'
#             matching_row_383 = df_28[df_28['RESOURCE_NAME'] == search_value_383]
#             file_03KAL_G02_383 = matching_row_383['DIPC_PRICE'].values[0]

#             search_value_384 = '03KAL_G03'
#             matching_row_384 = df_28[df_28['RESOURCE_NAME'] == search_value_384]
#             file_03KAL_G03_384 = matching_row_384['DIPC_PRICE'].values[0]

#             search_value_385 = '03KAL_G04'
#             matching_row_385 = df_28[df_28['RESOURCE_NAME'] == search_value_385]
#             file_03KAL_G04_385 = matching_row_385['DIPC_PRICE'].values[0]

#             search_value_386 = '04LEYTE_A'
#             matching_row_386 = df_28[df_28['RESOURCE_NAME'] == search_value_386]
#             file_04LEYTE_A_386 = matching_row_386['DIPC_PRICE'].values[0]

#             search_value_387 = '05KSPC_G01'
#             matching_row_387 = df_28[df_28['RESOURCE_NAME'] == search_value_387]
#             file_05KSPC_G01_387 = matching_row_387['DIPC_PRICE'].values[0]

#             search_value_388 = '05KSPC_G02'
#             matching_row_388 = df_28[df_28['RESOURCE_NAME'] == search_value_388]
#             file_05KSPC_G02_388 = matching_row_388['DIPC_PRICE'].values[0]

#             search_value_389 = '08BANTAP_L01'
#             matching_row_389 = df_28[df_28['RESOURCE_NAME'] == search_value_389]
#             file_08BANTAP_L01_389 = matching_row_389['DIPC_PRICE'].values[0]

#             search_value_390 = '08PEDC_T1L1'
#             matching_row_390 = df_28[df_28['RESOURCE_NAME'] == search_value_390]
#             file_08PEDC_T1L1_390 = matching_row_390['DIPC_PRICE'].values[0]

#             search_value_391 = '08PEDC_T1L2'
#             matching_row_391 = df_28[df_28['RESOURCE_NAME'] == search_value_391]
#             file_08PEDC_T1L2_391 = matching_row_391['DIPC_PRICE'].values[0]

#             search_value_392 = '08STBAR_T1L1'
#             matching_row_392 = df_28[df_28['RESOURCE_NAME'] == search_value_392]
#             file_08STBAR_T1L1_392 = matching_row_392['DIPC_PRICE'].values[0]

#             # Fifth Folder
#             filepath_29 = os.path.join(folder_path, files_in_folder[29]) 
#             df_29 = pd.read_csv(filepath_29)

#             search_value_393 = '03BOTOCA_G01'
#             matching_row_393 = df_29[df_29['RESOURCE_NAME'] == search_value_393]
#             file_03BOTOCA_G01_393 = matching_row_393['DIPC_PRICE'].values[0]

#             search_value_394 = '03CALACA_G01'
#             matching_row_394 = df_29[df_29['RESOURCE_NAME'] == search_value_394]
#             file_03CALACA_G01_394 = matching_row_394['DIPC_PRICE'].values[0]

#             search_value_395 = '03CALACA_G02'
#             matching_row_395 = df_29[df_29['RESOURCE_NAME'] == search_value_395]
#             file_03CALACA_G02_395 = matching_row_395['DIPC_PRICE'].values[0]

#             search_value_396 = '03KAL_G01'
#             matching_row_396 = df_29[df_29['RESOURCE_NAME'] == search_value_396]
#             file_03KAL_G01_396 = matching_row_396['DIPC_PRICE'].values[0]

#             search_value_397 = '03KAL_G02'
#             matching_row_397 = df_29[df_29['RESOURCE_NAME'] == search_value_397]
#             file_03KAL_G02_397 = matching_row_397['DIPC_PRICE'].values[0]

#             search_value_398 = '03KAL_G03'
#             matching_row_398 = df_29[df_29['RESOURCE_NAME'] == search_value_398]
#             file_03KAL_G03_398 = matching_row_398['DIPC_PRICE'].values[0]

#             search_value_399 = '03KAL_G04'
#             matching_row_399 = df_29[df_29['RESOURCE_NAME'] == search_value_399]
#             file_03KAL_G04_399 = matching_row_399['DIPC_PRICE'].values[0]

#             search_value_400 = '04LEYTE_A'
#             matching_row_400 = df_29[df_29['RESOURCE_NAME'] == search_value_400]
#             file_04LEYTE_A_400 = matching_row_400['DIPC_PRICE'].values[0]

#             search_value_401 = '05KSPC_G01'
#             matching_row_401 = df_29[df_29['RESOURCE_NAME'] == search_value_401]
#             file_05KSPC_G01_401 = matching_row_401['DIPC_PRICE'].values[0]

#             search_value_402 = '05KSPC_G02'
#             matching_row_402 = df_29[df_29['RESOURCE_NAME'] == search_value_402]
#             file_05KSPC_G02_402 = matching_row_402['DIPC_PRICE'].values[0]

#             search_value_403 = '08BANTAP_L01'
#             matching_row_403 = df_29[df_29['RESOURCE_NAME'] == search_value_403]
#             file_08BANTAP_L01_403 = matching_row_403['DIPC_PRICE'].values[0]

#             search_value_404 = '08PEDC_T1L1'
#             matching_row_404 = df_29[df_29['RESOURCE_NAME'] == search_value_404]
#             file_08PEDC_T1L1_404 = matching_row_404['DIPC_PRICE'].values[0]

#             search_value_405 = '08PEDC_T1L2'
#             matching_row_405 = df_29[df_29['RESOURCE_NAME'] == search_value_405]
#             file_08PEDC_T1L2_405 = matching_row_405['DIPC_PRICE'].values[0]

#             search_value_406 = '08STBAR_T1L1'
#             matching_row_406 = df_29[df_29['RESOURCE_NAME'] == search_value_406]
#             file_08STBAR_T1L1_406 = matching_row_406['DIPC_PRICE'].values[0]
               
#             # Sixth Folder
#             filepath_30 = os.path.join(folder_path, files_in_folder[30]) 
#             df_30 = pd.read_csv(filepath_30)

#             search_value_407 = '03BOTOCA_G01'
#             matching_row_407 = df_30[df_30['RESOURCE_NAME'] == search_value_407]
#             file_03BOTOCA_G01_407 = matching_row_407['DIPC_PRICE'].values[0]

#             search_value_408 = '03CALACA_G01'
#             matching_row_408 = df_30[df_30['RESOURCE_NAME'] == search_value_408]
#             file_03CALACA_G01_408 = matching_row_408['DIPC_PRICE'].values[0]

#             search_value_409 = '03CALACA_G02'
#             matching_row_409 = df_30[df_30['RESOURCE_NAME'] == search_value_409]
#             file_03CALACA_G02_409 = matching_row_409['DIPC_PRICE'].values[0]

#             search_value_410 = '03KAL_G01'
#             matching_row_410 = df_30[df_30['RESOURCE_NAME'] == search_value_410]
#             file_03KAL_G01_410 = matching_row_410['DIPC_PRICE'].values[0]

#             search_value_411 = '03KAL_G02'
#             matching_row_411 = df_30[df_30['RESOURCE_NAME'] == search_value_411]
#             file_03KAL_G02_411 = matching_row_411['DIPC_PRICE'].values[0]

#             search_value_412 = '03KAL_G03'
#             matching_row_412 = df_30[df_30['RESOURCE_NAME'] == search_value_412]
#             file_03KAL_G03_412 = matching_row_412['DIPC_PRICE'].values[0]

#             search_value_413 = '03KAL_G04'
#             matching_row_413 = df_30[df_30['RESOURCE_NAME'] == search_value_413]
#             file_03KAL_G04_413 = matching_row_413['DIPC_PRICE'].values[0]

#             search_value_414 = '04LEYTE_A'
#             matching_row_414 = df_30[df_30['RESOURCE_NAME'] == search_value_414]
#             file_04LEYTE_A_414 = matching_row_414['DIPC_PRICE'].values[0]

#             search_value_415 = '05KSPC_G01'
#             matching_row_415 = df_30[df_30['RESOURCE_NAME'] == search_value_415]
#             file_05KSPC_G01_415 = matching_row_415['DIPC_PRICE'].values[0]

#             search_value_416 = '05KSPC_G02'
#             matching_row_416 = df_30[df_30['RESOURCE_NAME'] == search_value_416]
#             file_05KSPC_G02_416 = matching_row_416['DIPC_PRICE'].values[0]

#             search_value_417 = '08BANTAP_L01'
#             matching_row_417 = df_30[df_30['RESOURCE_NAME'] == search_value_417]
#             file_08BANTAP_L01_417 = matching_row_417['DIPC_PRICE'].values[0]

#             search_value_418 = '08PEDC_T1L1'
#             matching_row_418 = df_30[df_30['RESOURCE_NAME'] == search_value_418]
#             file_08PEDC_T1L1_418 = matching_row_418['DIPC_PRICE'].values[0]

#             search_value_419 = '08PEDC_T1L2'
#             matching_row_419 = df_30[df_30['RESOURCE_NAME'] == search_value_419]
#             file_08PEDC_T1L2_419 = matching_row_419['DIPC_PRICE'].values[0]

#             search_value_420 = '08STBAR_T1L1'
#             matching_row_420 = df_30[df_30['RESOURCE_NAME'] == search_value_420]
#             file_08STBAR_T1L1_420 = matching_row_420['DIPC_PRICE'].values[0]

#             # Seventh Folder
#             filepath_31 = os.path.join(folder_path, files_in_folder[31]) 
#             df_31 = pd.read_csv(filepath_31)

#             search_value_421 = '03BOTOCA_G01'
#             matching_row_421 = df_31[df_31['RESOURCE_NAME'] == search_value_421]
#             file_03BOTOCA_G01_421 = matching_row_421['DIPC_PRICE'].values[0]

#             search_value_422 = '03CALACA_G01'
#             matching_row_422 = df_31[df_31['RESOURCE_NAME'] == search_value_422]
#             file_03CALACA_G01_422 = matching_row_422['DIPC_PRICE'].values[0]

#             search_value_423 = '03CALACA_G02'
#             matching_row_423 = df_31[df_31['RESOURCE_NAME'] == search_value_423]
#             file_03CALACA_G02_423 = matching_row_423['DIPC_PRICE'].values[0]

#             search_value_424 = '03KAL_G01'
#             matching_row_424 = df_31[df_31['RESOURCE_NAME'] == search_value_424]
#             file_03KAL_G01_424 = matching_row_424['DIPC_PRICE'].values[0]

#             search_value_425 = '03KAL_G02'
#             matching_row_425 = df_31[df_31['RESOURCE_NAME'] == search_value_425]
#             file_03KAL_G02_425 = matching_row_425['DIPC_PRICE'].values[0]

#             search_value_426 = '03KAL_G03'
#             matching_row_426 = df_31[df_31['RESOURCE_NAME'] == search_value_426]
#             file_03KAL_G03_426 = matching_row_426['DIPC_PRICE'].values[0]

#             search_value_427 = '03KAL_G04'
#             matching_row_427 = df_31[df_31['RESOURCE_NAME'] == search_value_427]
#             file_03KAL_G04_427 = matching_row_427['DIPC_PRICE'].values[0]

#             search_value_428 = '04LEYTE_A'
#             matching_row_428 = df_31[df_31['RESOURCE_NAME'] == search_value_428]
#             file_04LEYTE_A_428 = matching_row_428['DIPC_PRICE'].values[0]

#             search_value_429 = '05KSPC_G01'
#             matching_row_429 = df_31[df_31['RESOURCE_NAME'] == search_value_429]
#             file_05KSPC_G01_429 = matching_row_429['DIPC_PRICE'].values[0]

#             search_value_430 = '05KSPC_G02'
#             matching_row_430 = df_31[df_31['RESOURCE_NAME'] == search_value_430]
#             file_05KSPC_G02_430 = matching_row_430['DIPC_PRICE'].values[0]

#             search_value_431 = '08BANTAP_L01'
#             matching_row_431 = df_31[df_31['RESOURCE_NAME'] == search_value_431]
#             file_08BANTAP_L01_431 = matching_row_431['DIPC_PRICE'].values[0]

#             search_value_432 = '08PEDC_T1L1'
#             matching_row_432 = df_31[df_31['RESOURCE_NAME'] == search_value_432]
#             file_08PEDC_T1L1_432 = matching_row_432['DIPC_PRICE'].values[0]

#             search_value_433 = '08PEDC_T1L2'
#             matching_row_433 = df_31[df_31['RESOURCE_NAME'] == search_value_433]
#             file_08PEDC_T1L2_433 = matching_row_433['DIPC_PRICE'].values[0]

#             search_value_434 = '08STBAR_T1L1'
#             matching_row_434 = df_31[df_31['RESOURCE_NAME'] == search_value_434]
#             file_08STBAR_T1L1_434 = matching_row_434['DIPC_PRICE'].values[0]

#             # Eighth Folder
#             filepath_32 = os.path.join(folder_path, files_in_folder[32]) 
#             df_32 = pd.read_csv(filepath_32)

#             search_value_435 = '03BOTOCA_G01'
#             matching_row_435 = df_32[df_32['RESOURCE_NAME'] == search_value_435]
#             file_03BOTOCA_G01_99 = matching_row_99['DIPC_PRICE'].values[0]

#             search_value_100 = '03CALACA_G01'
#             matching_row_100 = df_8[df_8['RESOURCE_NAME'] == search_value_100]
#             file_03CALACA_G01_100 = matching_row_100['DIPC_PRICE'].values[0]

#             search_value_101 = '03CALACA_G02'
#             matching_row_101 = df_8[df_8['RESOURCE_NAME'] == search_value_101]
#             file_03CALACA_G02_101 = matching_row_101['DIPC_PRICE'].values[0]

#             search_value_102 = '03KAL_G01'
#             matching_row_102 = df_8[df_8['RESOURCE_NAME'] == search_value_102]
#             file_03KAL_G01_102 = matching_row_102['DIPC_PRICE'].values[0]

#             search_value_103 = '03KAL_G02'
#             matching_row_103 = df_8[df_8['RESOURCE_NAME'] == search_value_103]
#             file_03KAL_G02_103 = matching_row_103['DIPC_PRICE'].values[0]

#             search_value_104 = '03KAL_G03'
#             matching_row_104 = df_8[df_8['RESOURCE_NAME'] == search_value_104]
#             file_03KAL_G03_104 = matching_row_104['DIPC_PRICE'].values[0]

#             search_value_105 = '03KAL_G04'
#             matching_row_105 = df_8[df_8['RESOURCE_NAME'] == search_value_105]
#             file_03KAL_G04_105 = matching_row_105['DIPC_PRICE'].values[0]

#             search_value_106 = '04LEYTE_A'
#             matching_row_106 = df_8[df_8['RESOURCE_NAME'] == search_value_106]
#             file_04LEYTE_A_106 = matching_row_106['DIPC_PRICE'].values[0]

#             search_value_107 = '05KSPC_G01'
#             matching_row_107 = df_8[df_8['RESOURCE_NAME'] == search_value_107]
#             file_05KSPC_G01_107 = matching_row_107['DIPC_PRICE'].values[0]

#             search_value_108 = '05KSPC_G02'
#             matching_row_108 = df_8[df_8['RESOURCE_NAME'] == search_value_108]
#             file_05KSPC_G02_108 = matching_row_108['DIPC_PRICE'].values[0]

#             search_value_109 = '08BANTAP_L01'
#             matching_row_109 = df_8[df_8['RESOURCE_NAME'] == search_value_109]
#             file_08BANTAP_L01_109 = matching_row_109['DIPC_PRICE'].values[0]

#             search_value_110 = '08PEDC_T1L1'
#             matching_row_110 = df_8[df_8['RESOURCE_NAME'] == search_value_110]
#             file_08PEDC_T1L1_110 = matching_row_110['DIPC_PRICE'].values[0]

#             search_value_111 = '08PEDC_T1L2'
#             matching_row_111 = df_8[df_8['RESOURCE_NAME'] == search_value_111]
#             file_08PEDC_T1L2_111 = matching_row_111['DIPC_PRICE'].values[0]

#             search_value_112 = '08STBAR_T1L1'
#             matching_row_112 = df_8[df_8['RESOURCE_NAME'] == search_value_112]
#             file_08STBAR_T1L1_112 = matching_row_112['DIPC_PRICE'].values[0]

#             # Ninth Folder
#             filepath_9 = os.path.join(folder_path, files_in_folder[9]) 
#             df_9 = pd.read_csv(filepath_9)

#             search_value_113 = '03BOTOCA_G01'
#             matching_row_113 = df_9[df_9['RESOURCE_NAME'] == search_value_113]
#             file_03BOTOCA_G01_113 = matching_row_113['DIPC_PRICE'].values[0]

#             search_value_114 = '03CALACA_G01'
#             matching_row_114 = df_9[df_9['RESOURCE_NAME'] == search_value_114]
#             file_03CALACA_G01_114 = matching_row_114['DIPC_PRICE'].values[0]

#             search_value_115 = '03CALACA_G02'
#             matching_row_115 = df_9[df_9['RESOURCE_NAME'] == search_value_115]
#             file_03CALACA_G02_115 = matching_row_115['DIPC_PRICE'].values[0]

#             search_value_116 = '03KAL_G01'
#             matching_row_116 = df_9[df_9['RESOURCE_NAME'] == search_value_116]
#             file_03KAL_G01_116 = matching_row_116['DIPC_PRICE'].values[0]

#             search_value_117 = '03KAL_G02'
#             matching_row_117 = df_9[df_9['RESOURCE_NAME'] == search_value_117]
#             file_03KAL_G02_117 = matching_row_117['DIPC_PRICE'].values[0]

#             search_value_118 = '03KAL_G03'
#             matching_row_118 = df_9[df_9['RESOURCE_NAME'] == search_value_118]
#             file_03KAL_G03_118 = matching_row_118['DIPC_PRICE'].values[0]

#             search_value_119 = '03KAL_G04'
#             matching_row_119 = df_9[df_9['RESOURCE_NAME'] == search_value_119]
#             file_03KAL_G04_119 = matching_row_119['DIPC_PRICE'].values[0]

#             search_value_120 = '04LEYTE_A'
#             matching_row_120 = df_9[df_9['RESOURCE_NAME'] == search_value_120]
#             file_04LEYTE_A_120 = matching_row_120['DIPC_PRICE'].values[0]

#             search_value_121 = '05KSPC_G01'
#             matching_row_121 = df_9[df_9['RESOURCE_NAME'] == search_value_121]
#             file_05KSPC_G01_121 = matching_row_121['DIPC_PRICE'].values[0]

#             search_value_122 = '05KSPC_G02'
#             matching_row_122 = df_9[df_9['RESOURCE_NAME'] == search_value_122]
#             file_05KSPC_G02_122 = matching_row_122['DIPC_PRICE'].values[0]

#             search_value_123 = '08BANTAP_L01'
#             matching_row_123 = df_9[df_9['RESOURCE_NAME'] == search_value_123]
#             file_08BANTAP_L01_123 = matching_row_123['DIPC_PRICE'].values[0]

#             search_value_124 = '08PEDC_T1L1'
#             matching_row_124 = df_9[df_9['RESOURCE_NAME'] == search_value_124]
#             file_08PEDC_T1L1_124 = matching_row_124['DIPC_PRICE'].values[0]

#             search_value_125 = '08PEDC_T1L2'
#             matching_row_125 = df_9[df_9['RESOURCE_NAME'] == search_value_125]
#             file_08PEDC_T1L2_125 = matching_row_125['DIPC_PRICE'].values[0]

#             search_value_126 = '08STBAR_T1L1'
#             matching_row_126 = df_9[df_9['RESOURCE_NAME'] == search_value_126]
#             file_08STBAR_T1L1_126 = matching_row_126['DIPC_PRICE'].values[0]

#             # Tenth Folder
#             filepath_10 = os.path.join(folder_path, files_in_folder[10]) 
#             df_10 = pd.read_csv(filepath_10)

#             search_value_127 = '03BOTOCA_G01'
#             matching_row_127 = df_10[df_10['RESOURCE_NAME'] == search_value_127]
#             file_03BOTOCA_G01_127 = matching_row_127['DIPC_PRICE'].values[0]

#             search_value_128 = '03CALACA_G01'
#             matching_row_128 = df_10[df_10['RESOURCE_NAME'] == search_value_128]
#             file_03CALACA_G01_128 = matching_row_128['DIPC_PRICE'].values[0]

#             search_value_129 = '03CALACA_G02'
#             matching_row_129 = df_10[df_10['RESOURCE_NAME'] == search_value_129]
#             file_03CALACA_G02_129 = matching_row_129['DIPC_PRICE'].values[0]

#             search_value_130 = '03KAL_G01'
#             matching_row_130 = df_10[df_10['RESOURCE_NAME'] == search_value_130]
#             file_03KAL_G01_130 = matching_row_130['DIPC_PRICE'].values[0]

#             search_value_131 = '03KAL_G02'
#             matching_row_131 = df_10[df_10['RESOURCE_NAME'] == search_value_131]
#             file_03KAL_G02_131 = matching_row_131['DIPC_PRICE'].values[0]

#             search_value_132 = '03KAL_G03'
#             matching_row_132 = df_10[df_10['RESOURCE_NAME'] == search_value_132]
#             file_03KAL_G03_132 = matching_row_132['DIPC_PRICE'].values[0]

#             search_value_133 = '03KAL_G04'
#             matching_row_133 = df_10[df_10['RESOURCE_NAME'] == search_value_133]
#             file_03KAL_G04_133 = matching_row_133['DIPC_PRICE'].values[0]

#             search_value_134 = '04LEYTE_A'
#             matching_row_134 = df_10[df_10['RESOURCE_NAME'] == search_value_134]
#             file_04LEYTE_A_134 = matching_row_134['DIPC_PRICE'].values[0]

#             search_value_135 = '05KSPC_G01'
#             matching_row_135 = df_10[df_10['RESOURCE_NAME'] == search_value_135]
#             file_05KSPC_G01_135 = matching_row_135['DIPC_PRICE'].values[0]

#             search_value_136 = '05KSPC_G02'
#             matching_row_136 = df_10[df_10['RESOURCE_NAME'] == search_value_136]
#             file_05KSPC_G02_136 = matching_row_136['DIPC_PRICE'].values[0]

#             search_value_137 = '08BANTAP_L01'
#             matching_row_137 = df_10[df_10['RESOURCE_NAME'] == search_value_137]
#             file_08BANTAP_L01_137 = matching_row_137['DIPC_PRICE'].values[0]

#             search_value_138 = '08PEDC_T1L1'
#             matching_row_138 = df_10[df_10['RESOURCE_NAME'] == search_value_138]
#             file_08PEDC_T1L1_138 = matching_row_138['DIPC_PRICE'].values[0]

#             search_value_139 = '08PEDC_T1L2'
#             matching_row_139 = df_10[df_10['RESOURCE_NAME'] == search_value_139]
#             file_08PEDC_T1L2_139 = matching_row_139['DIPC_PRICE'].values[0]

#             search_value_140 = '08STBAR_T1L1'
#             matching_row_140 = df_10[df_10['RESOURCE_NAME'] == search_value_140]
#             file_08STBAR_T1L1_140 = matching_row_140['DIPC_PRICE'].values[0]

#             # Eleventh Folder
#             filepath_11 = os.path.join(folder_path, files_in_folder[11]) 
#             df_11 = pd.read_csv(filepath_11)

#             search_value_141 = '03BOTOCA_G01'
#             matching_row_141 = df_11[df_11['RESOURCE_NAME'] == search_value_141]
#             file_03BOTOCA_G01_141 = matching_row_141['DIPC_PRICE'].values[0]

#             search_value_142 = '03CALACA_G01'
#             matching_row_142 = df_11[df_11['RESOURCE_NAME'] == search_value_142]
#             file_03CALACA_G01_142 = matching_row_142['DIPC_PRICE'].values[0]

#             search_value_143 = '03CALACA_G02'
#             matching_row_143 = df_11[df_11['RESOURCE_NAME'] == search_value_143]
#             file_03CALACA_G02_143 = matching_row_143['DIPC_PRICE'].values[0]

#             search_value_144 = '03KAL_G01'
#             matching_row_144 = df_11[df_11['RESOURCE_NAME'] == search_value_144]
#             file_03KAL_G01_144 = matching_row_144['DIPC_PRICE'].values[0]

#             search_value_145 = '03KAL_G02'
#             matching_row_145 = df_11[df_11['RESOURCE_NAME'] == search_value_145]
#             file_03KAL_G02_145 = matching_row_145['DIPC_PRICE'].values[0]

#             search_value_146 = '03KAL_G03'
#             matching_row_146 = df_11[df_11['RESOURCE_NAME'] == search_value_146]
#             file_03KAL_G03_146 = matching_row_146['DIPC_PRICE'].values[0]

#             search_value_147 = '03KAL_G04'
#             matching_row_147 = df_11[df_11['RESOURCE_NAME'] == search_value_147]
#             file_03KAL_G04_147 = matching_row_147['DIPC_PRICE'].values[0]

#             search_value_148 = '04LEYTE_A'
#             matching_row_148 = df_11[df_11['RESOURCE_NAME'] == search_value_148]
#             file_04LEYTE_A_148 = matching_row_148['DIPC_PRICE'].values[0]

#             search_value_149 = '05KSPC_G01'
#             matching_row_149 = df_11[df_11['RESOURCE_NAME'] == search_value_149]
#             file_05KSPC_G01_149 = matching_row_149['DIPC_PRICE'].values[0]

#             search_value_150 = '05KSPC_G02'
#             matching_row_150 = df_11[df_11['RESOURCE_NAME'] == search_value_150]
#             file_05KSPC_G02_150 = matching_row_150['DIPC_PRICE'].values[0]

#             search_value_151 = '08BANTAP_L01'
#             matching_row_151 = df_11[df_11['RESOURCE_NAME'] == search_value_151]
#             file_08BANTAP_L01_151 = matching_row_151['DIPC_PRICE'].values[0]

#             search_value_152 = '08PEDC_T1L1'
#             matching_row_152 = df_11[df_11['RESOURCE_NAME'] == search_value_152]
#             file_08PEDC_T1L1_152 = matching_row_152['DIPC_PRICE'].values[0]

#             search_value_153 = '08PEDC_T1L2'
#             matching_row_153 = df_11[df_11['RESOURCE_NAME'] == search_value_153]
#             file_08PEDC_T1L2_153 = matching_row_153['DIPC_PRICE'].values[0]

#             search_value_154 = '08STBAR_T1L1'
#             matching_row_154 = df_11[df_11['RESOURCE_NAME'] == search_value_154]
#             file_08STBAR_T1L1_154 = matching_row_154['DIPC_PRICE'].values[0]

#             # Twelvth Folder
#             filepath_12 = os.path.join(folder_path, files_in_folder[12]) 
#             df_12 = pd.read_csv(filepath_12)

#             search_value_155 = '03BOTOCA_G01'
#             matching_row_155 = df_12[df_12['RESOURCE_NAME'] == search_value_155]
#             file_03BOTOCA_G01_155 = matching_row_155['DIPC_PRICE'].values[0]

#             search_value_156 = '03CALACA_G01'
#             matching_row_156 = df_12[df_12['RESOURCE_NAME'] == search_value_156]
#             file_03CALACA_G01_156 = matching_row_156['DIPC_PRICE'].values[0]

#             search_value_157 = '03CALACA_G02'
#             matching_row_157 = df_12[df_12['RESOURCE_NAME'] == search_value_157]
#             file_03CALACA_G02_157 = matching_row_157['DIPC_PRICE'].values[0]

#             search_value_158 = '03KAL_G01'
#             matching_row_158 = df_12[df_12['RESOURCE_NAME'] == search_value_158]
#             file_03KAL_G01_158 = matching_row_158['DIPC_PRICE'].values[0]

#             search_value_159 = '03KAL_G02'
#             matching_row_159 = df_12[df_12['RESOURCE_NAME'] == search_value_159]
#             file_03KAL_G02_159 = matching_row_159['DIPC_PRICE'].values[0]

#             search_value_160 = '03KAL_G03'
#             matching_row_160 = df_12[df_12['RESOURCE_NAME'] == search_value_160]
#             file_03KAL_G03_160 = matching_row_160['DIPC_PRICE'].values[0]

#             search_value_161 = '03KAL_G04'
#             matching_row_161 = df_12[df_12['RESOURCE_NAME'] == search_value_161]
#             file_03KAL_G04_161 = matching_row_161['DIPC_PRICE'].values[0]

#             search_value_162 = '04LEYTE_A'
#             matching_row_162 = df_12[df_12['RESOURCE_NAME'] == search_value_162]
#             file_04LEYTE_A_162 = matching_row_162['DIPC_PRICE'].values[0]

#             search_value_163 = '05KSPC_G01'
#             matching_row_163 = df_12[df_12['RESOURCE_NAME'] == search_value_163]
#             file_05KSPC_G01_163 = matching_row_163['DIPC_PRICE'].values[0]

#             search_value_164 = '05KSPC_G02'
#             matching_row_164 = df_12[df_12['RESOURCE_NAME'] == search_value_164]
#             file_05KSPC_G02_164 = matching_row_164['DIPC_PRICE'].values[0]

#             search_value_165 = '08BANTAP_L01'
#             matching_row_165 = df_12[df_12['RESOURCE_NAME'] == search_value_165]
#             file_08BANTAP_L01_165 = matching_row_165['DIPC_PRICE'].values[0]

#             search_value_166 = '08PEDC_T1L1'
#             matching_row_166 = df_12[df_12['RESOURCE_NAME'] == search_value_166]
#             file_08PEDC_T1L1_166 = matching_row_166['DIPC_PRICE'].values[0]

#             search_value_167 = '08PEDC_T1L2'
#             matching_row_167 = df_12[df_12['RESOURCE_NAME'] == search_value_167]
#             file_08PEDC_T1L2_167 = matching_row_167['DIPC_PRICE'].values[0]

#             search_value_168 = '08STBAR_T1L1'
#             matching_row_168 = df_12[df_12['RESOURCE_NAME'] == search_value_168]
#             file_08STBAR_T1L1_168 = matching_row_168['DIPC_PRICE'].values[0]
                    
#             botoca_g01_total_1 = (file_03BOTOCA_G01_1 + file_03BOTOCA_G01_15 + file_03BOTOCA_G01_29 + file_03BOTOCA_G01_43 + file_03BOTOCA_G01_57 + file_03BOTOCA_G01_71 + file_03BOTOCA_G01_85 + file_03BOTOCA_G01_99 + file_03BOTOCA_G01_113 + file_03BOTOCA_G01_127 + file_03BOTOCA_G01_141 + file_03BOTOCA_G01_155)/12
#             calaca_g01_total_2 = (file_03CALACA_G01_2 + file_03CALACA_G01_16 + file_03CALACA_G01_30 + file_03CALACA_G01_44 + file_03CALACA_G01_58 + file_03CALACA_G01_72 + file_03CALACA_G01_86 + file_03CALACA_G01_100 + file_03CALACA_G01_114 + file_03CALACA_G01_128 + file_03CALACA_G01_142 + file_03CALACA_G01_156)/12
#             calaca_g02_total_3 = (file_03CALACA_G02_3 + file_03CALACA_G02_17 + file_03CALACA_G02_31 + file_03CALACA_G02_45 + file_03CALACA_G02_59 + file_03CALACA_G02_73 + file_03CALACA_G02_87 + file_03CALACA_G02_101 + file_03CALACA_G02_115 + file_03CALACA_G02_129 + file_03CALACA_G02_143 + file_03CALACA_G02_157)/12
#             kal_g01_total_4 = (file_03KAL_G01_4 + file_03KAL_G01_18 + file_03KAL_G01_32 + file_03KAL_G01_46 + file_03KAL_G01_60 + file_03KAL_G01_74 + file_03KAL_G01_88 + file_03KAL_G01_102 + file_03KAL_G01_116 + file_03KAL_G01_130 + file_03KAL_G01_144 + file_03KAL_G01_158)/12
#             kal_g02_total_5 = (file_03KAL_G02_5 + file_03KAL_G02_19 + file_03KAL_G02_33 + file_03KAL_G02_47 + file_03KAL_G02_61 + file_03KAL_G02_75 + file_03KAL_G02_89 + file_03KAL_G02_103 + file_03KAL_G02_117 + file_03KAL_G02_131 + file_03KAL_G02_145 + file_03KAL_G02_159)/12
#             kal_g03_total_6 = (file_03KAL_G03_6 + file_03KAL_G03_20 + file_03KAL_G03_34 + file_03KAL_G03_48 + file_03KAL_G03_62 + file_03KAL_G03_76 + file_03KAL_G03_90 + file_03KAL_G03_104 + file_03KAL_G03_118 + file_03KAL_G03_132 + file_03KAL_G03_146 + file_03KAL_G03_160)/12
#             kal_g04_total_7 = (file_03KAL_G04_7 + file_03KAL_G04_21 + file_03KAL_G04_35 + file_03KAL_G04_49 + file_03KAL_G04_63 + file_03KAL_G04_77 + file_03KAL_G04_91 + file_03KAL_G04_105 + file_03KAL_G04_119 + file_03KAL_G04_133 + file_03KAL_G04_147 + file_03KAL_G04_161)/12
#             leyte_a_total_8 = (file_04LEYTE_A_8 + file_04LEYTE_A_22 + file_04LEYTE_A_36 + file_04LEYTE_A_50 + file_04LEYTE_A_64 + file_04LEYTE_A_78 + file_04LEYTE_A_92 + file_04LEYTE_A_106 + file_04LEYTE_A_120 + file_04LEYTE_A_134 + file_04LEYTE_A_148 + file_04LEYTE_A_162)/12
#             kspc_g01_total_9 = (file_05KSPC_G01_9 + file_05KSPC_G01_23 + file_05KSPC_G01_37 + file_05KSPC_G01_51 + file_05KSPC_G01_65 + file_05KSPC_G01_79 + file_05KSPC_G01_93 + file_05KSPC_G01_107 + file_05KSPC_G01_121 + file_05KSPC_G01_135 + file_05KSPC_G01_149 + file_05KSPC_G01_163)/12
#             kspc_g02_total_10 = (file_05KSPC_G02_10 + file_05KSPC_G02_24 + file_05KSPC_G02_38 + file_05KSPC_G02_52 + file_05KSPC_G02_66 + file_05KSPC_G02_80 + file_05KSPC_G02_94 + file_05KSPC_G02_108 + file_05KSPC_G02_122 + file_05KSPC_G02_136 + file_05KSPC_G02_150 + file_05KSPC_G02_164)/12
#             bantap_l01_total_11 = (file_08BANTAP_L01_11 + file_08BANTAP_L01_25 + file_08BANTAP_L01_39 + file_08BANTAP_L01_53 + file_08BANTAP_L01_67 + file_08BANTAP_L01_81 + file_08BANTAP_L01_95 + file_08BANTAP_L01_109 + file_08BANTAP_L01_123 + file_08BANTAP_L01_137 + file_08BANTAP_L01_151 + file_08BANTAP_L01_165)/12
#             pedc_t1l1_total_12 = (file_08PEDC_T1L1_12 + file_08PEDC_T1L1_26 + file_08PEDC_T1L1_40 + file_08PEDC_T1L1_54 + file_08PEDC_T1L1_68 + file_08PEDC_T1L1_82 + file_08PEDC_T1L1_96 + file_08PEDC_T1L1_110 + file_08PEDC_T1L1_124 + file_08PEDC_T1L1_138 + file_08PEDC_T1L1_152 + file_08PEDC_T1L1_166)/12
#             pedc_t1l2_total_13 = (file_08PEDC_T1L2_13 + file_08PEDC_T1L2_27 + file_08PEDC_T1L2_41 + file_08PEDC_T1L2_55 + file_08PEDC_T1L2_69 + file_08PEDC_T1L2_83 + file_08PEDC_T1L2_97 + file_08PEDC_T1L2_111 + file_08PEDC_T1L2_125 + file_08PEDC_T1L2_139 + file_08PEDC_T1L2_153 + file_08PEDC_T1L2_167)/12
#             stbar_t1l1_total_14 = (file_08STBAR_T1L1_14 + file_08STBAR_T1L1_28 + file_08STBAR_T1L1_42 + file_08STBAR_T1L1_56 + file_08STBAR_T1L1_70 + file_08STBAR_T1L1_84 + file_08STBAR_T1L1_98 + file_08STBAR_T1L1_112 + file_08STBAR_T1L1_126 + file_08STBAR_T1L1_140 + file_08STBAR_T1L1_154 + file_08STBAR_T1L1_168)/12


#             first_file_path = os.path.join(folder_path, files_in_folder[13])
#             df = pd.read_csv(first_file_path)
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[14])
#             second_df = pd.read_csv(second_file_path)
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[15])
#             third_df = pd.read_csv(third_file_path)
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[16])
#             fourth_df = pd.read_csv(fourth_file_path)
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[17])
#             fifth_df = pd.read_csv(fifth_file_path)
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[18])
#             sixth_df = pd.read_csv(sixth_file_path)
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[19])                 
#             seventh_df = pd.read_csv(seventh_file_path)
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[20])
#             eighth_df = pd.read_csv(eighth_file_path)
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[21])
#             ninth_df = pd.read_csv(ninth_file_path)
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[22])
#             tenth_df = pd.read_csv(tenth_file_path)
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]
    
#             eleventh_file_path = os.path.join(folder_path, files_in_folder[23])
#             eleventh_df = pd.read_csv(eleventh_file_path)
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[24])
#             twelvth_df = pd.read_csv(twelvth_file_path)
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

#             botoca_g01_total_1 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_1 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_1 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_1 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_1 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_1 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12     
#             kal_g04_total_1 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_1 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_1 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_1 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_1 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_1 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_1 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_1 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
                
#             first_file_path = os.path.join(folder_path, files_in_folder[25])
#             df = pd.read_csv(first_file_path)
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[26])
#             second_df = pd.read_csv(second_file_path)
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[27])
#             third_df = pd.read_csv(third_file_path)
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[28])
#             fourth_df = pd.read_csv(fourth_file_path)
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[29])
#             fifth_df = pd.read_csv(fifth_file_path)
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]
                
#             sixth_file_path = os.path.join(folder_path, files_in_folder[30])
#             sixth_df = pd.read_csv(sixth_file_path)
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[31])
#             seventh_df = pd.read_csv(seventh_file_path)
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[32])
#             eighth_df = pd.read_csv(eighth_file_path)
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[33])

#             ninth_df = pd.read_csv(ninth_file_path)
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[34])
#             tenth_df = pd.read_csv(tenth_file_path)

#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[35])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[36])
#             twelvth_df = pd.read_csv(twelvth_file_path)

#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

#             botoca_g01_total_2 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_2 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_2 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_2 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_2 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_2 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_2 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_2 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_2 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_2 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_2 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_2 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_2 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_2 = (second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
                
#             first_file_path = os.path.join(folder_path, files_in_folder[37])
#             df = pd.read_csv(first_file_path)
            
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_df = pd.read_csv(second_file_path)
#             second_pedc_til1 = second_df.iloc[751,5]
                
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[39])
#             third_df = pd.read_csv(third_file_path)
                
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[40])
#             fourth_df = pd.read_csv(fourth_file_path)

#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[41])
#             fifth_df = pd.read_csv(fifth_file_path)

#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[42])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[43])
#             seventh_df = pd.read_csv(seventh_file_path)

#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]
                    
#             eighth_file_path = os.path.join(folder_path, files_in_folder[44])
#             eighth_df = pd.read_csv(eighth_file_path)

#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[45])
#             ninth_df = pd.read_csv(ninth_file_path)

#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[46])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[47])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[48])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

#             botoca_g01_total_3 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_3 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_3 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_3 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_3 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_3 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_3 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_3 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_3 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_3 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_3 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_3 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_3 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_3 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
            
#             first_file_path = os.path.join(folder_path, files_in_folder[49])
#             df = pd.read_csv(first_file_path)
                    
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]
                    
#             second_file_path = os.path.join(folder_path, files_in_folder[50])
#             second_df = pd.read_csv(second_file_path)
                
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[51])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[52])
#             fourth_df = pd.read_csv(fourth_file_path)

#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[53])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[54])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[55])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[56])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[57])
#             ninth_df = pd.read_csv(ninth_file_path)

#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[58])
#             tenth_df = pd.read_csv(tenth_file_path)
                
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[59])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]
                
#             twelvth_file_path = os.path.join(folder_path, files_in_folder[60])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

#             botoca_g01_total_4 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_4 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_4 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_4 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_4 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_4 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_4 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_4 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_4 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_4 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_4 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_4 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_4 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_4 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
            
#             first_file_path = os.path.join(folder_path, files_in_folder[61])
#             df = pd.read_csv(first_file_path)
                
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[62])
#             second_df = pd.read_csv(second_file_path)

#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[63])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[64])
#             fourth_df = pd.read_csv(fourth_file_path)
                
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[65])
#             fifth_df = pd.read_csv(fifth_file_path)

#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[66])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]
            
#             seventh_file_path = os.path.join(folder_path, files_in_folder[67])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[68])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[69])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[70])
#             tenth_df = pd.read_csv(tenth_file_path)

#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[71])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]
                
#             twelvth_file_path = os.path.join(folder_path, files_in_folder[72])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

#             botoca_g01_total_5 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_5 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_5 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_5 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_5 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_5 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_5 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_5 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_5 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_5 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_5 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_5 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_5 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_5 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

#             first_file_path = os.path.join(folder_path, files_in_folder[73])
#             df = pd.read_csv(first_file_path)
                
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[74])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[75])
#             third_df = pd.read_csv(third_file_path)

#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[76])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[77])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[78])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[79])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[80])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[81])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[82])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[83])
#             eleventh_df = pd.read_csv(eleventh_file_path)

#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[84])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                
#             botoca_g01_total_6 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_6 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_6 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_6 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_6 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_6 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_6 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_6 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_6 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_6 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_6 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_6 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_6 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_6 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
            
#             first_file_path = os.path.join(folder_path, files_in_folder[85])
#             df = pd.read_csv(first_file_path)
                    
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[86])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[87])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[88])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[89])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[90])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[91])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[92])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[93])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[94])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[95])
#             eleventh_df = pd.read_csv(eleventh_file_path)

#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[96])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    
#             botoca_g01_total_7 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_7 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_7 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_7 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_7 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_7 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_7 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_7 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_7 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_7 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_7 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_7 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_7 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_7 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
                
#             first_file_path = os.path.join(folder_path, files_in_folder[97])
#             df = pd.read_csv(first_file_path)
                    
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[98])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[99])
#             third_df = pd.read_csv(third_file_path)
                    
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[100])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[101])
#             fifth_df = pd.read_csv(fifth_file_path)
                
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[102])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[103])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]
                
#             eighth_file_path = os.path.join(folder_path, files_in_folder[104])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[105])
#             ninth_df = pd.read_csv(ninth_file_path)

#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[106])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[107])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[108])
#             twelvth_df = pd.read_csv(twelvth_file_path)
                
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    
#             botoca_g01_total_8 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_8 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_8 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_8 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_8 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_8 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_8 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_8 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_8 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_8 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_8 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_8 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_8 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_8 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
                
            
#             first_file_path = os.path.join(folder_path, files_in_folder[109])
#             df = pd.read_csv(first_file_path)
            
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[110])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[111])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[112])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[113])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[114])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[115])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[116])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[117])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[118])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[119])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[120])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

            
#             botoca_g01_total_9 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_9 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_9 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_9 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_9 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_9 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_9 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_9 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_9 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_9 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_9 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_9 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_9 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_9 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
                   
#             first_file_path = os.path.join(folder_path, files_in_folder[121])
#             df = pd.read_csv(first_file_path)
                
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[122])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[123])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[124])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[125])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[126])
#             sixth_df = pd.read_csv(sixth_file_path)

#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[127])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[128])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[129])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[130])
#             tenth_df = pd.read_csv(tenth_file_path)

#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[131])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[132])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

#             botoca_g01_total_10 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_10 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_10 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_10 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_10 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_10 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_10 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_10 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_10 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_10 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_10 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_10 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_10 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_10 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
            
#             first_file_path = os.path.join(folder_path, files_in_folder[133])
#             df = pd.read_csv(first_file_path)
            
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[134])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[135])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]
                
#             fourth_file_path = os.path.join(folder_path, files_in_folder[136])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[137])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[138])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[139])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[140])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[141])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[142])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[143])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[144])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                    
#             botoca_g01_total_11 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_11 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_11 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_11 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_11 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_11 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_11 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_11 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_11 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_11 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_11 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_11 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_11 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_11 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
                
#             first_file_path = os.path.join(folder_path, files_in_folder[145])
#             df = pd.read_csv(first_file_path)
            
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[146])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[147])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[148])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[149])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[150])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[151])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[152])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[153])
#             ninth_df = pd.read_csv(ninth_file_path)
                
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[154])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[155])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[156])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]
            
#             botoca_g01_total_12 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_12 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_12 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_12 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_12 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_12 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_12 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_12 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_12 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_12 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_12 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_12 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_12 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_12 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
                    
#             first_file_path = os.path.join(folder_path, files_in_folder[157])
#             df = pd.read_csv(first_file_path)
            
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]
                
#             second_file_path = os.path.join(folder_path, files_in_folder[158])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[159])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[160])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[161])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[162])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[163])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]


#             eighth_file_path = os.path.join(folder_path, files_in_folder[164])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[165])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[166])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[167])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[168])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]
 
#             botoca_g01_total_13 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12     
#             calaca_g01_total_13 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_13 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_13 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_13 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_13 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_13 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_13 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_13 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_13 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_13 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_13 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_13 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_13 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
                    
#             first_file_path = os.path.join(folder_path, files_in_folder[169])
#             df = pd.read_csv(first_file_path)
                
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[170])
#             second_df = pd.read_csv(second_file_path)
        
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[171])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[172])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[173])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[174])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[175])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[176])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[177])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[178])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[179])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[180])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

#             botoca_g01_total_14 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_14 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_14 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_14 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_14 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_14 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_14 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
            
#             leyte_a_total_14 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_14 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_14 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_14 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_14 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_14 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_14 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
            
            
#             first_file_path = os.path.join(folder_path, files_in_folder[181])
#             df = pd.read_csv(first_file_path)
                    
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[182])
#             second_df = pd.read_csv(second_file_path)

#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[183])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[184])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[185])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[186])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[187])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[188])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[189])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]


#             tenth_file_path = os.path.join(folder_path, files_in_folder[190])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[191])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[192])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]
                
#             botoca_g01_total_15 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_15 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_15 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_15 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_15 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_15 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_15 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_15 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_15 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_15 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_15 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_15 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_15 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_15 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

              
#             first_file_path = os.path.join(folder_path, files_in_folder[193])
#             df = pd.read_csv(first_file_path)
                
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[194])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[195])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[196])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[197])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[198])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[199])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[200])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[201])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[202])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[203])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[204])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

                
#             botoca_g01_total_16 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_16 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_16 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_16 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_16 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_16 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_16 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_16 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_16 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_16 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_16 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_16 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_16 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_16 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
                              
            
#             first_file_path = os.path.join(folder_path, files_in_folder[205])
#             df = pd.read_csv(first_file_path)
                
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[206])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[207])
#             third_df = pd.read_csv(third_file_path)
                
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[208])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[209])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[210])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[211])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[212])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[213])
#             ninth_df = pd.read_csv(ninth_file_path)

#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[214])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[215])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[216])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]
                
#             botoca_g01_total_17 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_17 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_17 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_17 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_17 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_17 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_17 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_17 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_17 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_17 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_17 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_17 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_17 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_17 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
            
            
#             first_file_path = os.path.join(folder_path, files_in_folder[217])
#             df = pd.read_csv(first_file_path)
            
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[218])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[219])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[220])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[221])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[222])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[223])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[224])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[225])
#             ninth_df = pd.read_csv(ninth_file_path)
        
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[226])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[227])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[228])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

#             botoca_g01_total_18 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_18 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_18 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_18 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_18 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_18 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_18 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_18 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_18 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_18 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_18 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_18 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_18 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_18 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
                    
           
#             first_file_path = os.path.join(folder_path, files_in_folder[229])
#             df = pd.read_csv(first_file_path)
            
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[230])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[231])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[232])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[233])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[234])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[235])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[236])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[237])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[238])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[239])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[240])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

#             botoca_g01_total_19 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_19 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_19 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_19 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_19 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_19 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_19 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_19 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_19 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_19 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_19 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_19 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_19 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_19 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
                
#             first_file_path = os.path.join(folder_path, files_in_folder[241])
#             df = pd.read_csv(first_file_path)
            
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[242])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[243])
#             third_df = pd.read_csv(third_file_path)

#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[244])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[245])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[246])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[247])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[248])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[249])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[250])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[251])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[252])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

#             botoca_g01_total_20 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12  
#             calaca_g01_total_20 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_20 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_20 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_20 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_20 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_20 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_20 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_20 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_20 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_20 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_20 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_20 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_20 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
        
           
#             first_file_path = os.path.join(folder_path, files_in_folder[253])
#             df = pd.read_csv(first_file_path)
            
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[254])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[255])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[256])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[257])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[258])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[259])
#             seventh_df = pd.read_csv(seventh_file_path)

#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[260])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[261])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[262])
#             tenth_df = pd.read_csv(tenth_file_path)

#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[263])
#             eleventh_df = pd.read_csv(eleventh_file_path)
        
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[264])
#             twelvth_df = pd.read_csv(twelvth_file_path)

#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

#             botoca_g01_total_21 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12  
#             calaca_g01_total_21 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_21 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_21 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_21 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_21 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_21 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_21 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_21 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_21 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_21 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_21 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_21 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_21 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
               
#             first_file_path = os.path.join(folder_path, files_in_folder[265])
#             df = pd.read_csv(first_file_path)

#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]

#             second_file_path = os.path.join(folder_path, files_in_folder[266])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[267])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[268])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[269])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[270])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[271])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[272])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[273])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[274])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[275])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[276])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

#             botoca_g01_total_22 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_22 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_22 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_22 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_22 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_22 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_22 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_22 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_22 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_22 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_22 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_22 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_22 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_22 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12
            
#             first_file_path = os.path.join(folder_path, files_in_folder[277])
#             df = pd.read_csv(first_file_path)
            
#             file_03BOTOCA_G01 = df.iloc[364,5]
#             file_03CALACA_G01 = df.iloc[368,5]
#             file_03CALACA_G02 = df.iloc[369,5]
#             file_03KAL_G01 = df.iloc[417,5]
#             file_03KAL_G02 = df.iloc[418,5]
#             file_03KAL_G03 = df.iloc[419,5]
#             file_03KAL_G04 = df.iloc[420,5]
#             file_04LEYTE_A = df.iloc[532,5]
#             file_05KSPC_G01 = df.iloc[590,5]
#             file_05KSPC_G02 = df.iloc[591,5]
#             file_08BANTAP_L01 = df.iloc[717,5]
#             file_08PEDC_T1L1 = df.iloc[757,5]
#             file_08PEDC_T1L2 = df.iloc[758,5]
#             file_08STBAR_T1L1 = df.iloc[772,5]                  

#             second_file_path = os.path.join(folder_path, files_in_folder[278])
#             second_df = pd.read_csv(second_file_path)
            
#             second_file_03BOTOCA_G01 = second_df.iloc[364,5]
#             second_file_03CALACA_G01 = second_df.iloc[368,5]
#             second_file_03CALACA_G02 = second_df.iloc[369,5]
#             second_file_03KAL_G01 = second_df.iloc[417,5]
#             second_file_03KAL_G02 = second_df.iloc[418,5]
#             second_file_03KAL_G03 = second_df.iloc[419,5]
#             second_file_03KAL_G04 = second_df.iloc[420,5]
#             second_file_04LEYTE_A = second_df.iloc[532,5]
#             second_file_05KSPC_G01 = second_df.iloc[590,5]
#             second_file_05KSPC_G02 = second_df.iloc[591,5]
#             second_file_08BANTAP_L01 = second_df.iloc[717,5]
#             second_file_08PEDC_T1L1 = second_df.iloc[757,5]
#             second_file_08PEDC_T1L2 = second_df.iloc[758,5]
#             second_file_08STBAR_T1L1 = second_df.iloc[772,5]

#             third_file_path = os.path.join(folder_path, files_in_folder[279])
#             third_df = pd.read_csv(third_file_path)
            
#             third_file_03BOTOCA_G01 = third_df.iloc[364,5]
#             third_file_03CALACA_G01 = third_df.iloc[368,5]
#             third_file_03CALACA_G02 = third_df.iloc[369,5]
#             third_file_03KAL_G01 = third_df.iloc[417,5]
#             third_file_03KAL_G02 = third_df.iloc[418,5]
#             third_file_03KAL_G03 = third_df.iloc[419,5]
#             third_file_03KAL_G04 = third_df.iloc[420,5]
#             third_file_04LEYTE_A = third_df.iloc[532,5]
#             third_file_05KSPC_G01 = third_df.iloc[590,5]
#             third_file_05KSPC_G02 = third_df.iloc[591,5]
#             third_file_08BANTAP_L01 = third_df.iloc[717,5]
#             third_file_08PEDC_T1L1 = third_df.iloc[757,5]
#             third_file_08PEDC_T1L2 = third_df.iloc[758,5]
#             third_file_08STBAR_T1L1 = third_df.iloc[772,5]

#             fourth_file_path = os.path.join(folder_path, files_in_folder[280])
#             fourth_df = pd.read_csv(fourth_file_path)
            
#             fourth_file_03BOTOCA_G01 = fourth_df.iloc[364,5]
#             fourth_file_03CALACA_G01 = fourth_df.iloc[368,5]
#             fourth_file_03CALACA_G02 = fourth_df.iloc[369,5]
#             fourth_file_03KAL_G01 = fourth_df.iloc[417,5]
#             fourth_file_03KAL_G02 = fourth_df.iloc[418,5]
#             fourth_file_03KAL_G03 = fourth_df.iloc[419,5]
#             fourth_file_03KAL_G04 = fourth_df.iloc[420,5]
#             fourth_file_04LEYTE_A = fourth_df.iloc[532,5]
#             fourth_file_05KSPC_G01 = fourth_df.iloc[590,5]
#             fourth_file_05KSPC_G02 = fourth_df.iloc[591,5]
#             fourth_file_08BANTAP_L01 = fourth_df.iloc[717,5]
#             fourth_file_08PEDC_T1L1 = fourth_df.iloc[757,5]
#             fourth_file_08PEDC_T1L2 = fourth_df.iloc[758,5]
#             fourth_file_08STBAR_T1L1 = fourth_df.iloc[772,5]

#             fifth_file_path = os.path.join(folder_path, files_in_folder[281])
#             fifth_df = pd.read_csv(fifth_file_path)
            
#             fifth_file_03BOTOCA_G01 = fifth_df.iloc[364,5]
#             fifth_file_03CALACA_G01 = fifth_df.iloc[368,5]
#             fifth_file_03CALACA_G02 = fifth_df.iloc[369,5]
#             fifth_file_03KAL_G01 = fifth_df.iloc[417,5]
#             fifth_file_03KAL_G02 = fifth_df.iloc[418,5]
#             fifth_file_03KAL_G03 = fifth_df.iloc[419,5]
#             fifth_file_03KAL_G04 = fifth_df.iloc[420,5]
#             fifth_file_04LEYTE_A = fifth_df.iloc[532,5]
#             fifth_file_05KSPC_G01 = fifth_df.iloc[590,5]
#             fifth_file_05KSPC_G02 = fifth_df.iloc[591,5]
#             fifth_file_08BANTAP_L01 = fifth_df.iloc[717,5]
#             fifth_file_08PEDC_T1L1 = fifth_df.iloc[757,5]
#             fifth_file_08PEDC_T1L2 = fifth_df.iloc[758,5]
#             fifth_file_08STBAR_T1L1 = fifth_df.iloc[772,5]

#             sixth_file_path = os.path.join(folder_path, files_in_folder[282])
#             sixth_df = pd.read_csv(sixth_file_path)
            
#             sixth_file_03BOTOCA_G01 = sixth_df.iloc[364,5]
#             sixth_file_03CALACA_G01 = sixth_df.iloc[368,5]
#             sixth_file_03CALACA_G02 = sixth_df.iloc[369,5]
#             sixth_file_03KAL_G01 = sixth_df.iloc[417,5]
#             sixth_file_03KAL_G02 = sixth_df.iloc[418,5]
#             sixth_file_03KAL_G03 = sixth_df.iloc[419,5]
#             sixth_file_03KAL_G04 = sixth_df.iloc[420,5]
#             sixth_file_04LEYTE_A = sixth_df.iloc[532,5]
#             sixth_file_05KSPC_G01 = sixth_df.iloc[590,5]
#             sixth_file_05KSPC_G02 = sixth_df.iloc[591,5]
#             sixth_file_08BANTAP_L01 = sixth_df.iloc[717,5]
#             sixth_file_08PEDC_T1L1 = sixth_df.iloc[757,5]
#             sixth_file_08PEDC_T1L2 = sixth_df.iloc[758,5]
#             sixth_file_08STBAR_T1L1 = sixth_df.iloc[772,5]

#             seventh_file_path = os.path.join(folder_path, files_in_folder[283])
#             seventh_df = pd.read_csv(seventh_file_path)
            
#             seventh_file_03BOTOCA_G01 = seventh_df.iloc[364,5]
#             seventh_file_03CALACA_G01 = seventh_df.iloc[368,5]
#             seventh_file_03CALACA_G02 = seventh_df.iloc[369,5]
#             seventh_file_03KAL_G01 = seventh_df.iloc[417,5]
#             seventh_file_03KAL_G02 = seventh_df.iloc[418,5]
#             seventh_file_03KAL_G03 = seventh_df.iloc[419,5]
#             seventh_file_03KAL_G04 = seventh_df.iloc[420,5]
#             seventh_file_04LEYTE_A = seventh_df.iloc[532,5]
#             seventh_file_05KSPC_G01 = seventh_df.iloc[590,5]
#             seventh_file_05KSPC_G02 = seventh_df.iloc[591,5]
#             seventh_file_08BANTAP_L01 = seventh_df.iloc[717,5]
#             seventh_file_08PEDC_T1L1 = seventh_df.iloc[757,5]
#             seventh_file_08PEDC_T1L2 = seventh_df.iloc[758,5]
#             seventh_file_08STBAR_T1L1 = seventh_df.iloc[772,5]

#             eighth_file_path = os.path.join(folder_path, files_in_folder[284])
#             eighth_df = pd.read_csv(eighth_file_path)
            
#             eighth_file_03BOTOCA_G01 = eighth_df.iloc[364,5]
#             eighth_file_03CALACA_G01 = eighth_df.iloc[368,5]
#             eighth_file_03CALACA_G02 = eighth_df.iloc[369,5]
#             eighth_file_03KAL_G01 = eighth_df.iloc[417,5]
#             eighth_file_03KAL_G02 = eighth_df.iloc[418,5]
#             eighth_file_03KAL_G03 = eighth_df.iloc[419,5]
#             eighth_file_03KAL_G04 = eighth_df.iloc[420,5]
#             eighth_file_04LEYTE_A = eighth_df.iloc[532,5]
#             eighth_file_05KSPC_G01 = eighth_df.iloc[590,5]
#             eighth_file_05KSPC_G02 = eighth_df.iloc[591,5]
#             eighth_file_08BANTAP_L01 = eighth_df.iloc[717,5]
#             eighth_file_08PEDC_T1L1 = eighth_df.iloc[757,5]
#             eighth_file_08PEDC_T1L2 = eighth_df.iloc[758,5]
#             eighth_file_08STBAR_T1L1 = eighth_df.iloc[772,5]

#             ninth_file_path = os.path.join(folder_path, files_in_folder[285])
#             ninth_df = pd.read_csv(ninth_file_path)
            
#             ninth_file_03BOTOCA_G01 = ninth_df.iloc[364,5]
#             ninth_file_03CALACA_G01 = ninth_df.iloc[368,5]
#             ninth_file_03CALACA_G02 = ninth_df.iloc[369,5]
#             ninth_file_03KAL_G01 = ninth_df.iloc[417,5]
#             ninth_file_03KAL_G02 = ninth_df.iloc[418,5]
#             ninth_file_03KAL_G03 = ninth_df.iloc[419,5]
#             ninth_file_03KAL_G04 = ninth_df.iloc[420,5]
#             ninth_file_04LEYTE_A = ninth_df.iloc[532,5]
#             ninth_file_05KSPC_G01 = ninth_df.iloc[590,5]
#             ninth_file_05KSPC_G02 = ninth_df.iloc[591,5]
#             ninth_file_08BANTAP_L01 = ninth_df.iloc[717,5]
#             ninth_file_08PEDC_T1L1 = ninth_df.iloc[757,5]
#             ninth_file_08PEDC_T1L2 = ninth_df.iloc[758,5]
#             ninth_file_08STBAR_T1L1 = ninth_df.iloc[772,5]

#             tenth_file_path = os.path.join(folder_path, files_in_folder[286])
#             tenth_df = pd.read_csv(tenth_file_path)
            
#             tenth_file_03BOTOCA_G01 = tenth_df.iloc[364,5]
#             tenth_file_03CALACA_G01 = tenth_df.iloc[368,5]
#             tenth_file_03CALACA_G02 = tenth_df.iloc[369,5]
#             tenth_file_03KAL_G01 = tenth_df.iloc[417,5]
#             tenth_file_03KAL_G02 = tenth_df.iloc[418,5]
#             tenth_file_03KAL_G03 = tenth_df.iloc[419,5]
#             tenth_file_03KAL_G04 = tenth_df.iloc[420,5]
#             tenth_file_04LEYTE_A = tenth_df.iloc[532,5]
#             tenth_file_05KSPC_G01 = tenth_df.iloc[590,5]
#             tenth_file_05KSPC_G02 = tenth_df.iloc[591,5]
#             tenth_file_08BANTAP_L01 = tenth_df.iloc[717,5]
#             tenth_file_08PEDC_T1L1 = tenth_df.iloc[757,5]
#             tenth_file_08PEDC_T1L2 = tenth_df.iloc[758,5]
#             tenth_file_08STBAR_T1L1 = tenth_df.iloc[772,5]

#             eleventh_file_path = os.path.join(folder_path, files_in_folder[287])
#             eleventh_df = pd.read_csv(eleventh_file_path)
            
#             eleventh_file_03BOTOCA_G01 = eleventh_df.iloc[364,5]
#             eleventh_file_03CALACA_G01 = eleventh_df.iloc[368,5]
#             eleventh_file_03CALACA_G02 = eleventh_df.iloc[369,5]
#             eleventh_file_03KAL_G01 = eleventh_df.iloc[417,5]
#             eleventh_file_03KAL_G02 = eleventh_df.iloc[418,5]
#             eleventh_file_03KAL_G03 = eleventh_df.iloc[419,5]
#             eleventh_file_03KAL_G04 = eleventh_df.iloc[420,5]
#             eleventh_file_04LEYTE_A = eleventh_df.iloc[532,5]
#             eleventh_file_05KSPC_G01 = eleventh_df.iloc[590,5]
#             eleventh_file_05KSPC_G02 = eleventh_df.iloc[591,5]
#             eleventh_file_08BANTAP_L01 = eleventh_df.iloc[717,5]
#             eleventh_file_08PEDC_T1L1 = eleventh_df.iloc[757,5]
#             eleventh_file_08PEDC_T1L2 = eleventh_df.iloc[758,5]
#             eleventh_file_08STBAR_T1L1 = eleventh_df.iloc[772,5]

#             twelvth_file_path = os.path.join(folder_path, files_in_folder[0])
#             twelvth_df = pd.read_csv(twelvth_file_path)
            
#             twelvth_file_03BOTOCA_G01 = twelvth_df.iloc[364,5]
#             twelvth_file_03CALACA_G01 = twelvth_df.iloc[368,5]
#             twelvth_file_03CALACA_G02 = twelvth_df.iloc[369,5]
#             twelvth_file_03KAL_G01 = twelvth_df.iloc[417,5]
#             twelvth_file_03KAL_G02 = twelvth_df.iloc[418,5]
#             twelvth_file_03KAL_G03 = twelvth_df.iloc[419,5]
#             twelvth_file_03KAL_G04 = twelvth_df.iloc[420,5]
#             twelvth_file_04LEYTE_A = twelvth_df.iloc[532,5]
#             twelvth_file_05KSPC_G01 = twelvth_df.iloc[590,5]
#             twelvth_file_05KSPC_G02 = twelvth_df.iloc[591,5]
#             twelvth_file_08BANTAP_L01 = twelvth_df.iloc[717,5]
#             twelvth_file_08PEDC_T1L1 = twelvth_df.iloc[757,5]
#             twelvth_file_08PEDC_T1L2 = twelvth_df.iloc[758,5]
#             twelvth_file_08STBAR_T1L1 = twelvth_df.iloc[772,5]

#             botoca_g01_total_23 = (file_03BOTOCA_G01 + second_file_03BOTOCA_G01 + third_file_03BOTOCA_G01 + fourth_file_03BOTOCA_G01 + fifth_file_03BOTOCA_G01 + sixth_file_03BOTOCA_G01 + seventh_file_03BOTOCA_G01 + eighth_file_03BOTOCA_G01 + ninth_file_03BOTOCA_G01 + tenth_file_03BOTOCA_G01 + eleventh_file_03BOTOCA_G01 + twelvth_file_03BOTOCA_G01)/12
#             calaca_g01_total_23 = (file_03CALACA_G01 + second_file_03CALACA_G01 + third_file_03CALACA_G01 + fourth_file_03CALACA_G01 + fifth_file_03CALACA_G01 + sixth_file_03CALACA_G01 + seventh_file_03CALACA_G01 + eighth_file_03CALACA_G01 + ninth_file_03CALACA_G01 + tenth_file_03CALACA_G01 + eleventh_file_03CALACA_G01 + twelvth_file_03CALACA_G01)/12
#             calaca_g02_total_23 = (file_03CALACA_G02 + second_file_03CALACA_G02 + third_file_03CALACA_G02 + fourth_file_03CALACA_G02 + fifth_file_03CALACA_G02 + sixth_file_03CALACA_G02 + seventh_file_03CALACA_G02 + eighth_file_03CALACA_G02 + ninth_file_03CALACA_G02 + tenth_file_03CALACA_G02 + eleventh_file_03CALACA_G02 + twelvth_file_03CALACA_G02)/12
#             kal_g01_total_23 = (file_03KAL_G01 + second_file_03KAL_G01 + third_file_03KAL_G01 + fourth_file_03KAL_G01 + fifth_file_03KAL_G01 + sixth_file_03KAL_G01 + seventh_file_03KAL_G01 + eighth_file_03KAL_G01 + ninth_file_03KAL_G01 + tenth_file_03KAL_G01 + eleventh_file_03KAL_G01 + twelvth_file_03KAL_G01)/12
#             kal_g02_total_23 = (file_03KAL_G02 + second_file_03KAL_G02 + third_file_03KAL_G02 + fourth_file_03KAL_G02 + fifth_file_03KAL_G02 + sixth_file_03KAL_G02 + seventh_file_03KAL_G02 + eighth_file_03KAL_G02 + ninth_file_03KAL_G02 + tenth_file_03KAL_G02 + eleventh_file_03KAL_G02 + twelvth_file_03KAL_G02)/12
#             kal_g03_total_23 = (file_03KAL_G03 + second_file_03KAL_G03 + third_file_03KAL_G03 + fourth_file_03KAL_G03 + fifth_file_03KAL_G03 + sixth_file_03KAL_G03 + seventh_file_03KAL_G03 + eighth_file_03KAL_G03 + ninth_file_03KAL_G03 + tenth_file_03KAL_G03 + eleventh_file_03KAL_G03 + twelvth_file_03KAL_G03)/12
#             kal_g04_total_23 = (file_03KAL_G04 + second_file_03KAL_G04 + third_file_03KAL_G04 + fourth_file_03KAL_G04 + fifth_file_03KAL_G04 + sixth_file_03KAL_G04 + seventh_file_03KAL_G04 + eighth_file_03KAL_G04 + ninth_file_03KAL_G04 + tenth_file_03KAL_G04 + eleventh_file_03KAL_G04 + twelvth_file_03KAL_G04)/12
#             leyte_a_total_23 = (file_04LEYTE_A + second_file_04LEYTE_A + third_file_04LEYTE_A + fourth_file_04LEYTE_A + fifth_file_04LEYTE_A + sixth_file_04LEYTE_A + seventh_file_04LEYTE_A + eighth_file_04LEYTE_A + ninth_file_04LEYTE_A + tenth_file_04LEYTE_A + eleventh_file_04LEYTE_A + twelvth_file_04LEYTE_A)/12
#             kspc_g01_total_23 = (file_05KSPC_G01 + second_file_05KSPC_G01 + third_file_05KSPC_G01 + fourth_file_05KSPC_G01 + fifth_file_05KSPC_G01 + sixth_file_05KSPC_G01 + seventh_file_05KSPC_G01 + eighth_file_05KSPC_G01 + ninth_file_05KSPC_G01 + tenth_file_05KSPC_G01 + eleventh_file_05KSPC_G01 + twelvth_file_05KSPC_G01)/12
#             kspc_g02_total_23 = (file_05KSPC_G02 + second_file_05KSPC_G02 + third_file_05KSPC_G02 + fourth_file_05KSPC_G02 + fifth_file_05KSPC_G02 + sixth_file_05KSPC_G02 + seventh_file_05KSPC_G02 + eighth_file_05KSPC_G02 + ninth_file_05KSPC_G02 + tenth_file_05KSPC_G02 + eleventh_file_05KSPC_G02 + twelvth_file_05KSPC_G02)/12
#             bantap_l01_total_23 = (file_08BANTAP_L01 + second_file_08BANTAP_L01 + third_file_08BANTAP_L01 + fourth_file_08BANTAP_L01 + fifth_file_08BANTAP_L01 + sixth_file_08BANTAP_L01 + seventh_file_08BANTAP_L01 + eighth_file_08BANTAP_L01 + ninth_file_08BANTAP_L01 + tenth_file_08BANTAP_L01 + eleventh_file_08BANTAP_L01 + twelvth_file_08BANTAP_L01)/12
#             pedc_t1l1_total_23 = (file_08PEDC_T1L1 + second_file_08PEDC_T1L1 + third_file_08PEDC_T1L1 + fourth_file_08PEDC_T1L1 + fifth_file_08PEDC_T1L1 + sixth_file_08PEDC_T1L1 + seventh_file_08PEDC_T1L1 + eighth_file_08PEDC_T1L1 + ninth_file_08PEDC_T1L1 + tenth_file_08PEDC_T1L1 + eleventh_file_08PEDC_T1L1 + twelvth_file_08PEDC_T1L1)/12
#             pedc_t1l2_total_23 = (file_08PEDC_T1L2 + second_file_08PEDC_T1L2 + third_file_08PEDC_T1L2 + fourth_file_08PEDC_T1L2 + fifth_file_08PEDC_T1L2 + sixth_file_08PEDC_T1L2 + seventh_file_08PEDC_T1L2 + eighth_file_08PEDC_T1L2 + ninth_file_08PEDC_T1L2 + tenth_file_08PEDC_T1L2 + eleventh_file_08PEDC_T1L2 + twelvth_file_08PEDC_T1L2)/12
#             stbar_t1l1_total_23 = (file_08STBAR_T1L1 + second_file_08STBAR_T1L1 + third_file_08STBAR_T1L1 + fourth_file_08STBAR_T1L1 + fifth_file_08STBAR_T1L1 + sixth_file_08STBAR_T1L1 + seventh_file_08STBAR_T1L1 + eighth_file_08STBAR_T1L1 + ninth_file_08STBAR_T1L1 + tenth_file_08STBAR_T1L1 + eleventh_file_08STBAR_T1L1 + twelvth_file_08STBAR_T1L1)/12

# # 19/07/2024 01:00:00
# # 03BOTOCA_G01 6235.12
# # 03CALACA_G01 6005.46
# # 03CALACA_G02 -
# # 03KAL_G01 -
# # 03KAL_G02 -
# # 03KAL_G03 -
# # 03KAL_G04 -
# # 04LEYTE_A -
# # 05KSPC_G01 -
# # 05KSPC_G02 -
# # 08BANTAP_L01 -
# # 08PEDC_T1L1 - 
# # 08PEDC_T1L2 - 
# # 08STBAR_T1L1 - 

# from datetime import datetime

# # Get the current date
# current_date = datetime.now()

# # Format: 19/07/2024 12:00:00
# static_time_1 = " 01:00:00"
# static_time_2 = " 02:00:00"
# static_time_3 = " 03:00:00"
# static_time_4 = " 04:00:00"
# static_time_5 = " 05:00:00"
# static_time_6 = " 06:00:00"
# static_time_7 = " 07:00:00"
# static_time_8 = " 08:00:00"
# static_time_9 = " 09:00:00"
# static_time_10 = " 10:00:00"
# static_time_11 = " 11:00:00"
# static_time_12 = " 12:00:00"
# static_time_13 = " 13:00:00"
# static_time_14 = " 14:00:00"
# static_time_15 = " 15:00:00"
# static_time_16 = " 16:00:00"
# static_time_17 = " 17:00:00"
# static_time_18 = " 18:00:00"
# static_time_19 = " 19:00:00"
# static_time_20 = " 20:00:00"
# static_time_21 = " 21:00:00"
# static_time_22 = " 22:00:00"
# static_time_23 = " 23:00:00"
# static_time_24 = " 24:00:00"

# first_hour = current_date.strftime("%d/%m/%Y") + static_time_1
# second_hour = current_date.strftime("%d/%m/%Y") + static_time_2
# third_hour = current_date.strftime("%d/%m/%Y") + static_time_3
# fourth_hour = current_date.strftime("%d/%m/%Y") + static_time_4
# fifth_hour = current_date.strftime("%d/%m/%Y") + static_time_5
# sixth_hour = current_date.strftime("%d/%m/%Y") + static_time_6
# seventh_hour = current_date.strftime("%d/%m/%Y") + static_time_7
# eighth_hour = current_date.strftime("%d/%m/%Y") + static_time_8
# ninth_hour = current_date.strftime("%d/%m/%Y") + static_time_9
# tenth_hour = current_date.strftime("%d/%m/%Y") + static_time_10
# eleventh_hour = current_date.strftime("%d/%m/%Y") + static_time_11
# twelvth_hour = current_date.strftime("%d/%m/%Y") + static_time_12
# thirteenth_hour = current_date.strftime("%d/%m/%Y") + static_time_13
# fourteenth_hour = current_date.strftime("%d/%m/%Y") + static_time_14
# fifteenth_hour = current_date.strftime("%d/%m/%Y") + static_time_15
# sixteenth_hour = current_date.strftime("%d/%m/%Y") + static_time_16
# seventeenth_hour = current_date.strftime("%d/%m/%Y") + static_time_17
# eighteenth_hour = current_date.strftime("%d/%m/%Y") + static_time_18
# nineteenth_hour = current_date.strftime("%d/%m/%Y") + static_time_19
# twentieth_hour = current_date.strftime("%d/%m/%Y") + static_time_20
# twenty_first_hour = current_date.strftime("%d/%m/%Y") + static_time_21
# twenty_second_hour = current_date.strftime("%d/%m/%Y") + static_time_22
# twenty_third_hour = current_date.strftime("%d/%m/%Y") + static_time_23
# twenty_fourth_hour = current_date.strftime("%d/%m/%Y") + static_time_24

# data = {
#     "HOUR": [first_hour, second_hour, third_hour, fourth_hour, fifth_hour, sixth_hour, seventh_hour, eighth_hour, ninth_hour, tenth_hour, eleventh_hour, twelvth_hour, thirteenth_hour, fourteenth_hour, fifteenth_hour, sixteenth_hour, seventeenth_hour, eighteenth_hour, nineteenth_hour, twentieth_hour, twenty_first_hour, twenty_second_hour, twenty_third_hour, twenty_fourth_hour],
#     "03BOTOCA_G01": [botoca_g01_total, botoca_g01_total_1, botoca_g01_total_2, botoca_g01_total_3, botoca_g01_total_4, botoca_g01_total_5, botoca_g01_total_6, botoca_g01_total_7, botoca_g01_total_8, botoca_g01_total_9, botoca_g01_total_10, botoca_g01_total_11, botoca_g01_total_12, botoca_g01_total_13, botoca_g01_total_14, botoca_g01_total_15, botoca_g01_total_16, botoca_g01_total_17, botoca_g01_total_18, botoca_g01_total_19, botoca_g01_total_20, botoca_g01_total_21, botoca_g01_total_22, botoca_g01_total_23],
#     "03CALACA_G01": [calaca_g01_total, calaca_g01_total_1,calaca_g01_total_2, calaca_g01_total_3, calaca_g01_total_4, calaca_g01_total_5, calaca_g01_total_6, calaca_g01_total_7, calaca_g01_total_8, calaca_g01_total_9, calaca_g01_total_10, calaca_g01_total_11, calaca_g01_total_12, calaca_g01_total_13, calaca_g01_total_14, calaca_g01_total_15, calaca_g01_total_16, calaca_g01_total_17, calaca_g01_total_18, calaca_g01_total_19, calaca_g01_total_20, calaca_g01_total_21, calaca_g01_total_22, calaca_g01_total_23],
#     "03CALACA_G02": [calaca_g02_total, calaca_g02_total_1, calaca_g02_total_2, calaca_g02_total_3, calaca_g02_total_4, calaca_g02_total_5, calaca_g02_total_6, calaca_g02_total_7, calaca_g02_total_8, calaca_g02_total_9, calaca_g02_total_10, calaca_g02_total_11, calaca_g02_total_12, calaca_g02_total_13, calaca_g02_total_14, calaca_g02_total_15, calaca_g02_total_16, calaca_g02_total_17, calaca_g02_total_18, calaca_g02_total_19, calaca_g02_total_20, calaca_g02_total_21, calaca_g02_total_22, calaca_g02_total_23],
#     "03KAL_G01": [kal_g01_total, kal_g01_total_1, kal_g01_total_2, kal_g01_total_3, kal_g01_total_4, kal_g01_total_5, kal_g01_total_6, kal_g01_total_7, kal_g01_total_8, kal_g01_total_9, kal_g01_total_10, kal_g01_total_11, kal_g01_total_12, kal_g01_total_13, kal_g01_total_14, kal_g01_total_15, kal_g01_total_16, kal_g01_total_17, kal_g01_total_18, kal_g01_total_19, kal_g01_total_20, kal_g01_total_21, kal_g01_total_22, kal_g01_total_23], 
#     "03KAL_G02": [kal_g02_total, kal_g02_total_1, kal_g02_total_2, kal_g02_total_3, kal_g02_total_4, kal_g02_total_5, kal_g02_total_6, kal_g02_total_7, kal_g02_total_8, kal_g02_total_9, kal_g02_total_10, kal_g02_total_11, kal_g02_total_12, kal_g02_total_13, kal_g02_total_14, kal_g02_total_15, kal_g02_total_16, kal_g02_total_17, kal_g02_total_18, kal_g02_total_19, kal_g02_total_20, kal_g02_total_21, kal_g02_total_22, kal_g02_total_23], 
#     "03KAL_G03": [kal_g03_total, kal_g03_total_1, kal_g03_total_2, kal_g03_total_3, kal_g03_total_4, kal_g03_total_5, kal_g03_total_6, kal_g03_total_7, kal_g03_total_8, kal_g03_total_9, kal_g03_total_10, kal_g03_total_11, kal_g03_total_12, kal_g03_total_13, kal_g03_total_14, kal_g03_total_15, kal_g03_total_16, kal_g03_total_17, kal_g03_total_18, kal_g03_total_19, kal_g03_total_20, kal_g03_total_21, kal_g03_total_22, kal_g03_total_23],
#     "03KAL_G04": [kal_g04_total, kal_g04_total_1, kal_g04_total_2, kal_g04_total_3, kal_g04_total_4, kal_g04_total_5, kal_g04_total_6, kal_g04_total_7, kal_g04_total_8, kal_g04_total_9, kal_g04_total_10, kal_g04_total_11, kal_g04_total_12, kal_g04_total_13, kal_g04_total_14, kal_g04_total_15, kal_g04_total_16, kal_g04_total_17, kal_g04_total_18, kal_g04_total_19, kal_g04_total_20, kal_g04_total_21, kal_g04_total_22, kal_g04_total_23],
#     "04LEYTE_A": [leyte_a_total, leyte_a_total_1, leyte_a_total_2, leyte_a_total_3, leyte_a_total_4, leyte_a_total_5, leyte_a_total_6, leyte_a_total_7, leyte_a_total_8, leyte_a_total_9, leyte_a_total_10, leyte_a_total_11, leyte_a_total_12, leyte_a_total_13, leyte_a_total_14, leyte_a_total_15, leyte_a_total_16, leyte_a_total_17, leyte_a_total_18, leyte_a_total_19, leyte_a_total_20, leyte_a_total_21, leyte_a_total_22, leyte_a_total_23],
#     "05KSPC_G01": [kspc_g01_total, kspc_g01_total_1, kspc_g01_total_2, kspc_g01_total_3, kspc_g01_total_4, kspc_g01_total_5, kspc_g01_total_6, kspc_g01_total_7, kspc_g01_total_8, kspc_g01_total_9, kspc_g01_total_10, kspc_g01_total_11, kspc_g01_total_12, kspc_g01_total_13, kspc_g01_total_14, kspc_g01_total_15, kspc_g01_total_16, kspc_g01_total_17, kspc_g01_total_18, kspc_g01_total_19, kspc_g01_total_20, kspc_g01_total_21, kspc_g01_total_22, kspc_g01_total_23],
#     "05KSPC_G02": [kspc_g02_total, kspc_g02_total_1, kspc_g02_total_2, kspc_g02_total_3, kspc_g02_total_4, kspc_g02_total_5, kspc_g02_total_6, kspc_g02_total_7, kspc_g02_total_8, kspc_g02_total_9, kspc_g02_total_10, kspc_g02_total_11, kspc_g02_total_12, kspc_g02_total_13, kspc_g02_total_14, kspc_g02_total_15, kspc_g02_total_16, kspc_g02_total_17, kspc_g02_total_18, kspc_g02_total_19, kspc_g02_total_20, kspc_g02_total_21, kspc_g02_total_22, kspc_g02_total_23], 
#     "08BANTAP_L01": [bantap_l01_total, bantap_l01_total_1, bantap_l01_total_2, bantap_l01_total_3, bantap_l01_total_4, bantap_l01_total_5, bantap_l01_total_6, bantap_l01_total_7, bantap_l01_total_8, bantap_l01_total_9, bantap_l01_total_10, bantap_l01_total_11, bantap_l01_total_12, bantap_l01_total_13, bantap_l01_total_14, bantap_l01_total_15, bantap_l01_total_16, bantap_l01_total_17, bantap_l01_total_18, bantap_l01_total_19, bantap_l01_total_20, bantap_l01_total_21, bantap_l01_total_22, bantap_l01_total_23],
#     "08PEDC_T1L1": [pedc_t1l1_total, pedc_t1l1_total_1, pedc_t1l1_total_2, pedc_t1l1_total_3, pedc_t1l1_total_4, pedc_t1l1_total_5, pedc_t1l1_total_6, pedc_t1l1_total_7, pedc_t1l1_total_8, pedc_t1l1_total_9, pedc_t1l1_total_10, pedc_t1l1_total_11, pedc_t1l1_total_12, pedc_t1l1_total_13, pedc_t1l1_total_14, pedc_t1l1_total_15, pedc_t1l1_total_16, pedc_t1l1_total_17, pedc_t1l1_total_18, pedc_t1l1_total_19, pedc_t1l1_total_20, pedc_t1l1_total_21, pedc_t1l1_total_22, pedc_t1l1_total_23],
#     "08PEDC_T1L2": [pedc_t1l2_total, pedc_t1l2_total_1, pedc_t1l2_total_2, pedc_t1l2_total_3, pedc_t1l2_total_4, pedc_t1l2_total_5, pedc_t1l2_total_6, pedc_t1l2_total_7, pedc_t1l2_total_8, pedc_t1l2_total_9, pedc_t1l2_total_10, pedc_t1l2_total_11, pedc_t1l2_total_12, pedc_t1l2_total_13, pedc_t1l2_total_14, pedc_t1l2_total_15, pedc_t1l2_total_16, pedc_t1l2_total_17, pedc_t1l2_total_18, pedc_t1l2_total_19, pedc_t1l2_total_20, pedc_t1l2_total_21, pedc_t1l2_total_22, pedc_t1l2_total_23],
#     "08STBAR_T1L1": [stbar_t1l1_total, stbar_t1l1_total_1, stbar_t1l1_total_2, stbar_t1l1_total_3, stbar_t1l1_total_4, stbar_t1l1_total_5, stbar_t1l1_total_6, stbar_t1l1_total_7, stbar_t1l1_total_8, stbar_t1l1_total_9, stbar_t1l1_total_10, stbar_t1l1_total_11, stbar_t1l1_total_12, stbar_t1l1_total_13, stbar_t1l1_total_14, stbar_t1l1_total_15, stbar_t1l1_total_16, stbar_t1l1_total_17, stbar_t1l1_total_18, stbar_t1l1_total_19, stbar_t1l1_total_20, stbar_t1l1_total_21, stbar_t1l1_total_22, stbar_t1l1_total_23]
#     }

# # Get the current hour
# current_hour = datetime.now().hour

# # Only start processing if the current hour is 2 AM or later
# if current_hour >= 2:
#     # Calculate two hours before the current hour
#     two_hours_before = current_hour - 2

#     # Filter the data up to two hours before the current hour
#     filtered_data = {key: values[:two_hours_before+1] for key, values in data.items()}

#     fig = go.Figure()

#     for key, values in filtered_data.items():
#         if key != "HOUR":
#             fig.add_trace(go.Scatter(x=filtered_data["HOUR"], y=values, mode='lines', name=key))

#     fig.update_layout(
#         title='Substation Load Data',
#         xaxis_title='Hour',
#         yaxis_title='Total',
#         legend_title='Substation',
#         template='plotly_white'
#     )

#     fig.show()