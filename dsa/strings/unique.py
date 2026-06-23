def unique_char(s):
   smap={}
   for ch in s:
      if ch not in smap:
         smap[ch]=1
      else: 
         smap[ch]+=1
   for i,ch in enumerate(s):
         if smap[ch]==1:
           return i
   return -1
s=input(" enter a string  ")
print(unique_char(s))