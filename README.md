# Cryptography
A collection of scripts thats been used in University and for other occasions.

# Cryptography Scripts

This repository contains various cryptography scripts implemented in Python, C++, and C#. The following sections provide brief descriptions of each script and the required libraries.

## 1. Python HMAC (hmac.py)

This script implements the HMAC algorithm based on the SHA-256 hash function. It takes an input file, a key file, and an output file as command line arguments and generates an HMAC for the input file.

To run the script, execute the following command:

python hmac.py <input_file> <key_file> <output_file>

Required libraries: Python's standard library

## 2. C++ SHA-256 (sha256.cpp)

This script implements the SHA-256 algorithm in C++ using the Crypto++ library. It takes an input file and an output file as command line arguments and generates the hash of the input file.

To compile and run the program, execute the following commands:

g++ sha256.cpp -o sha256 -lcrypto++
./sha256 <input_file> <output_file>

Required libraries: [Crypto++](https://www.cryptopp.com/)

## 3. C# AES (AESExample.cs)

This script implements the AES encryption and decryption algorithm in C#. It demonstrates the encryption and decryption of a hardcoded plaintext using a randomly generated key.

To compile and run the program, use the following command (assuming you have .NET SDK installed):

dotnet build
dotnet run


Required libraries: .NET SDK

## 4. Python Blowfish (blowfish_example.py)

This script implements the Blowfish block cipher algorithm in Python using the `pycryptodome` library. It demonstrates the encryption and decryption of a hardcoded plaintext using a randomly generated key.

To run the program, use the following command:

python blowfish_example.py

Required libraries: [pycryptodome](https://pypi.org/project/pycryptodome/)

## Installation

Install the required libraries for each script as described in their respective sections above.

For Python, use `pip` to install the `pycryptodome` library:

pip install pycryptodome


For C++, install the [Crypto++ library](https://www.cryptopp.com/) according to the instructions for your operating system.

For C#, install the [.NET SDK](https://dotnet.microsoft.com/download) according to the instructions for your operating system.

