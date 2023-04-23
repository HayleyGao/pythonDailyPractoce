# 二叉树的实现

# 堆排序的实现
# 1.使用无序序列构建堆
# 2.筛选/调整:a.将堆顶节点的值与当前树的最后一个节点值进行交换，b.然后重新调整堆。

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def add(self, ele):
        """
        使用层次遍历的方式添加二叉树
        :param ele:
        :return:
        """
        node = Node(ele)

        if self.root is None:  # 树的根节点的初始化
            self.root = node
            return

        queue = [self.root]  # 队列,初始化队列；队列的特性是，先进先出

        while len(queue) != 0:
            cur_node = queue.pop(0)  # python pop()方法默认是弹出列表最后一个元素，pop(0)是符合"队列的'先进先出'的特性的"。

            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)

            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def breadth_travel(self):
        """
        广度遍历树
        :return:
        """
        if self.root is None:
            print("tree is None.")
            return self.root

        # 广度遍历需要使用队列结构
        queue = [self.root]

        while len(queue) != 0:
            cur_node = queue.pop(0)
            print(cur_node.value)

            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)


def initHeap():
    """
    1.为确保整棵树的堆结构正确，调整顺序，所有的根节点，从下到上，从右到左。
    2.每棵子树/每个根节点，根据最大堆、最小堆的定义进行堆调整。
    :return:
    """
    pass


def adjustHeap(arr, start, end):
    """
    调整树
    :param arr:待排序的序列
    :param start:调整的第s个节点
    :param end:待调整的节点
    :return:
    """
    s = start

    j = 2 * s + 1  # 左孩子的索引

    while j <= end:
        if j + 1 <= end and arr[j] < arr[j + 1]:  # 若是右边界没有溢出（也是一个有无右孩子的判断），且左节点值小于右节点值
            j = j + 1  # 若是满足比较条件，则j为右节点的索引值，否则j为左孩子的索引。
        if arr[s] < arr[j]:  # 若当前节点值比最大孩子值更大，则无需继续比较的作用，直接跳出循环
            # 若当前节点值比最大孩子值小，交换值
            arr[s], arr[j] = arr[j], arr[s]  # 交换值

            s = j  # --->s为指针，指向其孩子节点，继续进行筛选（s为指向需要调整的节点的指针）
            j = s * 2 + 1  # 更新j的值，进行下一轮循环

        else:
            break


def heapSort(arr):
    length = len(arr)
    i = (length // 2)-1  # python中的整除//
    for s in range(i, -1, -1):  # 从下到上，从右到左，对于每个非叶子节点的根节点进行调整，构建成为最大堆。
        adjustHeap(arr, s, length - 1)

    for end in range(length - 1, 0, -1):  # 有多少个节点，可能需要交换多少次，被交换的end=end-1是因为数组最后一部分是已有序的。
        # 交换最大堆的堆顶元素和堆尾元素，然后重新调整堆
        arr[0], arr[length - 1] = arr[length - 1], arr[0]
        adjustHeap(arr, 0, end - 1)  # 每一次交换堆顶与堆尾元素之后，将剩余序列（end=end-1）重新调整二叉树为最大堆。

    return arr


if __name__ == "__main__":
    arr = [49, 38, 65, 97, 76, 13, 27, 49]
    # arr=[]
    print("排序前：", arr)

    # # 构建树
    # tree = Tree()
    # for i in arr:
    #     tree.add(i)
    # # 层次遍历树
    # tree.breadth_travel()

    print("排序后：", heapSort(arr))
