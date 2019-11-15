def firstUniqChar(s):
    if s == "":
        return -1
    if s[0] not in s[1:len(s)] :
        print(s[1:len(s)])
        return 0
    for i in range(1, len(s)-1):
        unvisited = s[i + 1:]
        visited = s[:i]
        print("visited: " + visited + " unvisited: " + unvisited)
        if s[i] not in visited and s[i] not in unvisited:
            return i
    if s[-1] not in s[:len(s)-1] :
        print("here "+s[:len(s)-1])
        return len(s)-1
    return -1
    # build hash map : character and how often it appears
    # count = collections.Counter(s)

    # find the index
    # for idx, ch in enumerate(s):
    #     if count[ch] == 1:
    #         return idx
    # return -1

print(firstUniqChar("aadb"))