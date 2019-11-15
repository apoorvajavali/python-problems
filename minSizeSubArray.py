def minSubArrayLen(s, nums) :
    start = 0
    minsize = len(nums)
    size = 0
    total = 0
    for i, n in enumerate(nums):
        total += n
        size += 1
        if total >= s:
            minsize = min(size, minsize)
            size = 0
            total -= nums[i]
            start += i
        else:
            total += n
            size += 1
    return minsize

print(minSubArrayLen(7, [2,3,1,2,4,3]))