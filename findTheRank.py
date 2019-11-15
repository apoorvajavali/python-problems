def findTheRank(marks, rank):
    total = [sum(i) for i in marks]
    print(total)
    k = 0
    while k != rank:
        highest = total.index(max(total))
        total[highest] = -1
        k += 1
    return highest

marks = [[79, 89, 15], [85, 89, 92], [71, 96, 88], [71, 96, 88]]  #[[80, 96, 81, 77], [78, 71, 93, 75], [71, 98, 70, 95]]
print(findTheRank(marks, 2))