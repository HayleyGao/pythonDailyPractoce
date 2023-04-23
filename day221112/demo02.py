# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode):
    # 指向同一个节点，指针指向的节点相同（存储地址相同）
    # 方法一：分别遍历两个链表，若指针的地址相同，则表示指向了同一个节点
    # 方法二：消除链表长度差

    sett = set()
    p1 = headA
    p2 = headB

    while p1:
        sett.add(p1.val)
        p1 = p1.next

    while p2:
        if p2.val in sett:
            return p2
        else:
            p2 = p2.next

    return None


