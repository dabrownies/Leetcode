'14. Longest Common Prefix'

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        prefix = strs[0]
        prefix_len = len(prefix)

        for s in strs[1:]:
            while prefix != s[0: prefix_len]:
                prefix_len -= 1
                if prefix_len == 0:
                    return ""

                prefix = prefix[0:prefix_len]

        return prefix


# Time Complexity:
# Runtime: O(n*m)
# Space: O(1)