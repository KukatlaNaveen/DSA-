def sequential_prefix_sum(nums):
    n=len(nums)
    prefix_sum=nums[0]
    for i in range(1,n):
       if nums[i]==nums[i-1]+1:
          prefix_sum+=nums[i]
       else:
          break
    s=set(nums)
    sequential=prefix_sum
    while sequential in s:
        sequential+=1
    return sequential
nums=[1,2,3,2,5]
print (sequential_prefix_sum(nums))

     