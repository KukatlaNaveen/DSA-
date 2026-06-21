def plusone(arr):
  for i in reversed(range(len(arr))):
     if arr[i]!=9:
         arr[i]+=1
         return arr
     arr[i]=0
  return arr 

arr=[2,4,3,9]

print(plusone(arr))