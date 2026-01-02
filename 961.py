class Solution:
    def repeatedNTimes(nums):
        s = set()
        for n in nums:
            if n in s:
                return n
            s.add(n)