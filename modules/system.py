import platform
import socket
import getpass
import psutil
from datetime import datetime, timedelta


# Info sobre o pc e sobre o user logado
def get_system_info():

    system_info = {
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.architecture()[0],
        "username": getpass.getuser(),
        "uptime": format_uptime(get_uptime())
    }

    return system_info


# Info sobre o tempo de uso do pc desde que foi ligado pela última vez
def get_uptime():
    boot_timestamp = psutil.boot_time()

    boot_datetime = datetime.fromtimestamp(boot_timestamp)

    current_datetime = datetime.now()

    uptime = current_datetime - boot_datetime

    return uptime

# Aqui formata a data e a hora antes de exibir
def format_uptime(uptime):
    total_seconds = int(uptime.total_seconds())

    days, remainder = divmod(total_seconds, 86400)

    hours, remainder = divmod(remainder, 3600)

    minutes, seconds = divmod(remainder, 60)

    return f"{days:02}d {hours:02}h {minutes:02}m"

