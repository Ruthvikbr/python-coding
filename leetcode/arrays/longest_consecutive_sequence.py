def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    numset = set(nums)
    longest = 0

    for n in numset:
        if (n - 1) not in numset:
            length = 1
            while (n + length) in numset:
                length += 1
            longest = max(length, longest)

    print(longest)


nums = [100, 4, 200, 1, 3, 2]
longestConsecutive(nums)
