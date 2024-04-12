#!/usr/bin/env python3
import subprocess
import csv
from datetime import datetime, timedelta

fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('/home/carpeta/IPs_maliciosas.csv', 'w', newline='') as csvfile:
    fieldnames = ['Fecha', 'Hora', 'IP', 'Port', 'Nombre']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()

    ndias = input(f"Hola {subprocess.getoutput('echo $USER')}, ¿de cuántos días quieres filtrar el journalctl? ")
    ndias = int(ndias)

    journal_output = subprocess.getoutput(f"sudo journalctl -S -{ndias}d | grep 'invalid user'")
    for line in journal_output.splitlines():
        parts = line.split()
        if parts[11] != "port":
            writer.writerow({'Fecha': parts[0], 'Hora': parts[1], 'IP': parts[11], 'Port': parts[13], 'Nombre': parts[10]})
        else:
            writer.writerow({'Fecha': parts[0], 'Hora': parts[1], 'IP': parts[10], 'Port': parts[12], 'Nombre': 'desconocido'})

if subprocess.run(["echo", "$?"], capture_output=True).stdout.decode().strip() == "0":
    print("El archivo IPs_maliciosas ha sido creado correctamente")
    subprocess.run(["sudo", "chmod", "664", "/home/carpeta/IPs_maliciosas.csv"])
    subprocess.run(["sudo", "chown", "seginf_director:carpeta", "/home/carpeta/IPs_maliciosas.csv"])

    with open('/home/carpeta/IPs_maliciosas.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([])
        writer.writerow([f"Fichero actualizado: {fecha}"])
else:
    print("El archivo IPs_maliciosas no ha sido creado correctamente")

respuesta = input("¿Quieres mostrar por pantalla el resultado? 's' para aceptar: ")
if respuesta.lower() == "s":
    subprocess.run(["cat", "/home/carpeta/IPs_maliciosas.csv"])
