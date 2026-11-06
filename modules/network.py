import psutil
import socket
from scapy.config import conf


def get_gateway():
    try:
        route = conf.route.route("0.0.0.0")
        return route[2]
    except Exception as error:
        print(f"Erro ao consultar gateway: {error}")
        return None


def get_network_info():
    network_info = {
        "gateway": get_gateway(),
        "interfaces": {}
    }

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
            "ipv6": None,
        }

        for address in addresses:

            if address.family == socket.AF_INET:
                interface_info["ipv4"] = address.address
                interface_info["netmask"] = address.netmask

            elif address.family == socket.AF_INET6:
                interface_info["ipv6"] = address.address

            elif address.family == psutil.AF_LINK:
                interface_info["mac"] = address.address

        network_info["interfaces"][interface] = interface_info

    return network_info