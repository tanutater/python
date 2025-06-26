import random
secretnumber=random.randint(1,20)
print ("i am thinking of a number between 1 to 20 ")
for guessTaken in range (1,4):
  print("take Guess");
  guess=int(input())
  if(guess<secretnumber):
    print("guess is low")
  elif(guess>secretnumber):
    print("guess is high")
  else:
    break;
if guess==secretnumber:
  print('Good job! You guessed my number in ' + str(guessTaken) + 'guesses!')
else:
  print('Nope. The number I was thinking of was ' + str(secretnumber))