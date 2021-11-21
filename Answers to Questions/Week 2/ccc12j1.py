speedLimit = int(input())
speed = int(input())
dif = speed - speedLimit

if dif <= 0:
    print("Congratulations, you are within the speed limit!")
elif dif <= 20:
    print("You are speeding and your fine is $100.")
elif dif <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")