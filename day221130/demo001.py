# 1.先整体反转
# 2.再每个单词反转

def resverseSentence(s,begin,end):
    s = s[::-1]

    for i in range(end):
        if s[i]==" ":
            resverseSentence(s,begin,i-1)
            begin=i+1
        print(s)

    # print(s)


def reverse(s):
    length = len(s)
    resverseSentence(s,0,length)
    # print(s)



if __name__ == "__main__":
    s = "how are you?"
    reverse(s)
