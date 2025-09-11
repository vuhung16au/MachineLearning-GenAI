# Gamma and Beta Functions

## Why Gamma/Beta Functions?

### 1. Deeper Understanding of Bayesian Methods
- **Conjugate Priors**: Beta for Bernoulli/Binomial, Gamma for Poisson/Exponential
- **Posterior Distributions**: Normalization constants in Bayesian inference
- **Dirichlet Distribution**: Essential for topic modeling and NLP
- **Hierarchical Models**: Parameters with distributions

### 2. Mathematical Beauty
- Connect factorials, trigonometric integrals, and complex analysis
- **Creative Applications**: Elegant solutions to complex problems

## Gamma Function $\Gamma(z)$

The Gamma function is a fundamental special function that extends the factorial function to complex numbers. It is defined as:

$$\Gamma(z) = \int_0^{\infty} t^{z-1} e^{-t} dt$$

**Key Properties:**
- **Factorial relationship:** $\Gamma(n) = (n-1)!$ for positive integers $n$
- **Recursive relation:** $\Gamma(z+1) = z\Gamma(z)$
- **Reflection formula:** $\Gamma(z)\Gamma(1-z) = \frac{\pi}{\sin(\pi z)}$
- **Special values:** $\Gamma(1/2) = \sqrt{\pi}$, $\Gamma(1) = 1$

## Proof: $\Gamma(1) = 1$

Let us prove that $\Gamma(1) = 1$ using the definition of the Gamma function.

**Given:** The Gamma function is defined as:
$$\Gamma(z) = \int_0^{\infty} t^{z-1} e^{-t} dt$$

**To prove:** $\Gamma(1) = 1$

**Proof:**
Substituting $z = 1$ into the definition:

$$\Gamma(1) = \int_0^{\infty} t^{1-1} e^{-t} dt = \int_0^{\infty} t^0 e^{-t} dt = \int_0^{\infty} e^{-t} dt$$

Now we evaluate this integral:

$$\Gamma(1) = \int_0^{\infty} e^{-t} dt = \left[-e^{-t}\right]_0^{\infty}$$

Evaluating at the limits:
- At $t = \infty$: $-e^{-\infty} = -0 = 0$ (since $e^{-\infty} = 0$)
- At $t = 0$: $-e^{-0} = -e^0 = -1$

Therefore:
$$\Gamma(1) = 0 - (-1) = 0 + 1 = 1$$

**Conclusion:** $\Gamma(1) = 1$ ✓

This result is fundamental because it establishes the base case for the factorial relationship $\Gamma(n) = (n-1)!$ when $n = 1$.

## Proof: $\Gamma(n + 1) = n\Gamma(n) = n!$

Let us prove the recursive relation and its connection to the factorial function.

**Given:** The Gamma function is defined as:
$$\Gamma(n) = \int_0^{\infty} t^{n-1} e^{-t} dt$$

**To prove:** $\Gamma(n + 1) = n\Gamma(n) = n!$

**Proof:**

### Step 1: Derive $\Gamma(n + 1)$

Substituting $n = n + 1$ into the definition:

$$\Gamma(n + 1) = \int_0^{\infty} t^{(n+1)-1} e^{-t} dt = \int_0^{\infty} t^n e^{-t} dt \quad \text{(1.2)}$$

### Step 2: Integration by Parts

We evaluate $\int_0^{\infty} t^n e^{-t} dt$ using integration by parts:
$$\int u \, dv = uv - \int v \, du$$

Let:
- $u = t^n$ → $du = n t^{n-1} dt$
- $dv = e^{-t} dt$ → $v = -e^{-t}$

Applying integration by parts:

$$\Gamma(n + 1) = \left[t^n (-e^{-t})\right]_0^{\infty} - \int_0^{\infty} (-e^{-t}) \cdot n t^{n-1} dt$$

$$\Gamma(n + 1) = \left[-t^n e^{-t}\right]_0^{\infty} + n \int_0^{\infty} t^{n-1} e^{-t} dt$$

### Step 3: Evaluate the Boundary Terms

The first term $\left[-t^n e^{-t}\right]_0^{\infty}$ evaluates to:
- At $t = \infty$: $\lim_{t \to \infty} (-t^n e^{-t}) = 0$ (exponential decay dominates polynomial growth)
- At $t = 0$: $-0^n e^{-0} = 0$

Therefore: $\left[-t^n e^{-t}\right]_0^{\infty} = 0 - 0 = 0$

### Step 4: Complete the Recursive Relation

Substituting back:

$$\Gamma(n + 1) = 0 + n \int_0^{\infty} t^{n-1} e^{-t} dt = n \int_0^{\infty} t^{n-1} e^{-t} dt$$

But $\int_0^{\infty} t^{n-1} e^{-t} dt = \Gamma(n)$ by definition, so:

$$\Gamma(n + 1) = n\Gamma(n) \quad \text{(1.3)}$$

### Step 5: Derive the Factorial Relationship

Using the recursive property repeatedly:

$$\Gamma(n + 1) = n\Gamma(n) = n(n-1)\Gamma(n-1) = n(n-1)(n-2)\Gamma(n-2)$$

Continuing this process:

$$\Gamma(n + 1) = n(n-1)(n-2) \cdots 3 \cdot 2 \cdot 1 \cdot \Gamma(1)$$

Since $\Gamma(1) = 1$ (proven above):

$$\Gamma(n + 1) = n(n-1)(n-2) \cdots 3 \cdot 2 \cdot 1 = n! \quad \text{(1.4)}$$

### Step 6: Examples

```python
# Examples of the factorial relationship
import math

# Verify the relationship for small integers
for n in range(1, 6):
    gamma_n_plus_1 = math.gamma(n + 1)
    factorial_n = math.factorial(n)
    print(f"Γ({n+1}) = {gamma_n_plus_1}, {n}! = {factorial_n}")
    print(f"Γ({n+1}) = {n}! ✓" if gamma_n_plus_1 == factorial_n else "Error!")
```

**Results:**
- $\Gamma(2) = 1! = 1$
- $\Gamma(3) = 2! = 2$  
- $\Gamma(4) = 3! = 6$
- $\Gamma(5) = 4! = 24$
- $\Gamma(6) = 5! = 120$

### Step 7: Alternative Form

From equation (1.3), we can also write:
$$\Gamma(n) = \frac{\Gamma(n + 1)}{n}$$

**Conclusion:** $\Gamma(n + 1) = n\Gamma(n) = n!$ ✓

This establishes the fundamental connection between the Gamma function and factorials, showing that the Gamma function is indeed a continuous extension of the factorial function.

## Prove that: 

$$\Gamma(n) = z^n \int_0^{\infty} e^{-zx} x^{n-1} dx$$

Let us prove this alternative integral representation of the Gamma function.

**Given:** The standard Gamma function definition:
$$\Gamma(n) = \int_0^{\infty} e^{-x} x^{n-1} dx \quad \text{(1.1)}$$

**To prove:** $\Gamma(n) = z^n \int_0^{\infty} e^{-zx} x^{n-1} dx$ where $n, z > 0$

**Proof:**

### Step 1: Change of Variables

Let $x = zy$, then $dx = z \, dy$

The limits remain unchanged: when $x = 0$, $y = 0$; when $x = \infty$, $y = \infty$

### Step 2: Substitution

Substituting into equation (1.1):

$$\Gamma(n) = \int_0^{\infty} e^{-zy} (zy)^{n-1} z \, dy$$

### Step 3: Simplification

Expanding $(zy)^{n-1}$ and combining terms:

$$\Gamma(n) = \int_0^{\infty} e^{-zy} z^{n-1} y^{n-1} z \, dy$$

$$\Gamma(n) = \int_0^{\infty} e^{-zy} z^n y^{n-1} \, dy$$

