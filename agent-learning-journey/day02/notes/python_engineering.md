# Day 2 · 从 Java 过渡到 Python 工程代码

## 1. 函数：先读懂参数

```python
def greet(name: str, prefix: str = "Hello") -> str:
    return f"{prefix}, {name}"

print(greet("Ada"))
print(greet("Ada", prefix="Hi"))
```

`def` 定义函数；默认参数让调用者可以省略 `prefix`。
`name: str` 和 `-> str` 是类型提示，便于 IDE 和静态检查工具理解代码，
但 Python 运行时不会自动强制检查它们，不等同于 Java 的编译期约束。

```python
def describe(*args: str, **kwargs: str) -> None:
    print(args)    # tuple，例如 ("read", "write")
    print(kwargs)  # dict，例如 {"owner": "Ada"}

describe("read", "write", owner="Ada")
```

定义时 `*` / `**` 收集参数，调用时则可以展开 tuple / dict。
Java 可变参数 `String... args` 接近 `*args`，没有直接等价的 `**kwargs`。
`lambda task: task["id"]` 是只有一个表达式的匿名函数，可用作排序的 `key`。

### 重要坑：默认值只在定义函数时求值一次

```python
def broken_add(item, items=[]):
    items.append(item)
    return items
```

多次调用省略 `items` 时，共用同一个列表，而不是每次创建新列表。
安全模式是默认 `None`，在函数内部用 `if items is None` 创建新列表。
不要写成 `items = items or []`：调用者传入空列表时会被错误地换成新对象。

## 2. 类与鸭子类型

```python
class Console:
    def __init__(self, prefix: str):
        self.prefix = prefix

    def send(self, text: str) -> str:
        return f"{self.prefix}: {text}"

    def __str__(self) -> str:
        return f"Console({self.prefix})"
```

`self` 类似 `this`，但方法定义中必须显式写。
`__init__` 初始化实例；`str(obj)` 或 `print(obj)` 会使用 `__str__`。
继承写作 `class Child(Parent)`，父类初始化可用 `super().__init__(...)`。

鸭子类型：只要对象有调用代码所需要的方法，就能使用它，不要求继承共同的接口。
它不是“任何类型都能随便传”；缺少方法会在运行时失败。
后续可用 `typing.Protocol` 描述这种结构，交给静态工具检查。

## 3. 异常、with、pathlib

```python
import json
from pathlib import Path

path = Path("/tmp/day02-example.json")
try:
    with path.open("r", encoding="utf-8") as stream:
        data = json.load(stream)
except FileNotFoundError:
    data = []
except json.JSONDecodeError as exc:
    raise ValueError(f"损坏的 JSON: {path}") from exc
```

`with` 类似 try-with-resources，离开代码块时关闭文件，异常路径也会关闭。
`finally` 用于无论是否异常都要执行的清理，不应该吞掉异常或随意返回。
Python 不要求声明 Java 的 checked exceptions，也没有相同的编译期强制处理机制。
只捕获能处理的特定异常，不要用 `except: pass` 隐藏错误。

`Path(__file__).resolve().parent` 是脚本所在目录，不是命令执行时的工作目录。
`path.parent.mkdir(parents=True, exist_ok=True)` 可以准备父目录。
`json.dump(..., ensure_ascii=False, indent=2)` 用于易读的中文 JSON。
读取失败不等于没有数据，尤其不能将损坏文件静默重置为 `[]`。

## 4. 模块与包

一个 `.py` 文件是模块；带 `__init__.py` 的目录是常规包。
Python 也支持不带该文件的命名空间包，今天先掌握常规包。
同目录导入示例：`from todo_store import load_tasks`。

```python
if __name__ == "__main__":
    main()
```

这段保护让文件可以既作为脚本执行，也被其他模块导入，而不在导入时启动 CLI。
拆分时先分清“数据存储”与“参数解析”，不必照搬 Java 的大量分层。

## 5. 装饰器与生成器

`@decorate` 等价于定义函数后执行 `function = decorate(function)`。
包装函数通常接收 `*args, **kwargs`，保留返回值，使用 `functools.wraps` 保留名称和文档等元数据。
普通 Python 装饰器是函数转换，不完全等同于 Java 注解；后续 `@tool` 会用它注册工具。

含 `yield` 的函数调用时返回生成器；到 `next()` 或循环时才执行函数体。
`yield` 暂停并保存执行位置，下一次迭代接着执行；遍历结束后不会自动重置。
它能避免一次构造全部结果，但不代表所有操作都不占内存，也不等同于异步。

## 6. 今天的复盘（自己填写）

- 默认参数共享对象的问题：
- 类型提示与运行时校验的区别：
- JSON 读取失败时如何保护数据：
- 装饰器和生成器各一个使用场景：
