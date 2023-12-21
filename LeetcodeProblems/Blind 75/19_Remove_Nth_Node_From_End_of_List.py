"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

 

Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

 

Follow up: Could you do this in one pass?



"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head

        for _ in range(n):
            r = r.next

        if r == None:
            return head.next

        while r.next is not None:
            r = r.next
            l = l.next

        tmp = l.next
        l.next = l.next.next
        tmp.next = None

        return head

#Time Complexity = O(n)
#Space Complexity = O(1)
