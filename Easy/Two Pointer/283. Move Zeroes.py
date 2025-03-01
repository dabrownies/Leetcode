"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""

class Solution(object):
    def moveZeroes(self, nums):
        zero_ndx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_ndx], nums[i] = nums[i], nums[zero_ndx]
                zero_ndx += 1

# Time Complexity:
# Runtime: O(n)
# Space: O(1)