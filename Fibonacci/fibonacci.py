import time
import csv
import matplotlib.pyplot as plt

def fib_recursive(n):
    """Naive recursive approach - O(2^n) time complexity"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    """Iterative approach using dynamic programming - O(n) time, O(n) space"""
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

def fib_iterative_optimized(n):
    """Iterative approach with optimized space complexity - O(n) time, O(1) space"""
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

# This function is commented out to avoid excessive runtime for large n
# RecursionError: maximum recursion depth exceeded (most likely for n > 1000), a limit of Python
# recursion depth is 1000 by default.

# def fib_memo(n, memo=None):
#     """Memoization approach (top-down dynamic programming) - O(n) time and space"""
#     if memo is None:
#         memo = {}
#     if n in memo:
#         return memo[n]
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
#         memo[n] = result
#         return result

def fib_memo(n, memo=None):
    """Memoization approach (top-down dynamic programming) - O(n) time and space"""
    if memo is None:
        memo = {0: 0, 1: 1}  # Initialize with base cases
    
    # If n is already calculated, return it
    if n in memo:
        return memo[n]
    
    # Otherwise, calculate iteratively
    for i in range(2, n+1):
        if i not in memo:
            memo[i] = memo[i-1] + memo[i-2]
    
    return memo[n]

def multiply_matrices(A, B):
    """Helper function for matrix multiplication"""
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
    return C

def power(matrix, n):
    """Helper function for matrix exponentiation"""
    result = [[1, 0], [0, 1]]  # Identity matrix
    while n > 0:
        if n % 2 == 1:
            result = multiply_matrices(result, matrix)
        matrix = multiply_matrices(matrix, matrix)
        n //= 2
    return result

def fib_matrix(n):
    """Matrix exponentiation approach - O(log n) time, O(1) space"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_matrix_base = [[1, 1], [1, 0]]
        result_matrix = power(fib_matrix_base, n - 1)
        return result_matrix[0][0]

if __name__ == "__main__":
    n_value = 200000
    
    # For recursive approach, use a smaller n to avoid excessive runtime
    recursive_n = 500  # Using smaller value as recursive is very slow for large n

    if recursive_n < 40:
        start_time = time.time()
        recursive_result = fib_recursive(recursive_n)
        recursive_time = time.time() - start_time
        # print(f"Fibonacci({recursive_n}) using recursive approach: {recursive_result}")
        print(f"Time taken: {recursive_time:.6f} seconds\n")
    else:
        print("It will take too long if recursive_n > 40")


    start_time = time.time()
    iterative_result = fib_iterative(n_value)
    iterative_time = time.time() - start_time
    # print(f"Fibonacci({n_value}) using iterative DP: {iterative_result}")
    print(f"Time taken: {iterative_time:.6f} seconds\n")
    
    start_time = time.time()
    optimized_result = fib_iterative_optimized(n_value)
    optimized_time = time.time() - start_time
    # print(f"Fibonacci({n_value}) using iterative DP (optimized space): {optimized_result}")
    print(f"Time taken: {optimized_time:.6f} seconds\n")
    
    start_time = time.time()
    memo_result = fib_memo(n_value)
    memo_time = time.time() - start_time
    # print(f"Fibonacci({n_value}) using memoization: {memo_result}")
    print(f"Time taken: {memo_time:.6f} seconds\n")
    
    start_time = time.time()
    matrix_result = fib_matrix(n_value)
    matrix_time = time.time() - start_time
    # print(f"Fibonacci({n_value}) using matrix exponentiation: {matrix_result}")
    print(f"Time taken: {matrix_time:.6f} seconds\n")

    

    def benchmark_functions(n_values, functions):
        """Run benchmark and return timing results"""
        results = {func.__name__: [] for func in functions}
        
        for n in n_values:
            print(f"Running benchmarks for n={n}")
            
            for func in functions:
                start_time = time.time()
                func(n)
                elapsed_time = time.time() - start_time
                results[func.__name__].append(elapsed_time)
                print(f"{func.__name__}({n}) took {elapsed_time:.6f} seconds")
        
        return results

    def save_results(results, n_values, filename="runtime.txt"):
        """Save benchmark results to file"""
        with open(filename, 'w') as f:
            f.write("Fibonacci function runtime benchmarks\n")
            f.write("-" * 50 + "\n\n")
            f.write(f"{'n':<10}")
            
            # Write header
            for func_name in results:
                f.write(f"{func_name:<25}")
            f.write("\n")
            
            # Write data
            for i, n in enumerate(n_values):
                f.write(f"{n:<10}")
                for func_name in results:
                    f.write(f"{results[func_name][i]:<25.6f}")
                f.write("\n")

    def plot_results(results, n_values):
        """Plot benchmark results"""
        plt.figure(figsize=(12, 8))
        
        for func_name, times in results.items():
            plt.plot(n_values, times, marker='o', label=func_name)
        
        plt.xlabel('Input Size (n)')
        plt.ylabel('Time (seconds)')
        plt.title('Fibonacci Algorithms Performance Comparison')
        plt.legend()
        plt.grid(True)
        plt.savefig('fibonacci_performance.png')
        
        # Create a log scale plot for better comparison of fast algorithms
        plt.figure(figsize=(12, 8))
        for func_name, times in results.items():
            plt.plot(n_values, times, marker='o', label=func_name)
        
        plt.xlabel('Input Size (n)')
        plt.ylabel('Time (seconds) - Log Scale')
        plt.title('Fibonacci Algorithms Performance Comparison (Log Scale)')
        plt.legend()
        plt.grid(True)
        plt.yscale('log')
        plt.savefig('fibonacci_performance_log_scale.png')
        
        plt.show()

    # Run benchmark
    n_values = [10, 100, 200, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]
    functions = [
        fib_iterative,
        fib_iterative_optimized,
        fib_memo,
        fib_matrix
    ]

    # Run benchmarks and save results
    results = benchmark_functions(n_values, functions)
    save_results(results, n_values)
    
    # Plot and save results with the specified filename
    plt.figure(figsize=(12, 8))
    
    for func_name, times in results.items():
        plt.plot(n_values, times, marker='o', label=func_name)
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Fibonacci Algorithms Performance Comparison')
    plt.legend()
    plt.grid(True)
    plt.savefig('fibonacci-algorithms-performance-comparison.png')
    
    # Create a log scale plot
    plt.figure(figsize=(12, 8))
    for func_name, times in results.items():
        plt.plot(n_values, times, marker='o', label=func_name)
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds) - Log Scale')
    plt.title('Fibonacci Algorithms Performance Comparison (Log Scale)')
    plt.legend()
    plt.grid(True)
    plt.yscale('log')
    plt.savefig('fibonacci-algorithms-performance-comparison_log_scale.png')
    
    plt.show()

    # Add function to save the benchmark data as CSV for future reference
    def save_as_csv(results, n_values, filename="fibonacci_data.csv"):
        """Save benchmark results to CSV file for easier data analysis"""
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header
            header = ['n'] + list(results.keys())
            writer.writerow(header)
            
            # Write data rows
            for i, n in enumerate(n_values):
                row = [n]
                for func_name in results:
                    row.append(results[func_name][i])
                writer.writerow(row)
        
        print(f"CSV data saved to {filename}")

    # Save data as CSV
    save_as_csv(results, n_values)

    print("Benchmark complete. Results saved to runtime.txt and plots saved as PNG files.")