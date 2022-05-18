from numpydec import decrypt
from numpyenc import encrypt
from charcade import Arcade, color


def main():

    Arcade.erase()
    print(color('Would you like to (1) Encrypt or (2) Decrypt?', 'orange70'))
    print()
    ui = input(color('-> ', 'blue70', colorend=False))

    if ui == '1':
        Arcade.erase()
        print(color('What message would you like to encrypt?', 'purple60'))
        print()
        msg = input(color('-> ', 'pink', colorend=False))
        Arcade.erase()
        encrypt(msg)

    elif ui == '2':
        Arcade.erase()
        print(color('What is the encrypted message?', 'purple60'))
        print()
        msg = input(color('-> ', 'pink', colorend=False))
        print(color('\nWhat is the key?', 'green50'))
        print()
        key = input(color('-> ', 'white', colorend=False))
        Arcade.erase()
        decrypt(msg, key)
    else:
        main()
main()

