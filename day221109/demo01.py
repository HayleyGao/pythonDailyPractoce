def lengthOfLongestSubstring(s: str) -> int:
    length = len(s)
    # 滑动窗口解法

    # left,right,set

    sett = set()
    left = 0
    right = length
    max_ = 0

    for i in range(right):
        while s[i] in sett:
            sett.remove(s[left])  # 移除集合中该位置前的元素,直到当前集合为空
            left = left + 1  # 挪动左指针，直到该位置的的前一个位置，直到再没有与当前元素相同的元素

        # print(sett)
        sett.add(s[i])  # right,右指针一直继续向右
        print(sett)

        max_ = max(max_, len(sett))

    return max_


if __name__ == "__main__":
    s = "abcabcbb"
    result = lengthOfLongestSubstring(s)
    print(result)
