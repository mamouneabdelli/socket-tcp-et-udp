import socket
 
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('localhost', 5000))
    print('UDP Server listening on port 5000...')
 
    while True:
        data, addr = server.recvfrom(1024)
        msg = data.decode('utf-8')
        if msg.lower() == 'exit':
            print('Client disconnected.')
            break
        print(f'Client {addr}: {msg}')
        response = input('You: ')
        server.sendto(response.encode('utf-8'), addr)
        if response.lower() == 'exit':
            break
 
    server.close()
 
if __name__ == '__main__':
    main()
