import time
import matplotlib.pyplot as plt
import sys
import csv
import time
import pandas as pd
import numpy as np
import os
import glob

# Algorithm 1: Naive Recursive Approach
def min_coins_naive(coins, amount):
    """
    Solves the minimum coin problem using naive recursion.
    - coins: List of coin denominations.
    - amount: Target sum.
    - Returns: Minimum number of coins needed or -1 if impossible.
    """
    if amount == 0:
        return 0  # Base case: No coins needed for amount 0
    if amount < 0:
        return float('inf')  # Invalid combination
    if not coins:
        return float('inf')  # No coins left, but amount > 0
    
    min_coins = float('inf')
    for i in range(len(coins)):
        # Try excluding the i-th coin
        min_without_i = min_coins_naive(coins[:i] + coins[i+1:], amount)
        # Try including the i-th coin
        min_with_i = min_coins_naive(coins, amount - coins[i]) + 1 if coins[i] <= amount else float('inf')
        min_coins = min(min_coins, min_without_i, min_with_i)
    
    return min_coins if min_coins != float('inf') else -1

# Algorithm 2: Memoized Recursive Approach (Top-Down DP)
def min_coins_memo(coins, amount, memo=None):
    """
    Solves the minimum coin problem using memoized recursion.
    - coins: List of coin denominations.
    - amount: Target sum.
    - memo: Dictionary to store computed results.
    - Returns: Minimum number of coins needed or -1 if impossible.
    """
    if memo is None:
        memo = {}
    
    # Return memoized result if available
    if amount in memo:
        return memo[amount]
    
    # Base cases
    if amount == 0:
        memo[0] = 0
        return 0
    if amount < 0:
        return float('inf')  # Negative amounts are invalid
    
    min_coins = float('inf')
    for coin in coins:
        if coin <= amount:
            # Recursive call for remaining amount
            sub_problem = min_coins_memo(coins, amount - coin, memo)
            if sub_problem != float('inf'):
                min_coins = min(min_coins, sub_problem + 1)
    
    # Store result in memo
    memo[amount] = min_coins
    
    # Convert to -1 for final return if no solution found
    return -1 if min_coins == float('inf') else min_coins

# Algorithm 2b: Iterative Memoization (safer alternative)
def min_coins_memo_iterative(coins, amount):
    """
    Solves the minimum coin problem using memoization with an iterative approach.
    - coins: List of coin denominations.
    - amount: Target sum.
    - Returns: Minimum number of coins needed or -1 if impossible.
    """
    memo = {0: 0}  # Base case: 0 coins needed for amount 0
    
    # Fill memo table iteratively
    for i in range(1, amount + 1):
        memo[i] = float('inf')
        for coin in coins:
            if coin <= i and memo.get(i - coin, float('inf')) != float('inf'):
                memo[i] = min(memo[i], memo[i - coin] + 1)
    
    return -1 if memo[amount] == float('inf') else memo[amount]

