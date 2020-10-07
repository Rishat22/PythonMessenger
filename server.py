import socket, time

ENCODING_FORMAT = "utf-8"

host = socket.gethostbyname(socket.gethostname())

port = 9090

clients = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((host, port))

quit_server = False
print("[ Server Started ]")

while not quit_server:
    try:
        data, addr = server_socket.recvfrom(1024)

        if addr not in clients:
            clients.append(addr)

        current_time = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())

        print("[{0}]=[{1}]=[{2}]/".format(addr[0], str(addr[1]), current_time), end="")
        print(data.decode(ENCODING_FORMAT))

        for client in clients:
            if addr != client:
                server_socket.sendto(data, client)
    except:
        print("[ Server Stopped ]")
        quit_server = True

server_socket.close()
