# # create a list of 5 products and them with numbers
products=["cap","shirt","phone","charger","mouse","shoe"]
products.append("tie")
products.insert(0,"pen")
products[0]="watch"
products.remove("cap")
products.append("shoe")
count=0
for i,product in enumerate(products):
#     print(i,products)
    if product.startswith("s"):
          print("products:",product)

#     if products[i]=="shoe":
#           count+=1
    
# print("count:",count)
    
# print(products)
# print(products[::-1])
    
# #reverse list
# n=len(products)
# for i in range(n//2):
#    products[i],products[n-i-1]=products[n-1-i],products[i]
# print(products)