Since $z^n$ is constant with respect to $y$:

$$\Gamma(n) = z^n \int_0^{\infty} e^{-zy} y^{n-1} \, dy \quad \text{(1.5)}$$

### Step 4: Dummy Variable Property

For definite integrals, the choice of integration variable doesn't affect the result:
$$\int_a^b f(x) \, dx = \int_a^b f(y) \, dy \quad \text{(1.6)}$$

### Step 5: Conclusion

Applying the dummy variable property to equation (1.5):

$$\Gamma(n) = z^n \int_0^{\infty} e^{-zx} x^{n-1} \, dx \quad \text{(1.7)}$$

**Conclusion:** $\Gamma(n) = z^n \int_0^{\infty} e^{-zx} x^{n-1} dx$ ✓

This alternative representation is useful in various applications, particularly when working with exponential distributions and Laplace transforms.

## Proof: $\Gamma(n) = \int_0^1 (\log(1/y))^{n-1} dy$

Let us prove this alternative integral representation of the Gamma function.

**Given:** The standard Gamma function definition:
$$\Gamma(n) = \int_0^{\infty} e^{-x} x^{n-1} dx \quad \text{(1.8)}$$

**To prove:** $\Gamma(n) = \int_0^1 (\log(1/y))^{n-1} dy$

**Proof:**

### Step 1: Change of Variables

Let $x = \log(1/y)$, then:
$$e^x = 1/y \implies y = e^{-x}$$

### Step 2: Find the Differential

Differentiating $y = e^{-x}$:
$$dy = -e^{-x} dx$$

Therefore:
$$dx = -\frac{dy}{e^{-x}} = -\frac{dy}{y}$$

### Step 3: Change the Limits

When $x = 0$: $y = e^{-0} = 1$
When $x = \infty$: $y = e^{-\infty} = 0$

So the limits change from $[0, \infty]$ to $[1, 0]$.

### Step 4: Substitute into the Integral

Substituting into equation (1.8):
$$\Gamma(n) = \int_1^0 e^{-x} x^{n-1} dx = \int_1^0 y \cdot (\log(1/y))^{n-1} \cdot \left(-\frac{dy}{y}\right)$$

### Step 5: Simplify

$$\Gamma(n) = \int_1^0 -(\log(1/y))^{n-1} dy$$

### Step 6: Reverse Limits

To remove the negative sign, reverse the limits:
$$\Gamma(n) = -\int_1^0 (\log(1/y))^{n-1} dy = \int_0^1 (\log(1/y))^{n-1} dy$$

**Conclusion:** $\Gamma(n) = \int_0^1 (\log(1/y))^{n-1} dy$ ✓

This form is particularly useful in probability theory and statistics where integrals over $[0,1]$ are common.

## Example: Calculate $\int_0^{\infty} e^{-4x} x^{5/2} dx$

Let us evaluate this integral using the Gamma function.

**Given integral:**
$$\int_0^{\infty} e^{-4x} x^{5/2} dx$$

**Solution using Gamma function:**

### Step 1: Apply the Alternative Gamma Representation

From our previous proof, we know:
$$\Gamma(n) = z^n \int_0^{\infty} e^{-zx} x^{n-1} dx$$

### Step 2: Identify Parameters

Comparing with our integral:
- $z = 4$ (coefficient of $x$ in the exponential)
- $n - 1 = \frac{5}{2}$ → $n = \frac{5}{2} + 1 = \frac{7}{2}$

### Step 3: Apply the Formula

$$\Gamma\left(\frac{7}{2}\right) = 4^{7/2} \int_0^{\infty} e^{-4x} x^{5/2} dx$$

### Step 4: Solve for the Integral

$$\int_0^{\infty} e^{-4x} x^{5/2} dx = \frac{\Gamma\left(\frac{7}{2}\right)}{4^{7/2}}$$

### Step 5: Calculate $\Gamma\left(\frac{7}{2}\right)$

Using the recursive property $\Gamma(n+1) = n\Gamma(n)$:

$$\Gamma\left(\frac{7}{2}\right) = \frac{5}{2} \cdot \Gamma\left(\frac{5}{2}\right) = \frac{5}{2} \cdot \frac{3}{2} \cdot \Gamma\left(\frac{3}{2}\right) = \frac{5}{2} \cdot \frac{3}{2} \cdot \frac{1}{2} \cdot \Gamma\left(\frac{1}{2}\right)$$

Since $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$:

$$\Gamma\left(\frac{7}{2}\right) = \frac{5}{2} \cdot \frac{3}{2} \cdot \frac{1}{2} \cdot \sqrt{\pi} = \frac{15\sqrt{\pi}}{8}$$

### Step 6: Final Answer

$$\int_0^{\infty} e^{-4x} x^{5/2} dx = \frac{15\sqrt{\pi}}{8 \cdot 4^{7/2}} = \frac{15\sqrt{\pi}}{8 \cdot 128} = \frac{15\sqrt{\pi}}{1024}$$

**Answer:** $\int_0^{\infty} e^{-4x} x^{5/2} dx = \frac{15\sqrt{\pi}}{1024}$ ✓

## Example: Prove Legendre's Duplication Formula

**Problem:** Prove that 

$$\Gamma\left(\frac{1}{2}\right)\Gamma(2n) = 2^{2n-1}\Gamma(n)\Gamma\left(n + \frac{1}{2}\right)$$

**Solution:**

### Step 1: Expand $\Gamma\left(n + \frac{1}{2}\right)$

Using the recursive property $\Gamma(z+1) = z\Gamma(z)$:

$$\Gamma\left(n + \frac{1}{2}\right) = \left(n - \frac{1}{2}\right)\Gamma\left(n - \frac{1}{2}\right)$$

### Step 2: Continue Recursive Application

$$\Gamma\left(n + \frac{1}{2}\right) = \left(n - \frac{1}{2}\right)\left(n - \frac{3}{2}\right)\Gamma\left(n - \frac{3}{2}\right)$$

Continuing this process:

$$\Gamma\left(n + \frac{1}{2}\right) = \left(n - \frac{1}{2}\right)\left(n - \frac{3}{2}\right)\left(n - \frac{5}{2}\right) \cdots \Gamma\left(\frac{1}{2}\right)$$

### Step 3: Rewrite with Common Denominator

$$\Gamma\left(n + \frac{1}{2}\right) = \frac{2n-1}{2} \cdot \frac{2n-3}{2} \cdot \frac{2n-5}{2} \cdots \frac{1}{2} \cdot \Gamma\left(\frac{1}{2}\right)$$

### Step 4: Express as Product of Odd Numbers

$$\Gamma\left(n + \frac{1}{2}\right) = \frac{(2n-1)(2n-3)(2n-5) \cdots 1}{2^n} \Gamma\left(\frac{1}{2}\right)$$

### Step 5: Multiply and Divide by Even Numbers

Multiply numerator and denominator by $2n(2n-2)(2n-4) \cdots 4 \cdot 2$:

$$\Gamma\left(n + \frac{1}{2}\right) = \frac{(2n-1)(2n-3) \cdots 1 \cdot 2n(2n-2) \cdots 4 \cdot 2}{2^n \cdot 2n(2n-2) \cdots 4 \cdot 2} \Gamma\left(\frac{1}{2}\right)$$

### Step 6: Simplify

$$\Gamma\left(n + \frac{1}{2}\right) = \frac{(2n)!}{2^n \cdot 2^n n!} \Gamma\left(\frac{1}{2}\right) = \frac{(2n)!}{2^{2n} n!} \Gamma\left(\frac{1}{2}\right)$$

### Step 7: Prove the Identity

Now, starting with the left side:

$$\Gamma\left(\frac{1}{2}\right)\Gamma(2n) = \Gamma\left(\frac{1}{2}\right) \cdot (2n-1)!$$

Using our result from Step 6:

