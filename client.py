import socket, threading, time
from Crypto.Cipher import DES

ENCODING_FORMAT = "utf-8"
SERVER_PORT = 9090
SERVER_ADDRESS = "192.168.0.101"

key = b'abcdefgh'
shutdown = False
join = False


def fill_multiple_eight(text):
    while len(text) % 8 != 0:
        text += b' '
    return text


def receiving(name, sock):
    while not shutdown:
        try:
            while True:
                data, addr = sock.recvfrom(1024)
                data = data.decode(ENCODING_FORMAT)
                des = DES.new(key, DES.MODE_ECB)
                decrypted_text = des.decrypt(data)
                print(decrypted_text)
        except:
            pass


host = socket.gethostbyname(socket.gethostname())
port = 0
server = (SERVER_ADDRESS, SERVER_PORT)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind((host, port))
client_socket.setblocking(0)

alias = input("Name: ")
receiving_thread = threading.Thread(target=receiving, args=("RecvThread", client_socket))
receiving_thread.start()
