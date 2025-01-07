import requests

def encrypt(text, n, m):
    encrypted_text = ""
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                shift = n * m
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            elif 'n' <= char <= 'z':
                shift = -(n + m)
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                encrypted_text += char
        elif char.isupper():
            if 'A' <= char <= 'M':
                shift = -n
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            elif 'N' <= char <= 'Z':
                shift = m**2
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, n, m):
    decrypted_text = ""
    for char in text:
        if char.islower():
            if 'a' <= char <= 'm':
                shift = -(n * m)
                decrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            elif 'n' <= char <= 'z':
                shift = n + m
                decrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                decrypted_text += char
        elif char.isupper():
            if 'A' <= char <= 'M':
                shift = n
                decrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            elif 'N' <= char <= 'Z':
                shift = -(m**2)
                decrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                decrypted_text += char
        else:
            decrypted_text += char
    return decrypted_text

def verify_decryption(original, decrypted):
    return original == decrypted

# Pull Raw Text file from Github. Siam please ensure the file path is correct
github_url = "https://raw.githubusercontent.com/Aubid111/HIT-137-Assignment-02-HIT-137-Assignment-02/main/raw_text.txt"

# Encryption and decryption process
try:
    # Download raw text from GitHub
    response = requests.get(github_url)
    response.raise_for_status()  # Raise an error for failed requests
    raw_text = response.text

    # User to put the required parameters for the encrypption
    n = int(input("Enter value for n: "))
    m = int(input("Enter value for m: "))

    # Encrypt the text
    encrypted_text = encrypt(raw_text, n, m)

    # Write the encrypted text to a file as required and then save it. 
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

    # Decrypt the text
    decrypted_text = decrypt(encrypted_text, n, m)

    # Verify if the decryption matches the original text or not. 
    if verify_decryption(raw_text, decrypted_text):
        print("Decryption verification successful: The decrypted text matches the original text.")
    else:
        print("Decryption verification failed: The decrypted text does not match the original text.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching file from GitHub: {e}")
except FileNotFoundError as e:
    print(f"Error: {e}")
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
