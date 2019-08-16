# V0

# V1 
# http://bookshadow.com/weblog/2015/01/29/leetcode-reverse-linked-list-ii/
# IDEA : dummyNode
# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None
class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        dummyNode = ListNode(0)
        p = dummyNode
        q = head

        for x in range(m - 1):
            p.next = q
            q = q.next
            p = p.next

        start = None
        end = q
        next = None
        for x in range(m, n + 1):
            next = q.next
            q.next = start
            start = q
            q = next

        p.next = start
        end.next = next
        return dummyNode.next

# V2 
# Time:  O(n)
# Space: O(1)
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.__next__))
class Solution(object):
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        diff, dummy, cur = n - m + 1, ListNode(-1), head
        dummy.next = head

        last_unswapped = dummy
        while cur and m > 1:
            cur, last_unswapped, m = cur.__next__, cur, m - 1

        prev, first_swapped = last_unswapped,  cur
        while cur and diff > 0:
            cur.next, prev, cur, diff = prev, cur, cur.next, diff - 1

        last_unswapped.next, first_swapped.next = prev, cur

        return dummy.__next__