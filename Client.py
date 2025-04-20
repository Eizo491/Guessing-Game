import socket

HOST = '193.168.1.16'
PORT = 12345

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        message = client.recv(1024).decode()
        print(message, end='')

        if "closed" in message or "Correct!" in message:
            break

        user_input = input()
        client.sendall(user_input.encode())

    client.close()

if __name__ == "__main__":
    main()

