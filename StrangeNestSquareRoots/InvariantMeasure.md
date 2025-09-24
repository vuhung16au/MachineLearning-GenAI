The invariant measure of the mapping $T(x) = 2x\sqrt{1-x^2}$ on the interval $[0, 1]$ is given by the density function $p(x) = \frac{2}{\pi\sqrt{1-x^2}}$ with respect to the Lebesgue measure, i.e., $d\mu(x) = \frac{2}{\pi\sqrt{1-x^2}}dx$.

You can verify this by using the **Perron-Frobenius operator**, also known as the transfer operator. An invariant density $p(x)$ for a map $T(x)$ must satisfy the equation $p(y) = \sum_{x \in T^{-1}(y)} \frac{p(x)}{|T'(x)|}$, where the sum is over all preimages of $y$.

1.  **Find the preimages:** For a given $y \in (0, 1)$, the equation $y = 2x\sqrt{1-x^2}$ has two solutions for $x$, which are the preimages of $y$:
    $x_1 = \sqrt{\frac{1+\sqrt{1-y^2}}{2}}$ and $x_2 = \sqrt{\frac{1-\sqrt{1-y^2}}{2}}$.

2.  **Calculate the derivative:** The derivative of the map is $T'(x) = \frac{2-4x^2}{\sqrt{1-x^2}}$.

3.  **Substitute into the transfer operator equation:** If we propose the invariant density $p(x) = \frac{C}{\sqrt{1-x^2}}$ for some constant $C$, we find that the terms in the sum simplify remarkably. For the two preimages $x_1$ and $x_2$, the sum is:
    $\frac{p(x_1)}{|T'(x_1)|} + \frac{p(x_2)}{|T'(x_2)|} = \frac{C}{2\sqrt{1-y^2}} + \frac{C}{2\sqrt{1-y^2}} = \frac{C}{\sqrt{1-y^2}}$.

4.  **Confirm the result:** The result of the sum is exactly the form of the proposed density, $p(y)$, which confirms that it is an invariant density.

5.  **Normalize the density:** To be a valid probability measure, the integral of the density over the domain $[0, 1]$ must be 1.
    $\int_0^1 \frac{C}{\sqrt{1-x^2}}dx = C[\arcsin(x)]_0^1 = C(\arcsin(1)-\arcsin(0)) = C(\pi/2 - 0) = \frac{C\pi}{2}$.
    Setting this equal to 1 gives $C = \frac{2}{\pi}$.

Therefore, the invariant density is $p(x) = \frac{2}{\pi\sqrt{1-x^2}}$. This map is a specific case of a family of maps known as Chebyshev maps, for which this measure is a well-known result.
