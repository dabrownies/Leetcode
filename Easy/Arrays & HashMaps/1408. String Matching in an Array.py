'1408. String Matching in an Array'

# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

# A substring is a contiguous sequence of characters within a string

# Example 1:
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.

# Example 2:
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".

# Example 3:
# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.


class Solution(object):
    def stringMatching(self, words):
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] == words[j]:
                    continue
                elif words[i] in words[j]:
                    res.append(words[i])
                    break
        
        return res

# Time Complexity:
# Runtime: O(n^2)
# Space: O(n)