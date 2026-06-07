# Import the sys module
# It provides access to system-specific functions
# We use it here for faster input reading
import sys

def main():

    # input() is normally slower for large inputs
    # sys.stdin.readline() reads directly from standard input (keyboard/input file)
    # It is much faster and commonly used in competitive programming
    input = sys.stdin.readline

    # Read number of test cases
    t = int(input())

    # Process each test case
    while t:

        # One test case completed
        t -= 1

        # Length of array A
        n = int(input())

        # Read array A containing only 1s and 2s
        a = list(map(int, input().split()))

        # Total number of non-empty subarrays
        # Formula = n * (n + 1) / 2
        # Initially assume every subarray is stable
        res = n * (n + 1) // 2

        # Check every possible even-length center
        # Center lies between positions i and i+1
        for i in range(1, n - 2):

            # Tracks depth of current alternating pattern
            rem = 1

            # Left and right pointers for expansion
            l = i
            r = i + 1

            # Expand outward while pointers stay inside array
            while l >= 0 and r < n:

                # If both sides become equal
                # alternating pattern breaks
                # so stop expanding
                if a[l] == a[r]:
                    break

                # If adjacent equal values appear early
                # this pattern cannot become a bad subarray
                # so stop expanding
                if a[l] == a[l + 1] and rem <= 2:
                    break

                # If adjacent equal values appear later
                # alternating streak breaks
                # start counting from beginning
                if a[l] == a[l + 1]:
                    rem = 0

                # Increase alternating depth
                rem += 1

                # If alternating depth becomes 3 or more
                # an unstable subarray is found
                if rem >= 3:
                    res -= 1

                # Move outward to next layer
                l -= 1
                r += 1

        # Remaining subarrays are stable
        print(res)

# Program starts here
if __name__ == "__main__":
    main()

# Time Complexity: O(N²)
# Explanation:
# - We try every possible even-length center.
# - For each center, we expand outward using two pointers.
# - In the worst case, expansion can take O(N) time.
# - Therefore total complexity = O(N × N) = O(N²).

# Space Complexity: O(1)
# Explanation:
# - Apart from the input array A, only a constant number of variables
#   (res, rem, l, r, i, t, n) are used.
# - No additional data structures are created.
