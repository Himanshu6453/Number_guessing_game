m =input("Enter the gussing number for player : ")
print("*")
print("*")
print("*")
print("*")
print("*")
print("*")
print("*")
print("*")
print("*")
print("*")
print("*")
print("*")
n=int(m)
i = 0

while (i <= 10):
    i=i+1
    if i == 9:
        print('your chance is over')
        print("you use your",i-1,"chances")
        print("The number was:",n)
        break
    x = int(input("enter your guessing: "))

    if x < (n-20):
        print("your number is too small")

    elif x < (n-10):
        print("your number is much more small")

    elif x < (n-5):
        print("your number is more small")

    elif x <(n):
        print("your number is too close ,you need a lit bit bigger")

    elif x == n:
        print("congratulation! you win")
        print("you use your",i,"chances")
        break

    elif x < (n+4):
        print("your number is too close, you need a little bit smaller")

    elif x < (n+10):
        print("your number is a bit bigger")

    elif x < (n+15):
        print("your number is bigger")
        
    elif x > (n+20):
        print("your number is too big")

    else:
        print("try again")

jj=input("Press Enter to Exit")
