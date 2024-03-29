# Caesar Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip

# The string to be encrypted/decrypted:
message = '1234567890'  #'This is my secret message.'
# message = input('Message you want to encrypt/decrypt: >>>')
# The encryption/decryption key:
key = 21
# key = int(input('Key from 0 to 93: >>>'))
# Whether the program encrypts or decrypts:
mode = 'encrypt' # 'decrypt' # Set to either 'encrypt' or 'decrypt'.
# mode = input('enrypt to encrypt/decrypt to decrypt: >>>')
# Every possible symbol that can be encrypted:
# SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,<>/\|{}[];:*&^%$#@~`=+-_()'
# Stores the encrypted/decrypted form of the message:
translated = ''
# print(len(SYMBOLS))
for symbol in message:
    # Note: Only symbols in the 'SYMBOLS' string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption/decryption:
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # Handle wrap-around, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

# Output the translated string:
print(translated)
pyperclip.copy(translated)
