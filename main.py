from random import randint

first = randint(0,500)
second = randint(0,10)

print("Quiz Time!")




decider = randint(1,4)

if(decider == 1):
   print(first, "+" ,second)
   correctAnswer = first+second

if(decider == 2):
   print(first, "-" ,second)
   correctAnswer = first-second

if(decider == 3):
   print(first, "*" ,second)
   correctAnswer = first*second

if(decider == 4):
   print(first, "/" ,second)
   correctAnswer = first/second

answer = int(input("What's your answer? "))


if(correctAnswer == answer):
    print("You got it correct!")

else:
    print("You got it wrong.")