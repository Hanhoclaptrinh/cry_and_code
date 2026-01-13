def camelcase(s):
    cnt = 1

    for c in s:
        if c.isupper():
            cnt += 1
    return cnt