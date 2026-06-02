# Time Complexity: O(N) per test case
# - Building one[] and two[] arrays: O(N)
# - Finding the answer: O(N)
# Total: O(N)
#
# Space Complexity: O(N)
# - A array: O(N)
# - B array: O(N)
# - one array: O(N)
# - two array: O(N)
# Total: O(N)

# Number of test cases
T = int(input())

for _ in range(T):

    # Length of arrays
    N = int(input())

    # Input arrays A and B
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # one[x] = 1 if x appears in a pair (x,y)
    # where x != y
    one = [0] * (N + 1)

    # two[x] = 1 if pair (x,x) exists
    two = [0] * (N + 1)

    # Traverse all pairs
    # Time: O(N)
    for i in range(N):

        # Same value in both arrays
        if A[i] == B[i]:

            # Mark that pair (x,x) exists
            two[A[i]] = 1

        else:

            # Mark occurrence of both values
            one[A[i]] = 1
            one[B[i]] = 1

    # Counts how many values are
    # not forced into both arrays
    cnt = 0

    # Check values from 0 to N
    # Time: O(N)
    for x in range(N + 1):

        # Value x does not appear anywhere
        if one[x] == 0 and two[x] == 0:
            print(x)
            break

        # Value x is not forced into both arrays
        elif two[x] == 0:

            # First such value found
            if cnt == 0:
                cnt = 1

            # Second such value found
            # This becomes the answer
            else:
                print(x)
                break
