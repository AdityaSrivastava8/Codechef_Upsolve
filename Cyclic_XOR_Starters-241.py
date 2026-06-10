# The large prime number used to keep calculations within standard integer limits
MOD = 998244353

# Read the total number of test cases
t = int(input())

for _ in range(t):
    # n = size of the array, k = number of bits per element
    n, k = map(int, input().split())

    # Step 1: Count how many times 2 divides N (Finding the exponent of 2)
    # Time Complexity for this loop: O(log N) as N is halved each iteration
    temp = n
    v2 = 0
    while temp % 2 == 0:
        v2 += 1
        temp //= 2

    # Step 2: Find 'g' (the number of independent chains)
    # This mathematically calculates gcd(N, 2^K). 
    # '1 << x' is a highly optimized bitwise operation running in O(1) time
    g = 1 << min(v2, k)
    
    # Step 3: Find 'M' (the length of each independent chain)
    m = n // g

    # Step 4: Check if the chain length fits our 3-step XOR loop pattern
    if m % 3 != 0:
        # If the length is not a multiple of 3, the loops conflict. 
        # The only valid starting array is all zeros (exactly 1 choice).
        print(1)
    else:
        # If it is a multiple of 3, each chain has 4 options per bit.
        # pow(base, exp, mod) uses binary exponentiation running in O(log(exp)) time.
        
        # Calculate choices for 1 bit across all 'g' chains safely: 4^g % MOD -> O(log g) time
        choices_per_bit = pow(4, g, MOD)
        
        # Scale it up for all 'K' independent bit layers: (choices_per_bit)^K % MOD -> O(log K) time
        print(pow(choices_per_bit, k, MOD))

# ---------------------------------------------------------
# OVERALL COMPLEXITY ANALYSIS:
# ---------------------------------------------------------
# TIME COMPLEXITY: O(log N + log K) per test case. 
# - The factor extraction loop takes O(log N).
# - The modular exponentiation functions take O(log g + log K) which simplifies to O(log N + log K).
# - Across T test cases, total time is O(T * (log N + log K)), which easily runs within 0.1 seconds.
#
# SPACE COMPLEXITY: O(1) Auxiliary Space.
# - The algorithm only utilizes a few primitive integer variables.
# - No data structures (arrays, lists, maps) are created, resulting in constant memory usage.
# ---------------------------------------------------------

