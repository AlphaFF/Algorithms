# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


def mergeTwoLists(l1, l2):
	curr = dummy = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr.next = l1 or l2
        return dummy.next


def mergeTwoLists1(l1, l2):
    if a and b:
        if a.val > b.val:
            a, b = b, a
        a.next = self.mergeTwoLists1(a.next, b)
    return a or b