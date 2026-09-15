"""参考答案 · 01 语法基础（卡住 15 分钟以上再看，看完合上重写一遍）"""


def describe_types():
    x = 42
    x = "hello"           # 名字标签换贴了一个对象，类型随对象变
    return (x, type(x).__name__)


def make_greeting(name, score):
    grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 60 else "D"
    return f"{name} 的得分是 {score}，等级是 {grade}"
    # 等级也可以直接内联写在 f-string 里：
    # return f"{name} 的得分是 {score}，等级是 {'A' if score >= 90 else ...}"


def fizzbuzz(n):
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:      # 先判同时整除，否则永远轮不到它
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(i)
    return out


def sum_even_squares(limit):
    total = 0
    for x in range(1, limit + 1):
        if x % 2 == 0:
            total += x * x
    return total


def badge(level):
    # 原来的 bug：level == "admin" or "root" 先算左边（可能是 False），
    # 再和字符串 "root" 做 or —— 非空字符串恒为真，所以条件永远成立。
    # 正确写法（和 Java 一样要写完整比较）：
    if level == "admin" or level == "root":
        return "管理员"
    return "普通用户" if level == "user" else "访客"


if __name__ == "__main__":
    assert describe_types() == ("hello", "str")
    assert make_greeting("小明", 85) == "小明 的得分是 85，等级是 B"
    assert make_greeting("小红", 59) == "小红 的得分是 59，等级是 D"
    assert fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"]
    assert fizzbuzz(15)[14] == "FizzBuzz"
    assert sum_even_squares(10) == 220
    assert badge("admin") == "管理员"
    assert badge("user") == "普通用户"
    assert badge("guest") == "访客"
    print("✅ 上午练习全部通过！")
