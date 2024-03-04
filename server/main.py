from my_socket import MySocket
from my_service import MyService

def main():
    # create service instance
    my_service = MyService()

    # inject service
    my_socket = MySocket(my_service)

    # bind socket
    my_socket.bind_socket()
    
    # listen connection
    my_socket.listen_connection()

# call main
if __name__ == "__main__":
    main()
