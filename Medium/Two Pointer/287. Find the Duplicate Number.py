"""
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
"""

class Solution(object):
    def findDuplicate(self, nums):
        # fast and slow pointers
        # start slow at 0 and fast at 1 and move slow once, and move fast twice
        # if slow and fast have the same value but slow != fast, we return that value
        # handle out of bounds
        # if slow is == len(nums) we can set slow to 0
        # if fast is len(nums) we can do the same but there are cases where its > len
        # in that case we can do this:
        # if fast >= len(nums): fast -= len(nums) (MUST BE DONE FIRST)

        slow = fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

# Time Complexity:
# Runtime: O(n)
# Space: O(1)
