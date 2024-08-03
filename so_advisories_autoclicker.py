import schedule
import time
import subprocess

def run_notebook():
    # Command to execute the Jupyter notebook
    command = [
        'jupyter', 'nbconvert', '--to', 'notebook', '--execute',
        '--inplace', 'C:/Users/aslee/OneDrive - MORE ELECTRIC AND POWER CORPORATION/Desktop/DASHBOARD_FINAL/so_advisories.ipynb'
    ]
    subprocess.run(command, check=True)
    print("Notebook executed successfully.")

# Schedule the job every hour
schedule.every().hour.do(run_notebook)

while True:
    schedule.run_pending()
    time.sleep(1)