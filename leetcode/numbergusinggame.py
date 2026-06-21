import random
secret=random.randint(1,10)

while True:
   guess=int(input("Enter a number between 1 and 10:"))
   if secret==guess:
    print("you guess is correct")
    break
   elif guess>secret:
    print("Too high")
   else:
     print("Too low")