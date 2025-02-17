"""
844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty. 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
"""


class Solution(object):
    def backspaceCompare(self, s, t):
        stack_s = []
        stack_t = []

        for ch in s:
            if ch == "#":
                if stack_s:
                    stack_s.pop()
            else:
                stack_s.append(ch)
        
        for ch in t:
            if ch == "#":
                if stack_t:
                    stack_t.pop()
            else:
                stack_t.append(ch)
        
        return stack_s == stack_t

# Time Complexity:
# Runtime: O(n)
# Space: O(n)