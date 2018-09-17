'''
Python Program to convert a file into a list of lines


Read a file line by line and store each line into a list
You can then manipulate every line of the file
as an element of the list created
'''


def file_read(fname):                 # This is a function that reads to a file {fname}, and

    content_lisft = []                # returns it into a list
    with open(fname) as f:            # The file {fname} it is open and its content,
        content_list = f.readlines()  # line, by line, it is added to the content_list
        return content_list            # the function returns a list


list_of_lines = file_read("continusplitfiles.py")    # The new variable list_of_lines calls file_read() function
num_lines = len(list_of_lines)          # num_lines determines how many items are in the list_of_lines

for i in range(num_lines):              # The counting loop for prints the items of list_of_lines
    print(list_of_lines[i])             # one by one. This is not an essential result, but just a proof
                                        # that the elements of the original file {fname} can be manipulated
                                        # line by line