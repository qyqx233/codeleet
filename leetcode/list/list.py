class ListNode:
    def __init__(self, x):
        self.val = x+
        
        self.next = None

    @staticmethod
    def gen(*vals):
        ll = ListNode(vals[0])
        head = ll
        for i in range(1, len(vals)):
            ll.next = ListNode(vals[i])
            ll = ll.next
        return head

    def travel(self):
        vals = []
        ll = self
        while ll:
            vals.append(ll.val)
            ll = ll.next
        return vals


class Solution:
    @staticmethod
    def swapPairs(head: ListNode) -> ListNode:
        ''' 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
            你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
        '''
        # p: ListNode = head
        pass

    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        a, b, c = l1, l2, ListNode(0)
        p = c
        while a is not None or b is not None:
            if a is None:
                m = b.val
                b = b.next
            elif b is None:
                m = a.val
                a = a.next
            else:
                m, _ = (b.val, b) if a.val >= b.val else (a.val, a)
                # print(tmp)
                if _ is a:
                    a = a.next
                else:
                    b = b.next
            p.next = ListNode(m)
            p = p.next
        return c.next


def test_Solution():
    l1 = ListNode.gen(1, 3, 10)
    l2 = ListNode.gen(0, 4, 8)
    print(Solution.mergeTwoLists(l1, l2).travel())


test_Solution()
