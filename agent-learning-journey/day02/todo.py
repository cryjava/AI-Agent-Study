"""Day 2 Todo CLI 骨架：参数解析已提供，四个业务函数由你完成。

运行 uv run todo.py --help；数据默认保存在脚本同目录的 todos.json。
JSON 格式：[{"id": 1, "title": "read"}]
"""

import argparse
import json
import sys
from pathlib import Path
from typing import TypedDict


class TaskRecord(TypedDict):
    id: int
    title: str


def load_tasks(path: Path) -> list[TaskRecord]:
    """TODO 1：with + json.load 读取 UTF-8 JSON；文件不存在时返回 []。

    损坏 JSON 或结构不符时抛 ValueError，绝不能静默覆盖。
    结构要求：列表；每项为含正整数 id 和非空字符串 title 的字典；
    id 不重复（bool 虽是 int 的子类，但不能当 ID）。
    提示：只把 FileNotFoundError 视为“首次使用”。
    """
    raise NotImplementedError("TODO 1: load_tasks")


def save_tasks(path: Path, tasks: list[TaskRecord]) -> None:
    """TODO 2：创建父目录，用 with + json.dump 保存 UTF-8 JSON。

    使用 ensure_ascii=False, indent=2，保证中文可读。
    加练：先写同目录临时文件，再用 Path.replace 替换，降低中途失败风险。
    """
    raise NotImplementedError("TODO 2: save_tasks")


def add_task(tasks: list[TaskRecord], title: str) -> TaskRecord:
    """TODO 3：strip 标题；为空抛 ValueError；追加任务并返回该任务。

    新 ID = 当前最大 ID + 1，空列表从 1 开始。
    不能用 len(tasks) + 1，否则删除中间任务后可能发生 ID 冲突。
    """
    raise NotImplementedError("TODO 3: add_task")


def delete_task(tasks: list[TaskRecord], task_id: int) -> None:
    """TODO 4：按 ID 从原列表删除；不存在时抛 ValueError。"""
    raise NotImplementedError("TODO 4: delete_task")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Day 2 Todo CLI")
    parser.add_argument(
        "--file", type=Path,
        default=Path(__file__).resolve().with_name("todos.json"),
        help="JSON data file (put this option before the subcommand)",
    )
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="List tasks")
    add = commands.add_parser("add", help="Add a task")
    add.add_argument("title")
    delete = commands.add_parser("delete", help="Delete a task by ID")
    delete.add_argument("id", type=int)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        tasks = load_tasks(args.file)
        if args.command == "list":
            for task in tasks:
                print(f'{task["id"]}: {task["title"]}')
            if not tasks:
                print("No tasks.")
        elif args.command == "add":
            task = add_task(tasks, args.title)
            save_tasks(args.file, tasks)
            print(f'Added {task["id"]}: {task["title"]}')
        elif args.command == "delete":
            delete_task(tasks, args.id)
            save_tasks(args.file, tasks)
            print(f"Deleted {args.id}")
    except NotImplementedError as exc:
        print(f"练习尚未完成：{exc}", file=sys.stderr)
        return 1
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
