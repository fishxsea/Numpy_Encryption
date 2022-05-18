import string
from charcade import color, palettes
import numpy as np
from random import choice

def decrypt(msg_input, key_input):
    # Breaks key into parts for use in alphabet creation and cipher
    key_split = key_input.split('-')
    shift_key_alph = int(key_split[0])
    range_key = int(key_split[1])
    shift_key_cipher = int(key_split[2])


    alph = string.ascii_letters + string.digits + string.punctuation + ' '

    # Shuffles a 2d array of numbers 1 through the length of the alphabet
    num_array = np.arange(95).reshape(19, 5)

    num = 0
    for i in range(range_key):
        axis_num = 0
        if (num % 5) == 0:
            num += 1

        if (num % shift_key_alph) == 0:
            axis_num = 0
        else:
            axis_num = 1   
        
        if (range_key % 2) == 0:
            neg_num = -num 
        else:
            neg_num = num

        num_array = np.roll(num_array, num + num)
        num_array = np.roll(num_array, neg_num, axis=axis_num)
        num += 1


    # Converts numpy array into a string
    num_array = np.array2string(num_array)
    remove_char = '[]\n'
    for i in remove_char:
        num_array = num_array.replace(i, '')
    num_array = num_array.split()

    # Turns the shuffled numbers into a list for use in creating a unique alphabet by indexing
    num_list = []
    for i in num_array:
        num_list.append(i)

    # Alphabet creation through indexing
    new_alph = ''
    for i in num_list:
        int_i = int(i)
        index_alph = alph[int_i]
        new_alph += index_alph


    # CIPHER SECTION

    # Takes the first number of the key and concatenates it with the last numbers of the key
    shift_key = str(shift_key_alph) + str(shift_key_cipher)


    # Multiplies the numbers in the shift key in sequence
    cipher_num = 1
    for i in str(shift_key):
        if i == '0':
            i = '1'
        cipher_num *= int(i)


    num = 1
    decrypted = ''
    for i in range(len(msg_input)):
        char = msg_input[i]
        loc = new_alph.find(char)
        new_loc = (loc - (cipher_num + num)) % 95
        decrypted += new_alph[new_loc]
        num += (2 + num)

    color_palette = palettes('soft sun')
    print(color('\nDecrypted Message: ', choice(color_palette)) + color(decrypted + '\n', choice(color_palette))) 