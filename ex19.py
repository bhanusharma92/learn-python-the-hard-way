def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheese"%cheese_count)
    print("You have %d boxes of crackers"%boxes_of_crackers)
    print("Thats enough for party")
    print("Get a blanket\n")

print("we can jst give numbers directly to funtions")
cheese_and_crackers(20, 30)

print("We can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do maths inside it")
cheese_and_crackers(10 + 20, 5 + 6)

print("We can combine the two variables and the maths")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
