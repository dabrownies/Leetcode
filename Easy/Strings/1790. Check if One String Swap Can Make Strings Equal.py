"1790. Check if One String Swap Can Make Strings Equal"

"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
"""


class Solution(object):
    def areAlmostEqual(self, s1, s2):
        indices = [] # store indexes of mismatches

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indices.append(i)
            if len(indices) > 2: # impossible to fix with 1 swap
                return False

        if not indices:
            return True
        elif len(indices) == 1:
            return False
        else:
            i, j = indices
            return s1[i] == s2[j] and s1[j] == s2[i]


# Time Complexity:
# Runtime: O(n)
# Space: O(1)