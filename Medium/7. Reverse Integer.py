'7. Reverse Integer'

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21


class Solution(object):
    def reverse(self, x):
        reverse = 0
        negative = False
        # our bit ranges
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if x < 0: # handle negative cases
            negative = True
            x = abs(x) # make positive
        
        while (x > 0): # reverse the num
            reverse = reverse * 10 + x % 10
            x = x // 10
        
        if negative: # if x was negative, negate it again
            reverse = -reverse

        if reverse < INT_MIN or reverse > INT_MAX: # return 0 if outside bit range
            return 0

        return reverse


# Time Complexity:
# Runtime: O(log(n))
# Space: O(1)