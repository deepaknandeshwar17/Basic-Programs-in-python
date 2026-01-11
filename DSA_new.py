arr = [1,2,3,4,5,6,7]

target = 5

left = 0
right = len(arr)-1

found = False

while left < right:
    curr_sum = arr[left] + arr[right]


    if curr_sum == target:
        found = True
        print(left, right)
        break
    elif curr_sum < target:
        left +=1 
    else:
        right-=1

print(found)
