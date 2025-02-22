"""
46. Permutations

Given an array nums of distinct integers, return all the possible 
permutations. You can return the answer in any order.


Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""

class Solution:
    def permute(self, nums):
        n = len(nums)
        res = []
        perms = []

        def backtrack():
            if len(perms) == n:
                res.append(perms[:])
                return
        
            for num in nums:
                if num not in perms:
                    perms.append(num)
                    backtrack()
                    perms.pop()

        backtrack()   
        return res

# Time Complexity:
# Runtime: O(n!*n)
# Space: O(n!*n)