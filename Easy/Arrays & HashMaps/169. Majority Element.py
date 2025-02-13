'169. Majority Element'

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:

# Input: nums = [3,2,3]
# Output: 3

# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# Can you solve in O(1) space?


class Solution(object):
    def majorityElement(self, nums):
        count = 0
        current = None

        for num in nums:
            if count == 0: 
                current = num
            
            if current == num:
                count += 1
            else:
                count -= 1
        
        return current


# Time Complexity:
# Runtime: O(n)
# Space: O(1)