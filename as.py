# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:18:42 2018

@author: Eray
"""

""" Author:Eray Okutay 
    Nu:260201058
    Homework 1 """

#Entering our range values.
begin = int(input("Enter the natural number that you want your range begin with: "))
end = int(input("Enter the natural number that you want your range end with: "))
#Entering our guess count.
n = (end-begin)/5
a=-5
#Our first score

s = 100
#Selecting a random number.
import random
target = random.randint(int(begin),int(end))
while a != target:
    if end > begin and (end-begin) > 1 and begin >= 0:
        if (end-begin) < 4:
            print("Your target is in the range of",int(begin),",",int(end), "and you have",1," guess to know the target." )    
            b = int(input("Enter your guess: "))
            n= n-1
            if target != b:
                print("You lost! Your target was",target,"")
            else:
                print("Right Guess! Your score is ",s,"")
                
        else:
            print("Your target is in the range of",int(begin),",",int(end), "and you have",int(n)," guesses to know the target." )
            n= n-1
    #Entering our guess.
            b = int(input("Enter your guess: "))
    #The loop in the case of guess is wrong.
            while target != b:
                s = s - 5
                if int(n)>0 and s>0:
                    print("Wrong guess")
                    b = int(input("Enter your guess: "))
                    n = n - 1
    #Decreasing the range and setting a new guess count acoording to the range.
                elif int(n)==0 and s>0 and (end-begin)>5:
                    if (begin + ((end-begin)/2)) < target  :
                        begin = begin + ((end-begin)/2)
                    else:
                            print("Wrong guess")
                            end = end - ((end-begin)/2)
                            n = (end-begin)/5
                            print("Your target is in the range of",int(begin),",",int(end), "and you have",int(n)," guesses to know the target." )
                            b = int(input("Enter your guess: "))
    #It is what program displays when you are out of your guesses.
                else:
                    print("You lost! Your target was",target,"")
                    a==target
                    
    #It stops the program when last writing has displayed.
                    break
    #When you find the target correctly program displays that with your current score.
            if target==b:
                a==target
                print("Right Guess! Your score is ",s,"")
                break
    #If user enters an invalid value program will display that.
    else: 
        print("Please enter valid values.")
        begin = int(input("Enter the number that you want your range begin with: "))
        end = int(input("Enter the number that you want your range end with: "))
        