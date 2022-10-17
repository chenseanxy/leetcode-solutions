class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        res = head.next
        prev = None
        while head and head.next:
            ptr1, ptr2, ptr3 = head, head.next, head.next.next
            if prev:
                prev.next = ptr2
            prev = ptr1
            head, ptr1.next, ptr2.next = ptr3, ptr3, ptr1
        return res
