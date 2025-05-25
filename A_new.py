def two_sum_hash(nums,target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff],i]
        hashmap[num]=i
    
nums = [2,7,6,5]
target = 8
print(two_sum_hash(nums,target))