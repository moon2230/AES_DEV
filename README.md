AES Encryption Python Script
This script implements the AES (Advanced Encryption Standard) encryption algorithm in Python. It includes the basic AES encryption functions along with the ability to work in different modes of operation, such as ECB, CBC, CFB, OFB, and CTR. The script also demonstrates the padding and key expansion methods necessary for AES encryption.

Table of Contents
Overview
Requirements
Functions
Modes of Operation
Usage
License
1. Overview
AES is a symmetric key encryption algorithm that encrypts data in fixed-size blocks (128-bit). This script implements AES encryption using a variety of modes such as ECB (Electronic Codebook), CBC (Cipher Block Chaining), CFB (Cipher Feedback), OFB (Output Feedback), and CTR (Counter mode). The script provides functions for:

Key expansion
AES encryption/decryption
Padding
Block transformations (like SubBytes, ShiftRows, MixColumns)
Implementing different AES operation modes.
2. Requirements
To run this script, you will need Python 3.x installed.

No additional external libraries are required to run the script itself, but for modes like ECB, CBC, etc., the script assumes usage of raw byte data or byte arrays.

3. Functions
block2state(block)
Converts a 16-byte block (plaintext or ciphertext) into a 4x4 state matrix for AES processing.

subbyest(state)
Performs the SubBytes operation on the state matrix using the S-box.

AddRoundkey(state, rkey)
Performs the AddRoundKey operation, XORing the state with the round key.

shiftrows(state)
Performs the ShiftRows operation, where each row of the state matrix is shifted cyclically.

MIX_Column(state)
Performs the MixColumns operation, mixing the columns of the state matrix.

key_schedule_Enc(key_state)
Generates the round keys for AES encryption from the initial key.

AES_ENC(plaintext, key)
Performs AES encryption on a block of plaintext using the provided key.

padding(pt)
Pads the plaintext so that its length is a multiple of 16 bytes.

ECB(pt, key)
Encrypts the plaintext in ECB mode. Each block is encrypted independently.

cbc(pt, key)
Encrypts the plaintext in CBC mode, chaining the blocks together using an IV.

CFB(pt, key)
Encrypts the plaintext in CFB mode, using feedback from previous ciphertext blocks.

OFB(pt, key)
Encrypts the plaintext in OFB mode, using the feedback from previous keystream blocks.

CTR(pt, key)
Encrypts the plaintext in CTR mode, using a counter that increments with each block.

4. Modes of Operation
AES can operate in different modes to enhance security and allow different use cases. This script implements the following modes:

ECB (Electronic Codebook)
Each block is encrypted independently.
Simple but not secure for most real-world applications because identical plaintext blocks yield identical ciphertext blocks.
CBC (Cipher Block Chaining)
Each block of plaintext is XORed with the previous ciphertext block before being encrypted.
Requires an initialization vector (IV) for the first block.
CFB (Cipher Feedback)
Each byte of plaintext is XORed with the encrypted output of the previous block.
Suitable for applications where small amounts of data need to be encrypted at a time.
OFB (Output Feedback)
Encrypts a stream of bits rather than fixed-size blocks.
Uses feedback from the encrypted output rather than the previous ciphertext block.
CTR (Counter Mode)
Uses a counter that is incremented for each block.
Allows for parallel encryption and decryption and is often used for stream cipher-like behavior.
5. Usage
To run the AES encryption script, you can directly modify the block and key variables, or use any plaintext/ciphertext you want to encrypt or decrypt.

Example:

python
코드 복사
key = [ 0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, \
        0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c ]
block = [ 0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, \
          0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34 ]

# Choose the encryption mode: ECB, CBC, CFB, OFB, CTR
ct = ECB(block, key)  # Encrypt in ECB mode

# Print the ciphertext
for i in range(len(ct)):
    if (i % 16) == 0:
        print()
    print("%02x, " % ct[i], end=" ")

# Convert ciphertext to image or save it as needed (for image data)
# Process the ciphertext as required
Each encryption mode has its own behavior, and you can simply call one of the functions (e.g., ECB, cbc, etc.) to encrypt or decrypt data.