$$\Gamma\left(\frac{1}{2}\right)\Gamma(2n) = \Gamma\left(\frac{1}{2}\right) \cdot (2n-1)! = \Gamma\left(\frac{1}{2}\right) \cdot \frac{(2n)!}{2n}$$

And from Step 6:

$$\Gamma\left(n + \frac{1}{2}\right) = \frac{(2n)!}{2^{2n} n!} \Gamma\left(\frac{1}{2}\right)$$

Therefore:

$$\Gamma\left(\frac{1}{2}\right)\Gamma(2n) = \Gamma\left(\frac{1}{2}\right) \cdot \frac{(2n)!}{2n} = \frac{(2n)!}{2^{2n} n!} \Gamma\left(\frac{1}{2}\right) \cdot \frac{2^{2n} n!}{2n}$$

$$= \Gamma\left(n + \frac{1}{2}\right) \cdot \frac{2^{2n-1} n!}{n} = 2^{2n-1}\Gamma(n)\Gamma\left(n + \frac{1}{2}\right)$$

**Answer:** $\Gamma\left(\frac{1}{2}\right)\Gamma(2n) = 2^{2n-1}\Gamma(n)\Gamma\left(n + \frac{1}{2}\right)$ ✓

This is Legendre's Duplication Formula, which relates Gamma functions at different arguments.

## Example: Prove 

$$\int_0^1 x^m (\log x)^n dx = \frac{(-1)^n n!}{(m+1)^{n+1}}$$

**Solution:**

### Step 1: Define the Integral

Let $I = \int_0^1 x^m (\log x)^n dx$

### Step 2: First Substitution

Let $x = e^{-y}$, then:
- $\log x = -y$
- $dx = -e^{-y} dy$

### Step 3: Change Limits

When $x = 0$: $e^{-y} = 0 \implies y = \infty$
When $x = 1$: $e^{-y} = 1 \implies y = 0$

### Step 4: Transform the Integral

$$I = \int_{\infty}^0 (e^{-y})^m (-y)^n (-e^{-y}) dy$$

$$I = \int_{\infty}^0 e^{-my} (-1)^n y^n (-e^{-y}) dy$$

$$I = (-1)^n \int_{\infty}^0 e^{-(m+1)y} y^n (-1) dy$$

Reversing limits (using the negative sign):

$$I = (-1)^n \int_0^{\infty} e^{-(m+1)y} y^n dy$$

### Step 5: Second Substitution

Let $(m+1)y = u$, then:
- $y = \frac{u}{m+1}$
- $dy = \frac{du}{m+1}$

### Step 6: Final Transformation

$$I = (-1)^n \int_0^{\infty} e^{-u} \left(\frac{u}{m+1}\right)^n \frac{du}{m+1}$$

$$I = (-1)^n \int_0^{\infty} e^{-u} \frac{u^n}{(m+1)^n} \frac{du}{m+1}$$

$$I = \frac{(-1)^n}{(m+1)^{n+1}} \int_0^{\infty} e^{-u} u^n du$$

### Step 7: Recognize Gamma Function

The integral $\int_0^{\infty} e^{-u} u^n du = \Gamma(n+1) = n!$ (for non-negative integers $n$)

### Step 8: Final Answer

$$I = \frac{(-1)^n}{(m+1)^{n+1}} \cdot n! = \frac{(-1)^n n!}{(m+1)^{n+1}}$$

**Answer:** $\int_0^1 x^m (\log x)^n dx = \frac{(-1)^n n!}{(m+1)^{n+1}}$ ✓

This result is useful in probability theory and statistics, particularly when dealing with logarithmic transformations.

## Example: Show that $2 \cdot 4 \cdot 6 \cdots 2n = 2^n \Gamma(n + 1)$

**Problem:** Show that $2 \cdot 4 \cdot 6 \cdots 2n = 2^n \Gamma(n + 1)$

**Solution:**

### Step 1: Define the Left-Hand Side

$$LHS = 2 \cdot 4 \cdot 6 \cdots 2n$$

### Step 2: Factor Out Powers of 2

Each term in the product can be written as $2$ times an integer:
- $2 = 2 \cdot 1$
- $4 = 2 \cdot 2$  
- $6 = 2 \cdot 3$
- $\vdots$
- $2n = 2 \cdot n$

Therefore:
$$LHS = (2 \cdot 1) \cdot (2 \cdot 2) \cdot (2 \cdot 3) \cdots (2 \cdot n)$$

### Step 3: Factor Out $2^n$

Since there are $n$ factors of $2$:
$$LHS = 2^n \cdot (1 \cdot 2 \cdot 3 \cdots n)$$

### Step 4: Recognize the Factorial

The product $(1 \cdot 2 \cdot 3 \cdots n) = n!$

$$LHS = 2^n \cdot n!$$

### Step 5: Apply Gamma Function Property

Using the property $\Gamma(n + 1) = n!$:

$$LHS = 2^n \cdot \Gamma(n + 1) = RHS$$

**Answer:** $2 \cdot 4 \cdot 6 \cdots 2n = 2^n \Gamma(n + 1)$ ✓

This identity is useful in combinatorics and probability theory, particularly when dealing with products of even numbers.

## Example: Show that $1 \cdot 3 \cdot 5 \cdots (2n-1) = \frac{2^{1-n} \Gamma(2n)}{\Gamma(n)}$

**Problem:** Show that $1 \cdot 3 \cdot 5 \cdots (2n-1) = \frac{2^{1-n} \Gamma(2n)}{\Gamma(n)}$

**Solution:**

### Step 1: Define the Left-Hand Side

$$LHS = 1 \cdot 3 \cdot 5 \cdots (2n-1)$$

### Step 2: Introduce Even Numbers

Multiply numerator and denominator by the product of even numbers $2 \cdot 4 \cdot 6 \cdots 2n$:

$$LHS = \frac{1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdots (2n-1) \cdot 2n}{2 \cdot 4 \cdot 6 \cdots 2n}$$

### Step 3: Express in Terms of Factorials

The numerator is $(2n)!$ and the denominator is $2^n n!$ (from the previous example):

$$LHS = \frac{(2n)!}{2^n n!}$$

### Step 4: Convert Factorials to Gamma Functions

Using the property $\Gamma(z+1) = z\Gamma(z)$:
- $(2n)! = 2n \cdot \Gamma(2n)$
- $n! = n \cdot \Gamma(n)$

Therefore:
$$LHS = \frac{2n \cdot \Gamma(2n)}{2^n \cdot n \cdot \Gamma(n)}$$

### Step 5: Simplify

$$LHS = \frac{2n \cdot \Gamma(2n)}{2^n \cdot n \cdot \Gamma(n)} = \frac{2 \cdot \Gamma(2n)}{2^n \cdot \Gamma(n)} = \frac{2^{1-n} \Gamma(2n)}{\Gamma(n)} = RHS$$

**Answer:** $1 \cdot 3 \cdot 5 \cdots (2n-1) = \frac{2^{1-n} \Gamma(2n)}{\Gamma(n)}$ ✓

This identity is useful in combinatorics and probability theory, particularly when dealing with products of odd numbers and their relationship to Gamma functions.

## Example: Evaluate in terms of Gamma Function 

$$\int_0^{\infty} e^{-ax} x^{m-1} \sin(bx) dx$$ 

**Solution:**

### Step 1: Define the Integral

$$I = \int_0^{\infty} e^{-ax} x^{m-1} \sin(bx) dx$$

### Step 2: Express $\sin(bx)$ using Euler's Formula

Using $\sin(bx) = \frac{e^{ibx} - e^{-ibx}}{2i}$:

$$I = \int_0^{\infty} e^{-ax} x^{m-1} \frac{e^{ibx} - e^{-ibx}}{2i} dx$$

### Step 3: Split into Two Integrals

