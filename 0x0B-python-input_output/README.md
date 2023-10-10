<h1> 0x0B. Python - Input/Output</h1>
 open() returns a file object, and most commonly, used with two positional arguments and one keyword argument.
 To open a file, we use:
 open("filename", mode, encoding="utf-8")
 filename - represents the name of the file for example: story.txt
 mode - can be:
 r - for reading file
 w - for writing in to a file
 a - for append
 r+ - for reading and writing to a file
 rb+ - for reading and writing binary
 It is good practice to use with open() because it helps to close the file should in case there is a crash in the operation. 
