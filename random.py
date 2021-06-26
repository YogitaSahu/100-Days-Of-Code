import random
n=random.randint(0,1)
print(n)
repeat="yes"
while repeat=="yes":
    print(n)
    if n==0:
        print("Heads")
    else:
        print("Tails")
    repeat=input("Want to repeat?")
    n=random.randint(0,1)