# Algorithm 3: Bottom-Up Dynamic Programming
def min_coins_dp(coins, amount):
    """
    Solves the minimum coin problem using bottom-up dynamic programming.
    - coins: List of coin denominations.
    - amount: Target sum.
    - Returns: Minimum number of coins needed or -1 if impossible.
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Algorithm 4: Greedy Approach (for comparison)
def min_coins_greedy(coins, amount):
    """
    Solves the minimum coin problem using a greedy approach.
    - coins: List of coin denominations.
    - amount: Target sum.
    - Returns: Number of coins needed or -1 if impossible.
    Note: Not always optimal.
    """
    coins = sorted(coins, reverse=True)  # Sort in descending order
    total_coins = 0
    remaining = amount
    for coin in coins:
        while remaining >= coin:
            remaining -= coin
            total_coins += 1
    return total_coins if remaining == 0 else -1

# Function to measure and compare performance
def compare_algorithms(coins, amounts):
    """
    Measures execution time of each algorithm for different amounts.
    - coins: List of coin denominations.
    - amounts: List of target amounts to test.
    - Returns: Dictionary with algorithm names and their execution times.
    """
    results = {'Memoized DP': [], 'Bottom-Up DP': [], 'Greedy': []}
    memo = {}  # Reuse the same memo dictionary for all calls
    for amount in amounts:
        # Memoized DP (using iterative version to avoid recursion depth issues)
        start = time.time()
        min_coins_memo_iterative(coins, amount)  # Using iterative version instead
        results['Memoized DP'].append(time.time() - start)
        
        # Bottom-Up DP
        start = time.time()
        min_coins_dp(coins, amount)
        results['Bottom-Up DP'].append(time.time() - start)
        
        # Greedy
        start = time.time()
        min_coins_greedy(coins, amount)
        results['Greedy'].append(time.time() - start)
    
    return results

# Test and visualize performance
coins = [1, 2, 5, 10, 20, 50, 100]
amounts = [100, 200, 505, 1000, 2005, 5003]
times = compare_algorithms(coins, amounts)

# Plotting the results
plt.figure(figsize=(10, 6))
for algo, t in times.items():
    plt.plot(amounts, t, label=algo, marker='o')
plt.xlabel('Target Amount')
plt.ylabel('Execution Time (seconds)')
plt.title('Performance Comparison of Coin Change Algorithms')
plt.legend()
plt.grid(True)
plt.savefig('coin_change_performance.png')

# Example usage with Euro coins and target 734
amount = 734
print(f"Results for amount {amount} with coins {coins}:")
# print(f"Naive Recursive: {min_coins_naive(coins, amount)} coins")  # Commented out to avoid recursion depth issues
print(f"Memoized DP (Recursive): {min_coins_memo(coins, amount)} coins")
print(f"Memoized DP (Iterative): {min_coins_memo_iterative(coins, amount)} coins")
print(f"Bottom-Up DP: {min_coins_dp(coins, amount)} coins")
print(f"Greedy: {min_coins_greedy(coins, amount)} coins")

# Run all algorithms for different amounts and save runtime to CSV
def run_all_algorithms(coins, amounts):
    
    # Increase recursion limit for larger amounts
    original_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(10000)
    
    # Prepare headers for CSV
    headers = ['Amount', 'Memoized DP (Recursive)', 'Memoized DP (Iterative)', 'Bottom-Up DP', 'Greedy']
    
    # Create results list
    results = []
    
    for amount in amounts:
        row = [amount]
        print(f"\nTesting amount: {amount}")
        
        # Memoized DP (Recursive)
        try:
            start = time.time()
            result = min_coins_memo(coins, amount)
            elapsed = time.time() - start
            row.append(elapsed)
            print(f"  Memoized DP (Recursive): {result} coins, time: {elapsed:.6f} seconds")
        except RecursionError:
            row.append(None)
            print(f"  Memoized DP (Recursive): RecursionError")
        
        # Memoized DP (Iterative)
        start = time.time()
        result = min_coins_memo_iterative(coins, amount)
        elapsed = time.time() - start
        row.append(elapsed)
        print(f"  Memoized DP (Iterative): {result} coins, time: {elapsed:.6f} seconds")
        
        # Bottom-Up DP
        start = time.time()
        result = min_coins_dp(coins, amount)
        elapsed = time.time() - start
        row.append(elapsed)
        print(f"  Bottom-Up DP: {result} coins, time: {elapsed:.6f} seconds")
        
        # Greedy
        start = time.time()
        result = min_coins_greedy(coins, amount)
        elapsed = time.time() - start
        row.append(elapsed)
        print(f"  Greedy: {result} coins, time: {elapsed:.6f} seconds")
        
        # Add to results
        results.append(row)
    
    # Reset recursion limit
    sys.setrecursionlimit(original_limit)
    
    # Write results to CSV
    with open('runtime.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(results)
    
    print("\nResults saved to runtime.csv")

# Visualize the results from CSV
def visualize_from_csv(csv_file):
    # Read the CSV file using csv module
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Get the header row
        
        # Initialize data structures
        amounts = []
        data = {header: [] for header in headers[1:]}  # Skip the Amount column
        
        # Parse CSV data
        for row in reader:
            amounts.append(int(row[0]))  # First column is Amount
            
            # Process each algorithm's runtime
            for i, header in enumerate(headers[1:], 1):
                try:
                    # Convert to float, handle empty or 'None' values
                    value = float(row[i]) if row[i] and row[i].lower() != 'none' else float('nan')
                    data[header].append(value)
                except (ValueError, IndexError):
                    data[header].append(float('nan'))
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    
    # Plot each algorithm
    for algo_name, runtimes in data.items():
        # Convert to numpy array for easier filtering
        runtime_array = np.array(runtimes)
        amount_array = np.array(amounts)
        
        # Plot only non-NaN values
        mask = ~np.isnan(runtime_array)
        plt.plot(amount_array[mask], runtime_array[mask], marker='o', linewidth=2, label=algo_name)
    
    # Add labels and title
    plt.xlabel('Amount', fontsize=12)
    plt.ylabel('Runtime (seconds)', fontsize=12)
    plt.title('Algorithm Runtime Comparison for Min Coins Problem', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=10)
    
    # Save the plot
    plt.tight_layout()
    plt.savefig('algorithm_runtime_comparison.png', dpi=300)
    plt.show()

# Define the amounts to test
# Define different coin sets to test
coin_sets = {
    'Standard': [1, 2, 5, 10, 20, 50, 100],  # Standard set
    'US': [1, 5, 10, 25, 50, 100],  # US coins
    'Binary': [1, 2, 4, 8, 16, 32, 64, 128],  # Powers of 2
    'Prime': [1, 2, 3, 5, 7, 11, 13, 17, 19]  # Prime numbers
}

# Define the amounts to test
test_amounts = [734, 1000, 2001, 3003, 5000]

# Run tests for each coin set
for name, coin_set in coin_sets.items():
    print(f"\n\nTesting with {name} coins: {coin_set}")
    
    # Run all algorithms with this coin set
    run_all_algorithms(coin_set, test_amounts)
    
    # Rename the CSV file to include the coin set name
    os.rename('runtime.csv', f'runtime_{name}.csv')
    
    # Create visualization
    visualize_from_csv(f'runtime_{name}.csv')
test_amounts = [734, 1000, 2001, 3003, 5000]

# Run all algorithms and save results
# Run tests for all coin sets with all test amounts
for name, coin_set in coin_sets.items():
    print(f"\n\nTesting with {name} coins: {coin_set}")
    run_all_algorithms(coin_set, test_amounts)
    os.rename('runtime.csv', f'runtime_{name}.csv')
    visualize_from_csv(f'runtime_{name}.csv')

# Create visualization from the CSV file
# Visualize all runtime CSV files together
def visualize_all_runtime_files():
    import matplotlib.pyplot as plt
    
    # Find all runtime CSV files
    csv_files = glob.glob('runtime_*.csv')
    
    if not csv_files:
        print("No runtime CSV files found.")
        return
    
    # Create a figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    axes = axes.flatten()
    
    # Colors for different coin sets
    colors = {'Standard': 'blue', 'US': 'red', 'Binary': 'green', 'Prime': 'purple'}
    
    # Load data from each file
    all_data = {}
    algorithms = []
    
    for csv_file in csv_files:
        # Extract coin set name from filename
        coin_set = csv_file.replace('runtime_', '').replace('.csv', '')
        
        # Read data
        df = pd.read_csv(csv_file)
        all_data[coin_set] = df
        
        if not algorithms:
            algorithms = [col for col in df.columns if col != 'Amount']
    
    # Plot each algorithm in a separate subplot - commented out for display but still saving
    for i, algo in enumerate(algorithms):
        if i >= len(axes):
            break
            
        for coin_set, df in all_data.items():
            # Comment out visualization code
            # axes[i].plot(df['Amount'], df[algo], marker='o', label=coin_set, 
            #           color=colors.get(coin_set, 'black'))
            
            # Plot with no display, just for saving to file
            axes[i].plot(df['Amount'], df[algo], marker='o', label=coin_set, 
                      color=colors.get(coin_set, 'black'))
            
        # Comment out visualization settings
        # axes[i].set_title(f'{algo}', fontsize=12)
        # axes[i].set_xlabel('Amount')
        # axes[i].set_ylabel('Runtime (seconds)')
        # axes[i].grid(True, linestyle='--', alpha=0.7)
        # axes[i].legend()
        
        # Add minimal labels for saving to file
        axes[i].set_title(f'{algo}')
        axes[i].set_xlabel('Amount')
        axes[i].set_ylabel('Runtime (seconds)')
        axes[i].legend()
    
    plt.tight_layout()
    # Save the figure to disk
    plt.savefig('all_algorithms_comparison.png', dpi=300)
    
    # Comment out display
    # plt.show()
    
    print("Visualization saved to 'all_algorithms_comparison.png'")

# Visualize all runtime files
visualize_all_runtime_files()
