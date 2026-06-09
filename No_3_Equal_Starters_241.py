# Time Complexity: O(N) per test case
# Space Complexity: O(1)

t = int(input())  # Number of test cases

for _ in range(t):

    n = int(input())      # Length of the string
    s = input().strip()   # Input string

    ans = 0       # Stores minimum edits required
    count = 1     # Length of current consecutive character block

    # Traverse the string from the second character
    for i in range(1, n):

        # If current character continues the block
        if s[i] == s[i - 1]:
            count += 1

        # End of current block
        else:
            # For a block of length L,
            # minimum edits needed = L // 3
            ans += count // 3

            # Start counting the new block
            count = 1

    # Add contribution of the last block
    ans += count // 3

    # Print answer for this test case
    print(ans)
