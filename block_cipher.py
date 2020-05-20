##########
# convert plaintext with spaces to 5 letter all caps blocks, append 0 to pad if not divisible by 5
# 11.25.19
###########
import re


def add_buffer(string):
    remainder = len(string) % 5
    if remainder == 0:
        return string
    else:
        pad = 5 - remainder
        for i in range(pad):
            string = string + "0"
        return string


def block_space(string):
    if len(string)<6:
        return string
    string = ' '.join(string[i:i + 5] for i in range(0, len(string), 5))
    return string


def do_cipher():
    cipher = input("enter plaintext\n")
    cipher = re.sub(" ", "", cipher)
    cipher = add_buffer(cipher)
    cipher = block_space(cipher)
    if cipher.isupper() is False:
        cipher = cipher.upper()
    return cipher


print(do_cipher())