import string

def alphabet_position(character):
    alphabet = string.ascii_lowercase
    lower = character.lower()
    if lower.isalpha():
        return alphabet.index(lower)
    else:
        return lower


def rotate_character(char,rot):
    rotated = ''
    alphabet = string.ascii_lowercase
    rot = int(rot)
        
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