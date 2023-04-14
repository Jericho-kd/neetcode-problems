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
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
print(reverse_list(a))

def test(arr: list[int]) -> bool:
    if bool(arr):
        return True
    else:
        return False
    
print(test([]))