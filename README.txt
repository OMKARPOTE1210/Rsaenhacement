RSA Encryption with PKCS#1 v1.5 Padding

Overview

This Python script performs RSA 256-bit encryption using dynamically generated RSA key pairs. The encryption follows PKCS#1 v1.5 padding and includes a random salt for additional security. The script generates both public and private keys, encrypts user-provided messages, and displays the encrypted output in hexadecimal format.

Features

Dynamic RSA Key Generation: Generates a 2048-bit RSA key pair with a public exponent of 65537.

PKCS#1 v1.5 Padding: Ensures secure encryption.

Random Salt Generation: Generates a 16-byte random salt before encryption.

Hexadecimal Output: The encrypted message is displayed in hex format.

Prerequisites

Ensure you have Python installed (3.x recommended) and install the required package:

pip install cryptography

How It Works

User Input: The script prompts the user to enter a message for encryption.

Key Generation:

Creates a 2048-bit RSA key pair (private & public keys).

Saves the keys as private_key.pem and public_key.pem.

Salt Generation: A 16-byte random salt is generated and displayed.

Encryption:

The message is encrypted using the public key with PKCS#1 v1.5 padding.

The encrypted message is converted into hexadecimal format.

Output Display:

The generated salt (hex format).

The encrypted message (hex format).

Usage

Run the script in a terminal or command prompt:

python script.py

Enter a message when prompted. The script will generate keys, encrypt the message, and display the results.

Code Explanation

generate_keys()

Generates an RSA private and public key pair.

Saves keys as PEM format files.

rsa_encrypt(message, public_key)

Encrypts a given message using RSA 256-bit encryption with PKCS#1 v1.5 padding.

main()

Takes user input.

Calls generate_keys() to create the RSA key pair.

Generates a 16-byte random salt.

Encrypts the user message.

Prints the salt and encrypted message in hexadecimal format.

Example Output

Enter the message to encrypt: Hello, RSA!
Generated Salt (Hex): a1b2c3d4e5f67890abcd1234ef567890
Encrypted Message (Hex): 8a3d4f6e7b... (truncated)

Security Considerations

PKCS#1 v1.5 padding is used, but for higher security, OAEP padding is recommended.

RSA key length is 2048-bit. For stronger security, consider 4096-bit.

Private keys should be securely stored to prevent unauthorized decryption.