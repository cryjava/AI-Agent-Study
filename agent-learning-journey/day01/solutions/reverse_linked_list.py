"""参考答案 · LeetCode 206 反转链表"""

from __future__ import annotations
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def to_list(head: Optional[ListNode]) -> list[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def build(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    cur = head
    while cur:
        nxt = cur.next     # 先存后继
        cur.next = prev    # 反指
        prev = cur         # prev 前进
        cur = nxt          # cur 前进
    return prev
    # 彩蛋写法（一行完成指针旋转，右边先整体求值再赋值）：
    #   while cur:
    #       cur.next, prev, cur = prev, cur, cur.next
    #   return prev


if __name__ == "__main__":
    assert to_list(reverse(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(reverse(build([1]))) == [1]
    assert to_list(reverse(build([]))) == []
    print("✅ LeetCode 206 · 反转链表 通过！")
