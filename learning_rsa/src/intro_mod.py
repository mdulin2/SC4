import random
from math import gcd
from time import sleep

def print_header():
    prompt = '''I like loops.
In programming, we make loops all the time using mod.
x mod y (often written x % y) is the remainder of 
dividing x by y.

A few examples:
 10 mod 3 is 1, because 10 / 3 = 3 remainder 1
 15 % 5 = 0, because 5 divides 15
 14 % 4 = 2, because 14 = (3 * 4) + 2

So what we're really doing is making a loop that
starts at 0 and goes up to n-1, but then instead
of n we go back to 0. 

One of the cool things about this is that this means
someimtes you can have two numbers that multiply
to 1 mod n. These numbers are called the modular
inverses of each other.

 4 * 10 = 40 (mod 13)
        = (3 * 13) + 1 (mod 13)
        = 1  (mod 13)        (13 wraps around to 0)

'''
    for line in prompt.splitlines():
        print(line)
        sleep(0.1)

def print_flag():
    print('SC4{where_did_fractions_go}')

def gen_prompt(modulus: int):
    value = random.randint(2, modulus - 1)
    while gcd(value, modulus) != 1:
        value = random.randint(2, modulus - 1)

    inverse = pow(value, -1, modulus)

    print(f"What is the modular inverse of {value} mod {modulus} ?")
    
    guess = int(input())
    return guess == inverse

def fail():
    print('nope')
    exit()

def main():
    try:
        print_header()

        for i in range(1, 5):
            print(f"{i}/5")
            modulus = random.randint(i * 25, (i + 2) * 25)
            if gen_prompt(modulus):
                print('correct\n')
            else:
                fail()

        print('5/5')

        modulus = random.randint(2**37, 2**38-1)
        if gen_prompt(modulus):
            print_flag()
        else:
            fail()
    except ValueError:
        print('invalid')


if __name__ == '__main__':
    main()
