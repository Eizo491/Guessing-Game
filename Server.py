import socket
import threading
import random

PASSWORD = "secretpass"
HOST = '0.0.0.0'
PORT = 12345

def handle_client(conn, addr):
    print(f"Connected by {addr}")

    # Password authentication
    conn.sendall(b"Enter password: ")
    password = conn.recv(1024).decode().strip()
    if password != PASSWORD:
        conn.sendall(b"Incorrect password. Connection closed.\n")
        conn.close()
        return
    
    conn.sendall(b"Password accepted. Let's start the game!\n")

    # Game logic
    number_to_guess = random.randint(1, 100)
    guess_count = 0

    while True:
        conn.sendall(b"Guess a number (1-100): ")
        guess = conn.recv(1024).decode().strip()
        guess_count += 1

        if not guess.isdigit():
            conn.sendall(b"Invalid input. Enter a number.\n")
            continue

        guess = int(guess)
        if guess < number_to_guess:
            conn.sendall(b"Higher\n")
        elif guess > number_to_guess:
            conn.sendall(b"Lower\n")
        else:
            # Performance rating
            if guess_count <= 5:
                rating = "Excellent"
            elif guess_count <= 20:
                rating = "Very Good"
            else:
                rating = "Good/Fair"
            conn.sendall(f"Correct! You took {guess_count} guesses. Performance: {rating}\n".encode())
            break

    conn.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server listening on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

if __name__ == "__main__":
    main()
