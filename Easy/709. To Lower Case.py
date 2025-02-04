'709. To Lower Case'

"""
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"
"""


# without string method approach:
# same time complexity but runtime is a lot slower
class Solution(object):
    def toLowerCase(self, s):
        res = ""
        for i in range(len(s)):
            if ord(s[i]) in range(65,91): # is upper case
                asc = ord(s[i]) + 32
                res += chr(asc)
            else:
                res += s[i]

        return res

# Time Complexity:
# Runtime: O(n)
# Space: O(n)


# intuitive way, much faster:
class Solution(object):
    def toLowerCase(self, s):
        return s.lower()

# Time Complexity:
# Runtime: O(n)
# Space: O(n)

