# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def mergeTwoLists(l1, l2):
    merged = []
    merged.append(l1.head)
    if l1.next < l1.head:
        merged.append(l1.next)
    elif l1.next > l1.head:
        merged.append(l1.head)
    elif l1.next == l1.head:
        merged.append(l1.next)
        merged.append(l2.head)
    elif l1.next < l2.next:
        merged.append(l1.next)
    else:
        merged.append(l2.next)
    return merged