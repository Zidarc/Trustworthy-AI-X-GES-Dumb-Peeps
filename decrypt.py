
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]



def decrypt_aes(encrypted_data, key):
    key = key[:32].ljust(32, b'\0')
    iv = encrypted_data[:16]  # Extract the IV
    encrypted_data = encrypted_data[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data)
    return unpad(decrypted_data)


def read_binary_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def write_binary_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)



# Example usage
key = b'functionremainsunchangedasitwillcorrectly'  # Your encryption key
input_file_path = 'train.zip'  # Path to the input binary file
encrypted_file_path = 'train.bin'  # Path to the output encrypted file
decrypted_file_path = 'decrypted_file.zip'  # Path to the output decrypted file



# Read the encrypted data from the encrypted file
encrypted_data_from_file = read_binary_file(encrypted_file_path)

# Decrypt the data and write it to the decrypted file
decrypted_data = decrypt_aes(encrypted_data_from_file, key)
write_binary_file(decrypted_file_path, decrypted_data)

print('decryption completed successfully.')