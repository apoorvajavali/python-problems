
def maxCommonality(string):
    maxlength = 0
    for i in range(1,len(string)):
        length = 0
        s1, s2 = string[:i], string[i:]
        common = set(s1) & set(s2)
        for c in common:
            length += min(s1.count(c), s2.count(c))
        maxlength = max(length, maxlength)
    return maxlength

string = "abcdedeara" # "zzzxxxzzz"
print(maxCommonality(string))