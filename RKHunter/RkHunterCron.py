import os
import shutil
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import csv

def run_rkhunter():
    # Run RKHunter
    os.system("sudo rkhunter -c")

    # Copy log file to the desired location
    src = "/var/log/rkhunter.log"
    dst = "/home/auditoria/log_rkhunter.csv"

    with open(src, 'r') as log_file:
        log_content = log_file.readlines()

    # Convert log content to CSV
    with open(dst, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["RKHunter Log"])
        for line in log_content:
            csv_writer.writerow([line.strip()])

    os.chmod(dst, 0o644)
    shutil.chown(dst, user='seginf_director', group='auditoria')

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

# Run
if __name__ == "__main__":
    run_rkhunter()
