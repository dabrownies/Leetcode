'104. Maximum Depth of Binary Tree'

# Given the root of a binary tree, return its maximum depth.

# A binary trees maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:

# Input: root = [1,null,2]
# Output: 2


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        count = 0
        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            count += 1
        
        return count

# Time Complexity:
# Runtime: O(n) 
# Space: O(k)