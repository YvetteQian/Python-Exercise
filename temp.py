# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        p = head
        stack = []
        b = None
        while p:
            b = p.prev
            if p.child is not None:
                stack.append(p.next)
                p.next = p.child
                p.child = None
                p.next.prev = p
            p = p.next
        for s in stack[::-1]:
            b.next = s
            s.prev = b
            while b.next:
                b = b.next
        return head
