def fib(n,dp={}):
    if n in dp:
       return dp[n]
    if n<=1:
       return n
    dp[n]=fib(n-1,dp)+fib(n-2,dp)
    return dp[n]
print(fib(10))
# bottom up approch
def fib(n):
    if n<=1:
       return n
    dp=[0]*(n+1)
    dp[1]=1
    for i in range(2,n+1):
      dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print(5)