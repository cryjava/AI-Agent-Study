"""Day 2: 补全 TODO，运行 uv run exercises/01_functions.py。"""


def greet(name: str, prefix: str = "Hello") -> str:
    """题 1：返回 'Hello, Ada'；允许调用者覆盖 prefix。"""
    raise NotImplementedError("TODO 1: 默认参数与 f-string")


def append_item(item: str, items: list[str] | None = None) -> list[str]:
    """题 2：追加 item 并返回列表。

    省略 items 时每次创建新列表；传入列表时修改并返回原对象。
    注意：空列表也属于调用者传入的有效对象。
    """
    raise NotImplementedError("TODO 2: 用 is None 判断")


def total(*values: int, initial: int = 0) -> int:
    """题 3：返回 initial + 所有 values 的和。"""
    raise NotImplementedError("TODO 3: *args")


def make_profile(name: str, **extras: str) -> dict[str, str]:
    """题 4：返回含 name 及全部 extras 的字典。"""
    raise NotImplementedError("TODO 4: **kwargs")


def sort_tasks(tasks: list[dict]) -> list[dict]:
    """题 5：用 sorted + lambda 按 priority 升序，不能修改原列表。"""
    raise NotImplementedError("TODO 5: lambda")


if __name__ == "__main__":
    assert greet("Ada") == "Hello, Ada", "题 1"
    assert greet("Ada", prefix="Hi") == "Hi, Ada", "题 1：关键字参数"
    assert append_item("a") == ["a"], "题 2"
    assert append_item("b") == ["b"], "题 2：不能共享默认列表"
    original = []
    assert append_item("c", original) is original, "题 2：保留原对象"
    assert original == ["c"], "题 2：修改传入的空列表"
    assert total() == 0, "题 3：无实参"
    assert total(1, 2, 3, initial=10) == 16, "题 3"
    assert make_profile("Ada", role="engineer") == {
        "name": "Ada", "role": "engineer",
    }, "题 4"
    tasks = [{"id": 1, "priority": 2}, {"id": 2, "priority": 1}]
    assert sort_tasks(tasks) == [tasks[1], tasks[0]], "题 5"
    assert tasks[0]["id"] == 1, "题 5：不改变原列表"
    print("函数练习全部通过。请解释默认列表为什么会共享。")