$$I = \frac{1}{2i} \left[ \int_0^{\infty} e^{-ax} x^{m-1} e^{ibx} dx - \int_0^{\infty} e^{-ax} x^{m-1} e^{-ibx} dx \right]$$

### Step 4: Combine Exponential Terms

$$I = \frac{1}{2i} \left[ \int_0^{\infty} e^{-(a-ib)x} x^{m-1} dx - \int_0^{\infty} e^{-(a+ib)x} x^{m-1} dx \right]$$

### Step 5: Apply Gamma Function Formula

Using $\int_0^{\infty} e^{-zx} x^{m-1} dx = \frac{\Gamma(m)}{z^m}$:

$$I = \frac{1}{2i} \left[ \frac{\Gamma(m)}{(a-ib)^m} - \frac{\Gamma(m)}{(a+ib)^m} \right]$$

### Step 6: Factor Out $\Gamma(m)$

$$I = \frac{\Gamma(m)}{2i} \left[ \frac{1}{(a-ib)^m} - \frac{1}{(a+ib)^m} \right]$$

### Step 7: Simplify the Complex Expression

$$I = \frac{\Gamma(m)}{2i} \left[ \frac{(a+ib)^m - (a-ib)^m}{(a-ib)^m (a+ib)^m} \right]$$

Since $(a-ib)(a+ib) = a^2 + b^2$:

$$I = \frac{\Gamma(m)}{2i} \cdot \frac{(a+ib)^m - (a-ib)^m}{(a^2 + b^2)^m}$$

### Step 8: Express in Terms of Modulus and Argument

Let $a + ib = \sqrt{a^2 + b^2} e^{i\theta}$ where $\theta = \arctan(b/a)$

Then $(a+ib)^m = (a^2 + b^2)^{m/2} e^{im\theta}$ and $(a-ib)^m = (a^2 + b^2)^{m/2} e^{-im\theta}$

$$I = \frac{\Gamma(m)}{2i} \cdot \frac{(a^2 + b^2)^{m/2} (e^{im\theta} - e^{-im\theta})}{(a^2 + b^2)^m}$$

$$I = \frac{\Gamma(m)}{2i} \cdot \frac{e^{im\theta} - e^{-im\theta}}{(a^2 + b^2)^{m/2}}$$

### Step 9: Final Answer

Since $e^{im\theta} - e^{-im\theta} = 2i\sin(m\theta)$:

$$I = \frac{\Gamma(m)}{2i} \cdot \frac{2i\sin(m\theta)}{(a^2 + b^2)^{m/2}} = \frac{\Gamma(m) \sin(m\theta)}{(a^2 + b^2)^{m/2}}$$

where $\theta = \arctan(b/a)$

**Answer:** $\int_0^{\infty} e^{-ax} x^{m-1} \sin(bx) dx = \frac{\Gamma(m) \sin(m\theta)}{(a^2 + b^2)^{m/2}}$ where $\theta = \arctan(b/a)$ ✓

This result is useful in Laplace transforms and probability theory involving exponential distributions with sinusoidal components.

## Example: Prove 

$$\int_0^{\infty} \frac{x^a}{a^x} dx = \frac{\Gamma(a+1)}{(\log a)^{a+1}}$$

**Solution:**

### Step 1: Define the Integral

Let $I = \int_0^{\infty} \frac{x^a}{a^x} dx$

### Step 2: Express $a^x$ in Exponential Form

Taking logarithm on both sides of $a^x$:
$$\log(a^x) = x \log a$$

Taking exponential of both sides:
$$e^{\log(a^x)} = e^{x \log a}$$

Therefore: $a^x = e^{x \log a}$

### Step 3: Substitute into the Integral

$$I = \int_0^{\infty} \frac{x^a}{e^{x \log a}} dx = \int_0^{\infty} x^a e^{-x \log a} dx$$

### Step 4: Change of Variables

Let $x \log a = z$, then:
- $x = \frac{z}{\log a}$
- $dx = \frac{dz}{\log a}$

The limits remain from $0$ to $\infty$ for $z$.

### Step 5: Apply Substitution

$$I = \int_0^{\infty} \left(\frac{z}{\log a}\right)^a e^{-z} \frac{dz}{\log a}$$

### Step 6: Simplify

$$I = \int_0^{\infty} \frac{z^a}{(\log a)^a} e^{-z} \frac{dz}{\log a}$$

$$I = \frac{1}{(\log a)^a \cdot (\log a)} \int_0^{\infty} z^a e^{-z} dz$$

$$I = \frac{1}{(\log a)^{a+1}} \int_0^{\infty} z^a e^{-z} dz$$

### Step 7: Recognize Gamma Function

The integral $\int_0^{\infty} z^a e^{-z} dz = \Gamma(a+1)$

Therefore:
$$I = \frac{1}{(\log a)^{a+1}} \Gamma(a+1) = \frac{\Gamma(a+1)}{(\log a)^{a+1}}$$

**Answer:** $\int_0^{\infty} \frac{x^a}{a^x} dx = \frac{\Gamma(a+1)}{(\log a)^{a+1}}$ ✓

This result is useful in advanced calculus and special functions, demonstrating how the Gamma function can evaluate integrals involving exponential and power functions.

## Example: Prove 

$$ \Gamma(n) \Gamma(-n) = -\frac{\pi}{n \sin(n\pi)}$$

where $n$ is not an integer.

**Solution:**

### Step 1: Use Weierstrass Infinite Product for $1/\Gamma(z)$

The Weierstrass product for $1/\Gamma(z)$ is:
$$\frac{1}{\Gamma(z)} = z e^{\gamma z} \prod_{m=1}^{\infty} \left(1 + \frac{z}{m}\right) e^{-z/m}$$

where $\gamma$ is the Euler-Mascheroni constant.

### Step 2: Express $1/\Gamma(n)$ and $1/\Gamma(-n)$

For $z=n$:
$$\frac{1}{\Gamma(n)} = n e^{\gamma n} \prod_{m=1}^{\infty} \left(1 + \frac{n}{m}\right) e^{-n/m}$$

For $z=-n$:
$$\frac{1}{\Gamma(-n)} = (-n) e^{-\gamma n} \prod_{m=1}^{\infty} \left(1 - \frac{n}{m}\right) e^{n/m}$$

### Step 3: Multiply the Expressions

$$\frac{1}{\Gamma(n)\Gamma(-n)} = \left(n e^{\gamma n} \prod_{m=1}^{\infty} \left(1 + \frac{n}{m}\right) e^{-n/m}\right) \cdot \left(-n e^{-\gamma n} \prod_{m=1}^{\infty} \left(1 - \frac{n}{m}\right) e^{n/m}\right)$$

### Step 4: Simplify the Product

$$\frac{1}{\Gamma(n)\Gamma(-n)} = -n^2 e^{\gamma n - \gamma n} \prod_{m=1}^{\infty} \left(1 + \frac{n}{m}\right) \left(1 - \frac{n}{m}\right) e^{-n/m + n/m}$$

$$\frac{1}{\Gamma(n)\Gamma(-n)} = -n^2 \prod_{m=1}^{\infty} \left(1 - \frac{n^2}{m^2}\right)$$

### Step 5: Apply the Sine Product Formula

Recall the infinite product expansion for the sine function:
$$\frac{\sin(\pi z)}{\pi z} = \prod_{m=1}^{\infty} \left(1 - \frac{z^2}{m^2}\right)$$

Substituting $z=n$:
$$\prod_{m=1}^{\infty} \left(1 - \frac{n^2}{m^2}\right) = \frac{\sin(n\pi)}{n\pi}$$

### Step 6: Substitute and Conclude

$$\frac{1}{\Gamma(n)\Gamma(-n)} = -n^2 \left(\frac{\sin(n\pi)}{n\pi}\right) = -\frac{n \sin(n\pi)}{\pi}$$

