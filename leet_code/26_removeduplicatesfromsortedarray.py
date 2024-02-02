#leetcode
nums_test_1 = [1,1,2]

def removeDuplicates(nums) -> int:
    for i, v in enumerate(nums):
        print(nums[i])
        print(nums[i+1])
        if nums[i] == nums[i+1]:
            nums.remove(nums[i+1])
        else:
            continue
    return nums

removeDuplicates(nums_test_1)
