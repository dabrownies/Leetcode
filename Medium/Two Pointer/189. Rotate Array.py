"""
189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

class Solution:
    def rotate(self, nums, k) -> None:
        # helper function
        def reverse_arr(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        # the amount of ops to do that will yield a different output from the input
        k = k % len(nums)
        n = len(nums) - 1

        if k == 0 or len(nums) == 1:
            return nums
        
        # reverse input array
        reverse_arr(0, n)

        # reverse first k
        reverse_arr(0, k - 1)

        # reverse remaining
        reverse_arr(k, n)


# Time Complexity:
# Runtime: O(n)
# Space: O(1)