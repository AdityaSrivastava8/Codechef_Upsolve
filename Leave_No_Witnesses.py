T = int(input())  # Number of test cases

for _ in range(T):

    n = int(input())      # Length of binary string
    a = " " + input()     # Add dummy space for 1-based indexing

    # Check if n is a power of 2
    # Example: 8 & 7 = 0
    if (n & (n - 1)) == 0:
        print(-1)
        continue

    ans = 0  # Stores minimum flips needed

    # Check every position from 1 to n
    for i in range(1, n + 1):

        # -------------------------
        # RULE 1:
        # Powers of 2 must be 1
        # -------------------------

        # i is power of 2 if i&(i-1)==0
        if (i & (i - 1)) == 0:

            # If current value is 0,
            # we must flip it to 1
            if a[i] == '0':
                ans += 1

        # -------------------------
        # RULE 2:
        # Find whether i has a larger
        # supermask within [1,n]
        # -------------------------

        has_larger_supermask = False

        # Check every bit position
        for b in range(20):

            # If bit b is already set,
            # skip it
            if (i >> b) & 1:
                continue

            # Turn ON bit b
            new_num = i + (1 << b)

            # If still within range,
            # a larger supermask exists
            if new_num <= n:
                has_larger_supermask = True
                break

        # If no larger supermask exists,
        # position i must contain 0
        if not has_larger_supermask:

            # If current value is 1,
            # flip it to 0
            if a[i] == '1':
                ans += 1

    print(ans)

# Time Complexity:
# O(N * 20) ≈ O(N)
# Outer loop runs N times.
# Inner loop checks at most 20 bit positions for each index.
# Since 20 is a constant, overall complexity is O(N).

# Space Complexity:
# O(N)
# The input string 'a' stores N characters.
# Extra variables such as ans, i, b, and has_larger_supermask
# use only O(1) auxiliary space.
