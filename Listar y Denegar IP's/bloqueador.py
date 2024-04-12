#!/usr/bin/env python3
import csv
import subprocess

def block_ip(ip):
    subprocess.run(["sudo", "route", "add", "-host", ip, "reject"])


list_csv = '/home/carpeta/IPs_maliciosas.csv'


Doe_IPs = []


with open(list_csv, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ip = row['IP']
        Doe_IPs.append(ip)


for ip in Doe_IPs:
    block_ip(ip)

print("Se han bloqueado las siguientes IPs maliciosas: ")
print(Doe_IPs)
