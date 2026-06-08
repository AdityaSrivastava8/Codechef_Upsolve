# Time Complexity: O(N) per test case
# Space Complexity: O(N)

# Number of test cases
T = int(input())

for i in range(T):

    # Read size of array
    N = int(input())

    # Read array elements
    A = list(map(int, input().split()))

    # Calculate total sum of array
    Total = sum(A)

    # If total sum is even:
    # Even - Even = Even  
    # Even - Odd  = Odd   
    # Therefore, we need at least one even element to remove.
    if Total % 2 == 0:
        print("YES" if any(x % 2 == 0 for x in A) else "NO")

    # If total sum is odd:
    # Odd - Odd   = Even  
    # Odd - Even  = Odd   
    # Therefore, we need at least one odd element to remove.
    else:
        print("YES" if any(x % 2 == 1 for x in A) else "NO")

