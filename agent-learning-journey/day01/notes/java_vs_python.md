# Java vs Python 语法对照表

> 用法：右边的格子先**凭记忆**填，再查资料验证。今天填已给主题的部分，Day 2 继续扩充（函数 / 类 / 异常）。
> 这张表是 Day 2、Day 3 的预习资料，也是你第一篇博客的核心素材。

## 一、变量与类型

| 场景 | Java | Python |
|------|------|--------|
| 声明整数 | `int age = 25;` | `age = 25` |
| 常量 | `final int MAX = 100;` | （自己填） |
| 查看类型 | `x.getClass().getSimpleName()` | （自己填） |
| 强制转换 | `(int) 3.9` | （自己填，提示：截断规则不同！） |

## 二、控制流

| 场景 | Java | Python |
|------|------|--------|
| 多分支 | `else if` | （自己填） |
| 逻辑与/或/非 | `&&` `\|\|` `!` | （自己填） |
| 三元表达式 | `cond ? a : b` | （自己填，注意条件的位置） |
| switch | `switch / case` | （Day 2 填：match-case） |

## 三、循环

| 场景 | Java | Python |
|------|------|--------|
| 计数循环 | `for (int i = 0; i < n; i++)` | （自己填） |
| 遍历集合 | `for (var x : list)` | （自己填） |
| 带下标遍历 | `for (int i = 0; i < list.size(); i++)` | （自己填，提示：enumerate） |
| 无限循环 | `while (true)` | （自己填） |

## 四、数据结构

| 场景 | Java | Python |
|------|------|--------|
| 动态数组 | `ArrayList<String>` | （自己填） |
| 哈希表 | `HashMap<K, V>` | （自己填） |
| 取值带默认 | `map.getOrDefault(k, d)` | （自己填） |
| 去重集合 | `HashSet<T>` | （自己填） |
| 交集 | `s1.retainAll(s2)` | （自己填，提示：一个运算符） |
| 不可变序列 | （Java 没有直接对应） | （自己填） |

## 五、字符串与输出

| 场景 | Java | Python |
|------|------|--------|
| 格式化 | `String.format("%s=%d", k, v)` | （自己填） |
| 打印 | `System.out.println(x)` | （自己填） |
| 大写转换 | `s.toUpperCase()` | （自己填） |
| 判空 | `s == null \|\| s.isEmpty()` | （自己填，提示：真值判断） |

## 六、今天踩的坑（自由记录）

-
-
