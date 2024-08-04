def encrypt(text, shift):
    result = ""

    # Loop through each character in the input text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # Keep special characters unchanged
        else:
            result += char

    return result

def decrypt(text, shift):
    # Decrypting is just encrypting with the negative of the shift
    return encrypt(text, -shift)

def main():
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")
        return

    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (1-25): "))

    if choice == 'e':
        encrypted_text = encrypt(text, shift)
        print(f"Encrypted message: {encrypted_text}")
    elif choice == 'd':
        decrypted_text = decrypt(text, shift)
        print(f"Decrypted message: {decrypted_text}")

if __name__ == "_main_":
    main()