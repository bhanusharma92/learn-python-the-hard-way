formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ('one', 'two', 'three', 'four'))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (True, False, True, False))
print(formatter % (
    "I had this thing.",
    "That you could type up right",
    "But it did'nt sing",
    "so i said goodnight"
))
