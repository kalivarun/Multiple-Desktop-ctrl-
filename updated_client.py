import socket
import threading
import pyautogui as pi
import os
import platform
import webbrowser

# Client setup
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.208.30.29', 5000))

def receive_messages():
    while True:
        try:
            data = client.recv(1024)
            if not data:
                break
            decoded_data = data.decode('utf-8')
            print(f"Received: {decoded_data}")

            parts = decoded_data.split()
            command = parts[0]
            key = ' '.join(parts[1:])

            if command == 'MOVE_UP':
                pi.move(0, -10)  # Move mouse cursor up by 10 pixels
            elif command == 'MOVE_DOWN':
                pi.move(0, 10)  # Move mouse cursor down by 10 pixels
            elif command == 'MOVE_LEFT':
                pi.move(-10, 0)  # Move mouse cursor left by 10 pixels
            elif command == 'MOVE_RIGHT':
                pi.move(10, 0)  # Move mouse cursor right by 10 pixels
            elif command == 'LEFT_CLICK':
                pi.click()  # Perform left-click
            elif command == 'RIGHT_CLICK':
                pi.click(button='right')  # Perform right-click
            elif command == 'SHUTDOWN':
                if platform.system() == "Windows":
                    os.system("shutdown /s /t 1")  # Shutdown Windows
                elif platform.system() == "Linux":
                    os.system("poweroff")  # Shutdown Linux
            elif command == 'RESTART':
                if platform.system() == "Windows":
                    os.system("shutdown /r /t 1")  # Restart Windows
                elif platform.system() == "Linux":
                    os.system("reboot")  # Restart Linux
            elif command == 'LOCK_SCREEN':
                if platform.system() == "Windows":
                    os.system("rundll32.exe user32.dll,LockWorkStation")  # Lock screen on Windows
                elif platform.system() == "Linux":
                    os.system("gnome-screensaver-command -l")  # Lock screen on Linux
            elif command.startswith('KEY_PRESS'):
                pi.press(key.lower())  # Press the specified key
            elif command.startswith('BUTTON_PRESS'):
                if key == 'GO':
                    pi.press('up')
                elif key == 'STOP':
                    pi.press('down')
                elif key == 'ESC':
                    pi.press('esc')
                elif key == 'SHIFT':
                    pi.press('shift')
                elif key == 'LEFT':
                    pi.press('left')
                elif key == 'RIGHT':
                    pi.press('right')
                elif key == 'SPACE':
                    pi.press('space')
            elif command.startswith('http'):  # Check if it's a URL
                webbrowser.open(command)  # Open URL in the default browser
                
        except Exception as e:
            print(f"Error: {e}")
            break

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    pass  # Keep the client running
