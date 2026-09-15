"""
Day 1 · 上午练习：语法基础（变量 / f-string / 控制流 / 循环 / 真值）
====================================================================
怎么用：把每个 TODO 函数补完，然后运行本文件：
    uv run exercises/01_syntax_basics.py
全部通过会打印：✅ 上午练习全部通过！
卡住超过 15 分钟再看 solutions/01_syntax_basics.py（先自己试）。
"""

# ---------------------------------------------------------------
# 练习 1：变量与动态类型
# Java:  int age = 25;        类型绑定在变量上，编译期写死
# Py :   age = 25             变量只是「名字标签」，类型跟着对象走
# ---------------------------------------------------------------

def describe_types():
    """让 x 先指向 42，再指向 "hello"（Java 里这是编译错误，Python 完全合法）。
    返回 (x 的值, type(x).__name__)，结果应为 ("hello", "str")。"""
    x = 42
    # TODO: 把 x 重新赋值为 "hello"，然后返回 (x, type(x).__name__)
    x="hello"
    return (x, type(x).__name__)

# ---------------------------------------------------------------
# 练习 2：f-string（对比 String.format）
# Java:  String.format("用户 %s 年龄 %d", name, age)
# Py :   f"用户 {name} 年龄 {age}"       花括号里能放任意表达式
# ---------------------------------------------------------------

def make_greeting(name, score):
    """返回 "{name} 的得分是 {score}，等级是 {等级}"。
    等级规则：>=90 为 A，>=80 为 B，>=60 为 C，否则 D。
    要求：等级用条件表达式直接写在 f-string 的花括号里，一行 return。
    Python 三元写法：'A' if score >= 90 else 'B'（条件在中间，和 Java 相反）"""
    return f"{name} 的得分是 {score}，等级是 {'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 60 else 'D'}"

# ---------------------------------------------------------------
# 练习 3：控制流关键字（elif / and / or / not）
# Java:  else if / && / || / !
# ---------------------------------------------------------------

def fizzbuzz(n):
    """经典 FizzBuzz：返回 1..n 组成的列表。
    3 的倍数 -> "Fizz"；5 的倍数 -> "Buzz"；同时 -> "FizzBuzz"；其余 -> 数字本身。
    注意：返回列表，不是逐行打印（先算后输出，这是 Agent 代码的常态）。"""
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

# ---------------------------------------------------------------
# 练习 4：循环
# Java:  for (int i = 0; i < limit; i++)  /  for (var x : list)
# Py :   for i in range(limit)            /  for x in lst
# ---------------------------------------------------------------

def sum_even_squares(limit):
    """求 1..limit 内所有偶数的平方和。
    故意要求：用普通 for + if 写（推导式下午再学）。
    自检：sum_even_squares(10) 应为 220（即 4+16+36+64+100）。"""
    result = 0
    for i in range(1, limit+1):
        if i % 2 == 0:
            result += i**2
    return result

# ---------------------------------------------------------------
# 练习 5：修 bug —— 真值陷阱（truthiness）
# Python 里这些值都算「假」：None / False / 0 / 0.0 / "" / [] / {} / set()
# 其他一切（包括非空字符串）都算「真」—— 这和 Java 的布尔严格类型完全不同
# ---------------------------------------------------------------

def badge(level):
    """level 为 "admin" 或 "root" 返回 "管理员"；为 "user" 返回 "普通用户"；
    其他任何值返回 "访客"。
    下面的写法看似和 Java 的 || 等价，实则任何 level 都会返回 "管理员"。
    为什么？想明白原理，然后修好它。"""
    if level in ["admin", "root"]:   # bug 就在这一行
        return "管理员"
    return "普通用户" if level == "user" else "访客"


# ===============================================================
# 自测（不要改这里）
# ===============================================================
if __name__ == "__main__":
    assert describe_types() == ("hello", "str"), "练习 1 未通过"
    assert make_greeting("小明", 85) == "小明 的得分是 85，等级是 B", "练习 2 未通过"
    assert make_greeting("小红", 59) == "小红 的得分是 59，等级是 D", "练习 2 未通过"
    assert fizzbuzz(5) == [1, 2, "Fizz", 4, "Buzz"], "练习 3 未通过"
    assert fizzbuzz(15)[14] == "FizzBuzz", "练习 3 未通过"
    assert sum_even_squares(10) == 220, "练习 4 未通过"
    assert badge("admin") == "管理员", "练习 5 未通过"
    assert badge("user") == "普通用户", "练习 5 未通过"
    assert badge("guest") == "访客", "练习 5 未通过（bug 还没修好）"
    print("✅ 上午练习全部通过！")
