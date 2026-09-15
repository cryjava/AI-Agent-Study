"""参考答案 · 03 推导式（卡住 15 分钟以上再看）
对照 Java 版本感受一下：一行 vs 五行，这就是 Python 的表达力。"""

NUMS = [3, -1, 4, -1, 5, -9, 2, 6, -5, 3]
WORDS = ["agent", "java", "python", "ai", "llm", "rag"]


def positive_squares():
    return [x * x for x in NUMS if x > 0]


def long_words_upper():
    return [w.upper() for w in WORDS if len(w) >= 4]


def word_lengths():
    return {w: len(w) for w in WORDS}


def negative_abs_set():
    return {-x for x in NUMS if x < 0}


def sign_labels():
    return ["正" if x > 0 else "负" if x < 0 else "零" for x in NUMS]


if __name__ == "__main__":
    assert positive_squares() == [9, 16, 25, 4, 36, 9]
    assert long_words_upper() == ["AGENT", "JAVA", "PYTHON"]
    assert word_lengths() == {"agent": 5, "java": 4, "python": 6, "ai": 2, "llm": 3, "rag": 3}
    assert negative_abs_set() == {1, 9, 5}
    assert sign_labels() == ["正", "负", "正", "负", "正", "负", "正", "正", "负", "正"]
    print("✅ 推导式练习全部通过！")
