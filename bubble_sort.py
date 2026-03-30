def bubble_sort(arr):
    n=len(arr)
    if len(arr)<=1:
       return arr
    swap=0
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
               swap+=1
               arr[j],arr[j+1]=arr[j+1],arr[j]
    return "sorted array:",arr,"number of swaps:",swap
arr=[500, 100, 400, 200, 300]
print(bubble_sort(arr))
        
# A teacher has a list of student grades. Sort them in ascending order and return the sorted grades along with the number of swaps made. Fewer swaps indicate the grades were already close to sorted.
def ascending_order(arr):
    n=len(arr)
    if n<=1:
        return arr
    shifts=0
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                shifts+=1
    return f"sorted array:{arr} number of shifts:{shifts}"
arr=[90, 85, 80, 75, 70]
print(ascending_order(arr))