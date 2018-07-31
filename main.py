number=20
guess=-1
print(type(guess))
#print("数字猜谜游戏")
lis = [10, 2.0, "my name:", [1, 2]]
lis.append(10)
while guess != number :
    guess = input("Please input the number:\n")
    print(type(guess))
    if guess.isdigit() :
        guess = int(guess)
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

i = 0
for x in lis :
    print(x)
