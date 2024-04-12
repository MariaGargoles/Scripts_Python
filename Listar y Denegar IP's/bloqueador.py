#!/usr/bin/env python3
import csv
import subprocess

def bloquear_ip(ip):
    subprocess.run(["sudo", "route", "add", "-host", ip, "reject"])


archivo_csv = '/home/carpeta/IPs_maliciosas.csv'


ips_maliciosas = []


with open(archivo_csv, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ip = row['IP']
        ips_maliciosas.append(ip)


for ip in ips_maliciosas:
    bloquear_ip(ip)

print("Se han bloqueado las siguientes IPs maliciosas:")
print(ips_maliciosas)
