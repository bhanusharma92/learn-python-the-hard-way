#this one is your script like argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r"%(arg1,arg2))

#ok that *args is just pointless we can do that
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r"%(arg1, arg2))

#this just takes one argument
def print_one(arg1):
    print("arg1: %r"%arg1)

#this takes no argument
def print_none():
    print("I got nothing")

print_two("bhanu", "sharma")
print_two_again("this is ", "it")
print_one("oneeeeee")
print_none()