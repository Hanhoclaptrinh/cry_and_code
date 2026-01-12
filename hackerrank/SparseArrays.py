def matchingStrings(stringList, queries):
    fMap = {} # mang tan suat
    for s in stringList:
        fMap[s] = fMap.get(s, 0) + 1

    # tra cuu cac cau  truy van
    res = []
    for q in queries:
        res.append(fMap.get(q, 0))

    return res