def analyzeInvestments(string):
    substr = []
    main = ['A', 'B', 'C']
    count = 0
    res = [string[i: j] for i in range(len(string))
           for j in range(i + 1, len(string) + 1)]

    for s in set(res):
        if len(set(main) & set(s)) == 3:
            count += 1
    return count

string = "ABCCBA" #"ABBCZBAC"
print(string[5:5])
print(analyzeInvestments(string))
