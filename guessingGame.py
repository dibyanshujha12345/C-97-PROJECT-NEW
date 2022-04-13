import random
numint=random.randrange(1,9)

chances=5
while chances<5:
    chances=chances-1
guess=int(input("Enter any integer between 1-9 "))
 

if (guess==numint):

    print("Congratulations,U won")
    

if not (guess==numint):

    print("U lost the game")  
    guess1=input("Enter another Time ") 

if (guess==numint):

    print("Congratulations,U won")
     

     