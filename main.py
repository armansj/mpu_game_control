import socket
from datetime import time
import pydirectinput

HOST = "192.168.0.120"
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Connected to Pico W")

try:
    while True:
        data = client.recv(1024).decode()
        if not data:
            break

        print(f"Received: {data}")

        if data == "LEFT":
            pydirectinput.keyDown('left')
            time.sleep(0.1)
            pydirectinput.keyUp('left')
        elif data == "RIGHT":
            pydirectinput.keyDown('right')
            time.sleep(0.1)
            pydirectinput.keyUp('right')

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    client.close()
