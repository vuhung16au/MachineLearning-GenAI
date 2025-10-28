# Cantor's Expansion (Factoradic Representation)

## Overview

This document introduces the concept of **Cantor's expansion**, also known as the **factoradic representation** or **factorial number system**. This unique mathematical tool provides a powerful way to represent any non-negative integer or real number using factorials as the varying "place values" or bases. Beyond its theoretical elegance, Cantor's expansion has fascinating applications in combinatorics, number theory, and computer science, and presents some intriguing mathematical challenges to explore.

## Definition

### Cantor's Expansion of an Integer

For any positive integer $N$, its Cantor's expansion is a unique sum of the form:

$$N = a_n \cdot n! + a_{n-1} \cdot (n-1)! + \cdots + a_2 \cdot 2! + a_1 \cdot 1!$$

The key constraints that make this representation **unique** are the conditions on the coefficients (or "digits"), $a_k$:

- The coefficients $a_k$ are **integers**.
- $0 \le a_k \le k$ for $k \ge 1$.
  - Specifically, $0 \le a_1 \le 1$, $0 \le a_2 \le 2$, $0 \le a_3 \le 3$, and so on.

Unlike the standard base-10 system where the place values are $1, 10, 100, \ldots$ (powers of 10) and the digits are $0-9$, the factoradic system uses factorials $1!, 2!, 3!, \ldots$ as place values, and the maximum digit in the $k!$ position is $k$.

### Cantor's Expansion of a Real Number

The concept extends to real numbers $x$ in the interval $[0, 1)$ as an infinite series:

$$x = \sum_{k=1}^{\infty} \frac{a_k}{k!} = \frac{a_1}{1!} + \frac{a_2}{2!} + \frac{a_3}{3!} + \cdots$$

Here, the coefficients $a_k$ must satisfy:
- $a_k$ are integers.
- $0 \le a_k \le k - 1$ for $k \ge 1$.
  - Specifically, $a_1=0$, $0 \le a_2 \le 1$, $0 \le a_3 \le 2$, and so on.

This representation is also unique, except for rational numbers of the form $\frac{m}{n!}$, which have two possible expansions (analogous to $0.5 = 0.4\bar{9}$ in base 10).

## Examples

### Example 1: Find the Cantor's expansion of 50

To find the Cantor's expansion of $N=50$:

1. **Find the largest factorial less than 50:** $4! = 24$.
2. **Divide by $4!$:**
   $$50 = \mathbf{2} \cdot 4! + 2 \quad \implies \quad a_4 = 2$$
3. **Divide the remainder (2) by $3!$ (6):**
   $$2 = \mathbf{0} \cdot 3! + 2 \quad \implies \quad a_3 = 0$$
4. **Divide the remainder (2) by $2!$ (2):**
   $$2 = \mathbf{1} \cdot 2! + 0 \quad \implies \quad a_2 = 1$$
5. **Divide the remainder (0) by $1!$ (1):**
   $$0 = \mathbf{0} \cdot 1! + 0 \quad \implies \quad a_1 = 0$$

Thus, the Cantor's expansion of $50$ is $2 \cdot 4! + 0 \cdot 3! + 1 \cdot 2! + 0 \cdot 1!$. This is often written in positional notation as $\mathbf{(2, 0, 1, 0)}_{!}$.

### Example 2: Find the Cantor's expansion of 0.5

For the rational number $0.5$:

Since $0.5 = \frac{1}{2} = \frac{1}{2!}$, we can write:
$$0.5 = \frac{1}{2!} = \frac{1}{1!} - \frac{1}{2!} + \frac{1}{3!} - \frac{1}{4!} + \cdots$$

However, the standard Cantor expansion for $0.5$ is:
$$0.5 = \frac{1}{2!} + \frac{0}{3!} + \frac{0}{4!} + \cdots$$

This demonstrates the non-uniqueness for rational numbers of the form $\frac{m}{n!}$.

## Advanced Example

### Find the Cantor's expansion of a real number 0.1116

To find the Cantor's expansion of $0.1116$:

We need to find coefficients $a_k$ such that:
$$0.1116 = \sum_{k=1}^{\infty} \frac{a_k}{k!}$$

