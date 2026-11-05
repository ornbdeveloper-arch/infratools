import psutil
import socket

def get_network_info():
    network_info = {}

    network_interfaces = psutil.net_if_addrs()
    network_status = psutil.net_if_stats()

    for interface, addresses in network_interfaces.items():

        stats = network_status.get(interface)

        interface_info = {
            "status": "Ativa" if stats and stats.isup else "Inativa",
            "speed": stats.speed if stats else 0,
            "mtu": stats.mtu if stats else 0,
            "mac": None,
            "ipv4": None,
            "netmask": None,
            "ipv6": None
        }

        for address in addresses:

            if address.family == socket.AF_INET:
                interface_info["ipv4"] = address.address
                interface_info["netmask"] = address.netmask

            elif address.family == socket.AF_INET6:
                interface_info["ipv6"] = address.address

            elif address.family == psutil.AF_LINK:
                interface_info["mac"] = address.address

        network_info[interface] = interface_info
    return network_info












'''
import psutil
import socket

network_status = psutil.net_if_stats()
network_interfaces = psutil.net_if_addrs()

for interface, adresses in network_interfaces.items():
    print(f"\nInterface: {interface}")
    if network_status[interface].isup:
        print("Estado: Ativo")
    else:
        print("Estado: Inativo")

    print(f"Velocidade reportada: {network_status[interface].speed}Mbps")
    print(f"MTU {network_status[interface].mtu}")

    for adress in adresses:
        
        if adress.family == socket.AF_INET:
            print(f"IPv4: {adress.address}")
        elif adress.family == socket.AF_INET6:
            print(f"IPv6: {adress.address}")
        elif adress.family == socket.AF_LINK:
            print(f"MAC: {adress.address}")





'''