
# 二叉树的实现


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


if __name__ == "__main__":
    arr = [49, 38, 65, 97, 76, 13, 27, 49]
    # arr=[]

    # 构建树
    tree = Tree()
    for i in arr:
        tree.add(i)

    # 层次遍历树
    tree.breadth_travel()
