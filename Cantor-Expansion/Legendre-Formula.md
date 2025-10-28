# Legendre's Formula

Legendre's formula, named after the French mathematician Adrien-Marie Legendre, is a fundamental result in number theory that provides an elegant way to determine the highest power of a prime number that divides a factorial. This formula is essential for understanding the prime factorization of factorials and has numerous applications in combinatorics, number theory, and computational mathematics.

---

## Definition of Legendre's Formula

For any prime number $p$ and positive integer $n$, Legendre's formula states that the exponent of $p$ in the prime factorization of $n!$ is given by:

$$\nu_p(n!) = \sum_{k=1}^{\infty} \left\lfloor \frac{n}{p^k} \right\rfloor$$

Where:
- $\nu_p(n!)$ denotes the exponent of prime $p$ in the factorization of $n!$
- $\left\lfloor \frac{n}{p^k} \right\rfloor$ is the floor function, which gives the greatest integer less than or equal to $\frac{n}{p^k}$
- The sum is taken over all positive integers $k$, but in practice, it terminates when $p^k > n$

### Alternative Formulation

The formula can also be written as:

$$\nu_p(n!) = \left\lfloor \frac{n}{p} \right\rfloor + \left\lfloor \frac{n}{p^2} \right\rfloor + \left\lfloor \frac{n}{p^3} \right\rfloor + \cdots$$

This form makes it clear that we're counting:
1. Multiples of $p$ in the range $[1, n]$ (contribution of $p$)
2. Multiples of $p^2$ in the range $[1, n]$ (contribution of $p^2$)
3. Multiples of $p^3$ in the range $[1, n]$ (contribution of $p^3$)
4. And so on...

---

## Examples

### Example 1: Finding the exponent of 2 in 10!

Let's find how many times 2 appears in the prime factorization of $10! = 10 \times 9 \times 8 \times \cdots \times 1$.

Using Legendre's formula with $p = 2$ and $n = 10$:

$$\nu_2(10!) = \left\lfloor \frac{10}{2} \right\rfloor + \left\lfloor \frac{10}{4} \right\rfloor + \left\lfloor \frac{10}{8} \right\rfloor + \left\lfloor \frac{10}{16} \right\rfloor + \cdots$$

Calculating each term:
- $\left\lfloor \frac{10}{2} \right\rfloor = \left\lfloor 5 \right\rfloor = 5$ (multiples of 2: 2, 4, 6, 8, 10)
- $\left\lfloor \frac{10}{4} \right\rfloor = \left\lfloor 2.5 \right\rfloor = 2$ (multiples of 4: 4, 8)
- $\left\lfloor \frac{10}{8} \right\rfloor = \left\lfloor 1.25 \right\rfloor = 1$ (multiples of 8: 8)
- $\left\lfloor \frac{10}{16} \right\rfloor = \left\lfloor 0.625 \right\rfloor = 0$ (no multiples of 16)

Therefore: $\nu_2(10!) = 5 + 2 + 1 + 0 = 8$

### Example 2: Finding the exponent of 3 in 15!

For $p = 3$ and $n = 15$:

$$\nu_3(15!) = \left\lfloor \frac{15}{3} \right\rfloor + \left\lfloor \frac{15}{9} \right\rfloor + \left\lfloor \frac{15}{27} \right\rfloor + \cdots$$

Calculating:
- $\left\lfloor \frac{15}{3} \right\rfloor = 5$ (multiples of 3: 3, 6, 9, 12, 15)
- $\left\lfloor \frac{15}{9} \right\rfloor = 1$ (multiples of 9: 9)
- $\left\lfloor \frac{15}{27} \right\rfloor = 0$ (no multiples of 27)

Therefore: $\nu_3(15!) = 5 + 1 + 0 = 6$

### Example 3: Complete prime factorization of 12!

Let's find the complete prime factorization of $12!$:

For each prime $p \leq 12$ (primes: 2, 3, 5, 7, 11):

- $\nu_2(12!) = \left\lfloor \frac{12}{2} \right\rfloor + \left\lfloor \frac{12}{4} \right\rfloor + \left\lfloor \frac{12}{8} \right\rfloor = 6 + 3 + 1 = 10$
- $\nu_3(12!) = \left\lfloor \frac{12}{3} \right\rfloor + \left\lfloor \frac{12}{9} \right\rfloor = 4 + 1 = 5$
- $\nu_5(12!) = \left\lfloor \frac{12}{5} \right\rfloor = 2$
- $\nu_7(12!) = \left\lfloor \frac{12}{7} \right\rfloor = 1$
- $\nu_{11}(12!) = \left\lfloor \frac{12}{11} \right\rfloor = 1$

Therefore: $12! = 2^{10} \times 3^5 \times 5^2 \times 7^1 \times 11^1$

---

## Applications

### 1. Combinatorics and Binomial Coefficients

Legendre's formula is crucial for determining when binomial coefficients $\binom{n}{k} = \frac{n!}{k!(n-k)!}$ are divisible by a prime $p$. This is essential in:

- **Lucas' Theorem**: Determining $\binom{n}{k} \bmod p$ for prime $p$
- **Kummer's Theorem**: Finding the highest power of $p$ dividing $\binom{n}{k}$
- **Pascal's Triangle**: Understanding divisibility patterns

### 2. Number Theory

- **Prime Number Theory**: Analyzing the distribution of primes in factorials
- **Divisibility Problems**: Determining when $n!$ is divisible by specific powers of primes
- **Arithmetic Functions**: Computing functions like $\omega(n!)$ (number of distinct prime factors)

### 3. Computational Mathematics

- **Algorithm Design**: Efficient algorithms for computing large factorials modulo primes
- **Cryptography**: Applications in RSA and other cryptographic systems
- **Computer Science**: Analysis of algorithms involving factorials

### 4. Probability and Statistics

- **Stirling's Approximation**: Understanding the asymptotic behavior of factorials
- **Combinatorial Probability**: Calculating probabilities involving permutations and combinations

### 5. Mathematical Analysis

- **Series Convergence**: Analyzing the convergence of factorial-based series
- **Asymptotic Analysis**: Understanding the growth rate of factorials

---

## Conclusions

Legendre's formula is a cornerstone of number theory that elegantly connects prime numbers with factorials through a simple yet powerful relationship. Its applications span across multiple branches of mathematics, from pure number theory to practical computational problems.

### Key Insights:

1. **Efficiency**: The formula provides an efficient way to compute prime exponents in factorials without actually computing the factorial itself.

2. **Universality**: It works for any prime and any positive integer, making it universally applicable.

3. **Combinatorial Significance**: The formula reveals deep connections between prime factorization and combinatorial structures.

4. **Computational Importance**: It enables efficient algorithms for problems involving large factorials and their divisibility properties.

### Modern Relevance:

In today's computational world, Legendre's formula remains highly relevant for:
- Cryptography and security applications
- Algorithm optimization
- Mathematical software development
- Research in number theory and combinatorics

The beauty of Legendre's formula lies in its simplicity and power—a single equation that unlocks the structure of factorials and connects fundamental concepts in mathematics. It serves as a perfect example of how elegant mathematical results can have far-reaching applications across diverse fields of study.
