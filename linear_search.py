arr=[3,4,5,6,7,2]
target=6
for i,num in enumerate(arr):
    if num==target:
      print("index of target:",i,"target:",num)
      
def report(patients,search):
  for item in patients:
    if item["name"]==search:
      return f" patient found! \n name:{item["name"]} \n age:{item["age"]} \n disease:{item["disease"]}"
patients= [
     {"name": "Arjun","age": 34, "disease": "Fever"},
     {"name": "Meena","age": 22, "disease": "Flu"},
     {"name": "Ravi","age": 45, "disease": "Diabetes"},
     {"name": "Sneha", "age": 29, "disease": "Migraine"}
]
search="Arjun"
print(report(patients,search)) 