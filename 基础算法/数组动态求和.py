def runningSum(nums) :
    l = len(nums)
    for i in range(1,l) :
        nums[i]=nums[i]+nums[i-1]
    return nums
print(runningSum([1,2,3,4,5]))


