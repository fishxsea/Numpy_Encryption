from numpydec import decrypt
from numpyenc import encrypt
from charcade import Arcade, color, palettes, colorchart
from random import choice



def main():
    color_palette = palettes('soft sun')
    
    Arcade.erase()
    print(color('Would you like to (1) Encrypt or (2) Decrypt?', choice(color_palette)))
    print()
    ui = input(color('-> ', choice(color_palette), colorend=False))

    if ui == '1':
        Arcade.erase()
        print(color('What message would you like to encrypt?', choice(color_palette)))
        print()
        msg = input(color('-> ', choice(color_palette), colorend=False))
        Arcade.erase()
        encrypt(msg)

    elif ui == '2':
        Arcade.erase()
        print(color('What is the encrypted message?', choice(color_palette)))
        print()
        msg = input(color('-> ', choice(color_palette), colorend=False))
        print(color('\nWhat is the key?', choice(color_palette)))
        print()
        key = input(color('-> ', choice(color_palette), colorend=False))
        Arcade.erase()
        decrypt(msg, key)
    else:
        main()
main()

