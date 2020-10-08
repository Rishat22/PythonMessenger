import socket, threading, time
from Crypto.Cipher import DES

# ToDo move to global parameters
ENCODING_FORMAT = "utf-8"
SERVER_PORT = 9090
SERVER_ADDRESS = "127.0.0.1"
# end

# ToDo move class parameters
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
                # ToDo move to encryption class
                data = data.split(" => ", 1)
                des = DES.new(key, DES.MODE_ECB)
                decrypted_text = des.decrypt(data[1])
                # end
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

while not shutdown:
    if not join:
        client_socket.sendto(("[{0}] => join chat".format(alias)).encode(ENCODING_FORMAT), server)
        join = True
    else:
        try:
            message = input().encode(ENCODING_FORMAT)
            # ToDo move to encryption class
            des = DES.new(key, DES.MODE_ECB)
            padded_message = fill_multiple_eight(message)
            encrypted_text = des.encrypt(padded_message)
            # end

            if message != "":
                client_socket.sendto(("[{0}] :: {1}".format(alias, encrypted_text)).encode(ENCODING_FORMAT), server)
        except:
            client_socket.sendto(("[{0}] => left chat".format(alias)).encode(ENCODING_FORMAT), server)
receiving_thread.join()
client_socket.close()
