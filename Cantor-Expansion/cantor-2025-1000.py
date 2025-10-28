#!/usr/bin/env python3
"""
Cantor Expansion Verification for 1/2025^1000

This program verifies the solution to the Cantor expansion problem:
Find the smallest n such that 1/2025^1000 can be written as:
1/2025^1000 = a_1 + a_2/2! + a_3/3! + ... + a_n/n!

Where:
- n is a positive integer
- a_1, a_2, ..., a_n are nonnegative integers  
- a_k < k for k = 2, ..., n
- a_n > 0

The solution claims n = 8013.
"""

import math
from typing import Tuple


def prime_factorization(n: int) -> dict:
    """Find the prime factorization of n."""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def legendre_exponent(n: int, p: int) -> int:
    """
    Calculate the exponent of prime p in n! using Legendre's formula:
    v_p(n!) = floor(n/p) + floor(n/p^2) + floor(n/p^3) + ...
    """
    if n <= 0:
        return 0
    
    exponent = 0
    power = p
    while power <= n:
        exponent += n // power
        power *= p
    return exponent


def find_min_n_for_prime_exponent(prime: int, required_exponent: int) -> int:
    """Find the smallest n such that v_p(n!) >= required_exponent."""
    # Use approximation: v_p(n!) ≈ n/(p-1)
    approx_n = int(required_exponent * (prime - 1))
    
    # Binary search around the approximation
    left, right = max(1, approx_n - 1000), approx_n + 1000
    
    while left < right:
        mid = (left + right) // 2
        if legendre_exponent(mid, prime) >= required_exponent:
            right = mid
        else:
            left = mid + 1
    
    return left


