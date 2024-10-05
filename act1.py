import random 
playing = True 
number = str(random.randint(10,20))
print("I'll generate a num from 10 to 20 and u have to guess num 1")
print("game will end when you get 1 hero")
while playing :
   guess = input ("give me ur best guess \n")
   if number == guess:
    print ("u have won")
    print("num was",number)
    break
   
   else:
    print("ur guess is wrong try again \n")