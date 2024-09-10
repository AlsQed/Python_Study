def findLeft(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid -1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left == len(nums): return -1
    return left if nums[left] == target else -1

def findRight(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left - 1 < 0: return -1
    return left - 1 if nums[left-1] == target else - 1

def searchRange(nums, target):
    return [findLeft(nums, target), findRight(nums, target)]
print(searchRange([5,7,7,8,8,8,9],8))