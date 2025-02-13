'6. Zigzag Conversion'

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"


class Solution(object):
    def convert(self, s, numRows):
        # edge cases for when the structure of the string will never change
        # this will help perserve memory
        if len(s) == 1 or numRows == 1 or (len(s) == numRows):
            return s
        
        # use 2D array with the amount of rows and no limit to columns
        matrix = [ [] for _ in range(numRows)]
        startZigZag = False

        i = 0
        for ch in s:
            if startZigZag:
                i -= 1
                matrix[i].append(ch)
                if i == 0:
                    startZigZag = False
                    i += 1

            else:
                matrix[i].append(ch)
                i += 1
                if i == numRows:
                    startZigZag = True
                    i -= 1

        return ''.join(char for row in matrix for char in row)


# Time Complexity:
# Runtime: O(n)
# Space: O(n)