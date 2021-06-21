def num(x):
  list[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  r = list[x]
a = int(input("Admin enter the secret number: "))
y = num(a)
print("The Game Starts!")
prnt("Guess a Number betwen 1 to 15")

w = 0
for i in range(0,4):
  z = int(input("Guess the number: "))
  if z == y:
    print("You Won!")
    w = 1
    break
  elif z < y:
    print("Your guess is lower than the actual number! TRY AGAIN!!")
  elif z > y:
    print("Your guess is higher than the actual number! TRY AGAIN!!")
  else:
    print("Invalid Entry!!")
if w == 1:
  print("Congratulations!!!")
else:
  print("Oops!!You lost the GAME")
    
