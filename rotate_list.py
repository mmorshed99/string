# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        if B == 0:
            return A
        if A == None:
            return A
        if A.next == None:
            return A
        curr = A
        tot = 0
        last = None
        while(curr != None):
            tot += 1
            last = curr
            curr = curr.next
        if B >= tot:
            B = B % tot
            if B == 0:
                return A
        goal = tot - B + 1
        curr = A
        count = 1
        prev = None
        while(count != goal):
            count += 1
            prev = curr
            curr = curr.next
        prev.next = None
        last.next = A
        return curr
