"""
Day 1 · 下午练习（下）：推导式 —— Python 的灵魂
====================================================================
每题给出「Java 风格伪码」，请用一行推导式重写。
推导式四种形态：
    [x * x for x in nums]              # 列表推导：map
    [x for x in nums if x > 0]         # 列表推导：map + filter
    {k: v for k, v in pairs}           # 字典推导
    {x % 3 for x in nums}              # 集合推导（自动去重）
运行：uv run exercises/03_comprehensions.py
"""

NUMS = [3, -1, 4, -1, 5, -9, 2, 6, -5, 3]
WORDS = ["agent", "java", "python", "ai", "llm", "rag"]

# 练习 1 · Java 风格：
#   List<Integer> out = new ArrayList<>();
#   for (Integer x : NUMS) { if (x > 0) out.add(x * x); }
def positive_squares():
    """返回 NUMS 中所有正数的平方，用列表推导式一行完成。"""
    ...

# 练习 2 · Java 风格：
#   List<String> out = new ArrayList<>();
#   for (String w : WORDS) { if (w.length() >= 4) out.add(w.toUpperCase()); }
def long_words_upper():
    """返回 WORDS 中长度 >= 4 的单词的大写形式。"""
    ...

# 练习 3 · Java 风格：
#   Map<String, Integer> out = new HashMap<>();
#   for (String w : WORDS) { out.put(w, w.length()); }
def word_lengths():
    """返回 {单词: 长度} 的字典，用字典推导式。"""
    ...

# 练习 4 · Java 风格：
#   Set<Integer> out = new HashSet<>();
#   for (Integer x : NUMS) { if (x < 0) out.add(-x); }
def negative_abs_set():
    """返回 NUMS 中所有负数的绝对值组成的 set（集合推导式，自动去重）。"""
    ...

# 练习 5 · Java 风格（嵌套三元）：
#   List<String> out = new ArrayList<>();
#   for (Integer x : NUMS) {
#       out.add(x > 0 ? "正" : (x < 0 ? "负" : "零"));
#   }
def sign_labels():
    """返回每个数的符号标签列表："正" / "负" / "零"，条件表达式写进推导式。"""
    ...

# ===============================================================
# 自测（不要改这里）
# ===============================================================
if __name__ == "__main__":
    assert positive_squares() == [9, 16, 25, 4, 36, 9], "练习 1 未通过"
    assert long_words_upper() == ["AGENT", "JAVA", "PYTHON"], "练习 2 未通过"
    assert word_lengths() == {"agent": 5, "java": 4, "python": 6, "ai": 2, "llm": 3, "rag": 3}, "练习 3 未通过"
    assert negative_abs_set() == {1, 9, 5}, "练习 4 未通过"
    assert sign_labels() == ["正", "负", "正", "负", "正", "负", "正", "正", "负", "正"], "练习 5 未通过"
    print("✅ 推导式练习全部通过！")
