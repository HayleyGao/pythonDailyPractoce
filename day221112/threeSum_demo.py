def threeSum(nums):
    n = len(nums)
    res = []
    if not nums or n < 3:
        return []

    nums.sort()  # 数组排序
    res = []
    for i in range(n):
        if nums[i] > 0:     # 数组为已排序好的结构，若nums[i]>0,则三个数之和无等于0的可能，直接返回。？ 这个是必然的吗？不一定吧。
            return res
        if i > 0 and nums[i] == nums[i - 1]:  # 和当前元素相等，则跳过，去除重复元素
            continue
        L = i + 1
        R = n - 1
        while L < R:
            if nums[i] + nums[L] + nums[R] == 0:
                res.append([nums[i], nums[L], nums[R]])
                while L < R and nums[L] == nums[L + 1]:   # 和当前元素相等，则跳过，去除重复元素
                    L = L + 1
                while L < R and nums[R] == nums[R - 1]:   # 和当前元素相等，则跳过，去除重复元素
                    R = R - 1
                L = L + 1
                R = R - 1
            elif nums[i] + nums[L] + nums[R] > 0:    # 三个元素之后大于0，则左侧元素左移
                R = R - 1
            else:
                L = L + 1      # 三个元素之后小于0，则右侧元素右移，使得sum==0靠近。
    return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    res = threeSum(nums)
    print(res)
