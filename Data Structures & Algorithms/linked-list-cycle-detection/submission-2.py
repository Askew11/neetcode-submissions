# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Make set
        seen = set()
        curr = head

        # Go through linked list
        while curr is not None:
            # Check if we have seen this node and if so print True else add it
            if curr in seen:
                return True
            else:
                seen.add(curr)
                
            # move through the linked list and update index
            print(seen)
            curr = curr.next
        return False

