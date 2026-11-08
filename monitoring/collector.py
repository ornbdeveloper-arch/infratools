'''
Essa foi minha primeira experiência aqui sobre como remover funções da main que não precisam estar lá
'''

from modules.hardware import (
    get_cpu_info,
    get_memory_info,
    get_disk_info
)


'''
E essa função tá aqui pra só realizar a coleta quando for chamada, e o arquivo não ser executado sempre
'''

def collect_hardware():
    hardware_monitoring = {
    "cpu": get_cpu_info(),
    "ram": get_memory_info(),
    "disk": get_disk_info()
    }

    return hardware_monitoring


