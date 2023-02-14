## Loops 1 (intro_mod.py)

Students must compute the modular multiplicative inverse. Wikipedia's article is helpful.

The easiest solution is to use Python's `pow()` function.
`pow(a, -1, b)` will give the multiplicative inverse.

Alternatively, students can find or implement the extended euclidean algorithm directly.
```
function extended_gcd(a, b)
    (old_r, r) := (a, b)
    (old_s, s) := (1, 0)
    (old_t, t) := (0, 1)
    
    while r ≠ 0 do
        quotient := old_r div r
        (old_r, r) := (r, old_r − quotient × r)
        (old_s, s) := (s, old_s − quotient × s)
        (old_t, t) := (t, old_t − quotient × t)
    return old_r, old_s, old_t
```

Computing `extended_gcd(a,b)[1]` for the inverse of `a` mod `b` gives the multiplicative inverse.

## Loops 2 (babyrsa.py)

Students must determine any valid exponent which causes the base value to loop back to itself mod n.
As a hint, get students to look for patterns in the first few loops for a given prompt. It should
become apparent that exponentiating _always_ makes a loop length which is one plus a divisor of `n-1`. 

Although smaller loops may exist, `n` is always guaranteed to be a valid answer.

## Loops 3 (kidrsa.py)

Students must decrypt a value using an RSA-like structure that only uses a single prime
instead of the product of two primes.

The big mathematical idea is the combination of the previous two problems. We know that
`x^n = x (mod n)`. We're given `e` and `x^e`. So if we can get
`(x^e)^d = x^n = x^1 (mod n)`, we've decrypted the message. 

But we know `(x^e)^d = x^(e * d)`. We also know the loop length of exponentiation mod `n` is
`n-1` (`n` gets us back where we started). So we want to make `e * d = 1 (mod n-1)`. This is
just the modular multiplicative inverse from part 1.

So if `d` is the inverse of `e` mod `n-1`, we've solved the problem. 

In python, this is implemented as follows.

```
input: e, N, C where x^e % N = C
output: S

d = pow(e, -1, N-1)
x = pow(C, d, N)
```
