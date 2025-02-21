"""
1261. Find Elements in a Contaminated Binary Tree

Given a binary tree with the following rules:

root.val == 0
For any treeNode:
If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.

Example 1:

Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements(object):

    def __init__(self, root):
        self.root = root
        self.values = set()

        # set root node to 0 intitally then recurse from there
        if self.root:
            self.root.val = 0
            self.values.add(0)
            self.recover(self.root)
        
    def recover(self, node):
        # if left exists, apply formula then recurse on that node
        if node.left:
            node.left.val  = (2 * node.val + 1)
            self.values.add(node.left.val)
            self.recover(node.left)
        # if right exists, apply formula then recurse on that node
        if node.right:
            node.right.val  = (2 * node.val + 2)
            self.values.add(node.right.val)
            self.recover(node.right)

    def find(self, target):
        if target in self.values:
            return True
        else:
            return False

# Time Complexity:
# Runtime: O(n)
# Space: O(n)