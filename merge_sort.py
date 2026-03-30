def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    temp=[]
    i=j=0
    while i<len(left) and j<len(right):
          if left[i]<=right[j]:
             temp.append(left[i])
             i+=1
          else:
              temp.append(right[j])
              j+=1
    temp.extend(left[i:])
    temp.extend(right[j:])
    return temp
arr=[5,1,1,2,0,0]
print(merge_sort(arr))

