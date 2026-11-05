from rich.console import Console
from rich.table import Table
import sys
from modules.hardware import (
    get_cpu_info,
    get_memory_info,
    get_disk_info
)
from modules.system import (
    get_system_info,
    get_uptime
)
from modules.network import get_network_info

sys.stdout.reconfigure(encoding="utf-8")

cpu = get_cpu_info()
memory = get_memory_info()
disks = get_disk_info()
system = get_system_info()
uptime = get_uptime()
network = get_network_info()

console = Console()

def format_bytes(size):
    gib = size / (1024 ** 3)
    return f"{gib:.2f} GiB"


# Tabela do processador
cpu_table = Table(title="InfraTools | CPU")

cpu_table.add_column("Indicador", style="cyan")
cpu_table.add_column("Valor", style="green")

cpu_table.add_row("Uso da CPU", f"{cpu['cpu_usage']}%")
cpu_table.add_row("Frequência", f"{cpu['cpu_freq']}MHz")
cpu_table.add_row("Núcleos Físicos", f"{cpu['physical_cores']}")
cpu_table.add_row("Núcleos Lógicos", f"{cpu['logical_cores']}")
console.print(cpu_table)

# Tabela da memória RAM
ram_table = Table(title="InfraTools | RAM")

ram_table.add_column("Indicador", style="cyan")
ram_table.add_column("Valor", style="green")

ram_table.add_row("Quantidade de memória", format_bytes(memory['memory_quantity']))
ram_table.add_row("Quantidade em uso", format_bytes(memory['used_memory']))
ram_table.add_row("Quantidade disponível", format_bytes(memory['available_memory']))
ram_table.add_row("Porcentagem de uso", f"{memory['memory_percent']}%")
console.print(ram_table)

# Tabela de armazenamento
disk_table = Table(title="InfraTools | Armazenamento")

disk_table.add_column("Indicador", style="cyan")
disk_table.add_column("Valor", style="green")

for disk in disks:
    disk_table.add_row("Unidade", f"{disk['device']}")
    disk_table.add_row("Ponto de modelagem", f"{disk['mountpoint']}")
    disk_table.add_row("Sistema de arquivos", f"{disk['filesystem']}")
    disk_table.add_row("Capacidade total", format_bytes(disk['total']))
    disk_table.add_row("Espaço utilizado", format_bytes(disk['used']))
    disk_table.add_row("Disponível", format_bytes(disk['free']))
    disk_table.add_row("Usitlização", f"{disk['percent']}%")

console.print(disk_table)


# Tabela de informações do sistema
system_table = Table(title="InfraTools | Informações do Sistema")

system_table.add_column("Indicador", style="cyan")
system_table.add_column("Valor", style="green")

system_table.add_row("Hostname", f"{system['hostname']}")
system_table.add_row("Sistema Operacional", f"{system['operating_system']}")
system_table.add_row("Versão do sistema", f"{system['os_version']}")
system_table.add_row("Arquitetura", f"{system['architecture']}")
system_table.add_row("Username", f"{system['username']}")
system_table.add_row("Tempo ligado", f"{system['uptime']}")
console.print(system_table)


# Tabela de internet
network_table = Table(title="InfraTools | Rede")

network_table.add_column("Interface", style="cyan")
network_table.add_column("Status", style="green")
network_table.add_column("Velocidade", style="yellow")
network_table.add_column("MTU")
network_table.add_column("IPv4")
network_table.add_column("IPv6")
network_table.add_column("MAC")

for interface, info in network.items():
    network_table.add_row(
        interface,
        info["status"],
        f"{info['speed']} Mbps",
        str(info["mtu"]),
        info["ipv4"] or "-",
        info["ipv6"] or "-",
        info["mac"] or "-"
    )

console.print(network_table)













exit = input("Pressione qualquer tecla para sair")



