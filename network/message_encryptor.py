from cryptography.fernet import Fernet
import settings


class MessageEncryptor(object):

    def __init__(self, key):
        self.key = key
        self.fernet = Fernet(self.key)

    def encrypt(self, message):
        if message.find(" :: ") == -1:
            return message
        message_list = message.split(" :: ", 1)
        encrypt_message = self.fernet.encrypt(message_list[1].encode(settings.ENCODING_FORMAT))
        encrypt_message = "{0} :: {1}".format(message_list[0], encrypt_message.decode(settings.ENCODING_FORMAT))
        return encrypt_message

    def decrypt(self, message):
        if message.find(" :: ") == -1:
            return message
        message_list = message.split(" :: ", 1)
        decrypted_message = self.fernet.decrypt(message_list[1].encode())
        decrypted_message = "{0} :: {1}".format(message_list[0], decrypted_message.decode(settings.ENCODING_FORMAT))
        return decrypted_message
