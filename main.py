
from rich.console import Console
from rich.table import Table

from monitoring.collector import (
    collect_hardware,
    collect_network,
    collect_processes,
    collect_system
)

import sys

sys.stdout.reconfigure(encoding="utf-8")

console = Console()


# ==============================
# FUNÇÕES DE EXIBIÇÃO
# ==============================

def format_bytes(size):
    if size >= 1024 ** 3:
        gib = size / (1024 ** 3)
        return f"{gib:.2f} GiB"
    elif size >= 1024 ** 2:
        mib = size /(1024 ** 2)
        return f"{mib:.2f} MiB"
    elif size >= 1024:
        kib = size / 1024
        return f"{kib:.2f} KiB"
    else:
        return f"{size:.2f} B" 


def show_menu():
    console.print("\n[bold cyan]===== INFRA TOOLS =====[/bold cyan]")
    console.print("[1] - Hardware")
    console.print("[2] - Rede")
    console.print("[3] - Processos")
    console.print("[4] - Sistema")
    console.print("[5] - Monitoramento completo")
    console.print("[0] - Sair")


def show_hardware():
    hardware = collect_hardware()

    cpu = hardware["cpu"]
    ram = hardware["ram"]
    disks = hardware["disk"]

    # CPU
    table = Table(title="Informações da CPU")
    table.add_column("Indicador")
    table.add_column("Valor")

    table.add_row("Modelo", cpu["model"])
    table.add_row("Uso", f'{cpu["cpu_usage"]}%')
    table.add_row("Frequência", f'{cpu["cpu_freq"]:.2f} MHz')
    table.add_row("Núcleos físicos", str(cpu["physical_cores"]))
    table.add_row("Núcleos lógicos", str(cpu["logical_cores"]))

    console.print(table)

    # RAM
    table = Table(title="Memória RAM")
    table.add_column("Indicador")
    table.add_column("Valor")

    table.add_row("Total", format_bytes(ram["memory_quantity"]))
    table.add_row("Usada", format_bytes(ram["used_memory"]))
    table.add_row("Disponível", format_bytes(ram["available_memory"]))
    table.add_row("Uso", f'{ram["memory_percent"]}%')

    console.print(table)

    # Discos
    table = Table(title="Armazenamento")
    table.add_column("Dispositivo")
    table.add_column("Montagem")
    table.add_column("Sistema de arquivos")
    table.add_column("Total")
    table.add_column("Usado")
    table.add_column("Livre")
    table.add_column("Uso")

    for disk in disks:
        table.add_row(
            disk["device"],
            disk["mountpoint"],
            disk["filesystem"],
            format_bytes(disk["total"]),
            format_bytes(disk["used"]),
            format_bytes(disk["free"]),
            f'{disk["percent"]}%'
        )

    console.print(table)


def show_network():
    network = collect_network()

    table = Table(title="Interfaces de Rede")
    table.add_column("Interface")
    table.add_column("Status")
    table.add_column("Velocidade")
    table.add_column("MTU")
    table.add_column("IPv4")
    table.add_column("IPv6")
    table.add_column("MAC")

    for interface, info in network["interfaces"].items():
        table.add_row(
            interface,
            str(info["status"]),
            str(info["speed"]),
            str(info["mtu"]),
            info["ipv4"] or "-",
            info["ipv6"] or "-",
            info["mac"] or "-"
        )

    console.print(table)

    gateway_table = Table(title="Gateway")
    gateway_table.add_column("Indicador")
    gateway_table.add_column("Valor")

    gateway_table.add_row("Gateway padrão", str(network["gateway"]))

    console.print(gateway_table)


def show_processes():
    processes = collect_processes()

    table = Table(title="Processos em execução")
    table.add_column("PID")
    table.add_column("Processo")
    table.add_column("Usuário")

    for process in processes:
        table.add_row(
            str(process["ID"]),
            str(process["name"]),
            str(process["username"])
        )

    console.print(table)


def show_system():
    system = collect_system()

    table = Table(title="Informações do Sistema")
    table.add_column("Indicador")
    table.add_column("Valor")

    table.add_row("Hostname", system["hostname"])
    table.add_row("Sistema operacional", system["operating_system"])
    table.add_row("Versão", system["os_version"])
    table.add_row("Arquitetura", system["architecture"])
    table.add_row("Usuário", system["username"])
    table.add_row("Uptime", system["uptime"])

    console.print(table)


def show_monitoring():
    processes = collect_processes()

    console.print("\n[bold green]===== MONITORAMENTO COMPLETO =====[/bold green]")
    show_hardware()
    show_network()
    show_system()
    console.print(f"Processos em execução: {len(processes)}")


'''
Aqui o menu é ativado, mais um bom costume aplicado dentro do main
'''

def main():

    while True:

        show_menu()

        option = input("\nSelecione uma opção: ")

        if option == "1":
            show_hardware()

        elif option == "2":
            show_network()

        elif option == "3":
            show_processes()

        elif option == "4":
            show_system()

        elif option == "5":
            show_monitoring()

        elif option == "0":
            console.print("[yellow]Encerrando InfraTools...[/yellow]")
            break

        else:
            console.print("[red]Opção inválida![/red]")


if __name__ == "__main__":
    main()

'''
Por hora ainda mantenho as versões antigas do main aqui abaixo, mas por motivos de estudo e validação de informação, em etapas futuras vou remover essa seção e deixar o arquivo mais limpo
'''


