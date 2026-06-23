def minimum_number(nums):
    n=len(nums)
    sum_of_elements=n*(n+1)//2
    total_sum=sum(nums)
    print(sum_of_elements-total_sum)
nums=[3,0,1]
minimum_number(nums)

