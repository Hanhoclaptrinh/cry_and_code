class Solution:
    def hasCycle(head):
        s = head
        f = head

        while f and f.next:
            s = s.next # 1 step
            f = f.next.next # 2 step

            if s == f: return True

        return False