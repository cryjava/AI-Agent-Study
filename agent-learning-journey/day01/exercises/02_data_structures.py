"""
Day 1 · 下午练习（上）：四大内置结构 + 切片
====================================================================
Java 对照速记：
    list  ≈ ArrayList []      有序、可变、允许重复
    dict  ≈ LinkedHashMap {}    键值对（Python 3.7+ 保持插入顺序）
    tuple ≈ List.of(...)    不可变，因此可以当 dict 的键
    set   ≈ HashSet {}        自动去重，支持交 & 并 | 差 - 运算
运行：uv run exercises/02_data_structures.py
"""

# ============ list 与切片 ============
# 切片语法 lst[start:stop:step]，含头不含尾；start/stop 可省略；负数从末尾往前数

#1
def swap_head_tail(lst):
    """把第一个元素挪到最后，返回新列表（不修改原列表）。
    要求：一行，用两个切片拼接。例：[1,2,3,4] -> [2,3,4,1]"""
    return lst[1:] + lst[0:1] # 从索引 1 开始到末尾，加上从索引 0 到 1 结束的元素

#2
def middle(lst):
    """返回去掉首尾各一个元素的中间段，一行切片。例：[1,2,3,4,5] -> [2,3,4]"""
    return lst[1:-1] # 从索引 1 开始到倒数第二个元素

#3
def last_three_reversed(lst):
    """返回最后三个元素的倒序，一行切片。例：[1,2,3,4,5,6] -> [6,5,4]"""
    return lst[-3:][::-1]  # 先取最后三个，再倒序

# ============ dict ============
#4
def word_count(words):
    """统计每个单词出现的次数，返回 dict。例：["a","b","a"] -> {"a": 2, "b": 1}
    提示：d[w] = d.get(w, 0) + 1（get 的第二参数对应 Java 的 getOrDefault）"""
    d = {}
    for w in words:
        d[w] = d.get(w, 0) + 1
    return d

#5？
def get_nested(config, default="未知"):
    """安全读取嵌套配置：config 形如 {"db": {"host": "localhost"}}，
    返回 config["db"]["host"]；任何一层不存在就返回 default，不抛异常。
    提示：dict.get(key, fallback)，不许用 try/except（那是明天的内容）。"""
    return config.get("db", {}).get("host", default)

# ============ tuple 与 set ============
#6
def min_max_avg(nums):
    """返回 (最小值, 最大值, 平均值) 组成的 tuple。
    感受一下：Java 里想一次返回三个值得先定义一个类或 record，Python 直接还。
    自检：min_max_avg([3, 1, 4, 1, 5]) == (1, 5, 2.8)"""
    return min(nums), max(nums), sum(nums) / len(nums)

#7？
def common_tags(a, b):
    """两个标签列表共同出现的标签，去重后按字母排序返回。
    例：["ai","java","agent"] 与 ["agent","python","ai"] -> ["agent","ai"]
    提示：set(a) & set(b)，然后 sorted(...)"""
    return sorted(set(a) & set(b))

# ===============================================================
# 自测（不要改这里）
# ===============================================================
if __name__ == "__main__":
    assert swap_head_tail([1, 2, 3, 4]) == [2, 3, 4, 1], "练习 1 未通过"
    assert swap_head_tail([9]) == [9], "练习 1 未通过"
    assert middle([1, 2, 3, 4, 5]) == [2, 3, 4], "练习 2 未通过"
    assert middle([1, 2]) == [], "练习 2 未通过"
    assert last_three_reversed([1, 2, 3, 4, 5, 6]) == [6, 5, 4], "练习 3 未通过"
    assert word_count(["a", "b", "a"]) == {"a": 2, "b": 1}, "练习 4 未通过"
    assert get_nested({"db": {"host": "localhost"}}) == "localhost", "练习 5 未通过"
    assert get_nested({}) == "未知", "练习 5 未通过"
    assert min_max_avg([3, 1, 4, 1, 5]) == (1, 5, 2.8), "练习 6 未通过"
    assert common_tags(["ai", "java", "agent"], ["agent", "python", "ai"]) == ["agent", "ai"], "练习 7 未通过"
    print("✅ 四大结构练习全部通过！")
