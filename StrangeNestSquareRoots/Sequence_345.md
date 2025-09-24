# Sequence Computation for Pythagorean Triple (3, 4, 5)

Starting with $x_0 = \frac{3}{5}$ from the Pythagorean triple $(3, 4, 5)$.

Using the recurrence relation: $x_{{k+1}} = 2x_k\sqrt{{1 - x_k^2}}$

For a Pythagorean triple $(p, r, q)$ where $p^2 + r^2 = q^2$, if $x_k = \frac{p}{q}$, then:
$x_{{k+1}} = \frac{{2pr}}{{q^2}}$

## Sequence Values

- $x_{0} = \frac{3}{5}$ (from Pythagorean triple $(3, 4, 5)$)
- $x_{1} = \frac{24}{25}$ (from Pythagorean triple $(24, 7, 25)$)
- $x_{2} = \frac{336}{625}$ (from Pythagorean triple $(336, 527, 625)$)
- $x_{3} = \frac{354144}{390625}$ (from Pythagorean triple $(354144, 164833, 390625)$)
- $x_{4} = \frac{116749235904}{152587890625}$ (from Pythagorean triple $(116749235904, 98248054847, 152587890625)$)