def countApplesAndOranges(s, t, a, b, apples, oranges):
    # vi tri tao roi: a + d
    # vi tri cam roi: b + d
    # neu a + d nam trong doan [s,t] thi tinh la roi roi vao nha
    # neu b + d nam trong doan [s,t] thi tinh la cam roi vao nha
    appleCnt=sum(1 for d in apples if s<=a+d<=t)
    orangeCnt=sum(1 for d in oranges if s<=b+d<=t)
    
    print(appleCnt)
    print(orangeCnt)