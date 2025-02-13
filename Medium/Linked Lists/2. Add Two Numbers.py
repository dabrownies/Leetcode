'2. Add Two Numbers'

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []

        node1 = l1
        node2 = l2

        while node1 != None:
            stack1.append(node1.val)
            node1 = node1.next
        
        while node2 != None:
            stack2.append(node2.val)
            node2 = node2.next

        num1 = ""
        num2 = ""

        while stack1:
            num1 += str(stack1.pop())
        
        while stack2:
            num2 += str(stack2.pop())
        
        ans = int(num1) + int(num2)
        ans = str(ans)
        ans_stack = []

        for c in ans:
            ans_stack.append(c)
        
        head = ListNode(int(ans_stack.pop()))
        node = head

        while ans_stack:
            node.next = ListNode(int(ans_stack.pop()))
            node = node.next

        return head



# Time Complexity:
# Runtime: O(n + m)
# Space: O(n + m)