Therefore, inverting both sides:
$$\Gamma(n)\Gamma(-n) = -\frac{\pi}{n \sin(n\pi)}$$

**Answer:** $\Gamma(n) \Gamma(-n) = -\frac{\pi}{n \sin(n\pi)}$ ✓

This identity is fundamental in complex analysis and demonstrates the deep connection between the Gamma function and trigonometric functions.

## Other Forms of Gamma Functions

The Gamma function can be expressed in several equivalent forms, each with its own advantages in different mathematical contexts.

### 1. Integral Form (Standard Definition)

The Gamma function is most commonly defined by the integral form:

$$\Gamma(n) = \int_0^{\infty} x^{n-1} e^{-x} dx, \quad n > 0$$

This is the standard definition we have been using throughout our examples.

### 2. Euler's Form

Euler's form of the Gamma function is given as:

$$\Gamma(n) = \lim_{m \to \infty} \frac{1 \cdot 2 \cdot 3 \cdots m}{n(n+1)\cdots(n+m)} m^n \quad \text{(1.10)}$$

where $n$ is neither zero nor a negative number.

This form is particularly useful in number theory and combinatorics, as it directly relates to factorials and products of integers.

### 3. Weierstrass' Infinite Product Definition

Weierstrass' infinite product definition of the Gamma function is:

$$\frac{1}{\Gamma(n)} = n e^{rn} \prod_{m=1}^{\infty} \left(1 + \frac{n}{m}\right) e^{-n/m} \quad \text{(1.11)}$$

where $r$ is Euler's constant (also known as the Euler-Mascheroni constant):

$$r = \lim_{m \to \infty} \left(1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{m} - \ln m\right) = 0.577216 \ldots$$

This form is particularly useful in complex analysis and the study of analytic continuation of the Gamma function.

### Equivalence of Forms

The integral, Euler's, and Weierstrass' forms of the Gamma function are equivalent to one another. To prove this equivalence, consider the integral:

$$\int_0^m \left(1 - \frac{x}{m}\right)^m x^{n-1} dx$$

Taking the limit as $m \to \infty$:

$$\lim_{m \to \infty} \int_0^m \left(1 - \frac{x}{m}\right)^m x^{n-1} dx = \int_0^{\infty} \lim_{m \to \infty} \left(1 - \frac{x}{m}\right)^m x^{n-1} dx \quad \text{(1.12)}$$

Since $\lim_{m \to \infty} \left(1 - \frac{x}{m}\right)^m = e^{-x}$, this integral becomes:

$$\int_0^{\infty} e^{-x} x^{n-1} dx = \Gamma(n)$$

This demonstrates the connection between Euler's form and the standard integral definition.

### Applications of Different Forms

- **Integral Form**: Best for computational purposes and integration techniques
- **Euler's Form**: Useful for asymptotic analysis and factorial relationships
- **Weierstrass' Form**: Essential for complex analysis and analytic continuation

Each form provides different insights into the properties and behavior of the Gamma function, making them valuable tools in various branches of mathematics.

# Beta Function $B(\alpha, \beta)$

The Beta function is a special function that appears in the normalization constants of the Beta and Dirichlet distributions. It is defined as:

$$B(\alpha, \beta) = \int_0^1 t^{\alpha-1}(1-t)^{\beta-1} dt$$

### Simple Examples of Beta Function Calculations

Let us evaluate some specific values of the Beta function using the integral definition.

#### Example 1: $B(1, 1)$

$$B(1, 1) = \int_0^1 t^{1-1}(1-t)^{1-1} dt = \int_0^1 t^0 (1-t)^0 dt = \int_0^1 dt = [t]_0^1 = 1$$

**Answer:** $B(1, 1) = 1$ ✓

#### Example 2: $B(2, 3)$

$$B(2, 3) = \int_0^1 t^{2-1}(1-t)^{3-1} dt = \int_0^1 t (1-t)^2 dt$$

Expanding $(1-t)^2 = 1 - 2t + t^2$:

$$B(2, 3) = \int_0^1 t(1 - 2t + t^2) dt = \int_0^1 (t - 2t^2 + t^3) dt$$

$$B(2, 3) = \left[\frac{t^2}{2} - \frac{2t^3}{3} + \frac{t^4}{4}\right]_0^1 = \frac{1}{2} - \frac{2}{3} + \frac{1}{4} = \frac{6 - 8 + 3}{12} = \frac{1}{12}$$

**Answer:** $B(2, 3) = \frac{1}{12}$ ✓

#### Example 3: $B(3, 2)$

$$B(3, 2) = \int_0^1 t^{3-1}(1-t)^{2-1} dt = \int_0^1 t^2 (1-t) dt$$

$$B(3, 2) = \int_0^1 (t^2 - t^3) dt = \left[\frac{t^3}{3} - \frac{t^4}{4}\right]_0^1 = \frac{1}{3} - \frac{1}{4} = \frac{4 - 3}{12} = \frac{1}{12}$$

**Answer:** $B(3, 2) = \frac{1}{12}$ ✓

Note that $B(2, 3) = B(3, 2) = \frac{1}{12}$, demonstrating the symmetry property $B(\alpha, \beta) = B(\beta, \alpha)$.

#### Example 4: $B\left(\frac{1}{2}, \frac{1}{2}\right)$

$$B\left(\frac{1}{2}, \frac{1}{2}\right) = \int_0^1 t^{-\frac{1}{2}}(1-t)^{-\frac{1}{2}} dt = \int_0^1 \frac{1}{\sqrt{t(1-t)}} dt$$

Using the substitution $t = \sin^2 \theta$, $dt = 2\sin\theta\cos\theta d\theta$:

$$B\left(\frac{1}{2}, \frac{1}{2}\right) = \int_0^{\pi/2} \frac{2\sin\theta\cos\theta}{\sin\theta\cos\theta} d\theta = \int_0^{\pi/2} 2 d\theta = \pi$$

**Answer:** $B\left(\frac{1}{2}, \frac{1}{2}\right) = \pi$ ✓

These examples demonstrate how the Beta function can be evaluated directly from its integral definition for specific parameter values.

## Properties of Beta Function

In evaluating integrals, the following three properties of the Beta function are widely used:

### Property (a): Symmetry of Beta Function

$$B(m, n) = B(n, m)$$

**Proof:** This follows directly from the definition by interchanging the variables in the integral:

$$B(m, n) = \int_0^1 t^{m-1}(1-t)^{n-1} dt$$

Let $u = 1-t$, then $t = 1-u$ and $dt = -du$. When $t = 0$, $u = 1$; when $t = 1$, $u = 0$.

$$B(m, n) = \int_1^0 (1-u)^{m-1} u^{n-1} (-du) = \int_0^1 u^{n-1}(1-u)^{m-1} du = B(n, m)$$

### Property (b): Integral Representation

$$B(m, n) = \int_0^{\infty} \frac{x^{n-1}}{(1+x)^{m+n}} dx = \int_0^{\infty} \frac{x^{m-1}}{(1+x)^{m+n}} dx$$

**Proof:** Starting with the standard definition and using the substitution $t = \frac{x}{1+x}$:

Let $t = \frac{x}{1+x}$, then $1-t = \frac{1}{1+x}$ and $dt = \frac{dx}{(1+x)^2}$.

When $t = 0$, $x = 0$; when $t = 1$, $x = \infty$.

$$B(m, n) = \int_0^1 t^{m-1}(1-t)^{n-1} dt = \int_0^{\infty} \left(\frac{x}{1+x}\right)^{m-1} \left(\frac{1}{1+x}\right)^{n-1} \frac{dx}{(1+x)^2}$$

