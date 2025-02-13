'3. Longest Substring without Repeating Characters'

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if the string is empty
        if not s:
            return 0

        if len(s) == 1:
            return 1

        visited = set()  # Set to track unique characters
        max_sub = 0      # Maximum substring length
        l = 0            # Left pointer
        
        # Iterate through the string with right pointer
        for r in range(len(s)):
            # While the current character is already in the set
            while s[r] in visited:
                # Remove characters from the left side of the window
                visited.remove(s[l])
                l += 1
            
            # Add current character to the set
            visited.add(s[r])
            
            # Update maximum substring length
            max_sub = max(max_sub, r - l + 1)
        
        return max_sub


# Time Complexity:
# Runtime: O(n)
# Space: O(n)
