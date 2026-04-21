import socket
 
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ('127.0.0.1', 5000)
 
    while True:
        msg = input('You: ')
        client.sendto(msg.encode('utf-8'), addr)
        if msg.lower() == 'exit':
            break
        response, _ = client.recvfrom(1024)
        print(f'Server: {response.decode("utf-8")}')
        if response.decode('utf-8').lower() == 'exit':
            break
 
    client.close()
 
if __name__ == '__main__':
    main()
