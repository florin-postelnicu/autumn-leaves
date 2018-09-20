'''
Using import string

@ArashHowaida string.punctuation includes quotes (both double and single) - even in my example
 it strips out the double quotes. If you want to customize what gets stripped in addition to str.punctuation,
 just concatenate string.punctuation with a string of characters you also want removed,
  like translator = str.maketrans({key: None for key in string.punctuation + 'abc'})
   if you wanted to remove punctuation and any occurrences of the characters a, b, or c. – wkl Dec 28 '16 at 5:48
My quotes must have some encoding issues, good to know. Thank you! – Arash Howaida Dec 28 '16 at 6:00
1
str.maketrans('', '', string.punctuation) would also work. There is no need to loop, at any rate,
 even str.maketrans(dict.fromkeys(string.punctuation)) would be better here. – Martijn Pieters♦ Jan 16 '17 at 19:22

more info about maketrans(intab, outtab)

The maketrans() method returns a translation table that maps each character in the intabstring into the character
 at the same position in the outtab string. Then this table is passed to the translate() function.

Note − Both intab and outtab must have the same length.

str.maketrans(intab, outtab]);

Example

#!/usr/bin/python3

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example....wow!!!"
print (str.translate(trantab))

See the tutorialspoint Methods and formating operators
https://www.tutorialspoint.com/python3/python_strings.htm
'''
import string

# Thanks to Martijn Pieters for this improved version

# This uses the 3-argument version of str.maketrans
# with arguments (x, y, z) where 'x' and 'y'
# must be equal-length strings and characters in 'x'
# are replaced by characters in 'y'. 'z'
# is a string (string.punctuation here)
# where each character in the string is mapped
# to None
translator = str.maketrans('', '', string.punctuation)

# This is an alternative that creates a dictionary mapping
# of every character from string.punctuation to None (this will
# also work)
# translator = str.maketrans(dict.fromkeys(string.punctuation))

s = 'string with "punctuation" inside of it! Does this work? I hope so.'

# pass the translator to the string's translate method.
print(s.translate(translator))