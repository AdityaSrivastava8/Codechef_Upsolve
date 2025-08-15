# Read number of test cases
t = int(input())  # t: number of test cases | TC: O(1), SC: O(1)

for _ in range(t):  # Loop over each test case | TC: O(t)
    # Read a1, b1 (initial gold, silver) and a2, b2 (target gold, silver)
    a1, b1, a2, b2 = map(int, input().split())  # TC: O(1), SC: O(1)

    # Convert initial coins to "total value" in silver units
    # 1 gold = 5 silver
    v1 = 5 * a1 + b1  # TC: O(1), SC: O(1)

    # Convert target coins to "total value" in silver units
    v2 = 5 * a2 + b2  # TC: O(1), SC: O(1)

    # Check conditions:
    # 1. v1 >= v2 (can't increase total value)
    # 2. (v1 - v2) % 6 == 0 (can only reduce value in steps of 6)
    if v1 >= v2 and (v1 - v2) % 6 == 0:  # TC: O(1)
        print("Yes")  # Possible to reach target
    else:
        print("No")   # Not possible to reach target

# Overall TC: O(t) because each test case takes constant time
# Overall SC: O(1) because we only store a fixed number of integer variables