$$= \int_0^{\infty} \frac{x^{m-1}}{(1+x)^{m-1}} \cdot \frac{1}{(1+x)^{n-1}} \cdot \frac{dx}{(1+x)^2} = \int_0^{\infty} \frac{x^{m-1}}{(1+x)^{m+n}} dx$$

The second form follows from the symmetry property.

### Property (c): Trigonometric Integral Representation

$$B(m, n) = 2 \int_0^{\pi/2} (\sin \theta)^{2m-1} (\cos \theta)^{2n-1} d\theta$$

**Proof:** Using the substitution $t = \sin^2 \theta$ in the standard definition:

Let $t = \sin^2 \theta$, then $1-t = \cos^2 \theta$ and $dt = 2\sin\theta\cos\theta d\theta$.

When $t = 0$, $\theta = 0$; when $t = 1$, $\theta = \pi/2$.

$$B(m, n) = \int_0^1 t^{m-1}(1-t)^{n-1} dt = \int_0^{\pi/2} (\sin^2 \theta)^{m-1} (\cos^2 \theta)^{n-1} \cdot 2\sin\theta\cos\theta d\theta$$

$$= 2 \int_0^{\pi/2} (\sin \theta)^{2m-2} (\cos \theta)^{2n-2} \sin\theta\cos\theta d\theta = 2 \int_0^{\pi/2} (\sin \theta)^{2m-1} (\cos \theta)^{2n-1} d\theta$$

These three properties provide different ways to express and evaluate the Beta function, making it a versatile tool in integral calculus.

## Relationship Between Gamma and Beta Functions

Beta function and Gamma function can be related by the fundamental relationship:

$$B(m, n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m + n)} \quad \text{for } m > 0, n > 0 \quad \text{(3.1)}$$

This relation is quite useful for finding definite results in integral evaluation.

### Proof: $B(m, n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m + n)}$

**Given:** The standard Gamma function definition:
$$\Gamma(n) = \int_0^{\infty} e^{-x} x^{n-1} dx$$

**To prove:** $B(m, n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m + n)}$

**Proof:**

### Step 1: Use Alternative Gamma Function Property

From the alternative Gamma function property:
$$\Gamma(n) = z^n \int_0^{\infty} e^{-zx} x^{n-1} dx \quad \text{(i)}$$

Rearranging:
$$\frac{\Gamma(n)}{z^n} = \int_0^{\infty} e^{-zx} x^{n-1} dx \quad \text{(ii)}$$

### Step 2: Multiply by $e^{-z} z^{m-1}$ and Integrate

Multiply both sides of equation (i) by $e^{-z} z^{m-1}$ and integrate with respect to $z$ from $0$ to $\infty$:

$$\Gamma(n) \int_0^{\infty} e^{-z} z^{m-1} dz = \int_0^{\infty} e^{-z} z^{m-1} \left[z^n \int_0^{\infty} e^{-zx} x^{n-1} dx\right] dz$$

### Step 3: Simplify Left Side

The left side becomes:
$$\Gamma(n) \int_0^{\infty} e^{-z} z^{m-1} dz = \Gamma(n) \Gamma(m)$$

### Step 4: Form Double Integral on Right Side

$$\Gamma(n) \Gamma(m) = \int_0^{\infty} \int_0^{\infty} e^{-z(1+x)} z^{m+n-1} x^{n-1} dx \, dz$$

### Step 5: Change Order of Integration

$$\Gamma(n) \Gamma(m) = \int_0^{\infty} x^{n-1} \left[\int_0^{\infty} e^{-z(1+x)} z^{m+n-1} dz\right] dx$$

### Step 6: Evaluate Inner Integral

Using equation (ii) with $z(1+x)$ as the parameter:
$$\int_0^{\infty} e^{-z(1+x)} z^{m+n-1} dz = \frac{\Gamma(m+n)}{(1+x)^{m+n}}$$

### Step 7: Substitute and Recognize Beta Function

$$\Gamma(n) \Gamma(m) = \int_0^{\infty} x^{n-1} \left[\frac{\Gamma(m+n)}{(1+x)^{m+n}}\right] dx$$

$$\Gamma(n) \Gamma(m) = \Gamma(m+n) \int_0^{\infty} \frac{x^{n-1}}{(1+x)^{m+n}} dx$$

The integral $\int_0^{\infty} \frac{x^{n-1}}{(1+x)^{m+n}} dx$ is the integral representation of $B(m, n)$.

Therefore:
$$\Gamma(n) \Gamma(m) = \Gamma(m+n) B(m, n)$$

**Conclusion:** $B(m, n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m + n)}$ ✓

This fundamental relationship allows us to express Beta functions in terms of Gamma functions, making calculations more tractable.

## Example: Show that 

$$2 \int_0^{\pi/2} \sin^p \theta \cos^q \theta d\theta = \frac{\Gamma\left(\frac{p+1}{2}\right) \Gamma\left(\frac{q+1}{2}\right)}{\Gamma\left(\frac{p+q+2}{2}\right)}$$ 

and hence show 

$$ \Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$$

**Solution:**

### Step 1: Use the Relationship Between Beta and Gamma Functions

From the relation of Beta and Gamma function:
$$B(m, n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n)} \quad \text{(i)}$$

### Step 2: Use Property of Beta Function (Trigonometric Form)

From the properties of Beta function (property c):
$$B(m, n) = 2 \int_0^{\pi/2} (\sin \theta)^{2m-1} (\cos \theta)^{2n-1} d\theta \quad \text{(ii)}$$

### Step 3: Equate (i) and (ii)

Therefore from equations (i) and (ii):
$$2 \int_0^{\pi/2} (\sin \theta)^{2m-1} (\cos \theta)^{2n-1} d\theta = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n)} \quad \text{(iii)}$$

### Step 4: Make Substitution for Powers

Let:
- $2m-1 = p$ and $2n-1 = q$
- Therefore: $m = \frac{p+1}{2}$ and $n = \frac{q+1}{2}$

### Step 5: Substitute into Equation (iii)

Substituting the expressions for $m$ and $n$ into equation (iii):

$$2 \int_0^{\pi/2} (\sin \theta)^p (\cos \theta)^q d\theta = \frac{\Gamma\left(\frac{p+1}{2}\right) \Gamma\left(\frac{q+1}{2}\right)}{\Gamma\left(\frac{p+q+2}{2}\right)}$$

### Step 6: Derive $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$

Now putting $p = 0$ and $q = 0$, we get:

$$2 \int_0^{\pi/2} d\theta = \frac{\Gamma\left(\frac{0+1}{2}\right) \Gamma\left(\frac{0+1}{2}\right)}{\Gamma\left(\frac{0+0+2}{2}\right)}$$

$$2 \int_0^{\pi/2} d\theta = \frac{\Gamma\left(\frac{1}{2}\right) \Gamma\left(\frac{1}{2}\right)}{\Gamma(1)}$$

Evaluating the integral:
$$2 [\theta]_0^{\pi/2} = 2 \left(\frac{\pi}{2} - 0\right) = \pi$$

The right side becomes:
$$\frac{\left[\Gamma\left(\frac{1}{2}\right)\right]^2}{\Gamma(1)} = \frac{\left[\Gamma\left(\frac{1}{2}\right)\right]^2}{1} = \left[\Gamma\left(\frac{1}{2}\right)\right]^2$$

Therefore:
$$\pi = \left[\Gamma\left(\frac{1}{2}\right)\right]^2$$

Taking the square root of both sides:
$$\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$$

**Answer:** 
1. $2 \int_0^{\pi/2} \sin^p \theta \cos^q \theta d\theta = \frac{\Gamma\left(\frac{p+1}{2}\right) \Gamma\left(\frac{q+1}{2}\right)}{\Gamma\left(\frac{p+q+2}{2}\right)}$ ✓
2. $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$ ✓

This example demonstrates the power of the Beta-Gamma relationship in evaluating trigonometric integrals and deriving important special values.

