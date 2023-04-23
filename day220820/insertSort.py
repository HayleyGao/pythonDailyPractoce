def insertSort(arr):
    length = len(arr)
    for i in range(1, length):  # 外循环指针i
        x = arr[i]  # 哨兵，后边挪位置的时候，a[j+1]也就是a[i]的值会被覆盖掉，所以这里需要个哨兵来临时存放待插入的值。
        j = i - 1  # 内循环指针j
        while j > -1 and x < arr[j]:  # 这里，a[i]/哨兵/岗哨与有序序列的比较，需要从有序序列的最后一个位置开始比较
            # 先挪个位置,向后一个位置拷贝/复制值
            arr[j + 1] = arr[j]
            j = j - 1

        # 找到合适的位置之后，进行插入
        arr[j + 1] = x  # j指针是与待插入值进行比较的位置，由于是从后往前比较，当待插入值(a[i])满足a[i]>arr[j]，插入到a[j]后面，即被挪出来的a[j+1]的位置。


if __name__ == "__main__":
    list_ = [3, 1, 7, 5, 2, 4, 9, 6]
    print("排序前：\n", list_)
    insertSort(list_)
    print("排序后：\n", list_)
