import psutil

def get_processes_info():

    processes = []

    for process in psutil.process_iter(['pid', 'name', 'username']):
        try:
            username = process.info["username"] or "Desconhecido"

        except psutil.AccessDenied:
            username = "Acesso negado"

        except psutil.NoSuchProcess:
            continue

        processes_info = {
            "ID": process.info["pid"],
            "name": process.info["name"],
            "username": username
        }

        processes.append(processes_info)
          

        
    return processes




"""
Essa versão funciona, mas deu permissão negada ao buscar os processos, o código está otimizado para não impedir a execução, preferi manter aqui por fins de estudo


def get_processes_info():

    processes = []

    for process in psutil.process_iter(['pid', 'name', 'username']):
        try:
            process_info = {
                "ID": process.pid,
                "name": process.name(),
                "username": process.username()
            }
            processes.append(process_info)
        except psutil.AccessDenied:
            continue

        
    return processes


"""


"""

Esse aqui eu fiz de teste pra criar a função antes de implementar da forma correta

def get_processes_info():
    processes = []
    for process in psutil.process_iter(['pid', 'name', 'username']):
        processes.append(process)
    return processes

"""