def bonAppetit(bill, k, b):
    # bill - mang gia tien cac mon an
    # k - cac mon an anna khong an duoc
    # b - so tien brian thu cua anna

    # tong bill
    t=sum(bill)

    # so tien anna phai share
    aShr=(t - bill[k]) //  2

    if b==aShr:
        print('Bon Appetit') # thu dung tien
    else:
        print(b-aShr) # so tien brian tra lai cho anna