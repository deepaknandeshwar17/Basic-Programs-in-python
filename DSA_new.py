# arr = [1,2,3,4,5,6,7]
# target = 12

# left = 0
# right = len(arr)-1

# while left < right:
#     curr_sum = arr[left] + arr[right]

#     if curr_sum == target:
#         print(f'The sum found at {arr[left]} + {arr[right]} = {curr_sum}' )
#         break
#     elif curr_sum < target:
#         left+=1
#     else:
#         right-=1
# else:
#     print("Not found in the arraay")

# print(arr)


def count_digit(n):
    num = n
    count =0
    while num > 0:
        count += 1
        num = num//10
    return count
n = 123456
print(count_digit(n))