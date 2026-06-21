# nums=[7,1,5,3]
# ans=0
# max=0
# for i in range(len(nums)):
#    for j in range(len(nums)):
#       if j>i and nums[j]>nums[i]:
#           ans=nums[j]-nums[i]
#       if ans>max:
#           max=ans
# print(max)
# product of Array Except Self ,ex:[1,2,3,4] => [24,12,8,6]

# nums=[1,2,3,4]
# n=len(nums)
# answer=[]
# for i in range(n):
#     product=1
#     for j in range(n):
#         if i!=j:
#             product*=nums[j]
#     answer.append(product)
# print(answer)

# container with most water leetcode 11  ex:[]

# nums=15
# empty=4
# output=nums
# emptybottle=nums
# while emptybottle>=empty:
#     newbottles=emptybottle//empty
#     output+=newbottles
#     emptybottle=newbottles+emptybottle%empty
# print(output)

# traping rain water 42

def trap(height):
    n=len(height)
    if n==0:
        return 0
    water=0
    left=0
    right=n-1
    l_max=0
    r_max=0
    while left<=right:
        l=height[left]
        r=height[right]
        if l<=r:
            if l>=l_max:
                l_max=l
            else:
                water+=l_max-l
            left+=1
        else:
            if r>r_max:
                r_max=r
            else:
                water+=r_max-r
    return water
height=[4, 2, 0, 3, 2, 5]
print(trap(height))
            
            
# Median of two sorted arrays 4 

nums1=[10,9]
nums2=[2,6]
merged=nums1+nums2
print(merged)
merged.sort()

n=len(merged)
mid=n//2
if n%2==0:
    print((merged[mid]+merged[mid-1])/2)
else:
    print("mid :",merged[mid])
    
    
# highest sum of subarray of length 3 in below array

nums=[5,9,1,8,7]
n=len(nums)
ans=0
for i in range(n):
    for j in range(i,n):
        tli=[]
        sum=0
        for k in range(i,j+1):
            tli.append(nums[k])
            sum+=nums[k]
        # print(tli)
        if len(tli)==3:
            print(tli)
            ans=max(ans,sum)
print(ans)


li=[5,9,1,8,7]
n=len(li)
l=0
temp=0
k=3
ans=0
for r in range(n):
    temp+=li[r]
    
    if (r-l==3):
        temp-=li[l]
        l+=1
    if r-l+1==3:
        ans=max(ans,temp)
print(ans)