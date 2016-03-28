from sys import argv
script, user_name = argv
prompt = '> '
print("hi %s, i'm %s script"%(user_name, script))
print("I'd like to ask you a few questions")
print("Do you like me %s"%user_name)
likes = input(prompt)#raw input was renamed to input

print("What do you lives")
lives = input(prompt)

print("What kind of computer do you have")
computer = input(prompt)#raw input was renamed to input

print("""
So you said %r likes about me,
and you lives at %r , dont know where that is,
and you have %r type of computer"""%(likes, lives, computer))
