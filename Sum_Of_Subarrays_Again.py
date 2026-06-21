from bisect import bisect_left

# Read all input at once and split into tokens
data = open(0).read().split()

if data:
    t = int(data[0])  # Number of test cases
    idx = 1           # Pointer for reading input
    ans = []          # Stores answers for all test cases

    for _ in range(t):

        n = int(data[idx])  # Size of array
        idx += 1

        # Read array elements
        a = list(map(int, data[idx:idx + n]))
        idx += n

        base_sum = 0        # Sum of contributions of all elements
        cost = [0] * n      # Stores transformed negative values

        # Contribution Technique
        for i in range(n):

            # A[i] appears in (i+1)*(n-i) subarrays
            base_sum += a[i] * (i + 1) * (n - i)

            # Store contribution of negative elements
            if a[i] < 0:
                cost[i] = -2 * a[i]

        # Prefix sum of cost array
        pref = [0] * (n + 1)

        for i in range(n):
            pref[i + 1] = pref[i] + cost[i]

        # Prefix sum of prefix sums
        # Used for O(1) range sum queries later
        pref_sum = [0] * (n + 2)

        for i in range(n + 1):
            pref_sum[i + 1] = pref_sum[i] + pref[i]

        # V[i] stores gain value for positive elements
        v = [-float("inf")] * n

        for i in range(n):

            # Only positive elements can contribute
            if a[i] > 0:
                v[i] = pref[i] - 2 * a[i]

        # Previous Greater Element
        prev = [-1] * n
        stack = []

        for i in range(n):

            # Maintain decreasing stack
            while stack and v[stack[-1]] <= v[i]:
                stack.pop()

            # Nearest greater element on left
            if stack:
                prev[i] = stack[-1]

            stack.append(i)

        # Next Greater Element
        nxt = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):

            # Maintain decreasing stack
            while stack and v[stack[-1]] < v[i]:
                stack.pop()

            # Nearest greater element on right
            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        extra = 0  # Stores extra contribution

        for i in range(n):

            # Skip invalid positions
            if v[i] == -float("inf"):
                continue

            # First position where pref[pos] >= v[i]
            p = bisect_left(pref, v[i])

            # Valid range where v[i] remains dominant
            left = prev[i] + 1
            right = min(i, p - 1)

            if left <= right:

                # Number of valid starting positions
                count = right - left + 1

                # Sum of pref[left...right]
                total_pref = pref_sum[right + 1] - pref_sum[left]

                # Total contribution for those starts
                contribution = count * v[i] - total_pref

                # Multiply by valid ending positions
                extra += (nxt[i] - i) * contribution

        # Final answer = normal contribution + extra gain
        ans.append(str(base_sum + extra))

    # Print answers for all test cases
    print("\n".join(ans))


# Time Complexity:
# Building base_sum, cost, pref, pref_sum, v  -> O(N)
# Previous Greater Element (Monotonic Stack)  -> O(N)
# Next Greater Element (Monotonic Stack)      -> O(N)
# Binary Search for each index                -> O(N log N)
# Overall per test case                       -> O(N log N)

# Space Complexity:
# cost, pref, pref_sum, v, prev, nxt, stack
# Overall                                     -> O(N)
