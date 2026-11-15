

import hashlib
import subprocess

# SHA-256 HASHING

def hashText():
    text = input("Enter text: ")
    result = hashlib.sha256(text.encode()).hexdigest()
    print("SHA-256:", result)


def hashFile():
    fileName = input("Enter file path: ")

    try:
        with open(fileName, "rb") as file:
            result = hashlib.sha256(file.read()).hexdigest()
        print("SHA-256:", result)

    except FileNotFoundError:
        print("File not found.")


# CAESAR CIPHER

def caesarCipher():
    text = input("Enter text: ")
    shift = int(input("Enter shift amount: "))
    mode = input("Encrypt or decrypt? (E/D): ").upper()

    if mode == "D":
        shift = -shift

    result = ""

    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            newChar = chr((ord(char) - start + shift) % 26 + start)
            result += newChar
        else:
            result += char

    print("Result:", result)


# DIGITAL SIGNATURES

def generateKeys():
    subprocess.run([
        "openssl", "genpkey",
        "-algorithm", "RSA",
        "-out", "private.pem",
        "-pkeyopt", "rsa_keygen_bits:2048"
    ], check=True)

    subprocess.run([
        "openssl", "pkey",
        "-in", "private.pem",
        "-pubout",
        "-out", "public.pem"
    ], check=True)

    print("Keys generated.")


def signFile():
    fileName = input("Enter file to sign: ")

    subprocess.run([
        "openssl", "dgst", "-sha256",
        "-sign", "private.pem",
        "-out", "signature.bin",
        fileName
    ], check=True)

    print("File signed.")


def verifyFile():
    fileName = input("Enter original file: ")

    result = subprocess.run([
        "openssl", "dgst", "-sha256",
        "-verify", "public.pem",
        "-signature", "signature.bin",
        fileName
    ])

    if result.returncode == 0:
        print("Signature is valid.")
    else:
        print("Signature is invalid.")


# MAIN MENU

while True:
    print("\n--- CRYPTOGRAPHY APP ---")
    print("1. Hash text")
    print("2. Hash file")
    print("3. Caesar cipher")
    print("4. Generate RSA keys")
    print("5. Sign file")
    print("6. Verify signature")
    print("7. Exit")

    choice = input("Choose: ")

    if choice == "1":
        hashText()
    elif choice == "2":
        hashFile()
    elif choice == "3":
        caesarCipher()
    elif choice == "4":
        generateKeys()
    elif choice == "5":
        signFile()
    elif choice == "6":
        verifyFile()
    elif choice == "7":
        break
    else:
        print("Invalid choice.")
