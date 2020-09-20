def twoSum(nums, target):
    n = 0
    while n < len(nums):
        for k in range (n+1,len(nums)):
            if nums[n] + nums [k] == target:
                return n, k
        else: n+=1
        """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
print(twoSum([3,3],6))