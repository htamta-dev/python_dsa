def two_sum_sorted(arr, target):
    indexed_nums = [(num, i) for i,num in enumerate(arr)]
    indexed_nums.sort()
    left,right = 0, len(indexed_nums)-1

    while left < right:
        curr_sum = indexed_nums[left][0] + indexed_nums[right][0]
        if curr_sum == target:
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []

def test_two_sum_sorted():
    arr = [2, 7, 11, 15]
    target = 9
    result = two_sum_sorted(arr, target)
    print("Two sum sorted result : ", result)           