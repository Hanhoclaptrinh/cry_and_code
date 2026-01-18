def migratoryBirds(ar):
    # dict luu so lan xuat hien cua loai chim
    bCnt = {}
    
    # duyet danh sach ma loai chim de tim so lan xuat hien
    for b in ar:
        if b in bCnt: # chim da co trong dict -> tang them 1
            bCnt[b] += 1
        else:
            bCnt[b] = 1  # chua co -> them vao tu dien 
            
    # loai chim xuat hien nhieu nhat
    maxCnt = -1 # so lan xuat hien nhieu nhat
    bMaxCnt = -1 # luu ma loai chim xuat hien nhieu nhat
    
    for b, c in bCnt.items():
        # neu loai chim xuat hien nhieu hon so lan xuat hien nhieu nhat hien tai
        # hoac xuat hien xung so lan nhung ma loai chim nho hon
        if c > maxCnt or (c == maxCnt and b < bMaxCnt):
            maxCnt = c
            bMaxCnt = b
            
    return bMaxCnt