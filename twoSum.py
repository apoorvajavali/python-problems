# class Solution(object):
#     def twoSum(self, nums, target):
#         h = {}
#         for i, num in enumerate(nums):
#             diff = (target - num)
#             if diff not in h:
#                 h[num] = i
#             else:
#                 return [h[diff], i]
# s = Solution()
# print(s.twoSum([2,7,11,15], 9))

n = 1994
size = len(str(n))-1
for a in str(n):
    place = 10 ** size
    print(int(a)*place)
    size -= 1