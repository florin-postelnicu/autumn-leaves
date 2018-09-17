'''


 `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`
'''


f = open("test.dat", "w")
f.write("Hello\nIt is nice meeting you\nWould you learn about files?\n")
f.write('Now is the time ')
f.write("to close the file")
f.close()

f = open("test.dat", "r")
# text =f.read()
# print(text)
print(f.read(5))
print(f.read(1000006))
print(f.read())  # Would print nothing, since we are already at the end of the file.
                # Actually would print an empty row
f.close()

# Leson 2 f.readline(), and f.readlines

file = open("test.dat", "r")
print(file.readline)
print(file.readlines())
file.close()
'''
The following function copies a file, reading and writing up to fifty characters
at a time. The first argument is the name of the original file; the second is the
name of the new file:
'''

def copyFile(oldFile, newFile):
    f1 = open(oldFile, "r")
    f2 = open(newFile, "w")
    while True:
        text =f1.read(50)
        if text =="":
            break    # The break statement is new. Executing it breaks out of the loop; the flow of
                     # execution moves to the first statement after the loo
        f2.write(text)
    f1.close()
    f2.close()
    return

'''
The following is an example of a line-processing program. filterFile makes a
copy of oldFile, omitting any lines that begin with #:

'''
def filterFile(oldFile, newFile):
    f1 = open(oldFile,"r")
    f2 = open(newFile, "w")
    while True:
        text = f1.readline()
        if text == "":
            break
        if text[0] == '#':
            continue    # The continue statement ends the current iteration of the loop, but continues
                        # looping. The flow of execution moves to the top of the loop, checks the condition,
                        # and proceeds accordingly.
        f2.write(text)
    f1.close()
    f2.close()
    return