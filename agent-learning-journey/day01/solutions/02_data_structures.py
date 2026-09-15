"""参考答案 · 02 四大结构 + 切片（卡住 15 分钟以上再看）"""


def swap_head_tail(lst):
    return lst[1:] + lst[:1]


def middle(lst):
    return lst[1:-1]


def last_three_reversed(lst):
    return lst[:-4:-1]        # 或写全 lst[-1:-4:-1]：起点 -1，终点 -4（不含），步长 -1


def word_count(words):
    d = {}
    for w in words:
        d[w] = d.get(w, 0) + 1
    return d


def get_nested(config, default="未知"):
    # 每层都给 fallback，缺哪层都不会抛 KeyError
    return config.get("db", {}).get("host", default)


def min_max_avg(nums):
    return (min(nums), max(nums), sum(nums) / len(nums))


def common_tags(a, b):
    return sorted(set(a) & set(b))    # & 交集 | 并集 - 差集


if __name__ == "__main__":
    assert swap_head_tail([1, 2, 3, 4]) == [2, 3, 4, 1]
    assert swap_head_tail([9]) == [9]
    assert middle([1, 2, 3, 4, 5]) == [2, 3, 4]
    assert middle([1, 2]) == []
    assert last_three_reversed([1, 2, 3, 4, 5, 6]) == [6, 5, 4]
    assert word_count(["a", "b", "a"]) == {"a": 2, "b": 1}
    assert get_nested({"db": {"host": "localhost"}}) == "localhost"
    assert get_nested({}) == "未知"
    assert min_max_avg([3, 1, 4, 1, 5]) == (1, 5, 2.8)
    assert common_tags(["ai", "java", "agent"], ["agent", "python", "ai"]) == ["agent", "ai"]
    print("✅ 四大结构练习全部通过！")
