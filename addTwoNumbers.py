# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t1 = l1
        t2 = l2
        s = None
        carry = 0
        while t1 != None and t2 != None:
            sum = t1.val + t2.val + carry
            carry = int(sum / 10)
            val = sum % 10
            if s == None:
                s = ListNode(val)
            else:
                temp = s
                while temp.next != None:
                    temp = temp.next
                temp.next = ListNode(val)
            t1 = t1.next
            t2 = t2.next
        if t1 != None:
            while t1 != None:
                if s == None:
                    s = ListNode(t1.val)
                else:
                    temp = s
                    while temp.next != None:
                        temp = temp.next
                    temp.next = ListNode(t1.val)
        if t2 != None:
            while t2 != None:
                if s == None:
                    s = ListNode(t2.val)
                else:
                    temp = s
                    while temp.next != None:
                        temp = temp.next
                    temp.next = ListNode(t2.val)
        return s


l1 = ListNode(1)
l12 = ListNode(8)
l1.next = l12
l2 = ListNode(0)
s = Solution()
s.addTwoNumbers(l1, l2)