# Time Complexity: O(N × 30) = O(N)
# Space Complexity: O(30) = O(1)

# Number of test cases
t = int(input())

for _ in range(t):

    # Size of the array
    n = int(input())

    # Read array elements
    a = list(map(int, input().split()))

    # cnt[b] stores how many numbers contain bit b
    # We need 30 positions because Ai < 2^30
    cnt = [0] * 30

    # Assume reduction is possible initially
    possible = True

    # Process every number in the array
    for x in a:

        # Check all bit positions from 0 to 29
        for b in range(30):

            # If bit b is set in x
            if x & (1 << b):

                # Increase frequency of bit b
                cnt[b] += 1

                # If the same bit appears in more than one number,
                # complete reduction to one element is impossible
                if cnt[b] > 1:
                    possible = False

    # Print final answer
    print("Yes" if possible else "No")
