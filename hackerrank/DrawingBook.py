def pageCount(n, p):
    # so lan lat tu cuoi: (n//2)-(p//2)
    # so lan lat tu dau: (p//2)
    # so lan lat ca cuon: (n//2)

    return min((p//2), (n//2)-(p//2))