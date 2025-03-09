from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import os

def generate_keys():
    """Generates RSA 2048-bit keys dynamically with exponent 65537."""
    private_key = rsa.generate_private_key(
        public_exponent=65537,  # Padding level as per your request
        key_size=2048  # RSA 2048-bit key for security
    )
    public_key = private_key.public_key()

    # Save private key
    with open("private_key.pem", "wb") as priv_file:
        priv_file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        ))

    # Save public key
    with open("public_key.pem", "wb") as pub_file:
        pub_file.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

    return private_key, public_key

def rsa_encrypt(message, public_key):
    """Encrypts the message using RSA 256-bit encryption with PKCS#1 v1.5 padding."""
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.PKCS1v15()
    )
    return ciphertext

def main():
    user_input = input("Enter the message to encrypt: ")

    # Generate dynamic keys and store them
    private_key, public_key = generate_keys()

    # Generate random salt
    salt = os.urandom(16)  # 16-byte random salt
    print(f"Generated Salt (Hex): {salt.hex()}")

    # Encrypt the user input
    encrypted_message = rsa_encrypt(user_input, public_key)

    print(f"Encrypted Message (Hex): {encrypted_message.hex()}")

if __name__ == "__main__":
    main()
