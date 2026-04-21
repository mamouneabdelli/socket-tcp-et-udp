import socket
 
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 5000))
    server.listen(1)
    print('TCP Server listening on port 5000...')
 
    client, addr = server.accept()
    print(f'Client connected: {addr}')
 
    while True:
        data = client.recv(1024).decode('utf-8')
        if not data or data.lower() == 'exit':
            print('Client disconnected.')
            break
        print(f'Client: {data}')
        response = input('You: ')
        client.sendall(response.encode('utf-8'))
        if response.lower() == 'exit':
            break
 
    client.close()
    server.close()
 
if __name__ == '__main__':
    main()