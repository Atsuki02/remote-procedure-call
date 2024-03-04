import socket
import os
import json

class MySocket:

    # initialize
    def __init__(self, service):
        self.sock = None
        self.server_address = '/tmp/udp_socket_file'
        self.create_socket()
        self.unlink_socket()
        self.service = service


    # create socket
    def create_socket(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)


    # delete the existing path
    def unlink_socket(self):
        try:
            os.unlink(self.server_address)
        except FileNotFoundError:
            pass

    # bind the path to the socket
    def bind_socket(self):
        self.sock.bind(self.server_address)


    # ask and wait for the connection
    def listen_connection(self):
        self.sock.listen(1)
        print('\nwaiting to receive message')

        # return connection when accepting the client
        connection, _ = self.sock.accept()
        try:
            while True:
                # receive data
                data = connection.recv(4096)
                print('received {} bytes'.format(len(data)))
                if data:
                    # analyze request and return response
                    request = json.loads(data.decode('utf-8'))
                    method = request['method']
                    params = request['params']
                    result = self.service.call_method(method, *params)
                    response = json.dumps(result).encode('utf-8')
                    connection.sendall(response)
                else:
                    break
        finally:
            connection.close()



