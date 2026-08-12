# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head   # moves one step
        fast = head   # moves two steps

        # traverse list
        while fast and fast.next:
            slow = slow.next          # move slow by 1
            fast = fast.next.next     # move fast by 2

        # slow will be at middle
        return slow