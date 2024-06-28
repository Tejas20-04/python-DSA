# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # Handle edge case where the list has only one node
        if head.next is None:
            return None
        
        # Calculate the length of the list
        current = head
        length = 0
        while current is not None:
            current = current.next
            length += 1

        # Find the position to remove from the beginning
        nth = length - n

        # Handle edge case where the head needs to be removed
        if nth == 0:
            return head.next

        # Traverse the list to find the node just before the one to remove
        current = head
        for _ in range(nth - 1):
            current = current.next

        # Remove the nth node from the end
        current.next = current.next.next
        
        return head
