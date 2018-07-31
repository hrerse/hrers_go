number=20
guess=-1
print(type(guess))
#print("数字猜谜游戏")
lis = []
#lis.append(10)
while guess != number :
    guess = input("Please input the number:\n")
    print(type(guess))
    if guess.isdigit() :
        guess = int(guess)
        lis.append(guess)
        if guess==number :
            print("恭喜您，猜中了")
#            input("Please Enter a key to exit")
            break
        elif guess > number :
            print("猜大了")
        elif guess < number :
            print("猜小了")
    else :
        print("Please input a number")
# not len(lis[])
print("You guessed %d times totally" % len(lis))
for x in lis :
    print(x)
