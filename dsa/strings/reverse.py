name="naveen"
name=list(name)
n=len(name)
for i in range(n//2):
    name[i],name[n-i-1]=name[n-i-1],name[i]
name=" ".join(name)
print(name)

# anagrams
word1="Dusty"
word2="study"
results="anagram" if sorted(word1.lower())==sorted(word2.lower()) else "No"
print(results)

# find the first non repeating character in a string 
name="book"
count={}
for ch in name:
    count[ch]=count.get(ch,0)+1
for ch in name:
   if  count[ch]==1:
        print(ch)
#         break
word="nnaaveeenn"
seen=set()
result=""
for ch in word:
    if ch not in seen:
        seen.add(ch)
        result+=ch
print(result)

# check if string is palidrome ignoring case non alphanumeric chars
palindrome="madam"
temp=""
for ch in palindrome:
     if ch.isalnum():
        temp+=ch.lower()
print(temp==temp[::-1])

# find the longest substring without repeating characters