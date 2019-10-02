"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
import os
# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

def openFile():
    path = os.getcwd()+ '/src/foo.txt'
    print(path)
    f = open(path)
    for elem in f:
        print(elem)
    f.close()

openFile()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
def createFile():
    path = os.getcwd()+ '/src/bar.txt'
    print(path)
    f = open(path, 'w')
    f.write("This is a test \n") 
    f.write("To add more lines. \n")
    f.close()
    
createFile()