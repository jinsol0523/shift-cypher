# Shift Cipher Decryption

This Python script is designed to decrypt a text that has been encoded using a Caesar cipher, also known as a shift cipher. The script prompts the user to enter the ciphered text and then proceeds to decipher it using all possible key cases.

## Background

The Caesar cipher, a type of substitution cipher, is one of the simplest and most widely known encryption techniques. It was named after Julius Caesar, who is said to have used it to communicate with his generals. In a Caesar cipher, each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Motivation

This script was created by Jin Sol Park as a result of curiosity sparked during the Math 4175 Cryptography class. After learning about shift ciphers, the desire to explore and understand them further led to the development of this tool for convenience.

## Usage

### Installation

No installation is required. Simply ensure you have Python installed on your system.

### Running the Script

1. Run the script `shift_cipher_decryption.py`.
2. You will be prompted to enter the ciphered text.
3. After entering the text, press Enter.
4. The script will then print out all possible decrypted texts for all key cases.

## Encryption Example

Suppose we want to encrypt the text "Jin Sol Park" with a Caesar cipher using a key of 4.

The encryption process involves shifting each letter of the plaintext forward by 4 positions in the alphabet.

Here's how the encryption would look:

- "J" shifts 4 positions forward to "N".
- "i" shifts 4 positions forward to "m".
- "n" shifts 4 positions forward to "r".
- " " (space) remains unchanged.
- "S" shifts 4 positions forward to "W".
- "o" shifts 4 positions forward to "s".
- "l" shifts 4 positions forward to "p".
- " " (space) remains unchanged.
- "P" shifts 4 positions forward to "T".
- "a" shifts 4 positions forward to "e".
- "r" shifts 4 positions forward to "v".
- "k" shifts 4 positions forward to "o".

So, "Jin Sol Park" encrypted with a key of 4 would result in "Nmr Wsp Tevo".

## Decryption Example

Suppose we have the ciphertext "Zae Jfc Grib" and want to decrypt it with a Caesar cipher to find the original plaintext "Jin Sol Park".

The decryption process involves shifting each letter of the ciphertext backward by the key value in the alphabet.

Here's how the decryption would look for various keys:

- **Key 0**: Zae Jfc Grib
- **Key 1**: Yzd Ieb Fqha
- **Key 2**: Xyc Hda Epgz
- **Key 3**: Wxb Gcz Dofy
- **Key 4**: Vwa Fby Cnex
- **Key 5**: Uvz Eax Bmdw
- **Key 6**: Tuy Dzw Alcv
- **Key 7**: Stx Cyv Zkbu
- **Key 8**: Rsw Bxu Yjat
- **Key 9**: Qrv Awt Xizs
- **Key 10**: Qpu Zvs Whyr
- **Key 11**: Pot Yur Vgxq
- **Key 12**: Ons Xtq Ufwp
- **Key 13**: Nmr Wsp Tevo
- **Key 14**: Mlq Vqo Sdun
- **Key 15**: Lkp Upn Rctm
- **Key 16**: Kjo Tpm Qbsl
- **Key 17**: **Jin Sol Park** (Zae Jfc Grib)
- **Key 18**: Ihm Rnk Ozqj
- **Key 19**: Hgl Qmj Nypi
- **Key 20**: Gfk Pli Mxoh
- **Key 21**: Fej Okh Lwng
- **Key 22**: Edi Njg Kvmf
- **Key 23**: Dch Mif Julc
- **Key 24**: Cbg Lhe Itkb
- **Key 25**: Baf Kgd Hsja

So, with a key of 17, the ciphertext "Zae Jfc Grib" decrypts to "Jin Sol Park".