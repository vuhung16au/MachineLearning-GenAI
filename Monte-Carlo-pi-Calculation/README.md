# Introduction 

This method is a type of Monte Carlo simulation used to approximate π.

Based on the video you provided, here's a summary of the algorithm described for estimating the value of π (pi):

1.  Imagine a square and a circle perfectly inscribed within it (meaning the circle touches all four sides of the square) 
2.  The ratio of the circle's area to the square's area is π/4 
3.  If you randomly place a large number of points within the square, the proportion of points that fall *inside* the circle compared to the total number of points placed will be approximately equal to the ratio of the areas (π/4).
4.  To estimate π, you can calculate the ratio of (points inside the circle) / (total points inside the square) and then multiply this ratio by 4 .
5.  The accuracy of this estimation improves as you use more random points 

This method is a type of Monte Carlo simulation used to approximate π.

You've provided a very accurate and concise description of the Monte Carlo method for approximating $\pi$. Let's break it down mathematically:

# Mathematical Explanation

The Monte Carlo method is a statistical technique that allows us to make numerical estimates through random sampling. In the case of estimating the value of $\pi$, we can visualize the problem using geometry.

We will use a square and an inscribed circle to illustrate the concept. The following steps outline the mathematical formulation of the Monte Carlo method for estimating $\pi$:


**1. Defining the Geometry:**

* **Square:** Imagine a square centered at the origin (0, 0) of a Cartesian coordinate system. Let the side length of the square be $2r$. This means the coordinates $(x, y)$ of any point within the square will satisfy $-r \le x \le r$ and $-r \le y \le r$.
    * The area of the square ($A_{square}$) is side length squared:
        $A_{square} = (2r)^2 = 4r^2$

* **Inscribed Circle:** Now, consider a circle perfectly inscribed within this square. The diameter of this circle will be equal to the side length of the square, which is $2r$. Therefore, the radius of the circle is $r$.
    * The area of the circle ($A_{circle}$) is given by:
        $A_{circle} = \pi r^2$

**2. The Ratio of Areas:**

The ratio of the area of the inscribed circle to the area of the square is:

$\frac{A_{circle}}{A_{square}} = \frac{\pi r^2}{4r^2} = \frac{\pi}{4}$

**3. Random Point Generation:**

Imagine we randomly generate a large number of points within the boundaries of the square. Let the total number of points generated be $N$. Since the points are randomly distributed within the square, the probability of a single point falling within any specific region of the square is proportional to the area of that region.

**4. Probability and the Ratio:**

The probability ($P(\text{point inside circle})$) that a randomly chosen point within the square will also fall inside the inscribed circle is equal to the ratio of the circle's area to the square's area:

$P(\text{point inside circle}) = \frac{A_{circle}}{A_{square}} = \frac{\pi}{4}$

**5. Monte Carlo Approximation:**

In a Monte Carlo simulation, we approximate probabilities by performing a large number of trials (in this case, generating random points). Let $N_{inside}$ be the number of points that fall inside the circle out of the total $N$ points generated within the square.

The ratio of the number of points inside the circle to the total number of points is an experimental estimate of the probability:

$\frac{N_{inside}}{N} \approx P(\text{point inside circle}) = \frac{\pi}{4}$

**6. Estimating π:**

To approximate the value of $\pi$, we can rearrange the above equation:

$\pi \approx 4 \times \frac{N_{inside}}{N}$

**In Summary (Mathematical Formulation):**

1.  **Define the sample space:** A square with side length $2r$, area $4r^2$.
2.  **Define the event:** A point falling within the inscribed circle of radius $r$, area $\pi r^2$.
3.  **The theoretical probability of the event:** $P(\text{inside}) = \frac{\pi r^2}{4r^2} = \frac{\pi}{4}$.
4.  **Perform $N$ independent trials:** Generate $N$ random points $(x_i, y_i)$ uniformly within the square (where $-r \le x_i \le r$ and $-r \le y_i \le r$ for $i = 1, 2, ..., N$).
5.  **Count the number of successful events:** Determine how many of these points satisfy the condition for being inside the circle, which is $x_i^2 + y_i^2 \le r^2$. Let this count be $N_{inside}$.
6.  **Estimate the probability:** The experimental probability is $\frac{N_{inside}}{N}$.
7.  **Approximate π:** Since $\frac{N_{inside}}{N} \approx \frac{\pi}{4}$, we get the approximation $\pi \approx 4 \times \frac{N_{inside}}{N}$.

The accuracy of this approximation increases as the number of random points ($N$) becomes larger, due to the Law of Large Numbers. However, as discussed previously, the convergence is relatively slow.

# References
- [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method)
- [Monte Carlo method for estimating pi](https://en.wikipedia.org/wiki/Monte_Carlo_method#Estimating_%CF%80)

