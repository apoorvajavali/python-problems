def strangeSort(nums, actual):
    num_map = {}
    for i, n in enumerate(nums):
        real = ''
        for d in n:
            real += str((actual.index(int(d))))
        num_map[(n, i)] = int(real)
    print(num_map)
    num_map = sorted(num_map.items(), key=lambda x: x[1])
    for i in range(len(nums)):
        nums[i] = num_map[i][0][0]
    return nums


actual1 = [3, 5, 4, 6, 2, 7, 9, 8, 0, 1]
nums1 = ['990', '332', '32']
print(strangeSort(nums1, actual1))
actual2 = [2, 1, 4, 8, 6, 3, 0, 9, 7, 5]
nums2 = ['12', '02', '4', '023', '023', '83', '224', '50']
print(strangeSort(nums2, actual2))