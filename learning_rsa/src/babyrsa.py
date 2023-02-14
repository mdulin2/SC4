import random
from time import sleep
from sympy import factorint
from sympy.ntheory.primetest import isprime


def print_header():
    prompt = '''I really like loops!
Repeatedly multiplying a number mod n makes loops!
Here's a loop that has 4 values before repeating:
 3   (mod 10) = 3
 3^2 (mod 10) = 9
 3^3 (mod 10) = 9 * 3 (mod 10) = 27 (mod 10) = 7
                v------------------------------^
 3^4 (mod 10) = 7 * 3 (mod 10) = 21 (mod 10) = 1
 3^5 (mod 10) = 1 * 3 (mod 10) = 3

This means 3^(4n + 1) will always make a loop and
end up back at 3!
'''
    for line in prompt.splitlines():
        print(line)
        sleep(0.1)

def print_flag():
    print('SC4{right_back_where_we_started}')

def gen_prompt(bitlen: int, force_generator: bool, print_long: bool):
    # make a prime
    modulus = random.randint(2**(bitlen - 1), 2**bitlen - 1)
    while not isprime(modulus):
        modulus = random.randint(2**(bitlen - 1), 2**bitlen - 1)
    phimod_factors = factorint(modulus - 1).keys()

    # make the base of the exponent
    base = random.randint(2, modulus - 2)
    while force_generator ^ all(pow(base, ((modulus - 1)//factor), modulus) != 1 for factor in phimod_factors):
        base = random.randint(2, modulus - 2)

    if print_long:
        print(f"Can you find a loop when multiplying {base} mod {modulus}?")
        print(f"In other words, solve {base}^x mod {modulus} = {base}:")
    else:
        print(f"Now find one for {base}^x mod {modulus}:")

    guess = int(input())
    return guess != 1 and pow(base, guess, modulus) == base
    
def fail():
    print('nope')
    exit()

def main():
    try:
        print_header()

        print('1/6')
        if gen_prompt(6, force_generator=False, print_long=True):
            print('correct\n')
        else:
            fail()

        for i in range(2, 6):
            print(f"{i}/6")
            # guarantee the generator a few times to make the pattern easier to spot
            force_generator = i in (2, 5)

            if gen_prompt(7, force_generator, print_long=False):
                print('correct\n')
            else:
                fail()

        print('do you see a pattern?\n')
        print('6/6')

        if gen_prompt(48, force_generator=True, print_long=False):
            print_flag()
        else:
            fail()

    except ValueError:
        print('invalid')


if __name__ == '__main__':
    main()
