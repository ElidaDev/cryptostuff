# Cryptography App README

## Overview
This application demonstrates three cryptographic methods: SHA-256 hashing, Caesar cipher encryption/decryption, and RSA digital signatures.

## Code Functionality

**SHA-256 Hashing:**
Uses Python's `hashlib` library to generate a unique 64-character hexadecimal hash from text or files. SHA-256 is a one-way hashing algorithm, meaning the original input cannot be recovered from the hash.

**Caesar Cipher:**
Encrypts and decrypts text by shifting letters through the alphabet by a chosen number. Decryption reverses the shift to recover the original message.

**Digital Signatures:**
Uses OpenSSL and RSA keys to sign and verify files. The private key creates a digital signature, while the public key verifies it. SHA-256 is used to hash the file during signing and verification. This helps verify that a file has not been modified and that it was signed by the holder of the corresponding private key.

## How to Run
1. Install Python 3 and OpenSSL.
2. Save the program as `crypto_app.py`.
3. Run `python crypto_app.py`.
4. Select an option from the menu.

## Digital Signature Instructions
1. Select option 4 to generate RSA keys.
2. Select option 5 to sign a file.
3. Select option 6 to verify the signature.

## Generated Files
- `private.pem`: Private RSA key. Keep this secure.
- `public.pem`: Public RSA key.
- `signature.bin`: Digital signature of the selected file.

## Conclusion
This application demonstrates how hashing, encryption, and digital signatures are used in cryptography to protect information and verify data integrity.
