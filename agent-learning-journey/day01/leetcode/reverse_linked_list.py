"""
LeetCode 206 · 反转链表（简单）
------------------------------------------------------------------
顺便练 Python 的类与类型提示（Day 2 的预热）。
节点定义已给出，实现 reverse(head)，返回反转后的新头节点。
运行：uv run leetcode/reverse_linked_list.py
"""

from __future__ import annotations
from typing import Optional


class ListNode:
    """对比 Java：
    - __init__ 就是构造器，self 等价于 this
    - 没有 getter/setter，直接属性访问（Python 哲学：大家都是成年人）
    - val: int = 0 是「带默认值的类型提示」，Java 语法糖 record 的感觉"""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def to_list(head: Optional[ListNode]) -> list[int]:
    """工具：链表 -> 列表。遍历写法和 Java 一模一样。"""
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def build(values: list[int]) -> Optional[ListNode]:
    """工具：列表 -> 链表。感受「哨兵节点」写法，比 Java 简洁。"""
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    """TODO: 三指针迭代法（prev / cur / nxt），Java 里怎么写 Python 就怎么写。
    彩蛋：Python 支持多重赋值 a, b = b, a，可以一行完成三指针旋转（做完试试）。"""
    ...


if __name__ == "__main__":
    assert to_list(reverse(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1], "未通过"
    assert to_list(reverse(build([1]))) == [1], "未通过"
    assert to_list(reverse(build([]))) == [], "未通过"
    print("✅ LeetCode 206 · 反转链表 通过！")
