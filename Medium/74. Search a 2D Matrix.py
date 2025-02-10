"""74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bottom = ROWS - 1
        
        # perform BS on all matrix rows
        while top <= bottom:
            mid_row = (top + bottom) // 2

            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top = mid_row + 1
            else:
                break # found the correct row 
        
        # perform BS on matrix row
        l = 0
        r = COLS - 1

        while l <= r:
            mid = (l + r) // 2

            if target == matrix[mid_row][mid]:
                return True
            elif target < matrix[mid_row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return False

# Time Complexity:
# Runtime: O(log(m*n))
# Space: O(1)