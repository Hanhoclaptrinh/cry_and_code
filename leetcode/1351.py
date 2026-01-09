class Solution:
    def countNegatives(mat):
        m, n = len(mat), len(mat[0])
        cnt = 0
        r, c = m - 1, 0

        while r >= 0 and c < n:
            if mat[r][c] < 0:
                cnt += (n - c)
                r -= 1
            else:
                c += 1
        return cnt