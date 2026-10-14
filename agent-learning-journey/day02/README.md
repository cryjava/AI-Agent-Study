# Day 2 · Python 语法速成（下）与工程习惯

对应总计划 Day 2。今天把 Day 1 的 list / dict 变成可维护的小工具。
以下命令均在 `day02/` 目录执行；也可把 `uv run` 换成 `python3`。
练习中保留了 TODO，初次运行报 `NotImplementedError` 是正常的，不代表环境坏了。

## 上午：先从函数开始

- [ ] 阅读 `notes/python_engineering.md` 的函数部分。
- [ ] 补全 `exercises/01_functions.py`，运行 `uv run exercises/01_functions.py`。
- [ ] 阅读类、鸭子类型和模块部分。
- [ ] 补全 `exercises/02_classes.py`，运行 `uv run exercises/02_classes.py`。

第一轮只做函数练习的第 1、2 题（约 20 分钟），不要一次追完所有知识点。
自测通过后，解释：为什么默认参数不应该写成 `items=[]`？

## 下午：Todo CLI

- [ ] 阅读异常、文件和路径部分。
- [ ] 按顺序补全 `todo.py` 中的 `load_tasks`、`save_tasks`、`add_task`、`delete_task`。
- [ ] 用下列命令验收增删查与持久化。

```bash
uv run todo.py --help
uv run todo.py add "学习默认参数"
uv run todo.py add "完成 Todo CLI"
uv run todo.py list
uv run todo.py delete 1
uv run todo.py list
```

验收标准：

- 首次没有文件时，`list` 输出 `No tasks.`。
- 退出再运行仍能读到任务，JSON 使用 UTF-8，中文可读。
- 删除后新增任务不能与剩余任务 ID 冲突。
- 空白标题和不存在的 ID 给出友好错误，退出码为 1。
- 损坏的 JSON 报错，不当作空列表覆盖原数据。
- 用 `--file /tmp/day02-todos.json` 指定测试文件，不污染正式数据。

这是单进程学习工具；并发写入、数据库和 Web API 留到后续课程。
`argparse` 入口已经写好，重点是业务函数和文件操作。
若要练习包组织，可在跑通后把存储函数移到 `todo_store.py`，
再使用 `from todo_store import load_tasks, save_tasks`；导入不应触发 CLI。

## 晚上：装饰器与生成器

- [ ] 补全 `exercises/03_decorators_generators.py` 的两个装饰器、两个生成器。
- [ ] 运行 `uv run exercises/03_decorators_generators.py`。
- [ ] 在 `../day01/notes/java_vs_python.md` 追加函数、类、异常、with、yield 的对照笔记。
- [ ] 写下一个今天遇到的错误，以及你如何定位它。

不要让 AI 直接填完全部答案。每题先试 15 分钟，卡住时提供代码、报错和你的推测。

## 合上电脑前的自测

1. `*args` 与 `**kwargs` 分别收集成什么类型？
2. 类型提示会自动拒绝错误类型的实参吗？
3. 为什么 `self` 类似 Java 的 `this`，但要显式写出来？
4. `with` 和 `finally` 各负责什么？
5. `return` 与 `yield` 如何影响下一次调用或迭代？
6. 为什么包装函数要用 `functools.wraps`？

完成验收后再手动勾选总计划，并提交本日代码；不自动宣告 Day 1 或 Day 2 已完成。
