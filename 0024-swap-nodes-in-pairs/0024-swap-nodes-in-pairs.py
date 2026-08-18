class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            a = prev.next
            b = a.next

            # swap
            prev.next = b
            a.next = b.next
            b.next = a

            prev = a

        return dummy.next