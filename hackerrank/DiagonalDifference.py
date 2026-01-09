def diagonalDifference(arr):
    n = len(arr)
    s1 = sum(arr[i][i] for i in range(n)) # tong cheo chinh
    s2 = sum(arr[i][n-1-i] for i in range(n)) # tong cheo phu
    return abs(s1-s2)