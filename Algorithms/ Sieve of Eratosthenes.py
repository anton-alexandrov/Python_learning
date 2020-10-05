def sieve (n):
    nums = [n for n in range(2,n+1)]
    for i in range (0,len(nums)//2):
        for n in range(i+1, len(nums)):
            print (f'i: {i} n: {n} nums[n]: {nums[n]} nums[i] {nums[i]} ')
            if nums[i]!=0 and nums[n]!=0 and nums[n]%nums[i]==0 :
                nums[n]=0
    return [x for x in nums if x!=0]

print(sieve(100), len(sieve(100)))


