#Input name
name=input("Enter a Name : ")
print("                              \t\t\t", "Hi",name,"Welcome to GameInt")



#Generating 4 random numbers
import random
r1num=random.randint(1,6)
import random
r2num=random.randint(1,6)
import random
r3num=random.randint(1,6)
import random
r4num=random.randint(1,6)
list=[r1num,r2num,r3num,r4num]


print("Numbers to Guess - X X X X""""                                                                                        Color Mapping:


                                                                                                                             1-White 2-Blue 3-Red
                                                                                                                             4-Yellow 5-Green 6-Purple""")

print("                         Enter 4 numbers and each number should be in range of 0-6                                                                 ")
print("                         If you enter 0000 as guess numbers programme will be terminated                                                           ")


print("Attempt No","                         ","Guess","                  ","Result")
rep=0
while(rep==0):
 attempt=1
 while(attempt<=8):
     print(attempt)
    
#User entering 4 numbers
     while True:
         try:
             num1=int(input("Enter the guess number 1 : "))
             num2=int(input("Enter the guess number 2 : "))
             num3=int(input("Enter the guess number 3 : "))
             num4=int(input("Enter the guess number 4 : "))

         except ValueError:
             print("Invalid Input please enter again")
     list1=[num1,num2,num3,num4]
    
#If user enter 0000 Terminate the programme
     if(num1==0 and num2==0 and num3==0 and num4==0):
        print("Game Over")
        print("End Game")
        break
#Controling user enter numbers in range of 0-6
     if(num1>6):
        print("Invalid number")
     elif(num2>6):
        print("Invalid number")
     elif(num3>6):
        print("Invalid number")
     elif(num4>6):
        print("Invalid number")
     elif(num1<0):
        print("Invalid number")
     elif(num2<0):
        print("Invalid number")
     elif(num3<0):
        print("Invalid number")
     elif(num4<0):
        print("Invalid number")
     else:
        print(num1,num2,num3,num4)


    

# Matching random numbers in to colours
#r1num
     if(r1num==1):       
        r1num=="White"
     elif(r1num==2):
        r1num=="Blue"
     elif(r1num==3):
        r1num=="Red"
     elif(r1num==4):
        r1num=="Yellow"
     elif(r1num==5):
        r1num=="Green"
     elif(r1num==6):
        r1num=="Purple"

#r2num

     if(r2num==1): 
        r2num=="White"
     elif(r2num==2):
        r2num=="Blue"
     elif(r2num==3):
        r2num=="Red"
     elif(r2num==4):
        r2num=="Yellow"
     elif(r2num==5):
        r2num=="Green"
     elif(r2num==6):
        r2num=="Purple"


#r3num

     if(r3num==1):     
        r3num=="White"
     elif(r3num==2):
        r3num=="Blue"
     elif(r3num==3):
        r3num=="Red"
     elif(r3num==4):
        r3num=="Yellow"
     elif(r3num==5):
        r3num=="Green"
     elif(r3num==6):
        r3num=="Purple"

#r4num

     if(r4num==1):    
        r4num=="White"
     elif(r4num==2):
        r4num=="Blue"
     elif(r4num==3):
        r4num=="Red"
     elif(r4num==4):
        r4num=="Yellow"
     elif(r4num==5):
        r4num=="Green"
     elif(r4num==6):
        r4num=="Purple"




       
#check user entered number and system generated number is equal or not

    
#if the guess pegs are in the correct colour and the correct place or wrong colour in wrong place and entirely colour is different
     if(r1num==num1):
        result1="1"
     elif(r1num==num2):
        result1="0"
     elif(r1num==num3):
        result1="0"
     elif(r1num==num4):
        result1="0"
     else:
        result1="."
    



     if(r2num==num2):
        result2="1"
     elif(r2num==num1):
        result2="0"
     elif(r2num==num3):
        result2="0"
     elif(r2num==num4):
        result2="0"
     else:
        result2="."
    


     if(r3num==num3):
        result3="1"
     elif(r3num==num1):
        result3="0"
     elif(r3num==num2):
        result3="0"
     elif(r3num==num4):
        result3="0"
     else:
        result3="."
   


     if(r4num==num4):
        result4="1"
     elif(r4num==num1):
        result4="0"
     elif(r4num==num2):
        result4="0"
     elif(r4num==num3):
        result4="0"
     else:
        result4="."

#print the 4 guess numbers and 4 results
     print("                                   ",num1,num2,num3,num4,"                 ",result1,result2,result3,result4)
                                                                                        
     print("____________________________________________________________________________________")


#if guess numbers and generated numbers are correct
     if(r1num==num1 and r2num==num2 and r3num==num3 and r4num==num4):
         print("Congraduations!!!! You have won the game....")

         print("You have scored 100 points.")
         game=str(input("Do you want to continue this game (yes/no)?"))
         if(game=="yes"):
             
            rep==0
         else:
             break
     attempt=attempt+1
        
        
#game running process
 game=str(input("Do you want to continue this game (yes/no)?"))
 if(game=="yes"):
     rep==0
         
        
        
     
   
 else:
     rep=rep+1
     print("End Game")
     print("Game Over")
     break
    