"""
from monitoring.collector import (
    collect_hardware,
    collect_network,
    collect_processes,
    collect_system
)
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
from modules.processes import get_processes_info


sys.stdout.reconfigure(encoding="utf-8")

console = Console()


def format_bytes(size):
    gib = size / (1024 ** 3)
    return f"{gib:.2f} GiB"


def show_menu():
    print("=" * 50)
    print(
        "Selecione uma opção\n"
        "[1] - Hardware\n"
        "[2] - Rede\n"
        "[3] - Processos\n"
        "[4] - Sistema\n"
        "[5] - Monitoramento\n"
        "[0] - Sair"
    )
    print("=" * 50)


while True:
    show_menu()

    option = input("")

    if option == "1":
        cpu = get_cpu_info()
        memory = get_memory_info()
        disks = get_disk_info()

        # Tabela do processador
        cpu_table = Table(title="InfraTools | CPU")

        cpu_table.add_column("Indicador", style="cyan")
        cpu_table.add_column("Valor", style="green")

        cpu_table.add_row("Uso da CPU", f"{cpu['cpu_usage']}%")
        cpu_table.add_row("Frequência", f"{cpu['cpu_freq']}MHz")
        cpu_table.add_row("Núcleos Físicos", f"{cpu['physical_cores']}")
        cpu_table.add_row("Núcleos Lógicos", f"{cpu['logical_cores']}")
        cpu_table.add_row("Modelo", f"{cpu['model']}")

        console.print(cpu_table)

        # Tabela da memória RAM
        ram_table = Table(title="InfraTools | RAM")

        ram_table.add_column("Indicador", style="cyan")
        ram_table.add_column("Valor", style="green")

        ram_table.add_row(
            "Quantidade de memória",
            format_bytes(memory['memory_quantity'])
        )
        ram_table.add_row(
            "Quantidade em uso",
            format_bytes(memory['used_memory'])
        )
        ram_table.add_row(
            "Quantidade disponível",
            format_bytes(memory['available_memory'])
        )
        ram_table.add_row(
            "Porcentagem de uso",
            f"{memory['memory_percent']}%"
        )

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

    elif option == "2":
        # Tabela de rede
        network = get_network_info()

        network_table = Table(title="InfraTools | Rede")

        network_table.add_column("Interface", style="cyan")
        network_table.add_column("Status", style="green")
        network_table.add_column("Velocidade", style="yellow")
        network_table.add_column("MTU")
        network_table.add_column("IPv4")
        network_table.add_column("IPv6")
        network_table.add_column("MAC")

        for interface, info in network["interfaces"].items():
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

        gateway_table = Table(title="InfraTools | Roteamento")

        gateway_table.add_column("Indicador", style="cyan")
        gateway_table.add_column("Valor", style="green")

        gateway_table.add_row(
            "Gateway padrão",
            str(network["gateway"] or "-")
        )

        console.print(gateway_table)

    elif option == "3":
        #Tabela de processos
        processes = get_processes_info()

        processes_table = Table(title="InfraTools | Processos")

        processes_table.add_column("ID", style="cyan")
        processes_table.add_column("Nome", style="green")
        processes_table.add_column("Usuário", style="green")

        for process in processes:
            processes_table.add_row(
                str(process['ID']),
                process['name'] or "-",
                process['username'] or "-"
            )

        console.print(processes_table)

    elif option == "4":
        # Tabela de sistema
        system = get_system_info()
        uptime = get_uptime()

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

    elif option == "5":
        monitoring = collect_hardware(), collect_system(), collect_network(), collect_processes()
        console.print(monitoring)

    elif option == "0":
        break

    else:
        print("Opção inválida, tente novamente.")
"""


'''
Nessa etapa aqui eu decidi criar um menu, pois se tudo executar junto vai ser uma tela cheia de informação, são muitos processos e só essa tabela já ocuparia a tela sozinha.


# Tabela do processador
cpu_table = Table(title="InfraTools | CPU")

cpu_table.add_column("Indicador", style="cyan")
cpu_table.add_column("Valor", style="green")

cpu_table.add_row("Uso da CPU", f"{cpu['cpu_usage']}%")
cpu_table.add_row("Frequência", f"{cpu['cpu_freq']}MHz")
cpu_table.add_row("Núcleos Físicos", f"{cpu['physical_cores']}")
cpu_table.add_row("Núcleos Lógicos", f"{cpu['logical_cores']}")
cpu_table.add_row("Modelo", f"{cpu['model']}")
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


# Tabela de internet e tabela gateway

gateway_table = Table(title="InfraTools | Roteamento")

gateway_table.add_column("Indicador", style="cyan")
gateway_table.add_column("Valor", style="green")

gateway_table.add_row(
    "Gateway padrão",
    str(network["gateway"] or "-")
)
console.print(gateway_table)

network_table = Table(title="InfraTools | Rede")

network_table.add_column("Interface", style="cyan")
network_table.add_column("Status", style="green")
network_table.add_column("Velocidade", style="yellow")
network_table.add_column("MTU")
network_table.add_column("IPv4")
network_table.add_column("IPv6")
network_table.add_column("MAC")

for interface, info in network["interfaces"].items():
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


processes_table = Table(title="InfraTools | Processos")
processes_table.add_column("ID", style="cyan")
processes_table.add_column("Nome", style="green")
processes_table.add_column("Usuário", style="green")

for process in processes:
    processes_table.add_row(
        str(process['ID']),
        process['name'] or "-",
        process['username'] or "-"
    )

console.print(processes_table)

'''

