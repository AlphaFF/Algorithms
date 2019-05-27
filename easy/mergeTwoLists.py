# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#     def __repr__(self):
#         if self:
#             return "{} -> {}".format(self.val, self.next)


# def mergeTwoLists(l1, l2):
#   curr = dummy = ListNode()
#     while l1 and l2:
#         if l1.val < l2.val:
#             curr.next = l1
#             l1 = l1.next
#         else:
#             curr.next = l2
#             l2 = l2.next
#         curr.next = l1 or l2
#         return dummy.next


# def mergeTwoLists1(l1, l2):
#     if a and b:
#         if a.val > b.val:
#             a, b = b, a
#         a.next = self.mergeTwoLists1(a.next, b)
#     return a or b


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return '{}->{}'.format(self.val, self.next)


l3 = ListNode(4)
l2 = ListNode(2)
l2.next = l3
l1 = ListNode(1)
l1.next = l2
print(l1)


def merge_two_list(l1, l2):
    curr = dummy = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next


def merge_two_list1(l1, l2):
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = merge_two_list1(l1.next, l2)
    return l1 or l2
