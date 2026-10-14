"""Day 2: 两个装饰器 + 两个生成器，补全后直接运行。

提示：装饰器用 functools.wraps；生成器用 yield，不要返回完整列表。
"""

from collections.abc import Callable, Iterator
from functools import wraps
from typing import ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def logged(function: Callable[P, R]) -> Callable[P, R]:
    """题 1：包装后每次调用先打印 'Calling <函数名>'，再返回原函数结果。

    保留函数名称、文档和位置/关键字参数。P、R 是类型描述，不影响运行。
    """
    raise NotImplementedError("TODO 1: @wraps + wrapper")


def require_nonempty(function: Callable[[str], str]) -> Callable[[str], str]:
    """题 2：若 text.strip() 为空抛 ValueError，否则传原始 text 给原函数。

    同样保留函数元数据。
    """
    raise NotImplementedError("TODO 2: 校验装饰器")


def countdown(start: int) -> Iterator[int]:
    """题 3：依次 yield start 到 1；start <= 0 时不产生值。"""
    raise NotImplementedError("TODO 3: 惰性倒计时")


def nonempty_lines(lines: list[str]) -> Iterator[str]:
    """题 4：逐行 strip，只 yield 非空内容。"""
    raise NotImplementedError("TODO 4: 过滤生成器")


if __name__ == "__main__":
    def add(a: int, b: int = 1) -> int:
        """Add two integers."""
        return a + b

    decorated = logged(add)
    assert decorated(2, b=3) == 5, "题 1：参数与返回值"
    assert decorated.__name__ == "add", "题 1：wraps"
    assert decorated.__doc__ == add.__doc__, "题 1：文档"
    guarded = require_nonempty(lambda text: text.upper())
    assert guarded(" hi ") == " HI ", "题 2：保留原输入"
    try:
        guarded(" \t ")
    except ValueError:
        pass
    else:
        raise AssertionError("题 2：空白应抛 ValueError")
    numbers = countdown(3)
    assert iter(numbers) is numbers, "题 3：应返回迭代器"
    assert next(numbers) == 3, "题 3：第一步"
    assert list(numbers) == [2, 1], "题 3：接着执行"
    assert list(numbers) == [], "题 3：已耗尽"
    assert list(countdown(0)) == [], "题 3：边界"
    lines = nonempty_lines([" a \n", "", " \t", "b"])
    assert iter(lines) is lines, "题 4：应返回迭代器"
    assert list(lines) == ["a", "b"], "题 4"
    print("晚上练习全部通过。请解释 yield 的暂停位置。")
