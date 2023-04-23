# 栈结构的基本操作

# 数组实现、链表实现

# 栈结构，先进后出
# 数组表示的栈，需要个top指针表示栈顶位置
# 链栈，进栈，相当于，链表尾部，新增了一个结点。


class Node:
    def __init__(self, ele, next=None):
        self.ele = ele
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def initStack(self, data):
        """
        初始化栈
        :param data:
        :return:
        """
        # self.head = Node(data[0]) # 没有直接插入到链表的头节点，是头节点的下一个节点(元首节点)。
        self.head = Node(None)

        for i in data:
            node = Node(i)
            # 栈顶插入，链表头部插入
            node.next = self.head.next
            # 改变栈顶指针（链表头指针）指向新节点
            self.head.next = node

    def display(self):
        p = self.head

        while p:
            print(p.ele)
            p = p.next

    def push(self, ele):
        """
        入栈，链表头部插入，头插法
        :param ele:
        :return:
        """
        # 1.将新节点的指针指向头节点原先指向的节点
        # 2.改变头指针的指向，指向为新的节点。（将新节点变为头节点）

        node = Node(ele)  # 根据插入的元素，构建新节点

        node.next = self.head.next

        self.head.next = node

    def pop(self):
        """
        # 头部删除
        :return:
        """
        # 1.先判断，链表是否为空
        # 2.删除且返回链表头节点

        if self.head.next is None:
            print('栈已空')
            return

        # 链表删除节点（三个位置。需要知道被删除节点的前一个节点。）
        p = self.head

        print('pop:', p.next.ele)  # 要删除的是p.next,因为p指向的节点是(self.head=Node(None))(根据initStack方法判断)

        p.next = p.next.next  # 删除了原先p.next节点。


if __name__ == "__main__":
    stack = Stack()
    data = [6, 7, 8, 9]
    stack.initStack(data)
    stack.display()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    # stack.pop()
    # stack.pop()
    stack.display()
