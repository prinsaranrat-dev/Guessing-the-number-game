import random
num = random.randint(0,100)
count = 0
ans = -1
while ans != num:
    ans = int(input(""))
    count += 1
    print("Your guess is", ans)
    if ans > num:
        print("Too High!")
        count += 1
    elif ans < num:
        print("Too Low")
        count += 1
    else:
        print("You guessed correct!!")
        
print("You guessed it in", count, "tries!")
if count == 1:
    print("Are you a mind reader?! 😵")
elif count <= 5:
    print("Ok, that's great! 😆")
elif count <= 15:
    print("Seems frustrating, isn't it? 😜")
else:
    print("You got some real bad luck... 😬")
