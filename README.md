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
