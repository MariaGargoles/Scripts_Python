# pip install schedule smtplib
# Ensure schedule and smtplib libraries are installed or use Linux Crontab for scheduling

import os
import shutil
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import schedule
import time
import csv

def run_rkhunter():
    # Run RKHunter
    os.system("sudo rkhunter -c")

    # Copy log file to the desired location
    src = "/var/log/rkhunter.log"
    dst = "/home/folder/log_rkhunter.csv"

    with open(src, 'r') as log_file:
        log_content = log_file.readlines()

    # Convert log content to CSV
    with open(dst, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["RKHunter Log"])
        for line in log_content:
            csv_writer.writerow([line.strip()])

    os.chmod(dst, 0o644)
    shutil.chown(dst, user='root', group='root')

    # Send email alert with the log file
    send_email_alert(dst)

def send_email_alert(log_file):
    with open(log_file, 'r') as file:
        log_content = file.read()

    msg = MIMEText(log_content)
    msg['Subject'] = f'RKHunter Log - {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    msg['From'] = 'youremail@example.com'
    msg['To'] = 'recipient@example.com'

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('youremail@example.com', 'yourpassword')
        server.sendmail('youremail@example.com', 'recipient@example.com', msg.as_string())

# Schedule the task to run daily at 05:00 AM
schedule.every().day.at("05:00").do(run_rkhunter)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
