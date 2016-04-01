people = 30
cars = 40
trucks = 15

if cars > people:
    print("we should take the cars")
elif cars < people:
    print("we should not take the cars")
else:
    print("we can't decide")

if trucks > cars:
    print("thats too many trucks")
elif trucks < cars:
    print("maybe we can take the trucks")
else:
    print("we still can't decide")

if people > trucks:
    print("Alright let's juct take the trucks")
else:
    print("Lets stay home then")
