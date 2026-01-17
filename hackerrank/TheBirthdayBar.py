def birthday(s, d, m):
    cnt=0
    for i in range(len(s) - m+1):
        if sum(s[i:m+i]) == d:
            cnt+=1
    return cnt