import socket
import threading

class Server():

        users = []

        def __init__(self):
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
            self.server.bind(('', 9090))
            self.server.listen(10)
            
            print("Server listen...")
            self.accept_sockets()
            



        def __send(self, data):
            for user in self.users:
                user.send(data)


        def __listening(self, listened_socket):
            print("Listening user...\n")
            while True:
                data = listened_socket.recv(1024)
                # print(f"User sent {data}")
                self.__send(data)


        def accept_sockets(self):
            while True:
                client_socket, client_address = self.server.accept()
                print('Connected by', client_address)
                self.users.append(client_socket)
                listen_accepted_user = threading.Thread(target=self.__listening, args=(client_socket,))
                listen_accepted_user.start()


if __name__ == '__main__':
    Server()