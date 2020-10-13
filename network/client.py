import socket, threading, time
import settings
from message_encryptor import MessageEncryptor


class ClientTransceiver:
    def __init__(self):
        self.key = '5ItEZTzP1Ij_vXaugBo7jftzOG7iYYe4XYDR8pl1U6o='
        self.shutdown = False
        self.join = False
        self.message_encryptor = MessageEncryptor(self.key)

    def __receiving(self, name, sock):
        while not self.shutdown:
            try:
                while True:
                    data, addr = sock.recvfrom(1024)
                    data = data.decode(settings.ENCODING_FORMAT)
                    decrypted_text = self.message_encryptor.decrypt(data)
                    print(decrypted_text)
            except:
                pass

    def start(self, nickname):
        host = socket.gethostbyname(socket.gethostname())
        port = 0
        server = (settings.SERVER_ADDRESS, settings.SERVER_PORT)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.bind((host, port))
        client_socket.setblocking(0)

        receiving_thread = threading.Thread(target=self.__receiving, args=("RecvThread", client_socket))
        receiving_thread.start()

        while not self.shutdown:
            if not self.join:
                client_socket.sendto(("[{0}] => join chat".format(nickname)).encode(settings.ENCODING_FORMAT),
                                     server)
                self.join = True
            else:
                try:
                    message = input()
                    if message != "":
                        message = "[{0}] :: {1}".format(nickname, message)
                        encrypted_text = self.message_encryptor.encrypt(message)
                        client_socket.sendto(encrypted_text.encode(settings.ENCODING_FORMAT), server)
                except:
                    client_socket.sendto(("[{0}] => left chat".format(nickname)).encode(settings.ENCODING_FORMAT),
                                         server)
        receiving_thread.join()
        client_socket.close()


client = ClientTransceiver()
nickname = input("Name: ")
client.start(nickname)