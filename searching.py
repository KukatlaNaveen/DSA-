#find the first occurence of index in sorted list
def first_occurence(arr,target):
    n=len(arr)-1
    left=0
    right=n
    while left<=right:
         mid=(left+right)//2
         if arr[mid]==target:
            result=mid
            right=mid-1
         elif arr[mid]<target:
              left=mid+1
         else:
             right=mid-1
    return result
arr=[3,3,3,4,5,6,7,8]
print(first_occurence(arr,3))
# check if string contain substring using simple search
def simple(text,pattern):
    n=len(text)
    m=len(pattern)
    for i in range(n-m+1):
        if text[i:i+m]==pattern:
           return True
    return False
text="hello world"
pattern="world"
print(simple(text,pattern))
# implement linear search using list of dictionaries by key value
def search_all(data,key,value):
    for item in data:
        if item.get(key)==value:
           return item
    return None
data=[
  {"id":1,"name":"naveen"},
  {"id":2,"name":"vikram"},
  {"id":3,"name":"manoj"}]
print(search_all(data,"id",1))