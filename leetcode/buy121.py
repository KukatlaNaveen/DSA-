def buying(prices):
  max=0
  min_price=float('inf')
  for price in prices:
       if price<min_price:
          min_price=price
       profit=price-min_price
       
       if profit>max:
         max=profit
  return max
prices=[8,5,3,1,7]
print(buying(prices))

nums=[7,1,5,3,6,4]
minimum=nums[0]
maximum=0
for num in nums:
  minimum=min(minimum,num)
  maximum=(maximum,num,minimum)
print("max profit:",maximum)
          