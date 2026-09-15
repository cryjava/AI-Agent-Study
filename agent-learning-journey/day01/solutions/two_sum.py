"""参考答案 · LeetCode 1 两数之和"""


def two_sum(nums, target):
    # 第一版（暴力，O(n^2)）：
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    # 第二版（字典一次遍历，O(n)）：用空间换时间，思路和 Java HashMap 完全一致
    seen = {}                       # 值 -> 下标
    for i, x in enumerate(nums):    # enumerate：同时拿下标和值（明天细讲）
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("✅ LeetCode 1 · 两数之和 通过！")
