"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]

 

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.


SOLUTION: """

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        seen = set()
        dummy = ListNode(-1)
        dummy.next = head
        prevNode = dummy
        currNode = head
        
        while currNode is not None:
            if currNode.val in seen:
                prevNode.next = currNode.next
                currNode = currNode.next
            else:
                seen.add(currNode.val)
                prevNode = currNode
                currNode = currNode.next
        return dummy.next

Time Complexity: O(n)
Space Complexity: O(n)