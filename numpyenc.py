import string
import numpy as np
import random
from numpy.random import randint
from charcade import color, palettes
from random import choice

def encrypt(user_input):

    alph = string.ascii_letters + string.digits + string.punctuation + ' '

    # Shuffles a 2d array of numbers 1 through the length of the alphabet
    num_array = np.arange(95).reshape(19, 5)

    key = ''
    rand_num = randint(100,5000)
    division_nums = [2, 3, 4, 6, 7, 8, 9]
    div_num = random.choice(division_nums)
    shift_num = str(div_num) + str(rand_num)[0]
    shift = 1
    for i in shift_num:
        shift *= int(i)
    shift = (shift + div_num) * div_num

    key += str(div_num) + '-' + str(rand_num) + '-' + str(shift)

    num = 0
    for i in range(rand_num):
        axis_num = 0
        if (num % 5) == 0:
            num += 1

        if (num % div_num) == 0:
            axis_num = 0
        else:
            axis_num = 1   
        
        if (rand_num % 2) == 0:
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
    shift_key = key.replace('-', ' ')
    shift_key = shift_key.split()
    shift_key = shift_key[0] + shift_key[2]

    # Multiplies the numbers in the shift key in sequence
    cipher_num = 1
    for i in shift_key:
        if i == '0':
            i = '1'
        cipher_num *= int(i)

    # Ciphers the inputted message using the generated alphabet
    num = 1
    encrypted = ''
    for i in range(len(user_input)):
        char = user_input[i]
        loc = new_alph.find(char)
        new_loc = (loc + (cipher_num + num)) % 95 # Ensures that the same characters in sequence 
        encrypted += new_alph[new_loc]            # are not the same when shifted
        num += (2 + num)

    color_palette = palettes('soft sun')

    print(color('\nEncrypted Message: ', choice(color_palette)) + color(encrypted, choice(color_palette)))
    print(color('Key: ', choice(color_palette)) + color(key + '\n', choice(color_palette)))
    