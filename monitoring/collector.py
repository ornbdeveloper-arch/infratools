'''
Essa foi minha primeira experiência aqui sobre como remover funções da main que não precisam estar lá
'''

from modules.hardware import (
    get_cpu_info,
    get_memory_info,
    get_disk_info
)
from modules.system import get_system_info
from modules.network import get_network_info
from modules.processes import get_processes_info


"""
collect_hardware ficou diferente porque o dicionário não estava formatado na função de origem, já que no hardware.py os dados estão salvos em três funções distintas
"""
def collect_hardware():
    hardware_monitoring = {
    "cpu": get_cpu_info(),
    "ram": get_memory_info(),
    "disk": get_disk_info()
    }
    return hardware_monitoring


def collect_system():
    return get_system_info()

def collect_network():
    return get_network_info()

def collect_processes():
    return get_processes_info()
    

