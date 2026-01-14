def findDigits(n):
    cnt = 0
    chLst = str(n)
    intLst = [int(c) for c in chLst]
    for i in intLst:
        if i != 0 and n % i == 0:
            cnt += 1
    return cnt