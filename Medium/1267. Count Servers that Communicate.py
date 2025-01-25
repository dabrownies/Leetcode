'1267. Count Servers that Communicate'

'''
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Example 2:

Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.

Example 3:

Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
'''


def countServers(grid):
    ROWS = len(grid)
    COLS = len(grid[0])
    row_count = [0] * ROWS
    col_count = [0] * COLS
    server_count = 0

    # get the amount of servers for each row, and each column
    # the index represents the row/col number, and its respective value represents the number of servers in that row/col
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1:
                row_count[row] += 1
                col_count[col] += 1


    # iterate through the matrix and find every server
    # check if the row/col count for that row/col is > 1
    # if it is greater than 1, that means that server at grid[row][col] is valid and can be added to the total
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == 1 and (row_count[row] > 1 or col_count[col] > 1):
                server_count += 1

    return server_count


# Time Complexity:
# Runtime: O(n^2)
# Space: O(n)