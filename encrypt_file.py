from cryptography.fernet import Fernet

# Load the key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Encrypt a file
file_path = "example.txt"  # File you want to encrypt

with open(file_path, "rb") as file:
    original_data = file.read()

encrypted_data = fernet.encrypt(original_data)

with open("example_encrypted.txt", "wb") as enc_file:
    enc_file.write(encrypted_data)

print("File encrypted successfully!")
