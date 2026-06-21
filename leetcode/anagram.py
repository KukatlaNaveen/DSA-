def anagram(s,s1):
   if len(s)!=len(s1):
      return False
   freq1={}
   freq2={}
   for ch in s:
      freq1[ch]=freq1.get(ch,0)+1
   for ch in s1:
      freq2[ch]=freq2.get(ch,0)+1
   if freq1==freq2:
      return True
   else:
      return False
print(anagram("listen","silant"))

def is_angram(s,t):
   if len(s)!=len(t):
      return False
   countS,countT={},{}
   for i in range(len(s)):
      countS[s[i]]=1+countS.get(s[i],0)
      countT[t[i]]=1+countT.get(t[i],0)
   for c in countS:
      if countS[c]!=countT[c]:
         return False
   return True
s="abc"
t="abc"
print("anagram is",is_angram(s,t))

# group of anagram
def group_of_anagram(strs):
   group={}
   for word in strs:
      sorted_word="".join(sorted(word))
      if sorted_word not in group:
         group[sorted_word]=[]
      group[sorted_word].append(word)
   return list(group.values())
strs=["bat","eat","tea","nat","ate","tan"]
print(group_of_anagram(strs))

      