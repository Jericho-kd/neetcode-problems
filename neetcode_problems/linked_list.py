from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class ListNode:
    value: int = field(repr=True, default=0)
    next: ListNode | None = field(repr=True, default=None)


# 206. Reverse Linked List (easy)
def reverse_list(head: ListNode | None) -> ListNode | None:
    reversed_list = None
    current_head = head

    while current_head:
        new_head = current_head.next
        current_head.next = reversed_list
        reversed_list = current_head
        current_head = new_head

    return reversed_list
        

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

e = ListNode(1)
f = ListNode(3)
j = ListNode(5)
k = ListNode(6)
e.next = f
f.next = j
j.next = k



# 21. Merge Two Sorted Lists (easy)
def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    current = temp = ListNode()

    while list1 and list2:
        if list1.value < list2.value:
            current.next = list1
            list1, current = list1.next, list1
        else:
            current.next = list2
            list2, current = list2.next, list2

    if list1 or list2:
        current.next = list1 if list1 else list2

    return temp.next


print(merge_two_lists(a, e))