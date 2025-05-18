**Proof without using area:**

Let $y = f(x)$. Since $f$ is monotonic on $[a, b]$, it has an inverse function $x = f^{-1}(y)$ on the interval $[f(a), f(b)]$.

Consider the expression $b \cdot f(b) - a \cdot f(a)$. We can rewrite this using integration by parts.

Recall the integration by parts formula: $\int u \, dv = uv - \int v \, du$.

Let's consider the integral $\int_{a}^{b} f(x) \, dx$. We can't directly apply integration by parts here in a helpful way to arrive at the desired form without invoking geometric intuition.

Instead, let's work with the right-hand side of the equation and try to relate it to the integrals.

Consider the function $h(x) = x f(x)$. Let's find its derivative with respect to $x$:
$$h'(x) = \frac{d}{dx} (x f(x)) = 1 \cdot f(x) + x \cdot f'(x) = f(x) + x f'(x)$$

Now, let's integrate $h'(x)$ from $a$ to $b$:
$$\int_{a}^{b} h'(x) \, dx = [h(x)]_{a}^{b} = h(b) - h(a) = b f(b) - a f(a)$$

So, we have:
$$b f(b) - a f(a) = \int_{a}^{b} (f(x) + x f'(x)) \, dx = \int_{a}^{b} f(x) \, dx + \int_{a}^{b} x f'(x) \, dx$$

Now, we need to show that $\int_{a}^{b} x f'(x) \, dx = \int_{f(a)}^{f(b)} f^{-1}(x) \, dx$.

Let's use substitution in the integral $\int_{f(a)}^{f(b)} f^{-1}(x) \, dx$.
Let $x = f(u)$, then $dx = f'(u) \, du$.
When $x = f(a)$, $u = a$.
When $x = f(b)$, $u = b$.

Substituting these into the integral:
$$\int_{f(a)}^{f(b)} f^{-1}(x) \, dx = \int_{a}^{b} f^{-1}(f(u)) f'(u) \, du = \int_{a}^{b} u f'(u) \, du$$

Replacing the dummy variable $u$ with $x$:
$$\int_{f(a)}^{f(b)} f^{-1}(x) \, dx = \int_{a}^{b} x f'(x) \, dx$$

Now, substitute this back into the equation we derived from the derivative of $h(x)$:
$$b f(b) - a f(a) = \int_{a}^{b} f(x) \, dx + \int_{a}^{b} x f'(x) \, dx = \int_{a}^{b} f(x) \, dx + \int_{f(a)}^{f(b)} f^{-1}(x) \, dx$$

This proves the theorem without explicitly using the concept of area. The proof relies on the fundamental theorem of calculus and integration by substitution.

Final Answer: The final answer is $\boxed{\int_{a}^{b} f(x) \, dx + \int_{f(a)}^{f(b)} f^{-1}(x) \, dx = b \cdot f(b) - a \cdot f(a)}$
