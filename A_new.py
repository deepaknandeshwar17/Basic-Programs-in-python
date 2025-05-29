def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right)//2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def find_min(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left+right)//2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left,nums[left]

def find_min_with_dup(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left+right)//2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        elif nums[mid] < nums[right]:
            right = mid
        else:
            right = right - 1
    return left,nums[left]

# nums = [1,2,3,4,5,6,7]
nums = [3,4,5,6,7,1,2]
target = 2
# print(binary_search(nums,target))
print(find_min_with_dup(nums))