# The density and distribution of CM elliptic curves over Q

- Adrian Barquero-Sanchez
- Jimmy Calvo-Monge

:dog2:

This repository contains the python files with the code that was implemented for the computations that were used in the paper *The density and distribution of CM elliptic curves over Q*.

## Files Description

- `results` folder: contains dictionaries with $`j`$-invariants distributions for the family $`\mathcal{E}(10^k)`$ for $`k`$ between $`4`$ and $`12`$.
- `utils.py`: contains util functions `disc(a, b)`, `naive_height(a, b)`, `prime_condition(a, b)`, `is_k_power_free(n, k)` and `get_power_free_integers(X, k)`.
- `script.py`: implements sequentially the distribution computations for families $`\mathcal{E}`$ and $`\mathcal{ET}`$.
- `script_parallel.py`: implements in parallel the distribution computations for family $`\mathcal{E}`$.

## Article Abstract

In this paper we study the density and distribution of CM elliptic curves over $`\mathbb{Q}`$. In particular, we prove that the natural density of CM elliptic curves over $`\mathbb{Q}`$, when ordered by naive height, is zero. Furthermore, we analyze the distribution of these curves among the thirteen possible CM orders of class number one. Our results show that asymptotically, $`100\%`$ of them have complex multiplication by the order $`\mathbb{Z}\left[\frac{-1 + \sqrt{-3}}{2} \right]`$, that is, have $j$-invariant 0. We conduct this analysis within two different families of representatives for the $`\mathbb{Q}`$-isomorphism classes of CM elliptic curves: one commonly used in the literature and another constructed using the theory of twists. As part of our proofs, we give asymptotic formulas for the number of elliptic curves with a given $j$-invariant and bounded naive height.


## Code Description

This code computes the distribution of $`j`$-invariants of CM elliptic curves with naive height less than $`X`$ by counting the appearances of $`j`$-invariants in each family $\mathcal{E}$ and $\mathcal{ET}$.

Here is a detailed explanation of what each function in the code does, along with its role in the overall analysis.

- `disc(a, b)`: Calculates the discriminant of the elliptic curve $`E_{a,b}: y^2 = x^3 + ax + b`$.

- `naive_height(a, b)`: Computes the *naive height* of the elliptic curve $`E_{a,b}`$.

- `prime_condition(a, b)`: Checks the primality condition on the integers $`a`$ and $`b`$, ensuring there is no prime $`p`$ such that $`p^4`$ divides $`a`$ and $`p^6`$ divides $`b`$. The function analyzes the prime factorizations of $`a`$ and $`b`$ and returns `True` if the condition is satisfied, otherwise `False`.

- `Get_Distribution_J_invariants_in_family_E(Xmax)`:
Computes the distribution of $`j`$-invariants in the family $`\mathcal{E}`$ for elliptic curves with naive height $`\leq X_{\text{max}}`$.

**Steps**:
- Iterates over integers $`a`$ and $`b`$ within the range dictated by $`X_{\text{max}}`$.
- For each pair $`(a, b)`$, checks that the discriminant is non-zero and that the curve satisfies the prime condition.
- Computes the $`j`$-invariant for valid curves and counts how often specific $`j`$-invariants appear.

This function finds all elliptic curves in the family $`\mathcal{E}`$ up to the given height bound and generates a dictionary of $`j`$-invariants and their frequency.

- `is_k_power_free(n, k)` Checks if the integer $`n`$ is k-power-free, meaning no prime factor of $`n`$ is raised to an exponent of $`k`$ or more in its factorization.

- `get_power_free_integers(X, k)` Generates a list of integers $`d`$ such that $`d`$ is $`k`$-power-free and $`|d| \leq X`$.

- `Get_Distribution_J_invariants_in_family_ET(Xmax)`
Computes the distribution of $`j`$-invariants the family $`\mathcal{ET}`$, focusing on curves that have *complex multiplication* (CM).

**Steps**:
- Starts with a list of fixed elliptic curves corresponding to known $`j`$-invariants.
- For each fixed curve, scales the coefficients by integers $`d`$, which are filtered to be $`k`$-power-free, where $`k`$ depends on the $`j`$-invariant.
- For each scaled elliptic curve, checks whether the curve has CM and counts the number of CM curves for each $`j`$-invariant.

This code can be run sequentially or in parallel. We recommend to use the parallelized version for larger values of $X$. This code imports the SageMath library `sage` to compute factorizations and $`j`$-invariants.

2024