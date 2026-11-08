
from rich.console import Console
from rich.table import Table

from monitoring.collector import (
    collect_hardware,
    collect_network,
    collect_processes,
    collect_system
)
from utils.formatters import format_bytes

import sys

sys.stdout.reconfigure(encoding="utf-8")

console = Console()


# ==============================
# FUNÇÕES DE EXIBIÇÃO
# ==============================


def get_menu_options():
    return [
        "[1] - Hardware",
        "[2] - Rede",
        "[3] - Processos",
        "[4] - Sistema",
        "[5] - Monitoramento completo",
        "[0] - Sair"
    ]

def show_menu():
    console.print("\n[bold cyan]===== INFRA TOOLS =====[/bold cyan]")
    for option in get_menu_options():
        console.print(option)


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

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

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

