"""3174. Clear Digits

You are given a string s.

Your task is to remove all digits by doing this operation repeatedly:

Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.


Example 1:

Input: s = "abc"

Output: "abc"

Explanation:

There is no digit in the string.

Example 2:

Input: s = "cb34"

Output: ""

Explanation:

First, we apply the operation on s[2], and s becomes "c4".

Then we apply the operation on s[1], and s becomes "".
"""


class Solution(object):
    def clearDigits(self, s):
        stack = []
        for i in range(len(s)):
            if s[i].isalpha():
                stack.append(s[i])
                continue
            else:
                stack.pop()
        
        if not stack:
            return ""
        else:
            res = "".join(ch for ch in stack)
        
        return res

# Time Complexity:
# Runtime: O(n)
# Space: O(1)