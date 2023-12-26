def productExceptSelf(nums):
    n = len(nums)
    pre, post = 1, 1
    output = [1 for i in nums]

    for i in range(1, n):
        output[i] = output[i - 1] * nums[i - 1]
    for k in range(n, 0, -1):
        output[k - 1] *= post
        post *= nums[k - 1]

    print(output)

productExceptSelf([1, 2, 3, 4])
