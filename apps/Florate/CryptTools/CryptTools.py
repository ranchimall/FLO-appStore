
import base64
import os
from Crypto.Cipher import AES
"""
This Module is not used by default it is included if we wish to encrypt/decrpyt the data
while transferring over block chain.

Encryption Technique Used: Advanced Encryption Standard (AES)
Key Length: 32

Usage:
cipher_text = CryptTools.encrypt(plain_text,key)
plain_text = CryptTools.decrypt(ciper_text,key)

For random key generation use: CryptTools.keyGen()
"""

def pad(data):
    """
    Function Name: pad

    Function use: pad the data for encryption
    """
    padding = 16 - len(data) % 16
    return data + padding * chr(padding+97)

def unpad(data):
    """
    Function Name: unpad

    Function use: unpad the data for decryption
    """

    data = str(data)
    padding =  ord(data[-2]) - 96
    return data[2:-padding]

def keyGen():
    # Generating random key of 32 bytes
    key = os.urandom(32)
    return key


def encryptMsg(plaintext, key):
    # Genarating Initialization vector for AES (16 bytes)
    IV = os.urandom(16)
    # Encrypting The plaintext
    cipher = AES.new(key, AES.MODE_CBC, IV)
    plaintext=base64.b64encode(plaintext.encode('utf-8')).decode('utf-8')
    ciphertext = cipher.encrypt(pad(plaintext).encode('utf-8'))
    # Append IV and Ciphertext
    ciphertext = base64.b64encode(IV).decode('utf-8') + base64.b64encode(ciphertext).decode('utf-8')
    return ciphertext


def decryptMsg(ciphertext, key):
    # Initialization vector in AES should be 16 bytes
    IV = base64.b64decode(ciphertext[:24])
    ciphertext=base64.b64decode(ciphertext[24:])
    # Creation of encryptor and decryptor object using above details
    cipher = AES.new(key, AES.MODE_CBC, IV)
    plaintext=unpad(cipher.decrypt(ciphertext))
    plaintext = (base64.b64decode(plaintext)).decode('utf-8')
    return plaintext
