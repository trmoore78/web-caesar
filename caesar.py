import string
from helpers import alphabet_position, rotate_character



def encrypt(text,rot):
    rotated = ''
    alphabet = string.ascii_lowercase
    rot = int(rot)

    for char in text:
        if char.isalpha():
            rotated_idx = (alphabet_position(char) + rot) %26
            if char.isupper(): # if it was uppercase originally, make it uppercase
                rotated += alphabet[rotated_idx].upper()
            else: # keep it lowercase
                rotated += alphabet[rotated_idx]
        elif char == " ": 
            rotated += char
        else:
            rotated += char
    return rotated



