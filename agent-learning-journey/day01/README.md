# Day 1 · Python 环境与语法速成（上）

> 第一周 Day 1 · 标签：基础
> 节奏：上午理论 → 下午实践 → 晚上输出。所有文件在 `day01/` 目录下用 `uv run` 直接跑。

## 上午（理论 + 基础语法）
- [ ] 快读理论：廖雪峰 Python 教程「Python 基础」到「函数」之前，或官方 Tutorial 第 3–4 章（视频 1.5 倍速，别恋战）
- [ ] 跑通 `uv run hello.py`
- [ ] 完成 `exercises/01_syntax_basics.py`（5 题，含 1 个修 bug 题）

## 下午（数据结构 + 推导式）
- [ ] 完成 `exercises/02_data_structures.py`（list / dict / tuple / set + 切片，7 题）
- [ ] 完成 `exercises/03_comprehensions.py`（5 个 Java 循环改写成推导式）

## 晚上（LeetCode + 输出）
- [ ] `leetcode/two_sum.py`（先暴力再字典）
- [ ] `leetcode/reverse_linked_list.py`（顺便学 Python 的类）
- [ ] `leetcode/valid_parentheses.py`（dict + list 实战）
- [ ] 填写 `notes/java_vs_python.md`（先凭记忆填，再查证）
- [ ] Git 首次提交：
  ```bash
  git add -A
  git commit -m "Day 1: Python 语法速成 —— 从 Java 出发的第一天"
  ```

## 合上电脑前的自测（答不上就翻回练习）
1. `elif` / `and` / `or` / `not` 分别对应 Java 的什么？
2. `lst[1:-1]` 返回什么？`lst[:-4:-1]` 呢？
3. `d.get(k, 0)` 对应 Java 的哪个方法？
4. `if level == "admin" or "root"` 这个 bug 的原理是什么？
5. 为什么说「类型在对象上，不在变量上」？

## 卡住了？
每题先试 15 分钟。超时再看 `solutions/` 对应文件 —— 看完合上，自己再写一遍才算学会。
