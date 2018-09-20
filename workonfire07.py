'''
The link to Fairy Tales
https://www.cs.cmu.edu/~spok/grimmtmp/

For methods on strings ( string.strip(args), string.split(args)) look on:
https://www.tutorialspoint.com/python

I will generate a random index for the url text. The index ia between 1 and 209,
the last index of the texts  at https://www.cs.cmu.edu/~spok/grimmtmp/

index = random.randint(1, 209)
data = urllib.request.urlopen(("https://www.cs.cmu.edu/~spok/grimmtmp/{:003d}.txt").format(index)).read()

Documentation urllib3
https://media.readthedocs.org/pdf/urllib3/latest/urllib3.pdf

'''
import random
import urllib.request  # the library that handles the url


more = "m"
while more == "m":
    index = random.randint(1, 209)
    data = urllib.request.urlopen("https://www.cs.cmu.edu/~spok/grimmtmp/{:003d}.txt".format(index)).read()
    data = data.decode("utf-8")
    f = open("NewFile", "w")
    f.write(data)
    f.close()

    f = open("NewFile", "r")
    text1 = f.read()
    sentences = text1.rstrip("  ").split(".")
    f.close()
    print()
    print("The index of the text is {:003}".format(index))
    print("\n\n")
    cond = "y"
    while cond == "y":
        if len(sentences) <= 0:
            break
        else:
            n = random.randint(0, len(sentences) - 1)  
            print("\n" + sentences[n], end=".")
            print("\n, \n")
            del sentences[n]  
            print("If you want to continue , press y, else press n")
            cond = input("\n")
        print("It was a pleasure to have you play!")
    print("Do you want to read from another text? Press m, else press anything")
    more = input()
print("Let's have a look!")
quit()
