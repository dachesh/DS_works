# String Difference

import difflib

str1 = "First things first, I'm an artist."
#print(type(str1))
str2 = "Second thing first, I can't count because I'm an artist"
#print(type(str2))

strset1 = str1.split()
print(strset1)
strset2 = str2.split()
print(strset2)

diff = difflib.Differ(strset1,strset2)
print(diff)