import random
randNamber = random.randint(1,100)
print(randNamber)

userguess=int(input("enter your guess::"))
if(userguess==randNamber):
    print("your guess right")
else:
    print("wrong guess")
