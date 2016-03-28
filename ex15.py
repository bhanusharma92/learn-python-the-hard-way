from sys import argv
script, filename = argv

#open the file whose filename is supplied by command line
txt = open(filename)

print("Here is your file %r"%filename)
#read the file using object of file and print its contents
print(txt.read())
txt.close()

print("Type the filename again")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())
txt_again.close()