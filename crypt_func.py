from cryptography.fernet import Fernet
import base64

def encode1(text: str, key : str):
    try:
        key = key.encode()
        encrypt_text = Fernet(base64.urlsafe_b64encode(key)).encrypt(text.encode())
        return str(encrypt_text.decode())
    except Exception:
        return str('(!) Encryption_error (!)')
def decode1(encrypt_text : str, key : str):
    try:
        key = key.encode()
        decipher_text = Fernet(base64.urlsafe_b64encode(key)).decrypt(encrypt_text)
        return str(decipher_text.decode())
    except Exception:
        return str('(!) Decryption_error (!)')
# print(encode1('inst', '123321321123yryryryryryryryryryr'))