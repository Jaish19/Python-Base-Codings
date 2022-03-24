# 1. Write a Python program to check that a string 
# contains only a certain set of characters (in this case a-z, A-Z and 0-9). 

b='abcdef1234@#$%^'
re.findall('[a-zA-z0-9]',b)

re.findall('\w',b)

re.findall('\W',c) - To pick not a char
-------------------------------------------------

# Write a Python program that matches a string that has an a followed by zero or more b's.

x='abc'
x='ac'
x='abbbc'

re.findall("ab*?",x)

---------------------------------------------------
# Write a Python program to find the occurrence and position of the substrings within a string.

for i in re.finditer("exercises",a):
	print a[i.start():i.end()],i.start(), i.end()


---------------------------------------------------------------------

# Write a Python program that matches a string that has an a followed by one or more b's.

x='abc'
x='ac'
x='abbbc'
re.findall("ab+?",x)

----------------------------------------------------

# 5. Write a Python program that matches a string that has an a followed by three 'b'. Go to the editor

re.findall('ab{3}',a)

----------------------------------------------------------------

# 6. Write a Python program that matches a string that has an a followed by two to three 'b'. Go to the editor

re.findall('ab{2,3}',a)

------------------------------------------------------------------

# Write a Python program to find sequences of lowercase letters joined with a underscore.

re.findall('^[a-z]+_[a-z]+',b)

------------------------------------------------------------
# 8. Write a Python program to find the sequences of one upper case letter followed by lower case letters. Go to the editor

re.findall('^[A-Z]+[a-z]+',a)

----------------------------------------------------
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

re.findall('^a.*b$',a)

-----------------------------------------------------------
# Write a Python program that matches a word at the beginning of a string.

re.findall('\AThe',c)

---------------------------------------------------------
# Write a Python program that matches a word at the end of a string, with optional punctuation.

re.findall('solution\W$',c)
re.findall('^.*solution\W$',c)

----------------------------------------------
# Write a Python program that matches a word containing 'z'.

x='The quick brown fox jumps over the lazy dog.'

re.findall(r'\w*z\w*',x)  -- To find a word

re.findall(r'\Bz',x) - To find a 'z' letter present 
------------------------------------------
# Write a Python program that matches a word containing 'z', not at the start or end of the word.

re.findall(r'\w*\Bz\B.\w*',x)

re.findall(r'\Bz\B',x)

-------------------------------------------------------
# 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores. Go to the editor

re.findall("^[a-zA-Z0-9_]*$",a)

---------------------------------------------------------------

# 15. Write a Python program where a string will start with a specific number.


a='2ackdk'

re.findall('^\d\w+',a)

b='6abced'

re.findall('^6\w+',b)

c='52415'

re.findall('^5\d+',c)

----------------------------------------------------------------------

# Write a Python program to remove leading zeros from an IP address.

ip = "216.08.094.196"

re.sub('0','',ip)

re.findall('[0-9]+[0-9]',ip)
--------------------------------------------------------

# 17. Write a Python program to check for a number at the end of a string.

re.findall('.*\d$',a)

------------------------------------------------

# 18. Write Python program to search the numbers (0-9) of length between 1 to 3 in a given string.

re.findall('[0-9]{1,3}',a)

-----------------------------------------------

# 19. Write a Python program to search some literals strings in a string.

a='The quick brown fox jumps over the lazy dog.'

# Mtd 1:

re.findall('dog',a)

#############################

# Mtd 2:

v=['dog','horse','fox','cow']
>>> for i in v:
	if re.search(i, a):
		print "matched"
	else:
		print "Not matched"

-----------------------------------------------------------

# 20.Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.


a='The quick brown fox jumps over the lazy dog.'

re.findall('fox',a)
re.search('fox',a).span()

---------------------------------------------------

input_val='geeksforgeeks'
check='for'
replace='abcd'
import re

print re.sub('geeks','abcd',input_val)

------------------------------------------------
# Python | Word location in String

wordToFind='geeks'
value='geeksforgeeks'

import re

print len(re.findall('geeks',value))

-------------------------------------------------------
# Python – Extract Unique values dictionary values

# output: [1, 2, 5, 6, 7, 8, 10, 11, 12]

test_dict = {'gfg' : [5, 6, 7, 8], 
             'is' : [10, 11, 7, 5], 
             'best' : [6, 12, 10, 8], 
             'for' : [1, 2, 5]}

l1=list(set([k for i,j in test_dict.items() for k in j]))
print l1


---------------------------------------------------------

# Write a Python program to find the occurrence and position of the substrings within a string.


for i in re.finditer('exercises',a):
    print a[i.start():i.end()], i.start(), i.end()

-------------------------------------------------------

# 23.Write a Python program to replace whitespaces with an underscore and vice versa.


a='Python exercises'

re.sub('\s','_',a)

re.sub('_',' ',a)  # vice versa

a.replace(' ','_') # using non-regExp.

------------------------------------------------

string = "engineers rock"

# output: engineers

re.findall(r'^e.*s',string)

re.findall('engineers',string)

-------------------------------------------------
# 24 Python: Extract year, month and date from an url

url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"

re.findall(r"/(\d{4})/(\d{1,2})/(\d{1,2})/",url1)

dt1 = "2026-01-02"

re.findall(r"(\d{4})-(\d{1,2})-(\d{1,2})",dt1)
---------------------------------------------------

# Capture IP Address


import re

if re.search("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$",'172.168.2.2'):
    print "True"
else:
    print "False"

-------------------------------------------------
