import sys
import hashlib
import cipher

BLOCK_SIZE = 64
SHA256_DIGEST_SIZE = 32

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def hmac_sha256(key, message):
    if len(key) > BLOCK_SIZE:
        key = key[:BLOCK_SIZE]
    if len(key) < BLOCK_SIZE:
        key = key + b'\x00' * (BLOCK_SIZE - len(key))

    o_key_pad = xor_bytes(key, b'\x5c' * BLOCK_SIZE)
    i_key_pad = xor_bytes(key, b'\x36' * BLOCK_SIZE)

    inner_hash = hashlib.sha256(i_key_pad + message).digest()
    hmac = hashlib.sha256(o_key_pad + inner_hash).digest()

    return hmac

def main(input_file, key_file, output_file):
    message = cipher.read_file(input_file)
    key = cipher.read_file(key_file)

    mac = hmac_sha256(key, message)

    cipher.write_file(output_file, [mac])

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python hmac.py <input_file> <key_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    key_file = sys.argv[2]
    output_file = sys.argv[3]

    main(input_file, key_file, output_file)
