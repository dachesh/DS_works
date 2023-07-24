# String Difference

import difflib

str1 = "First things first, I'm an artist."
#print(type(str1))
str2 = "Second thing first, I can't count because I'm an artist."
#print(type(str2))

strset1 = str1.split()
#print(strset1)
strset2 = str2.split()
#print(strset2)

wordlist = list(set((strset1 + strset2)))
uniqlist = []

for i in range(len(wordlist)):
	item = wordlist[i]
	if item in strset1 and item in strset2:
		continue
	else:
		uniqlist.append(item)

print(uniqlist)