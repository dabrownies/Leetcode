"""
2570. Merge Two 2D Arrays by Summing Values

You are given two 2D integer arrays nums1 and nums2.

nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.


Example 1:

Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
Output: [[1,6],[2,3],[3,2],[4,6]]
Explanation: The resulting array contains the following:
- id = 1, the value of this id is 2 + 4 = 6.
- id = 2, the value of this id is 3.
- id = 3, the value of this id is 2.
- id = 4, the value of this id is 5 + 1 = 6.
Example 2:

Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
Explanation: There are no common ids, so we just include each id with its value in the resulting list.
"""

class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        we know theres two arrays, all ids are unique so each id can have a max
        of 2 values. 

        map will have all ids and if we've seen a value already we know to sum its
        current value
        if not we add it to the map with its respective value

        then for every pair in the map, we append a list of key, val to res
        then sort res by keys
        """
        adj = {}

        for k, v in nums1:
            adj[k] = adj.get(k, 0) + v
        
        for k, v in nums2:
            adj[k] = adj.get(k, 0) + v
        
        res = [[k, v] for k, v in adj.items()]

        return sorted(res)

# Time Complexity:
# Runtime: O(nlogn)
# Space: O(n+m)