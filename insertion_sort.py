def insertion_sort(arr):
    n=len(arr)
    if n<=1:
       return arr
    shifts=0
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
             arr[j+1]=arr[j]
             shifts+=1
             j-=1
        arr[j+1]=key
    return arr,shifts
arr=[500, 100, 400, 200, 300]
print(insertion_sort(arr))
        