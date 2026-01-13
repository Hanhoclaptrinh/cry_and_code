def minimumBribes(q):
    tb = 0

    q = [ i - 1 for i in q ] # chuyen mang ve index 0

    for i, p in enumerate(q):
        if p - i > 2: # neu nguoi nay nhay qua 2 vi tri (hoi lo 2 lan)
            print("Too chaotic")
            return

        # dem xem co bao nhieu nguoi da hoi lo nguoi p
        for j in range(max(p - 1, 0), i):
            if q[j] > p:
                tb += 1

    print(tb)