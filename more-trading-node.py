# Necessary imports
from datetime import datetime
from ftplib import FTP, error_perm, all_errors
import os
import time

# FTP server details
FTP_SERVER = "120.28.19.206"
FTP_USER = "MORE_01"
FTP_PASSWD = "ar@pNkRW4v"
FTP_DIRECTORY = "/LMP/DIPC/"
LOCAL_DIRECTORY = "C:\\Users\\aslee\\OneDrive - MORE ELECTRIC AND POWER CORPORATION\\Desktop\\DASHBOARD_FINAL\\MORE Trading Node\\"
CHECK_INTERVAL = 60  # In seconds

# Function to connect to the FTP server
def connect_ftp():
    ftp = FTP(FTP_SERVER)
    ftp.login(user=FTP_USER, passwd=FTP_PASSWD)
    ftp.cwd(FTP_DIRECTORY)
    return ftp

# Function to download files from the FTP server
def download_files():
    now = datetime.now()  
    date_today = now.strftime("%Y%m%d")

    # Connect to FTP server
    ftp = connect_ftp()

    # List the files in the FTP directory
    files = ftp.nlst()

    for addtl_folder in files:
        # If the folder name is the same with today's date
        if addtl_folder == date_today:
            ftp_folder_file = f"/LMP/DIPC/{addtl_folder}"
            local_folder_file = os.path.join(LOCAL_DIRECTORY, addtl_folder)

            print(f"Checking FTP folder path: {ftp_folder_file}")
            print(f"Checking local folder path: {local_folder_file}")

            try:
                # Check if the folder exists on the FTP server
                ftp.cwd(ftp_folder_file)
                folder_exists = True
            except error_perm:
                folder_exists = False
                print(f"FTP folder does not exist: {ftp_folder_file}")

            if folder_exists:
                # Ensure the destination folder exists
                if not os.path.exists(local_folder_file):
                    os.makedirs(local_folder_file)

                # Download the files from the FTP server to the local folder
                filenames = ftp.nlst()
                for filename in filenames:
                    local_file_path = os.path.join(local_folder_file, filename)
                    try:
                        with open(local_file_path, 'wb') as local_file:
                            ftp.retrbinary('RETR ' + filename, local_file.write)
                        print(f"Copied {filename} to {local_file_path}")
                    except error_perm as e:
                        print(f"Could not copy {filename}: {e}")
                    except all_errors as e:
                        print(f"An FTP error occurred: {e}")

    ftp.quit()

# Main loop to check for new files every CHECK_INTERVAL seconds
while True:
    try:
        download_files()
    except all_errors as e:
        print(f"An error occurred: {e}")
    time.sleep(CHECK_INTERVAL)

# RESOURCE NAMES -> 08PEDC_T1L1, 08PEDC_T1L2, 08STBAR_T1L1 