# Definite Integral Visualization

This project visualizes Riemann sum approximations of definite integrals using matplotlib animations.

# How to Use the Web Application
1. Open the `index.html` file in a web browser.
2. The simulation will start automatically when the page loads.
3. You can input an "error threshold" to control the precision of the approximation.
4. Click the "Start" button to begin the simulation.
5. Click the "Stop" button to halt the simulation.
6. Click the "Reset" button to reset the simulation.
7. The simulation will stop automatically when the error is less than the specified threshold or when the maximum number of iterations is reached.
8. The elapsed time of the program will be displayed.
9. The mathematical explanation of the Riemann sum will be shown below the "Start Calculation" button.
10. The status of the simulation will be displayed in a table format, with the "error" value in red and the "Riemann Sum" in yellow.


## How to Run Python Code

### Setting up a Virtual Environment

1. Make sure you have Python installed on your system (Python 3.7+ recommended)

2. Open a terminal/command prompt and navigate to the project directory:
   ```
   cd /Users/vuhung/Desktop/MachineLearning-GenAI/Definite-Integral
   ```

3. Create a virtual environment named ".venv":
   ```
   python -m venv .venv
   ```

4. Activate the virtual environment:
   
   - On macOS/Linux:
     ```
     source .venv/bin/activate
     ```
   
   - On Windows:
     ```
     .venv\Scripts\activate
     ```

5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Script

After activating the virtual environment and installing dependencies, run the script with:
```
python definite-integral.py
```

### Deactivating the Virtual Environment

When you're done, you can deactivate the virtual environment:
```
deactivate
```

# **Mathematical Explanation using Markdown and LaTeX:**

We want to calculate the definite integral:

$$
\int_{0}^{1} x^2 \, dx
$$

Using the definition of the definite integral with right endpoints:

$$
\int_{a}^{b} f(x) \, dx = \lim_{n \to \infty} \sum_{i=1}^{n} f(x_i) \Delta x
$$

For our problem, $f(x) = x^2$, $a = 0$, and $b = 1$.

1.  **Width of the subintervals:**

$$
\Delta x = \frac{b - a}{n} = \frac{1 - 0}{n} = \frac{1}{n}
$$

2.  **Right endpoints of the subintervals:**

The $i$-th subinterval is $[x_{i-1}, x_i]$, where $x_i = a + i \Delta x$.
$$
x_i = 0 + i \left(\frac{1}{n}\right) = \frac{i}{n}
$$

3.  **Evaluate the function at the right endpoints:**

$$
f(x_i) = f\left(\frac{i}{n}\right) = \left(\frac{i}{n}\right)^2 = \frac{i^2}{n^2}
$$

4.  **Form the Riemann sum:**

$$
\sum_{i=1}^{n} f(x_i) \Delta x = \sum_{i=1}^{n} \left(\frac{i^2}{n^2}\right) \left(\frac{1}{n}\right) = \sum_{i=1}^{n} \frac{i^2}{n^3} = \frac{1}{n^3} \sum_{i=1}^{n} i^2
$$

5.  **Use the formula for the sum of the first $n$ squares:**

$$
\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}
$$

6.  **Substitute the sum back into the Riemann sum:**

$$
\frac{1}{n^3} \sum_{i=1}^{n} i^2 = \frac{1}{n^3} \cdot \frac{n(n+1)(2n+1)}{6} = \frac{n(2n^2 + 3n + 1)}{6n^3} = \frac{2n^3 + 3n^2 + n}{6n^3}
$$

7.  **Take the limit as $n \to \infty$:**

$$
\int_{0}^{1} x^2 \, dx = \lim_{n \to \infty} \frac{2n^3 + 3n^2 + n}{6n^3} = \lim_{n \to \infty} \frac{2 + \frac{3}{n} + \frac{1}{n^2}}{6} = \frac{2 + 0 + 0}{6} = \frac{2}{6} = \frac{1}{3}
$$

Thus, the definite integral of $f(x) = x^2$ from $0$ to $1$ is $\frac{1}{3}$. The animation will visually show how the sum of the areas of the rectangles approaches this value as the number of subintervals $n$ increases.

# References

- [Riemann Sum - Wikipedia](https://en.wikipedia.org/wiki/Riemann_sum)
- [Definite Integral - Wikipedia](https://en.wikipedia.org/wiki/Definite_integral)
- [Integral Calculus - Wikipedia](https://en.wikipedia.org/wiki/Integral_calculus)