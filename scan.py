from socket import socket, AF_INET, SOCK_STREAM


def scanTarget(host, port):
    try:
        connection = socket(AF_INET, SOCK_STREAM)
        connection.settimeout(0.2)
        data = connection.connect_ex((host, port))
        if data == 0:
            print(f"[{port}] - open")
        connection.close()
    except:
        print(f'[{port}] - closed')
