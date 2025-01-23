'1765. Map of Highest Peak'

# You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

# If isWater[i][j] == 0, cell (i, j) is a land cell.
# If isWater[i][j] == 1, cell (i, j) is a water cell.
# You must assign each cell a height in a way that follows these rules:

# The height of each cell must be non-negative.
# If the cell is a water cell, its height must be 0.
# Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
# Find an assignment of heights such that the maximum height in the matrix is maximized.

# Return an integer matrix height of size m x n where height[i][j] is cell (i, j)s height. If there are multiple solutions, return any of them.


class Solution(object):
    def highestPeak(self, isWater):
        ROWS = len(isWater)
        COLS = len(isWater[0])
        # the idea here is to set all unvisited cells to -1
        # if we encounter any anything > -1, we know that cell has been processed
        # we should avoid updating already processed cells to prevent inaccuracy
        res = [ [-1] * COLS for _ in range(ROWS)]
        queue = deque()

        # enqueue our water cells
        # since water cells are of a fixed value, we should always start with them first
        for row in range(ROWS):
            for col in range(COLS):
                if isWater[row][col] == 1: # if its a water cell
                    queue.append((row, col))
                    res[row][col] = 0
        
        # add, validate, and process all valid adjacent cells starting at water cells
        # save the current height of every processed cell, and +1 to all its neighbors
        while queue:
            row, col = queue.popleft()
            height = res[row][col]
            adjacent_cells = [ [row+1, col], [row, col+1], [row-1,col], [row, col-1] ]

            for adjRow, adjCol in (adjacent_cells):
                # check validity: must be in bounds, and not visited
                if (adjRow < 0 or adjCol < 0 or
                    adjRow >= ROWS or adjCol >= COLS or
                    res[adjRow][adjCol] != -1
                ):
                    continue # if invalid, skip that cell

                res[adjRow][adjCol] = height + 1 # add one to valid adjacent cell
                queue.append((adjRow, adjCol)) # enqueue valid cell
        
        return res


# Time Complexity:
# Runtime: O(n)
# Space: O(n)