"""参考答案 · LeetCode 20 有效的括号"""

PAIRS = {")": "(", "]": "[", "}": "{"}


def is_valid(s: str) -> bool:
    stack = []                       # list 就是栈
    for ch in s:
        if ch in "([{":              # 左括号入栈
            stack.append(ch)
        else:                        # 右括号：查栈顶
            if not stack or stack.pop() != PAIRS[ch]:
                return False
    return not stack                 # 栈空才合法；空串自然合法


if __name__ == "__main__":
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("") is True
    print("✅ LeetCode 20 · 有效的括号 通过！")
