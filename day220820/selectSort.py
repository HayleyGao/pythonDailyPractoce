# http://c.biancheng.net/view/3446.html
# 1、外循环控制总的遍历轮数
# 2、每轮，选出最小值，即，从当前结点（默认哨兵值）向后选出最小的值，返回其下标/指针，与当前默认哨兵值进行交换。
# 2.1 selectMin，总共需要2个指针，min指针，向后遍历的i指针；
#


def selectMin(arr, i, len):
    # 从列表i的位置，到列表右侧结束，选出一个最小的。返回其下标/指针。
    min = i  # 给定默认最小值，从列表的首个元素开始。

    while i < len:
        if arr[min] > arr[i]:
            min = i
        i = i + 1
    return min


# def swap(arr, a, b):
#     pass

def selectSort(arr):
    length = len(arr)
    for i in range(length):  # 左闭右开
        min = selectMin(arr, i, length)
        if i != min:  # 只是为了说明当前结点不是最小结点
            arr[i], arr[min] = arr[min], arr[i]  # python 特有的swap方式，也可以通过增加临时变量进行交换值。


if __name__ == "__main__":
    list_ = [56, 12, 80, 91, 20]
    print("排序前：\n", list_)
    selectSort(list_)
    print("排序后：\n", list_)
