def divisibleSumPairs(n, k, ar):
    frg=[0]*k
    cnt=0

    for x in ar:
        r=x%k
        nd=(k-r)%k
        cnt+=frg[nd]
        frg[r]+=1

    return cnt