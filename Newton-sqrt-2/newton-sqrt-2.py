def newton_sqrt2(initial_guess, max_iterations=10, tolerance=1e-10):
    """
    Approximate the square root of 2 using Newton's method.
    
    Parameters:
    - initial_guess: The starting value for the approximation
    - max_iterations: Maximum number of iterations to perform
    - tolerance: Stop when the change between iterations is less than this value
    
    Returns:
    - List of tuples containing (iteration, approximation, error)
    """
    x = initial_guess
    result = []
    
    for i in range(max_iterations):
        # Calculate f(x) = x^2 - 2
        fx = x**2 - 2
        
        # Calculate f'(x) = 2x
        fpx = 2 * x
        
        # Newton's formula: x_(n+1) = x_n - f(x_n)/f'(x_n)
        next_x = x - fx / fpx
        
        # Calculate error (compared to actual sqrt(2))
        error = abs(next_x - 2**0.5)
        
        # Store iteration data
        result.append((i, x, next_x, error))
        
        # Check for convergence
        if abs(next_x - x) < tolerance:
            break
            
        # Update x for next iteration
        x = next_x
    
    return result

def main():
    initial_guess = 11.5
    iterations = newton_sqrt2(initial_guess)
    
    # Print results
    print(f"Approximating √2 using Newton's method with initial guess {initial_guess}")
    print("-" * 70)
    print(f"{'Iteration':^10} | {'x_n':^15} | {'x_(n+1)':^15} | {'Error':^15}")
    print("-" * 70)
    
    for i, x, next_x, error in iterations:
        print(f"{i:^10} | {x:^15.10f} | {next_x:^15.10f} | {error:^15.10e}")
    
    # Print final approximation
    final_approximation = iterations[-1][2]
    actual_sqrt2 = 2**0.5
    print("-" * 70)
    print(f"Final approximation: {final_approximation:.12f}")
    print(f"Actual √2 value:     {actual_sqrt2:.12f}")
    print(f"Absolute error:      {abs(final_approximation - actual_sqrt2):.12e}")

if __name__ == "__main__":
    main()
