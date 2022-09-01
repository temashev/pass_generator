# python password generator
import random


def get_password():
    _range = random.randint(8, 13)
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*1234567890'

    end_pass = ''

    for symbol in range(_range):
        end_pass += random.choice(alphabet)

    return end_pass


print(get_password())
