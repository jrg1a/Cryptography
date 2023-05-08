from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt(plaintext, key):
    cipher = Blowfish.new(key, Blowfish.MODE_CBC)
    ciphertext = cipher.iv + cipher.encrypt(pad(plaintext.encode(), Blowfish.block_size))
    return base64.b64encode(ciphertext).decode()

def decrypt(ciphertext, key):
    ciphertext = base64.b64decode(ciphertext.encode())
    iv = ciphertext[:Blowfish.block_size]
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext[Blowfish.block_size:]), Blowfish.block_size).decode()

def main():
    key = get_random_bytes(16)  # Generate a random 16-byte key
    plaintext = "This is a test message."

    print(f"Original message: {plaintext}")

    encrypted = encrypt(plaintext, key)
    print(f"Encrypted message: {encrypted}")

    decrypted = decrypt(encrypted, key)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
