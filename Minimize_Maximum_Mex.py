# Time Complexity: O(N) per test case
# Space Complexity: O(N)

# Number of test cases
t = int(input())

for _ in range(t):

    # Length of arrays
    n = int(input())

    # Input arrays
    # Space: O(N)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # cnt[x] = total occurrences of value x
    # Space: O(N)
    cnt = [0] * (n + 1)

    # same[x] = 1 if pair (x,x) exists
    # Space: O(N)
    same = [0] * (n + 1)

    # Traverse all pairs
    # Time: O(N)
    for i in range(n):

        # If both values are same
        if a[i] == b[i]:

            # Count x once
            cnt[a[i]] += 1

            # Mark existence of (x,x)
            same[a[i]] = 1

        else:

            # Count both values
            cnt[a[i]] += 1
            cnt[b[i]] += 1

    # Start checking from 0
    ans = 0

    # In the worst case ans moves from 0 to N
    # Time: O(N)
    while True:

        # Number does not appear at all
        if cnt[ans] == 0:
            break

        # Number appears only once
        if cnt[ans] == 1:
            break

        # Number appears exactly twice
        # but there is no (x,x) pair
        if cnt[ans] == 2 and same[ans] == 0:
            break

        # Check next value
        ans += 1

    print(ans)

# Overall Time Complexity:
# O(N) + O(N) = O(N)

# Overall Space Complexity:
# a + b + cnt + same
# O(N) + O(N) + O(N) + O(N)
# = O(N)
