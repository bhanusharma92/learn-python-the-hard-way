def add(a,b):
    print("Adding %d and %d"%(a, b))
    return a + b

def sub(a, b):
    print("Subtract %d and %d"%(a, b))
    return a - b

def multiply(a, b):
    print("Multiply %d and %d"%(a, b))
    return a * b

def divide(a , b):
    print("Dividing %d and %d"%(a, b))
    return a / b

print("Lets do some maths with just functions")

age = add(30, 5)
height = sub(78, 4)
weight = multiply(90, 2)
iq = divide(100,2)

print("Age: %d, height: %d, weight: %d, iq: %d"%(age, height, weight, iq))

print("A puzzule for extra credit type it anyway")

what = add(age, sub(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "can you do it by hand")
