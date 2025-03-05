"""
78. Subsets

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

class Solution(object):
    def subsets(self, nums):
        res = []
        curr = []
        
        def backtrack(i):
            if i == len(nums):
                res.append(curr[:])
                return

            # option 1: dont select value
            backtrack(i+1)

            # option 2: select value
            curr.append(nums[i])
            backtrack(i+1)
            curr.pop()

        backtrack(0)
        return res


# Time Complexity:
# Runtime: O(2^n)
# Space: O(n)