import sys
import math


# cyclic left shift on k bits
def shift(bits, k):
    return bits[k:] + bits[:k]


# logical and on two lists of bits
def AND(bits1, bits2):
    assert len(bits1) == len(bits2)
    return [b[0] * b[1] for b in zip(bits1, bits2)]


# xor on two lists of bits
def XOR(bits1, bits2):
    assert len(bits1) == len(bits2)
    return [(b[0] + b[1]) % 2 for b in zip(bits1, bits2)]


# one round of the Feistel network; returns the new left half,
# since the right half is the same as the former left half
def round(L, R, K):
    s1 = shift(L, 1)
    s2 = shift(L, 5)
    s3 = shift(L, 2)

    x1 = XOR(R, AND(s1, s2))
    x2 = XOR(x1, s3)
    x3 = XOR(x2, K)

    return x3


# derives the 4 8-bit round keys from the 32-bit key
def keySchedule(K):
    assert len(K) == 32
    return [K[off:off + 8] for off in [0, 8, 16, 24]]


# encrypts 16-bit plaintext P with 4 round keys
def encryption(P, Ks):
    # split plaintext into left and right half
    L = P[:8]
    R = P[8:]

    # repeat the same operation 4 times
    for i in range(4):
        t = L
        L = round(L, R, Ks[i])
        R = t

    # final swap
    return R + L


# encryption with 16-bit plaintext and 32-bit key
def encrypt(P, K):
    assert len(P) == 16
    assert len(K) == 32
    Ks = keySchedule(K)
    return encryption(P, Ks)


# decryption with 16-bit ciphertext and 32-bit key
def decrypt(C, K):
    assert len(C) == 16
    assert len(K) == 32
    Ks = keySchedule(K)
    Ks.reverse()
    return encryption(C, Ks)


# Converts a sequence of bytes (read from a file) into a list of bits (0s and 1s)
def bytes_to_bits(B):
    bits = []
    for i in range(len(B)):
        current_byte = B[i]
        mask = 128
        for j in range(8):
            if (current_byte >= mask):
                bits.append(1)
                current_byte -= mask
            else:
                bits.append(0)
            mask = mask // 2
    return bits


# opposite of the above operation
def bits_to_bytes(B):
    byteseq = []
    num_bytes = len(B) // 8
    assert 8 * num_bytes == len(B)
    for i in range(num_bytes):
        current_byte = 0
        bit_sequence = B[(i * 8):((i + 1) * 8)]
        mask = 128
        for j in range(8):
            current_byte += mask * bit_sequence[j]
            mask = mask // 2
        byteseq.append(current_byte.to_bytes(1, "big"))
    return byteseq


# writes a sequence of bytes to a file
def write_file(output_file, byteseq):
    f = open(output_file, "wb")
    for i in range(len(byteseq)):
        f.write(byteseq[i])
    f.close()


# reads a sequence of bytes from a file
def read_file(input_file):
    f = open(input_file, "rb")
    data = f.read()
    f.close()

    return data


def splitIntoBlocks(bits, blocksize):
    blocks = []
    number_of_blocks = math.ceil(len(bits) / blocksize)
    for i in range(number_of_blocks - 1):
        blocks.append(bits[blocksize * i:blocksize * (i + 1)])
    number_of_padded_bits = (blocksize - (len(bits) % blocksize)) % blocksize
    final_block = bits[(number_of_blocks - 1) * blocksize:]
    for j in range(number_of_padded_bits):
        final_block.append(0)
    blocks.append(final_block)
    return blocks


def mergeBlocks(blocks):
    llist = []
    for b in blocks:
        llist = llist + b
    return llist


def cbc_enc(plaintext_blocks, iv, key):
    ciphertext_blocks = [iv]
    for i in range(len(plaintext_blocks)):
        xored_block = XOR(ciphertext_blocks[-1], plaintext_blocks[i])
        ciphertext_blocks.append(encrypt(xored_block, key))
    return ciphertext_blocks[1:]


def cbc_dec(ciphertext_blocks, iv, key):
    ciphertext_blocks = [iv] + ciphertext_blocks
    plaintext_blocks = []
    for i in range(1, len(ciphertext_blocks)):
        tmp_block = decrypt(ciphertext_blocks[i], key)
        plaintext_blocks.append(XOR(tmp_block, ciphertext_blocks[i - 1]))
    return plaintext_blocks


def padding_plaintext(plaintext_bits):
    bits_needed = (16 - (len(plaintext_bits) % 16)) % 16
    if bits_needed == 0:
        padding_bits = [1, 0] * 8  #2 bytes with value 16
    else:
        padding_bits = [0] * (bits_needed - 1) + [1] #p-1 zeros and a 1
    padded_plaintext_bits = plaintext_bits + padding_bits
    return padded_plaintext_bits


def unpad_plaintext(padded_plaintext_bits):
    index = len(padded_plaintext_bits) - 1
    while padded_plaintext_bits[index] != 1:
        index -= 1
    unpadded_plaintext_bits = padded_plaintext_bits[:index]
    return unpadded_plaintext_bits




def main():
    if len(sys.argv) != 6:
        print("Usage: " + sys.argv[0] + " <enc/dec> PLAINTEXT_FILE KEY_FILE IV_FILE OUTPUT_FILE")
    else:
        mode = sys.argv[1]
        plaintext_file = sys.argv[2]
        key_file = sys.argv[3]
        iv_file = sys.argv[4]
        output_file = sys.argv[5]

        plaintext_bytes = read_file(plaintext_file)
        key_bytes = read_file(key_file)
        iv_bytes = read_file(iv_file)

        #Convertto bits!
        plaintext_bits = bytes_to_bits(plaintext_bytes)
        key_bits = bytes_to_bits(key_bytes)
        iv_bits = bytes_to_bits(iv_bytes)

        if mode == "enc": #encryptz
            padded_plaintext_bits = padding_plaintext(plaintext_bits)
            plaintext_blocks = splitIntoBlocks(padded_plaintext_bits, 16)
            ciphertext_blocks = cbc_enc(plaintext_blocks, iv_bits, key_bits)


            ciphertext_bits = mergeBlocks(ciphertext_blocks)
            ciphertext_bytes = bits_to_bytes(ciphertext_bits)
            write_file(output_file, ciphertext_bytes)

        elif mode == "dec": #decrypt!
            ciphertext_blocks = splitIntoBlocks(plaintext_bits, 16)
            decrypted_blocks = cbc_dec(ciphertext_blocks, iv_bits, key_bits)

            decrypted_bits = mergeBlocks(decrypted_blocks)
            unpadded_decrypted_bits = unpad_plaintext(decrypted_bits)
            decrypted_bytes = bits_to_bytes(unpadded_decrypted_bits)

            write_file(output_file, decrypted_bytes)

        else:
            print("Invalid actin. Use 'enc' or 'dec' :) .")
main()

