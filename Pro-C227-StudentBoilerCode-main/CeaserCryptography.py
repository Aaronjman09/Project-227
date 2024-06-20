
print("Welcome to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("encrypting...")
    message = input("Please type a message to encrypt : ")
    key = int(input("Type an encryption key (1 - 94) : "))
    if (key < 1 or key > 94):
        print("Wrong Key")
    else:
            encrypted_text = ""
            for i in range(len(message)):
                temp = (ord(message[i]) + key)
                if (temp > 126):
                    temp = temp - 127 + 32
                encrypted_text += chr(temp)
            print("Encrypted Text : ", encrypted_text)


    


def decryption():
    print("decryption...")
    message = input("Enter encrypted text : ")
    key = int(input("Type the encryption key you used to encrypt the message to decrypt (1 - 94) : "))
    if (key < 1 or key > 94):
        print("Wrong Key")
    else:
        decrypted_text = ""
        for i in range(len(message)):
            temp = (ord(message[i]) - key)
            if (temp < 32):
                temp = temp + 127 - 32
            decrypted_text += chr(temp)
        print("Decrypted Text : ", decrypted_text)



    
    

        
if __name__ == "__main__":
    main()
