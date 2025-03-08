"""
2379. Minimum Recolors to Get K Consecutive Black Blocks

You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.
"""

class Solution(object):
    def minimumRecolors(self, blocks, k):
        min_ops = 999
        white_count = 0

        for i in range(k):
            if blocks[i] == 'W':
                white_count += 1

        min_ops = min(min_ops, white_count)

        for j in range(k, len(blocks)):
            if blocks[j] == 'W': # the next element
                white_count += 1
            if blocks[j - k] == 'W': # get the first element from previous window
                white_count -= 1
            
            min_ops = min(min_ops, white_count)
        
        return min_ops

# Time Complexity:
# Runtime: O(n)
# Space: O(1)