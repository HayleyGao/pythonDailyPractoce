# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # 创建一个最终返回的链表
        head = ListNode()
        tail = head

        # 初始值
        carry = 0

        while l1 or l2:
            sum = l1.val + l2.val + carry

            tmp = ListNode(sum % 10)
            tail.next = tmp

            tail = tail.next  # 移动指针，新sum节点，使用尾插法插入新链表中

            # 新的进位值
            carry = (l1.val + l2.val + carry) // 10  # 整除,python的整除//

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:  # 若最后进位值不为0，则生成新的节点加在链表最后。
            tail = ListNode(carry)
            tail = tail.next

        return head.next

