arr=[3,5,6,7,8,9]
target=8
left=0
right=len(arr)-1
while left<=right:
      mid=(left+right)//2
      if arr[mid]==target:
         print(mid,arr[mid])
         break
      elif arr[mid]<target:
          left=mid+1
      else: 
          right=mid-1
