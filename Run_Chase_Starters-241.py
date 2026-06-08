# Time Complexity: O(1)
# Space Complexity: O(1)

# Read input
N = int(input())

# Find how many complete groups of 20 can be formed
A = N // 20

# Add 1 to get the required answer
A += 1

# Print the result
print(A)
