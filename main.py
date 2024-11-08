import socket
import platform
import os

def get_system_info():
    # Obter hostname
    hostname = socket.gethostname()

    # Obter IP de rede
    ip_address = socket.gethostbyname_ex(hostname)[-1][0]

    # Obter versão do sistema operacional
    os_release = platform.platform()

    return {
        "Hostname": hostname,
        "IP Address": ip_address,
        "OS Release": os_release
    }

if __name__ == "__main__":
    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"{key}: {value}")
