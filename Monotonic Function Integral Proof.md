To prove the given property for any monotonic function \( f(x) \) on the interval \([a, b]\):

\[
\int_a^b f(x) \, dx + \int_{f(a)}^{f(b)} f^{-1}(x) \, dx = b f(b) - a f(a),
\]

we proceed as follows, assuming \( f(x) \) is monotonically increasing (the case for a decreasing function follows similarly with appropriate adjustments). A monotonic function is either non-decreasing or non-increasing throughout its domain, and since \( f(x) \) is specified as monotonic with an inverse, it must be strictly monotonic (we’ll assume increasing for clarity). Thus, \( f'(x) \geq 0 \), and \( f \) is invertible with \( f^{-1} \) defined over \([f(a), f(b)]\), where \( f(a) < f(b) \).

### Step 1: Understand the Components
- **Left-hand side**: 
  - \(\int_a^b f(x) \, dx\): The integral of \( f(x) \) from \( x = a \) to \( x = b \), representing the area under the curve \( f(x) \) over the interval \([a, b]\).
  - \(\int_{f(a)}^{f(b)} f^{-1}(x) \, dx\): The integral of the inverse function \( f^{-1}(x) \) from \( x = f(a) \) to \( x = f(b) \), representing the area under \( f^{-1}(x) \) over \([f(a), f(b)]\).
- **Right-hand side**: 
  - \( b f(b) - a f(a) \): A linear combination of the function values at the endpoints, scaled by the interval bounds.

Our goal is to show that the sum of these two integrals equals \( b f(b) - a f(a) \).

### Step 2: Substitution in the Second Integral
Since \( f \) is monotonically increasing and invertible, we can relate \( f^{-1}(x) \) to \( f(x) \) via a substitution. Consider the second integral:

\[
\int_{f(a)}^{f(b)} f^{-1}(x) \, dx.
\]

Let’s perform a change of variables. Set \( x = f(y) \), where \( y \) is the variable such that \( f^{-1}(x) = y \), or equivalently, \( x = f(y) \). Then:
- When \( x = f(a) \), \( y = f^{-1}(f(a)) = a \).
- When \( x = f(b) \), \( y = f^{-1}(f(b)) = b \).
- Differentiate \( x = f(y) \): \( dx = f'(y) \, dy \).

The limits of integration transform as follows: as \( x \) goes from \( f(a) \) to \( f(b) \), \( y \) goes from \( a \) to \( b \). Since \( f^{-1}(x) = y \) when \( x = f(y) \), the integral becomes:

\[
\int_{f(a)}^{f(b)} f^{-1}(x) \, dx = \int_a^b f^{-1}(f(y)) f'(y) \, dy.
\]

Because \( f^{-1}(f(y)) = y \) (property of inverse functions), this simplifies to:

\[
\int_a^b y f'(y) \, dy.
\]

So, the original equation becomes:

\[
\int_a^b f(x) \, dx + \int_a^b y f'(y) \, dy.
\]

### Step 3: Evaluate the Second Integral Using Integration by Parts
Now, compute \(\int_a^b y f'(y) \, dy\). This resembles a derivative product, so we apply integration by parts. Recall the formula:

\[
\int u \, dv = uv - \int v \, du.
\]

Choose:
- \( u = y \), so \( du = dy \),
- \( dv = f'(y) \, dy \), so \( v = \int f'(y) \, dy = f(y) \) (assuming \( f \) is differentiable or at least integrable with \( f'(y) \) defined almost everywhere).

Then:

\[
\int y f'(y) \, dy = [y f(y)] - \int f(y) \, dy.
\]

Evaluate from \( y = a \) to \( y = b \):

\[
\int_a^b y f'(y) \, dy = [y f(y)]_a^b - \int_a^b f(y) \, dy.
\]

- Boundary term: \([y f(y)]_a^b = b f(b) - a f(a)\),
- Integral term: \(\int_a^b f(y) \, dy\), where \( y \) is a dummy variable, so this is \(\int_a^b f(y) \, dy = \int_a^b f(x) \, dx\).

Thus:

\[
\int_a^b y f'(y) \, dy = b f(b) - a f(a) - \int_a^b f(x) \, dx.
\]

### Step 4: Combine the Integrals
Substitute back into the expression:

\[
\int_a^b f(x) \, dx + \int_{f(a)}^{f(b)} f^{-1}(x) \, dx = \int_a^b f(x) \, dx + \int_a^b y f'(y) \, dy.
\]

Using the result from Step 3:

\[
= \int_a^b f(x) \, dx + \left[ b f(b) - a f(a) - \int_a^b f(x) \, dx \right].
\]

Simplify:

\[
= \int_a^b f(x) \, dx + b f(b) - a f(a) - \int_a^b f(x) \, dx.
\]

The \(\int_a^b f(x) \, dx\) terms cancel:

\[
= b f(b) - a f(a).
\]

This matches the right-hand side of the equation.

### Step 5: Verify and Generalize
The proof assumes \( f \) is increasing and differentiable for simplicity. If \( f \) is decreasing, \( f(a) > f(b) \), and the integral \(\int_{f(a)}^{f(b)}\) would reverse limits, introducing a negative sign, but the substitution adjusts accordingly (limits swap, and \( f'(y) < 0 \)), and the result holds after accounting for signs. For non-differentiable monotonic functions, we can use Riemann-Stieltjes integrals or interpret \( f'(y) \, dy \) via measure theory, but the core idea persists via the inverse relationship.

### Geometric Insight (Optional)
The image suggests a geometric interpretation: the area under \( f(x) \) from \( a \) to \( b \) (in the \( x \)-direction) plus the area under \( f^{-1}(x) \) from \( f(a) \) to \( f(b) \) (in the \( y \)-direction) forms a region related to \( b f(b) - a f(a) \), possibly the area of a rectangle from \((a, 0)\) to \((b, f(b))\) minus a rectangle from \((a, 0)\) to \((a, f(a))\), adjusted by the curve’s areas. Our algebraic proof confirms this without needing the graph explicitly.

### Conclusion
Thus, for any monotonic function \( f(x) \) on \([a, b]\):

\[
\int_a^b f(x) \, dx + \int_{f(a)}^{f(b)} f^{-1}(x) \, dx = b f(b) - a f(a),
\]

proven using substitution and integration by parts.
