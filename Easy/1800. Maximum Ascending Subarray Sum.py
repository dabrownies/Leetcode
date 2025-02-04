'1800. Maximum Ascending Subarray Sum'

"""
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
Example 2:

Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
Example 3:

Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
"""


class Solution(object):
    def maxAscendingSum(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        l = 0
        r = 1
        max_sum = nums[l]
        curr_sum = nums[l]

        while r != len(nums):
            if nums[l] < nums[r]:
                curr_sum += nums[r]
                max_sum = max(max_sum, curr_sum)
                r += 1
                l += 1
            else:
                l = r
                r += 1
                curr_sum = nums[l]
                max_sum = max(max_sum, curr_sum)
        
        return max_sum

# Time Complexity:
# Runtime: O(n)
# Space: O(1)