
from sage.all import ZZ

def disc(a, b):
    # This calculates the discriminant of E_{a, b}
    return -16*(4*a**3 + 27*b**2)


def naive_height(a, b):
    # This calculates the naive height h(E_{a, b}) := max(4|a|^3, 27|b|^2)
    return max(4*abs(a**3), 27*b**2)


def prime_condition(a, b): 
    # This checks the primality condition, i.e., that there are no primes p such that p^4|a and p^6|b
    # # and returns TRUE if the condition is satisfied
    if a == 0:
        b_factors = list(ZZ(b).factor())
        Lb = len(b_factors)
        m = 0
        Condition = True
        while (Condition == True) and (m < Lb):
            if b_factors[m][1] < 6:
                m = m + 1
            else:
                Condition = False
    else:
        a_factors = list(ZZ(a).factor())
        La = len(a_factors)
        n = 0
        Condition = True
        while (Condition == True) and (n < La):
            if a_factors[n][1] < 4:
                n = n + 1
            else:
                if (a_factors[n][0]^6).divides(b):
                    Condition = False
                n = n + 1
    return Condition


def is_k_power_free(n, k):
    # Checks if the integer n is k-power-free, meaning no prime factor of n
    # is raised to an exponent of k or more in its factorization.
    factorization = list(ZZ(n).factor())
    exponents = [f[1] for f in factorization]
    return k in exponents


def get_power_free_integers(X, k):
    # Generates a list of integers d such that d is k-power-free and
    # |d| ≤ X
    integers = [d for d in range(1, int(X)+1) if not is_k_power_free(d,k)]
    integers = integers + [-1*i for i in integers]
    return integers