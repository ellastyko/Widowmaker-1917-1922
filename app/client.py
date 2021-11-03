from config import *
import socket
from app.audio import Audio
from threading import Thread

class Client():
    __PORT__ = 9090
    __ADDR__ = 'localhost'

    def __init__(self):
        try:
            # Устанавливаем соеденение с сервером
            self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__client.connect((self.__ADDR__, self.__PORT__)) 
            listen_Theard = Thread(target=self.listen)
            listen_Theard.start()

            self.audio = Audio(client=self.__client, status=1)
        except Exception as e:
            print(f'Server is not responding {e}')
    
    @property
    def client(self):
        return self.__client

    
    def listen(self):
        while True:
            data = self.__client.recv(1024)
            self.audio.hear(data)
            #print(data) #.decode('utf-8')
    
    def send(self, request):
        try: 
            self.__client.send(request) #.encode('utf-8')
        except Exception as e:
            print(f'Connection lost: {e}')