## Example: Prove Legendre's Duplication Formula 

$$\Gamma(m) \Gamma\left(m + \frac{1}{2}\right) = \frac{\sqrt{\pi}}{2^{2m-1}} \Gamma(2m)$$

**Problem:** Prove that $\Gamma(m) \Gamma\left(m + \frac{1}{2}\right) = \frac{\sqrt{\pi}}{2^{2m-1}} \Gamma(2m)$ for $m > 0$

**Solution:**

### Step 1: Use the Integral Identity from Example 3.2

From equation (iii) of Example 3.2:
$$2 \int_0^{\pi/2} (\sin \theta)^{2m-1} (\cos \theta)^{2n-1} d\theta = \frac{\Gamma(m) \Gamma(n)}{\Gamma(m + n)} \quad \text{(i)}$$

### Step 2: First Substitution ($n = \frac{1}{2}$)

Putting $n = \frac{1}{2}$ in equation (i):
$$2 \int_0^{\pi/2} (\sin \theta)^{2m-1} (\cos \theta)^{2(1/2)-1} d\theta = \frac{\Gamma(m) \Gamma\left(\frac{1}{2}\right)}{\Gamma\left(m + \frac{1}{2}\right)}$$

$$2 \int_0^{\pi/2} (\sin \theta)^{2m-1} (\cos \theta)^0 d\theta = \frac{\Gamma(m) \Gamma\left(\frac{1}{2}\right)}{\Gamma\left(m + \frac{1}{2}\right)}$$

Since $(\cos \theta)^0 = 1$ and $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$:
$$2 \int_0^{\pi/2} (\sin \theta)^{2m-1} d\theta = \frac{\Gamma(m) \sqrt{\pi}}{\Gamma\left(m + \frac{1}{2}\right)} \quad \text{(ii)}$$

### Step 3: Second Substitution ($n = m$)

Putting $n = m$ in equation (i):
$$2 \int_0^{\pi/2} (\sin \theta)^{2m-1} (\cos \theta)^{2m-1} d\theta = \frac{\Gamma(m) \Gamma(m)}{\Gamma(m + m)}$$

$$2 \int_0^{\pi/2} (\sin \theta \cos \theta)^{2m-1} d\theta = \frac{[\Gamma(m)]^2}{\Gamma(2m)}$$

### Step 4: Use Trigonometric Identity

Since $\sin \theta \cos \theta = \frac{\sin(2\theta)}{2}$:
$$2 \int_0^{\pi/2} \left(\frac{\sin(2\theta)}{2}\right)^{2m-1} d\theta = \frac{[\Gamma(m)]^2}{\Gamma(2m)}$$

$$\frac{2}{2^{2m-1}} \int_0^{\pi/2} (\sin(2\theta))^{2m-1} d\theta = \frac{[\Gamma(m)]^2}{\Gamma(2m)}$$

### Step 5: Change of Variables

Let $2\theta = t$, then $d\theta = \frac{1}{2} dt$. When $\theta = 0$, $t = 0$; when $\theta = \frac{\pi}{2}$, $t = \pi$.

$$\frac{1}{2^{2m-1}} \int_0^{\pi} (\sin t)^{2m-1} dt = \frac{[\Gamma(m)]^2}{\Gamma(2m)}$$

Since $\int_0^{\pi} (\sin t)^{2m-1} dt = 2 \int_0^{\pi/2} (\sin t)^{2m-1} dt$:
$$\frac{2}{2^{2m-1}} \int_0^{\pi/2} (\sin t)^{2m-1} dt = \frac{[\Gamma(m)]^2}{\Gamma(2m)}$$

### Step 6: Equate the Two Results

From equation (ii): $2 \int_0^{\pi/2} (\sin \theta)^{2m-1} d\theta = \frac{\Gamma(m) \sqrt{\pi}}{\Gamma\left(m + \frac{1}{2}\right)}$

From Step 5: $2 \int_0^{\pi/2} (\sin t)^{2m-1} dt = 2^{2m-1} \frac{[\Gamma(m)]^2}{\Gamma(2m)}$

Since the integrals are identical (just different dummy variables):
$$\frac{\Gamma(m) \sqrt{\pi}}{\Gamma\left(m + \frac{1}{2}\right)} = 2^{2m-1} \frac{[\Gamma(m)]^2}{\Gamma(2m)}$$

### Step 7: Solve for the Desired Product

$$\Gamma(m) \sqrt{\pi} \cdot \Gamma(2m) = 2^{2m-1} [\Gamma(m)]^2 \cdot \Gamma\left(m + \frac{1}{2}\right)$$

Dividing both sides by $\Gamma(m)$:
$$\sqrt{\pi} \Gamma(2m) = 2^{2m-1} \Gamma(m) \Gamma\left(m + \frac{1}{2}\right)$$

**Answer:** $\Gamma(m) \Gamma\left(m + \frac{1}{2}\right) = \frac{\sqrt{\pi}}{2^{2m-1}} \Gamma(2m)$ ✓

This is Legendre's Duplication Formula, which is fundamental in the theory of special functions and has important applications in number theory and mathematical physics.

## Example: Prove $B(m, n) = B(m, n + 1) + B(m + 1, n)$

**Problem:** Prove that 

$$B(m, n) = B(m, n + 1) + B(m + 1, n)$$

**Solution:**

### Step 1: Use the Definition of Beta Function

We know that:
$$B(m, n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m + n)}$$

### Step 2: Expand the Right-Hand Side

Now $B(m, n + 1) + B(m + 1, n) =$

$$= \frac{\Gamma(m)\Gamma(n + 1)}{\Gamma(m + n + 1)} + \frac{\Gamma(m + 1)\Gamma(n)}{\Gamma(m + n + 1)}$$

### Step 3: Apply Gamma Function Recursive Property

Using $\Gamma(z + 1) = z\Gamma(z)$:
- $\Gamma(n + 1) = n\Gamma(n)$
- $\Gamma(m + 1) = m\Gamma(m)$
- $\Gamma(m + n + 1) = (m + n)\Gamma(m + n)$

Substituting:
$$= \frac{\Gamma(m) \cdot n\Gamma(n)}{(m + n)\Gamma(m + n)} + \frac{m\Gamma(m) \cdot \Gamma(n)}{(m + n)\Gamma(m + n)}$$

### Step 4: Factor Out Common Terms

$$= \frac{\Gamma(m)\Gamma(n)}{\Gamma(m + n)} \left[\frac{n}{m + n} + \frac{m}{m + n}\right]$$

### Step 5: Simplify the Bracketed Expression

$$\frac{n}{m + n} + \frac{m}{m + n} = \frac{n + m}{m + n} = 1$$

### Step 6: Final Result

Therefore:
$$B(m, n + 1) + B(m + 1, n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m + n)} \cdot 1 = B(m, n)$$

**Answer:** $B(m, n) = B(m, n + 1) + B(m + 1, n)$ ✓

This identity is useful in establishing recursive relationships for Beta functions and has applications in probability theory and combinatorics.

## Example: Prove $\frac{B(m+1, n)}{m} = \frac{B(m, n+1)}{n} = \frac{B(m, n)}{m+n}$

**Problem:** Prove that 

$$ \frac{B(m+1, n)}{m} = \frac{B(m, n+1)}{n} = \frac{B(m, n)}{m+n}$$

**Solution:**

### Step 1: Use the Definition of Beta Function

We know that:
$$B(m, n) = \frac{\Gamma(m)\Gamma(n)}{\Gamma(m+n)} \quad \text{(i)}$$

### Step 2: Prove $\frac{B(m+1, n)}{m} = \frac{B(m, n)}{m+n}$

Now:
$$\frac{B(m+1, n)}{m} = \frac{1}{m} \cdot \frac{\Gamma(m+1)\Gamma(n)}{\Gamma(m+n+1)}$$

