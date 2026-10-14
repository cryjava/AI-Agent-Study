"""Day 2: 类、继承、魔术方法与鸭子类型。补全后直接运行。"""


class Task:
    def __init__(self, title: str):
        """题 1：保存 title，并把 done 初始化为 False。"""
        raise NotImplementedError("TODO 1: self.title / self.done")

    def complete(self) -> None:
        """题 2：将 done 改为 True。"""
        raise NotImplementedError("TODO 2: 修改实例状态")

    def __str__(self) -> str:
        """题 3：未完成返回 '[ ] read'，完成返回 '[x] read'。"""
        raise NotImplementedError("TODO 3: __str__")


class PriorityTask(Task):
    def __init__(self, title: str, priority: int):
        """题 4：通过 super() 初始化父类，再保存 priority。"""
        raise NotImplementedError("TODO 4: 继承")


class ConsoleSender:
    def send(self, message: str) -> str:
        return f"console: {message}"


class EmailSender:
    def send(self, message: str) -> str:
        return f"email: {message}"


def notify(sender, task: Task) -> str:
    """题 5：调用 sender.send(str(task))，返回结果。

    两种 Sender 没有共同的自定义父类；不要用 isinstance 分支判断它们。
    """
    raise NotImplementedError("TODO 5: 鸭子类型")


if __name__ == "__main__":
    task = Task("read")
    assert task.title == "read" and task.done is False, "题 1"
    assert str(task) == "[ ] read", "题 3：未完成"
    assert task.complete() is None, "题 2：无需返回值"
    assert str(task) == "[x] read", "题 2、3"
    assert Task("another").done is False, "状态应属于实例"
    urgent = PriorityTask("ship", 1)
    assert urgent.title == "ship" and urgent.priority == 1, "题 4"
    assert urgent.done is False and isinstance(urgent, Task), "题 4：父类初始化"
    assert notify(ConsoleSender(), task) == "console: [x] read", "题 5"
    assert notify(EmailSender(), task) == "email: [x] read", "题 5"
    print("类练习全部通过。请解释这里为何不需要 Java 风格的接口继承。")
