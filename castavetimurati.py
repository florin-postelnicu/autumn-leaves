'''
thinkCSpy 122

In this  version Python3.6 and greater,
pickling it is done with dual mode 'wb', and 'rb'
string and binary
'''
import pickle
f = open("test.pck", "wb")
pickle.dump(12.3, f)
pickle.dump([1,2,3], f)
f.close()

f = open("test.pck", 'rb')
x = pickle.load(f)
print(x)

grades = {'Bart':75, 'Lisa':98, 'Milhouse':80, 'Nelson':65}


f1 = open('gradesdict.p', 'wb')   # Pickle file is newly created where foo1.py is
pickle.dump(grades, f1)          # dump data to f
f1.close()

f1 = open('gradesdict.p', 'rb')   # 'r' for reading; can be omitted
mydict = pickle.load(f1)         # load file content as mydict
f1.close()

print(mydict)