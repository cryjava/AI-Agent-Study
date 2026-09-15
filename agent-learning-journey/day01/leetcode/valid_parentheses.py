"""
LeetCode 20 · 有效的括号（简单）
------------------------------------------------------------------
判断字符串是否合法：'()'、'[]'、'{}' 可任意嵌套但必须正确闭合。
Java 里用 Stack<Character> / ArrayDeque；Python 直接用 list：
    stack.append(x)  ==  push
    stack.pop()      ==  pop
    not stack        ==  isEmpty()
这题就是今天下午学的「dict + list」双结构实战。
运行：uv run leetcode/valid_parentheses.py
"""

PAIRS = {")": "(", "]": "[", "}": "{"}   # 右括号 -> 左括号


def is_valid(s: str) -> bool:
    """TODO: 遍历 s，用一个 list 当栈：
    - 左括号 -> 入栈
    - 右括号 -> 栈空或栈顶不配对返回 False；配对则出栈
    全部遍历完，栈为空才是 True（别忘了空字符串是合法的）。"""
    ...


if __name__ == "__main__":
    assert is_valid("()") is True, "未通过"
    assert is_valid("()[]{}") is True, "未通过"
    assert is_valid("(]") is False, "未通过"
    assert is_valid("([)]") is False, "未通过"
    assert is_valid("{[]}") is True, "未通过"
    assert is_valid("") is True, "未通过"
    print("✅ LeetCode 20 · 有效的括号 通过！")
