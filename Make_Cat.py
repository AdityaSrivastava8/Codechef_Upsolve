from collections import Counter  # Import Counter to count occurrences of each element

W = input().strip()  # Remove leading/trailing spaces from the input string

# Compare frequency of characters in input string W with frequency of characters in "cat"
if Counter(W) == Counter("cat"):  # O(n) time for counting characters
    print("Yes")  # If both have same character counts, print "Yes"
else:
    print("No")   # Otherwise, print "No"

# Time Complexity: O(n) - Counting characters in W takes O(n), comparison is O(1) since "cat" is fixed size
# Space Complexity: O(1) - Extra space is constant because "cat" length is fixed and W's Counter depends only on 26 lowercase letters max
