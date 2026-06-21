def duplicate():
  arr=[1,2,3,1]
  k=3
  ans=0
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i]==arr[j]:
        if abs(i-j)==k:
              return True
  return False
print(duplicate())

# optimized code
def containduplicate(nums):
  freq={}
  for num in nums:
    if num in freq:
      freq[num]+=1
    else:
      freq[num]=1
  for num in nums:
    if freq[num]>1:
      return True
  return False
nums=[2,1,4,5,2]
print(containduplicate(nums))

                              