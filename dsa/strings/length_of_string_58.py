# def length(s):
#    print(len(s)-1)
s="   fly me   to   the moon  "
i=len(s)-1
length=0
while i>=0 and s[i]==" ":
   i-=1
   print('q')
while i>=0 and s[i]!=" ":
   length+=1
   i-=1
   print('l')
print(length)