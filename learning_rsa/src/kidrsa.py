from math import gcd
import random
from time import sleep
from sympy.ntheory.primetest import isprime

def print_header():
    prompt = '''I still like loops!
Maybe I can be clever and hide secret values using loops?
If I start with a secret number S and raise it to the
11th power (mod 37), I get a number A that's part of the
loop. Maybe we can do something to go from X back to S?

Think about exponentiating A (mod 37):
 A = S^11 (mod 37)
 A^2 = (A^11)^2 = S^(11*2) = S^22 (mod 37)
 A^5 = (A^11)^5 = S^(11*5) = S^55 (mod 37)

But remember that S mod 37 makes a loop with 36 elements 
(the 37th element is S, which was already the first).
So
 A^5 = S^55 (mod 37)
     = S^(55 mod 36) (mod 37)
     = S^19 (mod 37)

If we're careful with our math, maybe we can raise A to
some power and end up with S?

'''
    for line in prompt.splitlines():
        print(line)
        sleep(0.1)


def print_flag():
    print('SC4{wait_this_is_almost_rsa}')

def gen_prompt(exponent: int, modulus: int):
    s = random.randint(2, modulus - 1)
    x = pow(s, exponent, modulus)

    print(f"If S ^ {exponent} = {x} ( mod {modulus} ), what was the secret value S?")

    guess = int(input())
    return guess == s

def gen_prime(max_val: int):
    candidate = random.randint(max_val//2, max_val)
    while not isprime(candidate):
        candidate = random.randint(max_val//2, max_val)
    return candidate

def gen_exponent(modulus: int):
    exponent = random.randint(3, modulus - 2)
    while gcd(exponent, modulus - 1) != 1:
        exponent = random.randint(3, modulus - 2)
    return exponent

def fail():
    print('nope')
    exit()

def main():
    try:
        print_header()

        print('1/5')
        if gen_prompt(11, 37):
            print('correct\n')
        else:
            fail()

        for i in range(2, 5):
            print(f"{i}/5")

            modulus = gen_prime(307 * (10**(i-1)))
            exponent = gen_exponent(modulus)

            if gen_prompt(exponent, modulus):
                print('correct\n')
            else:
                fail()

        print('5/5')
        modulus = gen_prime(2**48)
        exponent = gen_exponent(modulus)

        if gen_prompt(exponent, modulus):
            print_flag()
        else:
            fail()

    except ValueError:
        print('invalid')

if __name__ == '__main__':
    main()