def verify_cantor_solution() -> Tuple[bool, dict]:
    """
    Verify the Cantor expansion solution for 1/2025^1000.
    
    Returns:
        Tuple of (is_valid, verification_results)
    """
    print("🔍 Verifying Cantor Expansion Solution for 1/2025^1000")
    print("=" * 60)
    
    # Step 1: Prime factorization of 2025^1000
    print("\n📊 Step 1: Prime Factorization")
    print("-" * 30)
    
    # 2025 = 3^4 * 5^2
    base_factors = {3: 4, 5: 2}
    print(f"2025 = {3}^4 * {5}^2")
    
    # 2025^1000 = 3^4000 * 5^2000
    K_factors = {3: 4000, 5: 2000}
    print(f"2025^1000 = 3^4000 * 5^2000")
    print(f"Required: v_3(n!) >= 4000 and v_5(n!) >= 2000")
    
    # Step 2: Find minimum n for factor of 5
    print("\n🔍 Step 2: Finding minimum n for 5^2000")
    print("-" * 40)
    
    n_5 = find_min_n_for_prime_exponent(5, 2000)
    v_5_n5 = legendre_exponent(n_5, 5)
    print(f"Minimum n for v_5(n!) >= 2000: n = {n_5}")
    print(f"v_5({n_5}!) = {v_5_n5}")
    
    # Step 3: Check if n_5 satisfies factor of 3 constraint
    print("\n🔍 Step 3: Checking 3^4000 constraint")
    print("-" * 35)
    
    v_3_n5 = legendre_exponent(n_5, 3)
    print(f"v_3({n_5}!) = {v_3_n5}")
    
    if v_3_n5 >= 4000:
        n_final = n_5
        print(f"✅ n = {n_5} satisfies both constraints")
    else:
        # Find minimum n for factor of 3
        n_3 = find_min_n_for_prime_exponent(3, 4000)
        n_final = max(n_5, n_3)
        v_3_final = legendre_exponent(n_final, 3)
        v_5_final = legendre_exponent(n_final, 5)
        print(f"n_5 = {n_5} insufficient for 3^4000 constraint")
        print(f"Minimum n for v_3(n!) >= 4000: n = {n_3}")
        print(f"Final n = max({n_5}, {n_3}) = {n_final}")
        print(f"v_3({n_final}!) = {v_3_final}")
        print(f"v_5({n_final}!) = {v_5_final}")
    
    # Debug: Let's check the specific values mentioned in the solution
    print("\n🔍 Debug: Checking specific values from solution")
    print("-" * 45)
    for n_test in [8000, 8005, 8010, 8011, 8012, 8013]:
        v_3_test = legendre_exponent(n_test, 3)
        v_5_test = legendre_exponent(n_test, 5)
        print(f"n={n_test}: v_3={v_3_test}, v_5={v_5_test}")
        if v_3_test >= 4000 and v_5_test >= 2000:
            print(f"  ✅ {n_test} satisfies both constraints")
        else:
            print(f"  ❌ {n_test} does not satisfy constraints")
    
    # Manual verification of the solution's calculations
    print("\n🔍 Manual verification of solution calculations")
    print("-" * 50)
    
    # Check v_5(8000!) as calculated in solution
    print("v_5(8000!) calculation:")
    v_5_8000_manual = 8000//5 + 8000//25 + 8000//125 + 8000//625 + 8000//3125
    print(f"Manual: {8000//5} + {8000//25} + {8000//125} + {8000//625} + {8000//3125} = {v_5_8000_manual}")
    print(f"Program: {legendre_exponent(8000, 5)}")
    
    # Check v_3(8010!) as calculated in solution  
    print("\nv_3(8010!) calculation:")
    v_3_8010_manual = (8010//3 + 8010//9 + 8010//27 + 8010//81 + 8010//243 + 
                      8010//729 + 8010//2187 + 8010//6561)
    print(f"Manual: {8010//3} + {8010//9} + {8010//27} + {8010//81} + {8010//243} + {8010//729} + {8010//2187} + {8010//6561} = {v_3_8010_manual}")
    print(f"Program: {legendre_exponent(8010, 3)}")
    print("⚠️  SOLUTION ERROR: Claims 3999 but actual value is 4000!")
    
    # Check v_3(8013!) as calculated in solution
    print("\nv_3(8013!) calculation:")
    v_3_8013_manual = (8013//3 + 8013//9 + 8013//27 + 8013//81 + 8013//243 + 
                      8013//729 + 8013//2187 + 8013//6561)
    print(f"Manual: {8013//3} + {8013//9} + {8013//27} + {8013//81} + {8013//243} + {8013//729} + {8013//2187} + {8013//6561} = {v_3_8013_manual}")
    print(f"Program: {legendre_exponent(8013, 3)}")
    
    print("\n🎯 CORRECTED SOLUTION:")
    print("The solution contains an arithmetic error.")
    print("v_3(8010!) = 4000 (not 3999 as claimed)")
    print("Therefore, n = 8010 is the correct answer, not n = 8013")
    
    # Step 4: Verify a_n > 0 constraint
    print("\n📝 Step 4: Verifying a_n > 0 constraint")
    print("-" * 40)
    
    # Calculate N = n! / K
    # We need to check if N is divisible by n
    # If not, then a_n = N mod n > 0
    
    # For large numbers, we work with exponents
    v_3_n = legendre_exponent(n_final, 3)
    v_5_n = legendre_exponent(n_final, 5)
    
    print(f"n = {n_final}")
    print(f"v_3({n_final}!) = {v_3_n}")
    print(f"v_5({n_final}!) = {v_5_n}")
    print(f"v_3(K) = 4000")
    print(f"v_5(K) = 2000")
    
    # N = n! / K, so v_p(N) = v_p(n!) - v_p(K)
    v_3_N = v_3_n - 4000
    v_5_N = v_5_n - 2000
    
    print(f"v_3(N) = v_3({n_final}!) - v_3(K) = {v_3_n} - 4000 = {v_3_N}")
    print(f"v_5(N) = v_5({n_final}!) - v_5(K) = {v_5_n} - 2000 = {v_5_N}")
    
    # Check if n is divisible by 3 or 5
    n_divisible_by_3 = n_final % 3 == 0
    n_divisible_by_5 = n_final % 5 == 0
    
    print(f"n = {n_final} divisible by 3: {n_divisible_by_3}")
    print(f"n = {n_final} divisible by 5: {n_divisible_by_5}")
    
    # For a_n to be 0, N must be divisible by n
    # This requires v_p(N) >= v_p(n) for all primes p dividing n
    a_n_is_zero = True
    
    if n_divisible_by_3:
        v_3_n_value = legendre_exponent(n_final, 3) - legendre_exponent(n_final - 1, 3)
        if v_3_N < v_3_n_value:
            a_n_is_zero = False
            print(f"❌ v_3(N) = {v_3_N} < v_3(n) = {v_3_n_value}, so a_n ≠ 0")
    
    if n_divisible_by_5:
        v_5_n_value = legendre_exponent(n_final, 5) - legendre_exponent(n_final - 1, 5)
        if v_5_N < v_5_n_value:
            a_n_is_zero = False
            print(f"❌ v_5(N) = {v_5_N} < v_5(n) = {v_5_n_value}, so a_n ≠ 0")
    
    if a_n_is_zero:
        print("✅ N is divisible by n, so a_n = 0 (contradiction!)")
        is_valid = False
    else:
        print("✅ N is not divisible by n, so a_n > 0")
        is_valid = True
    
    # Step 5: Check if this is the minimal n
    print("\n🔍 Step 5: Checking minimality")
    print("-" * 30)
    
    # Check n-1
    n_minus_1 = n_final - 1
    v_3_nm1 = legendre_exponent(n_minus_1, 3)
    v_5_nm1 = legendre_exponent(n_minus_1, 5)
    
    print(f"Checking n-1 = {n_minus_1}:")
    print(f"v_3({n_minus_1}!) = {v_3_nm1} (need >= 4000)")
    print(f"v_5({n_minus_1}!) = {v_5_nm1} (need >= 2000)")
    
    if v_3_nm1 >= 4000 and v_5_nm1 >= 2000:
        print("❌ n-1 also satisfies constraints - n is not minimal!")
        is_valid = False
    else:
        print("✅ n-1 does not satisfy constraints - n is minimal")
    
    # Results summary
    results = {
        'n': n_final,
        'v_3_n': v_3_n,
        'v_5_n': v_5_n,
        'v_3_N': v_3_N,
        'v_5_N': v_5_N,
        'a_n_is_zero': a_n_is_zero,
        'is_minimal': not (v_3_nm1 >= 4000 and v_5_nm1 >= 2000)
    }
    
    return is_valid, results


def main():
    """Main function to run the verification."""
    print("Cantor Expansion Verification Program")
    print("=" * 50)
    
    try:
        is_valid, results = verify_cantor_solution()
        
        print("\n" + "=" * 60)
        print("📋 FINAL RESULTS")
        print("=" * 60)
        
        if is_valid and results['is_minimal']:
            print(f"✅ SOLUTION VERIFIED: n = {results['n']}")
            print(f"   - v_3({results['n']}!) = {results['v_3_n']} >= 4000 ✓")
            print(f"   - v_5({results['n']}!) = {results['v_5_n']} >= 2000 ✓")
            print(f"   - a_{results['n']} > 0 ✓")
            print(f"   - n is minimal ✓")
        else:
            print("❌ SOLUTION INVALID")
            if not results['is_minimal']:
                print("   - n is not minimal")
            if results['a_n_is_zero']:
                print("   - a_n = 0 (should be > 0)")
        
        print(f"\nDetailed results: {results}")
        
    except Exception as e:
        print(f"❌ Error during verification: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
