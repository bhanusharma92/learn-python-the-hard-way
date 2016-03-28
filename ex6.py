#x is a variable of type string and it uses %d and % sign
x = "There are %d types of people"%10

#binary is string object
binary = "binary"

#do_not is also string object
do_not = "don't"

#y is also a string object and somewhat defined like x is defined
y = "those who know %s and those who %s"%(binary, do_not)

#value of x and y are printed on screen
print(x)
print(y)

#this is a print statement and here %r is used and anything represented using it comes under single quotes
print("I said %r :"%x)
print("I also said %s"%y)

#hillarious is boolean object
hilarious = False

#This is a string and there is somethis unusual about this string as it contain %r
joke_evaluation = "Is.nt that joke funny! %r"

#In this print statement joke_evaluation strint contain %r and 5 sign is used by hilarious
print(joke_evaluation % hilarious)

w = "this is left side of..."
e = "a string with right side."

#There is concat of string occurs
print(w + e)