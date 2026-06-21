nums=[1,2,3,2,2,2,1]
freq={}
for num in nums:
     freq[num]=freq.get(num,0)+1
     
for key in freq:
    if freq[key]>len(nums)//2:
        print(key)
# time complexity o(nlogn)

# time-complexity o(n) sc=o(1)
count=0
digit=None
for num in nums:
   if count==0:
     digit=num
   if num==digit:
      count+=1
   else:
      count-=1
print(digit)
    