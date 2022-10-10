# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createNode(list=[]):
    header = ListNode(numbers[0])
    temp = header
    for i in range(1,len(list)):
        value = list[i]
        nextP = ListNode(value)
        temp.next = nextP
        temp = nextP
    return header

def printListNode(node):
    p = node
    while p.next:
        print(p.val)
        p = p.next
    print(p.val)

numbers = [2,3,4,5,3,4]  
header = createNode(numbers)
printListNode(header)


# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: