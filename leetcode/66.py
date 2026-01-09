class Solution:
    def plusOne(d):
        n = len(d)

        for i in range(n - 1, -1, -1):
            if d[i] < 9:
                d[i] += 1
                return d

            d[i] = 0

        return [1] + d