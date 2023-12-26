target = 9
nums = [2, 7, 11, 12]

d = dict()
for i in range(len(nums)):
    difference = target - nums[i]
    if difference in d.keys():
        print([nums.index(difference), i])
    else:
        d[nums[i]] = difference
