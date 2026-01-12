def rotateLeft(d, ar):
    n = len(ar)

    d %= n

    return ar[d:] + ar[:d]