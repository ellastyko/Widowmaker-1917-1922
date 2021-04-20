import socket
from threading import Thread
from config import *

class Online():
    __PORT__ = 9090
    __ADDR__ = 'localhost'

    def __init__(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.__ADDR__, self.__PORT__)) # Устанавливаем соеденение с сервером
            listen_Theard = Thread(target=self.__listen)
            listen_Theard.start()
            self.send('hello')
        except Exception:
            print(f'Server is not responding {Exception}')
        
        
    
    def __listen(self):
        while True:
            data = self.client.recv(1024)
            print(data.decode('utf-8'))
    
    def send(self, request):
        try: 
            self.client.send(request.encode('utf-8'))
        except Exception:
            print(f'Connection lost: {Exception}')



