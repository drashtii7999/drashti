#Python basic program

#Silly Sandwhich Maker

bread = input("Choose your bread (white / brown ):")
filling = input("Choose your filling (cheese / jelly / banana):")
print ("Here your silly sandwhich!!")
print (bread + " " + "bread"+" "+ filling + " " + "rainbow glitter !!")

#pet talk simulator

pet = input("What pet do you have (dog / cat /fish)?:")
if pet == "dog":
    print ("woof! I want treats.")
elif pet == "cat":
    print ("Meow! I rule this house.")
elif pet == "fish":
    print ("Blub blub...I am swimming in style.")
else:
    print ("That's a unique pet! ")



#Rock Paper Scissor game
import random
choice = ["rock","paper","scissor"]

computer = random.choice(choice)

player = input("choose rock,paper or scissor :")
print("computer choose:",computer)
if player == computer:
   print("it's a tie")
elif (player == "rock" and computer == "scissor") or
     (player == "paper" and computer == "rock") or
     (player == "scissor" and computer == "paper"):
             print("You win!!")
     else :
         print("Computer win!!")























