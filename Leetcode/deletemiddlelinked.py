# Definition for singly-linked list.
from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or head.next==None:
            return None

        count=0
        current_node=head

        while current_node:
            count+=1
            current_node=current_node.next

        middle=count//2
        current_node=head

        for i in range(middle-1):
            current_node=current_node.next
        
        current_node.next=current_node.next.next

        return head
