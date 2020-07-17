# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:15:23 2018

@author: Eray
"""

"""
Author: Eray Okutay
Nu:260201058
Homework1
"""
print("Welcome to the Guess Game" )

#Program asks range values from the user.
begin = input("Enter the number that you want your range begin with: ")
end = input("Enter the number that you want your range end with: ")

#string.isdigit function doesn't count negative numbers as digits so I wrote this function for using negative numbers too.
def integer(x):
    #I had to use try and except for not receiving any errors.
    try:
        #If function can successfully turns input to integer it turns to true.
        int(x)
        return True
    #I checked the internet for how to find errors and I found ValueError piece.
    except ValueError:
        return False 
    
#if values are digits loop starts.
while integer(begin) and integer(end) :
    
    #Transforms values to integers. 
    begin = int(begin) 
    end = int(end)
    
    #If begin is bigger than end program asks for another inputs.
    if begin>= end :
        begin = input("Enter a number smaller than end: ")
        end = input("Enter a number greater than begin: ")
   
    #If everythings is OK.
    else:
        break        
        


    
    
  
    #If numbers are not numeric program asks another inputs.
    
while integer(begin) == False or integer(end) == False:
  
    

    print("Please enter numeric values")
    begin = input("Enter the number that you want your range begin with: ")
    end = input("Enter the number that you want your range end with: ")
#Transforms values to integers.    
begin = int(begin) 
end = int(end)


#Determines our guess count     
n = (end-begin)/5
#Our first score
s = 100
#Selecting a random number.
import random
target = random.randint(int(begin),int(end))

#When end-begin was smaller than 5, program was giving 0 to guess count so I wrote this lines to avoid that.
if (end-begin) <= 5:
    print("Your target is in the range of",int(begin),",",int(end), "and you have",1," guesses to know the target." )
    b = input("Enter a guest: ")
    while integer(b) == False:
        b= input("Please enter numeric values")
    b = int(b)
    
    while b < begin or b> end:
        b= input("Please enter a value in specified range: ")
    if target == b:
        print("Right Guess! Your score is ",100,"") 
    else :
        print("You lost! Your target was",target,"")
    b = int(b)

#When end > begin
else:
    print("Your target is in the range of",int(begin),",",int(end), "and you have",abs(int(n))," guesses to know the target." )
    b = input("Enter a guest: ")
    n= n-1
    while integer(b) == False:
        b= input("Please enter numeric values")
    b = int(b)
    while b < begin or b> end:
        b= input("Please enter a value in specified range: ")
        b= int(b)
    #When the guess is wrong.
    while  b != target :
        
        s= s-5
        """If range is smaller or equal to 5 and guess counter
                is one program executes this paragraph(In this specific values i encountered lot of bugs.Therefore, i had to put this paragraph.)."""
        if s>0 and int(n)==1 and (end-begin) <= 5:
            print("Wrong guess!")
            print("Your target is in the range of",int(begin),",",int(end), "and you have",1," guesses to know the target." )
            b = input("Enter a guest: ")
            while integer(b) == False:
                b= input("Please enter numeric values")
            while b < begin or b> end:
                b= input("Please enter a value in specified range: ")
            b = int(b)
            if target != b:
                print("You lost! Your target was",target,"")
                break
            else:
                continue
                        
                
                
                
                #If the user still have points and have equal or over 1 in guess counter also have greater range than 5 this paragraph will be executed.
        elif s>0 and int(n)>=1 and (end-begin) > 5:
            print("Wrong guess!")
            n= n-1
            b = input("Enter a guest: ")
            while integer(b) == False:
                b= input("Please enter numeric values")
                b = int(b)
            while int(b) < begin or int(b)> end:
                b= input("Please enter a value in specified range: ")
            b = int(b)
                    
                    
                    
                        
               
                
                #Another control point to check whether guess in range or not.
        elif int(b)> end or int(b)<begin:
            b= input("Please enter a value in specified range: ")
            s= s+5
            b= int(b)
                #Program increases the score by 5 to make user's points still when user enters invalid values. 
            
                
                
                
            #When user outs of his points or outs of guess counter.
        elif (s <=0) or (n==0 and (end-begin) <= 5)  : 
            print("You lost! Your target was",target,"")
            break
                
                
            #To the decrease range and refreshes the counter.
        else:
                #Checks the target is closer to whether begin or end.
            if (begin + ((end-begin)/2)) < target  :
                begin = int(begin + ((end-begin)/2))
                n = int((end-begin)//5)
                print("Your target is in the range of",int(begin),",",int(end), "and you have",abs(int(n))," guesses to know the target." )
                b = input("Enter a guest: ")
                n= n-1
                while integer(b) == False:
                    b= input("Please enter numeric values")
                    b = int(b)
                while int(b) < begin or int(b)> end:
                    b= input("Please enter a value in specified range: ")
                if (s <=0) or (target!= b and abs((end-begin)) <= 5)  : 
                    print("You lost! Your target was",target,"")
                    break
                
            else: 
                end = int(end - ((end-begin)/2))
                n = int((end-begin)//5)
                print("Your target is in the range of",int(begin),",",int(end), "and you have",abs(int(n))," guesses to know the target." )
                b = input("Enter a guest: ")
                n = n-1
                while integer(b) == False:
                    b= input("Please enter numeric values")
                b = int(b)
                while int(b) < begin or int(b)> end:
                    b= input("Please enter a value in specified range: ")
                if (s <=0) or (target!= b and abs((end-begin)) <= 5)  : 
                    print("You lost! Your target was",target,"")
                    break
                
            continue
    
    #If the guess is True.
    if target==b:
        print("Right Guess! Your score is ",s,"")

print("Thank you for playing my game")

abc = input("For close the game press enter.")