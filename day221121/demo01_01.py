
# 链接：https://leetcode.cn/problems/count-and-say/solution/wai-guan-shu-lie-by-leetcode-solution-9rt8/
# 外观数列

def countAndSay(n: int) -> str:
        prev = "1"        # S1=1
        for i in range(n-1):
            curr = ""
            pos = 0
            start = 0

            while pos < len(prev):
                while pos < len(prev) and prev[pos] == prev[start]:  # prev,pos,start代表什么意思
                    pos += 1
                curr += str(pos - start) + prev[start] #
                start = pos   # 移动start的位置
            prev = curr    # curr,描述

        return prev


if __name__=="__main__":
    countAndSay(2)
