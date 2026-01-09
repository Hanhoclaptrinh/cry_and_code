class Solution:
    def reverseList(head):
        prev = None
        curr = head
        while curr:
            nextNode = curr.next # node tiep theo
            curr.next = prev # dao chieu mui ten
            prev = curr # di chuyen prev len
            curr = nextNode # di chuyen curr len
        
        return prev