'347. Top K Frequent Elements'

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


class Solution(object):
    def topKFrequent(self, nums, k):
        res = []
        count = {}
        buckets = [ [] for _ in range(len(nums)+1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, count in count.items():
            buckets[count].append(num)

        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:# we have our top k elements
                    return res


# Time Complexity
# Runtime: O(n)
# Space: O(n)