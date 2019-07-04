import random
q=int(input("Enter your guess number"))
import random
p=random.randint(1,6)
print("random number",p)
if p==q:
    print("Guess number correct")
else:
    print("Wrong Choice")
    if q>p:
        print("the number is too high")
    elif q<p:
        print("the number is too low")