where $0 \le a_k \le k-1$ for $k \ge 1$.

**Step-by-step calculation:**

1. $a_1 = 0$ (since $a_1$ must be 0)
2. For $a_2$: $0 \le a_2 \le 1$
   - If $a_2 = 0$: $\frac{0}{2!} = 0$
   - If $a_2 = 1$: $\frac{1}{2!} = 0.5 > 0.1116$
   - So $a_2 = 0$

3. For $a_3$: $0 \le a_3 \le 2$
   - If $a_3 = 0$: $\frac{0}{3!} = 0$
   - If $a_3 = 1$: $\frac{1}{3!} = 0.1667 > 0.1116$
   - So $a_3 = 0$

4. For $a_4$: $0 \le a_4 \le 3$
   - If $a_4 = 0$: $\frac{0}{4!} = 0$
   - If $a_4 = 1$: $\frac{1}{4!} = 0.0417 < 0.1116$
   - If $a_4 = 2$: $\frac{2}{4!} = 0.0833 < 0.1116$
   - If $a_4 = 3$: $\frac{3}{4!} = 0.125 > 0.1116$
   - So $a_4 = 2$

Continuing this process, we find the Cantor's expansion of $0.1116$ begins as:
$$0.1116 = \frac{0}{1!} + \frac{0}{2!} + \frac{0}{3!} + \frac{2}{4!} + \frac{3}{5!} + \frac{4}{6!} + \cdots$$

## Fun Facts about Cantor's Expansion

1. **Uniqueness**: Cantor's expansion is unique for integers and almost all real numbers. The only exceptions are rational numbers of the form $\frac{m}{n!}$, which have exactly two representations.

2. **Bijection with Natural Numbers**: Cantor's expansion establishes a bijection between the set of natural numbers and the set of real numbers in $[0,1)$. This is a fundamental result in set theory.

3. **Bijection with Permutations**: Cantor's expansion provides a bijection between the set of permutations of $n$ elements and the set of natural numbers from $0$ to $n!-1$. This is the basis for the Lehmer code in combinatorics.

## Applications of Cantor's Expansion

1. **Combinatorics**: Cantor's expansion is used to map permutations to a unique number and vice versa. This is sometimes called the **Lehmer code** or **inversion vector**. For $n$ items, there are $n!$ possible permutations, and the Cantor expansion of an integer $N$ where $0 \le N < n!$ gives a unique sequence of digits that corresponds to the $(N+1)$-th permutation in lexicographical order.

2. **Number Theory**: Cantor's expansion is used to study the properties of numbers, particularly in the context of factorial bases and their relationship to prime numbers and divisibility.

3. **Computer Science**: Cantor's expansion is used to represent numbers in a compact way, especially in algorithms that need to efficiently encode and decode permutations or sequences.

## Problems


### Problem 1: Cantor's expansion of $\frac{1}{2025^{1000}}$ in base 10

Given: 
$$\frac{1}{2025^{1000}} = a_1 + \frac{a_2}{2!} + \frac{a_3}{3!} + \cdots + \frac{a_n}{n!}$$

We are given the following conditions:
1.  $n$ is a **positive integer**.
2.  $a_1, a_2, \ldots, a_n$ are **nonnegative integers**.
3.  $a_k < k$ for $k = 2, \ldots, n$.
4.  $a_n > 0$.

This is the Cantor's expansion of the fraction $\frac{1}{2025^{1000}}$.
Find n.

## Conclusion

Cantor's expansion is a powerful tool for representing and manipulating numbers in a unique and efficient way. Its applications span from pure mathematics to practical computer science, offering elegant solutions to problems involving permutations, number representation, and combinatorial algorithms. The factorial number system provides a fascinating alternative to traditional positional notation, revealing deep connections between number theory, combinatorics, and real analysis.

The challenges presented by the advanced problems show that while Cantor's expansion is theoretically elegant, practical implementation requires careful consideration of computational precision and algorithmic efficiency, especially when dealing with extreme values.

---

*This project explores the mathematical beauty and practical applications of Cantor's expansion, providing both theoretical understanding and computational challenges for further exploration.*