Using the recursive property $\Gamma(z+1) = z\Gamma(z)$:
- $\Gamma(m+1) = m\Gamma(m)$
- $\Gamma(m+n+1) = (m+n)\Gamma(m+n)$

Substituting:
$$= \frac{1}{m} \cdot \frac{m\Gamma(m)\Gamma(n)}{(m+n)\Gamma(m+n)} = \frac{\Gamma(m)\Gamma(n)}{(m+n)\Gamma(m+n)} = \frac{B(m, n)}{m+n} \quad \text{(ii)}$$

### Step 3: Prove $\frac{B(m, n+1)}{n} = \frac{B(m, n)}{m+n}$

Now:
$$\frac{B(m, n+1)}{n} = \frac{1}{n} \cdot \frac{\Gamma(m)\Gamma(n+1)}{\Gamma(m+n+1)}$$

Using the recursive property:
- $\Gamma(n+1) = n\Gamma(n)$
- $\Gamma(m+n+1) = (m+n)\Gamma(m+n)$

Substituting:
$$= \frac{1}{n} \cdot \frac{\Gamma(m) \cdot n\Gamma(n)}{(m+n)\Gamma(m+n)} = \frac{\Gamma(m)\Gamma(n)}{(m+n)\Gamma(m+n)} = \frac{B(m, n)}{m+n} \quad \text{(iii)}$$

### Step 4: Conclusion

From equations (i), (ii), and (iii), we get:
$$\frac{B(m+1, n)}{m} = \frac{B(m, n+1)}{n} = \frac{B(m, n)}{m+n}$$

**Answer:** $\frac{B(m+1, n)}{m} = \frac{B(m, n+1)}{n} = \frac{B(m, n)}{m+n}$ ✓

This identity demonstrates the symmetry and recursive properties of the Beta function and is useful in various applications involving Beta function calculations.

## Example: Evaluate 

$$ \int_0^1 x^5 (1-x^3)^{10} dx$$

**Solution:**

### Step 1: Define the Integral and Beta Function

Let the given integral be $I$:
$$I = \int_0^1 x^5 (1-x^3)^{10} dx$$

The Beta function is defined as:
$$B(m, n) = \int_0^1 t^{m-1}(1-t)^{n-1} dt \quad \text{(i)}$$

### Step 2: Apply Substitution

To transform the integral into the Beta function form, let $x^3 = y$. Then:
- $3x^2 dx = dy$
- $dx = \frac{dy}{3x^2} = \frac{dy}{3y^{2/3}}$

Also, $x^5 = (y^{1/3})^5 = y^{5/3}$.

### Step 3: Change Limits of Integration

- When $x = 0$, $y = 0$
- When $x = 1$, $y = 1$

The limits remain from 0 to 1.

### Step 4: Substitute into the Integral

$$I = \int_0^1 y^{5/3} (1-y)^{10} \frac{dy}{3y^{2/3}}$$

### Step 5: Simplify the Integral

$$I = \frac{1}{3} \int_0^1 y^{5/3 - 2/3} (1-y)^{10} dy$$

$$I = \frac{1}{3} \int_0^1 y^1 (1-y)^{10} dy$$

### Step 6: Express in Terms of Beta Function

Comparing with the Beta function definition:
- $m-1 = 1 \implies m = 2$
- $n-1 = 10 \implies n = 11$

Therefore:
$$I = \frac{1}{3} B(2, 11)$$

**Answer:** $\int_0^1 x^5 (1-x^3)^{10} dx = \frac{1}{3} B(2, 11)$ ✓

This example demonstrates how substitution can transform complex integrals into standard Beta function form for evaluation.

## Example: Evaluate using Gamma Function

$$\int_0^{\infty} e^{-x^2} dx$$ 

**Solution:**

### Step 1: Define the Integral

Let $I = \int_0^{\infty} e^{-x^2} dx$

### Step 2: Use the Alternative Gamma Function Representation

From the alternative Gamma function property:
$$\Gamma(n) = z^n \int_0^{\infty} e^{-zx} x^{n-1} dx$$

### Step 3: Apply to Our Integral

For our integral, we need to match the form $e^{-x^2}$. Let's use the substitution $u = x^2$:
- $du = 2x dx$
- $dx = \frac{du}{2x} = \frac{du}{2\sqrt{u}}$

When $x = 0$, $u = 0$; when $x = \infty$, $u = \infty$.

### Step 4: Transform the Integral

$$I = \int_0^{\infty} e^{-u} \frac{du}{2\sqrt{u}} = \frac{1}{2} \int_0^{\infty} e^{-u} u^{-1/2} du$$

### Step 5: Recognize the Gamma Function

The integral $\int_0^{\infty} e^{-u} u^{-1/2} du$ is in the form of the Gamma function:
$$\Gamma(n) = \int_0^{\infty} e^{-u} u^{n-1} du$$

For our case: $n-1 = -\frac{1}{2} \implies n = \frac{1}{2}$

Therefore:
$$\int_0^{\infty} e^{-u} u^{-1/2} du = \Gamma\left(\frac{1}{2}\right)$$

### Step 6: Use the Known Value

We know that $\Gamma\left(\frac{1}{2}\right) = \sqrt{\pi}$.

### Step 7: Final Answer

$$I = \frac{1}{2} \Gamma\left(\frac{1}{2}\right) = \frac{1}{2} \sqrt{\pi} = \frac{\sqrt{\pi}}{2}$$

**Answer:** $\int_0^{\infty} e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$ ✓

This result is fundamental in probability theory and statistics, particularly in the context of the normal distribution.

**Key Properties:**
- **Symmetry:** $B(\alpha, \beta) = B(\beta, \alpha)$
- **Relationship to Gamma function:** $B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$
- **Recursive relation:** $B(\alpha+1, \beta) = \frac{\alpha}{\alpha+\beta} B(\alpha, \beta)$

**Multivariate Beta Function:**
For the Dirichlet distribution, the multivariate Beta function is defined as:

$$B(\boldsymbol{\alpha}) = \frac{\prod_{i=1}^K \Gamma(\alpha_i)}{\Gamma\left(\sum_{i=1}^K \alpha_i\right)}$$

where $\boldsymbol{\alpha} = (\alpha_1, \alpha_2, \ldots, \alpha_K)$ is a vector of positive parameters.

## Relationship Between Gamma and Beta Functions

The Gamma and Beta functions are intimately connected through several fundamental relationships:

### 1. Fundamental Relationship
The most important connection is given by:

$$B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$$

This formula allows us to express the Beta function entirely in terms of Gamma functions, making it possible to compute Beta function values using Gamma function implementations.

### 2. Derivation from Gamma Functions
The Beta function can be derived from Gamma functions through the following integral representation:

$$B(\alpha, \beta) = \int_0^{\infty} \frac{t^{\alpha-1}}{(1+t)^{\alpha+\beta}} dt = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$$

### 3. Applications in Probability Theory
This relationship is crucial in probability theory because:

- **Beta Distribution:** The Beta distribution's normalization constant is $1/B(\alpha, \beta)$
- **Dirichlet Distribution:** The multivariate Beta function $B(\boldsymbol{\alpha})$ normalizes the Dirichlet distribution
- **Bayesian Inference:** Both functions appear in conjugate prior relationships

### 4. Computational Advantages
Using the Gamma-Beta relationship provides computational benefits:

```python
# Example: Computing Beta function using Gamma functions
import math

def beta_function(alpha, beta):
    """Compute Beta function using Gamma function relationship"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

# Example usage
result = beta_function(2, 3)  # B(2, 3) = Γ(2)Γ(3)/Γ(5) = 1!2!/4! = 1/12
```

The Beta function ensures that probability distributions integrate to 1, making them proper probability density functions.
