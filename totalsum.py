# nums=[1,2,3]
# total=0
# for i in range(len(nums)):
#     total+=nums[i]
# print(total)


# array=[5,3,8,9,1,2]
# maxi=float('-inf')
# mini=float("inf")
# for n in range(len(array)) :
#     if array[n]>maxi:
#       maxi=array[n]
#     if array[n]<mini:
#        mini=array[n]
# print(maxi)
# print(mini)

nums=[1,2,3,4,6]
target=6
left=0
right=len(nums)-1
while left<right:
   sum=nums[left]+nums[right]
   if sum==target: 
      print("target is found",left,right)
      break
   elif sum>target:
        right-=1
   else:
    
      left+=1
                          