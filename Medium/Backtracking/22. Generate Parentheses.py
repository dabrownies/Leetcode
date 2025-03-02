"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

class Solution(object):
    def generateParenthesis(self, n):
        res = []
        curr = []

        # base case: number of open and close brackets == n
        # two choices:
        # if number of open is < n: append "("
        # if number of closed is < opened: append "("
        def backtrack(opened, closed):
            if opened == closed == n:
                res.append("".join(curr))
                return

            if opened < n:
                curr.append("(")
                backtrack(opened + 1, closed)
                curr.pop()
            
            if closed < opened:
                curr.append(")")
                backtrack(opened, closed + 1)
                curr.pop()

        backtrack(0, 0)
        return res

# Time Complexity:
# Runtime: O(n)
# Space: O(n)