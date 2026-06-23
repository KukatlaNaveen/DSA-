def longest_common_prefix(s):
     if not s:
       return s
     first=s[0]
     for i in range(len(first)):
         for word in s:
            if first[i]!=word[i]:
               return  first[:i]
     return first
s=["flower","flow","flight"]
print(longest_common_prefix(s))