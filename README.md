# Automatización de Seguridad para Sistemas Linux

¡Bienvenido a mi proyecto de Automatización de Seguridad para Sistemas Linux!

## Descripción

Tengo como objetivo proporcionar herramientas de automatización para fortalecer la seguridad en entornos Linux, mediante el uso de scripts en Python y Bash. Iré actualizando el repositorio con distintas carpetas, las cuales contendrán uno o varios scripts que se utilizarán conjuntamente para una funcionalidad concreta.

## Funcionalidades

**1. Abrimos con la primera funcionalidad que es :
Listar y Denegar IP's**

- **Análisis de Journalctl:** Nuestros scripts procesan archivos CSV generados a partir de registros de sistema, identificando IPs indeseadas.
- **Bloqueo Automático:** Configuramos automáticamente reglas de firewall para bloquear el acceso desde estas IPs maliciosas, protegiendo así el sistema de futuros intentos de intrusión.

[Listar y Denegar IP's](https://github.com/MariaGargoles/Scripts_Python/tree/main/Listar%20y%20Denegar%20IP's)

## Uso

### Preparación del Entorno:

- Asegúrate de tener los privilegios necesarios para ejecutar scripts y configurar el firewall.

### Ejecución de los Scripts:

Ejecuta el script principal..

```bash
python main_script.py
```

# Funcionalidades

## 2. Monitoreo y Alerta de Seguridad con RKHunter

- **Ejecución de RKHunter:** Se configura un script que ejecuta RKHunter para realizar chequeos de seguridad en el sistema.

- **Registro y Alerta:** Los logs generados por RKHunter se convierten a formato CSV y se almacenan en una ubicación específica. Se envía una alerta por correo electrónico con el contenido del log para una revisión inmediata.

### Script de Python sin Schedule
Este script ejecuta RKHunter, convierte el log a CSV, lo guarda en una ubicación designada y envía una alerta por correo electrónico. Se puede programar usando cron en Linux.

[Script sin Schedule](https://github.com/MariaGargoles/Scripts_Python/blob/main/RKHunter/RkHunterCron.py)

### Script de Python con Schedule
Similar al anterior, pero usa la biblioteca `schedule` para ejecutar automáticamente la tarea a las 05:00 AM todos los días.

[Script con Schedule](https://github.com/MariaGargoles/Scripts_Python/blob/main/RKHunter/RkHunterSchedule.py)

