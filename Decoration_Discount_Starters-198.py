T = int(input())  # Number of test cases

for _ in range(T):
    N = int(input())  # Number of elements in the array
    A = list(map(int, input().split()))  # Read array A

    min_cost = float("inf")  # Initialize with a very large value

    # Iterate over all possible pairs (i, j)
    for i in range(N):
        for j in range(N):  # Compare element A[i] with element A[j]
            if i == j:
                continue  # Skip same element
            elif j == i + 1:
                cost = A[i] + A[j] // 2  # If j is next to i, half price for A[j]
            elif i == j + 1:
                cost = A[j] + A[i] // 2  # If i is next to j, half price for A[i]
            else:
                cost = A[i] + A[j]  # Otherwise, no discount

            min_cost = min(min_cost, cost)  # Update minimum cost

    print(min_cost)  # Output minimum cost for this test case

# Time Complexity: O(N^2) - Two nested loops over array of size N
# Space Complexity: O(1) - Only a few extra variables used, no extra data structure
