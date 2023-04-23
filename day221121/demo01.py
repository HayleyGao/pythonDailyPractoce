
# 链接：https://leetcode.cn/problems/count-and-say/solution/wai-guan-shu-lie-by-leetcode-solution-9rt8/

def countAndSay(n: int) -> str:
        prev = "1"
        for i in range(n-1):
            curr = ""
            pos = 0
            start = 0

            while pos < len(prev):
                while pos < len(prev) and prev[pos] == prev[start]:
                    pos += 1
                curr += str(pos - start) + prev[start]
                start = pos
            prev = curr

        return prev


if __name__=="__main__":
    countAndSay(2)
