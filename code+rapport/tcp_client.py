import socket
 
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5000))
    print('Connected to TCP server.')
 
    while True:
        msg = input('You: ')
        client.sendall(msg.encode('utf-8'))
        if msg.lower() == 'exit':
            break
        response = client.recv(1024).decode('utf-8')
        print(f'Server: {response}')
        if response.lower() == 'exit':
            break
 
    client.close()
 
if __name__ == '__main__':
    main()