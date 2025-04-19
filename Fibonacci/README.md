
## 1. Iterative Approach (Dynamic Programming)

**Complexity: O(n)**

* **Time Complexity:** The algorithm iterates through a loop `n-1` times (for `n > 1`). Inside the loop, constant-time operations (addition and assignment) are performed. Therefore, the time complexity grows linearly with `n`.
* **Space Complexity: O(n)** We store a list `fib_sequence` of size `n+1` to hold the Fibonacci numbers.

**Python Code:**

```python
def fib_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_sequence = [0] * (n + 1)
        fib_sequence[0] = 0
        fib_sequence[1] = 1
        for i in range(2, n + 1):
            fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2]
        return fib_sequence[n]

# Illustration
n_value = 10
result = fib_iterative(n_value)
print(f"Fibonacci({n_value}) using iterative DP: {result}")
```

**Improved Space Complexity (O(1)):**

We can optimize the space complexity to O(1) by only storing the previous two Fibonacci numbers:

```python
def fib_iterative_optimized(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for _ in range(2, n + 1):
            temp = a + b
            a = b
            b = temp
        return b

# Illustration
n_value = 10
result = fib_iterative_optimized(n_value)
print(f"Fibonacci({n_value}) using iterative DP (optimized space): {result}")
```

## 2. Memoization (Top-Down Dynamic Programming)

**Complexity: O(n)**

* **Time Complexity:** Although it's a recursive approach, each Fibonacci number is calculated only once. The results are stored in the `memo` dictionary. When `fib_memo(n)` is called again for a previously computed `n`, it directly returns the stored value in O(1) time. The number of unique subproblems is `n`, and each takes O(1) time to solve after the initial computation.
* **Space Complexity: O(n)** We store the `memo` dictionary which can hold up to `n` Fibonacci numbers. Additionally, the recursion depth can go up to `n` in the worst case.

**Python Code:**

```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        memo[n] = result
        return result

# Illustration
n_value = 10
result = fib_memo(n_value)
print(f"Fibonacci({n_value}) using memoization: {result}")
```

## 3. Matrix Exponentiation

**Complexity: O(log n)**

* **Time Complexity:** The core idea is to use the following matrix representation of Fibonacci numbers:

    ```
    [ F(n+1) ]   [ 1  1 ] ^ n   [ F(1) ]   [ 1 ]
    [ F(n)   ] = [ 1  0 ]     * [ F(0) ] = [ 0 ]
    ```

    Calculating the nth power of a 2x2 matrix can be done efficiently using the method of exponentiation by squaring (binary exponentiation) in O(log n) matrix multiplications. Since each matrix multiplication takes constant time (for 2x2 matrices), the overall time complexity is O(log n).

* **Space Complexity: O(1)** We are only storing a few matrices of constant size during the calculation.

**Python Code:**

```python
def multiply_matrices(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
    return C

def power(matrix, n):
    result = [[1, 0], [0, 1]]  # Identity matrix
    while n > 0:
        if n % 2 == 1:
            result = multiply_matrices(result, matrix)
        matrix = multiply_matrices(matrix, matrix)
        n //= 2
    return result

def fib_matrix(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_matrix_base = [[1, 1], [1, 0]]
        result_matrix = power(fib_matrix_base, n - 1)
        return result_matrix[0][0]

# Illustration
n_value = 10
result = fib_matrix(n_value)
print(f"Fibonacci({n_value}) using matrix exponentiation: {result}")
```

**Comparison of Complexities:**

| Algorithm                     | Time Complexity | Space Complexity |
| ----------------------------- | --------------- | ---------------- |
| Recursive (Naive)             | O(2^n)        | O(n)             |
| Iterative (Dynamic Programming) | O(n)          | O(n)             |
| Iterative (DP, Optimized)     | O(n)          | O(1)             |
| Memoization                   | O(n)          | O(n)             |
| Matrix Exponentiation         | O(log n)      | O(1)             |

As you can see, Matrix Exponentiation provides the most efficient time complexity for calculating Fibonacci numbers, especially for very large values of `n`. Iterative DP and Memoization offer a significant improvement over the naive recursive approach with a linear time complexity. The space-optimized iterative DP is the most memory-efficient linear time solution.