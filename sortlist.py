prices=[1200,800,1500,999]
n=len(prices)

for i in range(n):
    for j in range(n-i-1):
        if prices[j]<prices[j+1]:
           prices[j],prices[j+1]=prices[j+1],prices[j]
print(prices)