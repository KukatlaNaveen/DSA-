def selection_sort(arr):
    n=len(arr)
    if n<=1:
       return arr
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
               min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    
    return arr
arr=[5,6,2,3,8]
print(selection_sort(arr))

# problem number:153 

def find_min(arr):
    n=len(arr)
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
               min_idx=j
        if min_idx!=i:
           arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr,arr[0]
arr=[4,5,6,7,0,1,2]
print(find_min(arr))

# problems number: 414 
def third_max(arr):
    arr=list(set(arr))
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]>arr[min_idx]:
               min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    if n<=3:
       return arr[2]
    else:
       return arr[0]
arr=[3,2,1]
print(third_max(arr))