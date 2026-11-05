import psutil

def get_cpu_info():
    cpu_info = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "cpu_freq": psutil.cpu_freq().current,
        "cpu_cores": psutil.cpu_percent(interval=None, percpu=True),
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True)
    }

    return cpu_info

def get_memory_info():
    memory = psutil.virtual_memory()

    memory_info = {
        "memory_quantity": memory.total,
        "used_memory": memory.used,
        "available_memory": memory.available,
        "memory_percent": memory.percent
    }

    return memory_info

def get_disk_info():
    disk_info = []
    partitions = psutil.disk_partitions()

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)

        partition_info = {
            "device": partition.device,
            "mountpoint": partition.mountpoint,
            "filesystem": partition.fstype,
            "total": usage.total,
            "used": usage.used,
            "free": usage.free,
            "percent": usage.percent
        }

        disk_info.append(partition_info)

    return disk_info