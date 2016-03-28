from sys import argv
script, filename = argv
#some important file operations
#open - open the file
#close - close the file like file -> save ...
#readline - read just one line of the text
#truncate - Empties the file watch out if you care about file
#write('stuff') - write "stuff" to the file

print("we are going to erase %r"%filename)
print("If you do not want that hit ctrl-C(^C)")
print("If you want to continue hit return")

input("?")

print("opening the file.....")
target = open(filename, 'w')

print("truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines")
line1 = input('line1: ')
line2 = input('linw2: ')
line3 = input('line3: ')

print("now I'm going to write these to file")
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)

print("And finally we close it.")
target.close()
