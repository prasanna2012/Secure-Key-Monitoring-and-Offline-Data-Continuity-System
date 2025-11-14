from cryptography.fernet import Fernet

# Load the key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Decrypt a file
encrypted_file_path = "example_encrypted.txt"

with open(encrypted_file_path, "rb") as enc_file:
    encrypted_data = enc_file.read()

decrypted_data = fernet.decrypt(encrypted_data)

with open("example_decrypted.txt", "wb") as dec_file:
    dec_file.write(decrypted_data)

print("File decrypted successfully!")
