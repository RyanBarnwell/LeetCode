# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        newHead = ListNode(0)
        tail = newHead
        car = 0
        asum = 0
        
        while(l1 is not None or l2 is not None or car != 0):
            if(l1 is not None):
                d1 = l1.val
            else:
                d1 = 0
            if(l2 is not None):
                d2 = l2.val
            else:
                d2 = 0
            
            asum = d1+d2+car
            d = asum % 10
            car = asum // 10
            
            newNode = ListNode(d)
            tail.next = newNode
            tail = tail.next
            
            if(l1 is not None):
                l1 = l1.next
            else:
                l1 = None
            if(l2 is not None):
                l2 = l2.next
            else:
                l2 = None
                
        result = newHead.next
        newHead.next = None
        return result