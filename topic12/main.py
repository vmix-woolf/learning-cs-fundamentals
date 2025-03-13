import threading
from aa_server_socket import echo_server
from aa_client_socket import simple_client


HOST = '127.0.0.1'
PORT = 9090

server = threading.Thread(target=echo_server, args=(HOST, PORT))
client = threading.Thread(target=simple_client, args=(HOST, PORT))

server.start()
client.start()
server.join()
client.join()
print('Done!')
