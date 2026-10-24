# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Make hashmap: 
        seen = set()
        index = 0
        curr = head

        # Go through linked list
        while curr is not None:
            # Check if next is already in hashmap: if so return True 
            # Else add to hashmap with val->index
            if curr in seen:
                return True
            else:
                seen.add(curr)
                
            # move through the linked list and update index
            print(seen)
            curr = curr.next
            index += 1 
        return False

