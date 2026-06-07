# Import sys for faster input reading
import sys

def main():

    # Faster than input() for competitive programming
    input = sys.stdin.readline

    # Number of test cases
    t = int(input())

    while t:

        # One test case completed
        t -= 1

        # Lengths of A and B
        n, m = map(int, input().split())

        # Read arrays A and B
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        # Number of elements that can be deleted
        ans = 0

        # Last position containing 1 in B seen so far
        one = -1

        # Last position containing 0 in B seen so far
        zero = -1

        # Process every element of A
        for i in range(n):

            # Update latest positions of 0 and 1 in B
            if i < m:

                if b[i] == 0:
                    zero = i

                else:
                    one = i

            # Case 1:
            # Current positions already match
            # So this element can be deleted immediately
            if i < m and a[i] == b[i]:
                ans += 1

            else:

                # Effective position after previous deletions
                # Since ans elements before this are deleted,
                # this element shifts left by ans positions
                pos = i - ans

                # Current element is 1
                if a[i] == 1:

                    # If it can reach a position in B
                    # containing 1, delete it
                    if pos <= one:
                        ans += 1

                # Current element is 0
                else:

                    # If it can reach a position in B
                    # containing 0, delete it
                    if pos <= zero:
                        ans += 1

        # Minimum final length
        # = Original length - Deleted elements
        print(n - ans)

# Program starts here
if __name__ == "__main__":
    main()

# Time Complexity: O(N)
# Explanation:
# - We scan array A exactly once.
# - Every operation inside the loop takes O(1).
# - Therefore total complexity per test case is O(N).

# Space Complexity: O(1)
# Explanation:
# - Only a few variables are used:
#   ans, one, zero, pos, i
# - No extra arrays proportional to N are created.
# - Therefore extra space is constant.
