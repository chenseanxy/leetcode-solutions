class ResultManager:
    def __init__(self):
        self.result = None
        self.to_insert = None
    def insert(self, val):
        if not self.result or not self.to_insert:
            self.result = ListNode(val)
            self.to_insert = self.result
        else:
            self.to_insert.next = ListNode(val)
            self.to_insert = self.to_insert.next

    def append(self, node):
        if not self.result or not self.to_insert:
            self.result = node
            self.to_insert = None
        else:
            self.to_insert.next = node

    def _output(self):
        ptr = self.result
        ls = []
        while ptr:
            ls.append(ptr.val)
            ptr = ptr.next
        print(ls)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        rm = ResultManager()
        while list1 and list2:
            if list1.val < list2.val:
                rm.insert(list1.val)
                list1 = list1.next
            else:
                rm.insert(list2.val)
                list2 = list2.next
        if list1:
            rm.append(list1)
        if list2:
            rm.append(list2)
        return rm.result
