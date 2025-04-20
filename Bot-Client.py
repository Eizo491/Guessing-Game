import socket

HOST = '193.168.1.16'
PORT = 12345
PASSWORD = "secretpass"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        message = client.recv(1024).decode()
        print(message, end='')

        if "password" in message:
            client.sendall(PASSWORD.encode())
        elif "Guess a number" in message:
            # Bot's binary search algorithm
            global low, high, guess
            guess = (low + high) // 2
            print(f"Bot guesses: {guess}")
            client.sendall(str(guess).encode())
        elif "Higher" in message:
            low = guess + 1
        elif "Lower" in message:
            high = guess - 1
        elif "Correct!" in message or "closed" in message:
            break

    client.close()

if __name__ == "__main__":
    low = 1
    high = 100
    guess = 50
    main()
