'''

https://stackabuse.com/reading-files-with-pytho
The link to Fairy Tales
https://www.cs.cmu.edu/~spok/grimmtmp/

For methods on strings ( string.strip(args), string.split(args)) look on:
https://www.tutorialspoint.com/python
'''
import random
import urllib.request  # the library that handles the url
index = random.randint(1,209)
data = urllib.request.urlopen(("https://www.cs.cmu.edu/~spok/grimmtmp/{:003d}.txt").format(index)).read()

data = data.decode("utf-8")


f = open("NewFile", "w")
f.write(data)
f.close()

f = open("NewFile", "r")
text1 = f.read()

sentences = text1.rstrip("  ").split(".")
for sentence in sentences:

    print("\n" + sentence, end=".")

f.close()

