def quick_sort(arr):
    n=len(arr)
    if n<=1:
       return arr
    pivot=arr[0]
    left=[]
    right=[]
    for i in range(1,n):
        if arr[i][1]>=pivot[1]:
           left.append(arr[i])
        else:
           right.append(arr[i])
    return quick_sort(left)+[pivot]+quick_sort(right)

arr=[("Rohit",85), ("Virat",120), ("Dhoni",60),("Hardik",95), ("Rahul",110) ]
print(quick_sort(arr))

def flight(seats,prefered_seat):
   n=len(seats)
   left=0
   right=n-1
   comparisons=0
   while left<=right:
      mid=(left+right)//2
      comparisons+=1
      if seats[mid]==prefered_seat:
         
         return f" seat:{seats[mid]} \n is available position in list:{mid} \n comparison made:{comparisons} "
         
      elif seats[mid]<prefered_seat:
         left=mid+1
      else:
         right=mid-1
         
   return f"{prefered_seat} is not in stock,\ncomparison:{comparisons}"
seats=["Aspirin","Cetirizine","Dolo650","Ibuprofen","Metformin", "Omeprazole", "Paracetamol","Ranitidine"]

print(flight(seats,"Amoxicillin")) 
