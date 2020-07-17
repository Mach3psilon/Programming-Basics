# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 10:13:34 2019

@author: Eray Okutay
Number : 260201058
"""




def valid_or_invalid(acid):
    def valid_acid(acid):
        acid_elements = []
        for elements in acid :
            acid_elements.append(elements)
        #Function stops recursion in case of funtion length becomes 0.
        if len(acid) == 0:
            
            return 0
            
        else :
            #It checks whether a DNA and RNA diversion is exist or not.
            if ("T" in acid_elements) and ("U" in acid_elements) :
                return 1 
            else:
                #It checks the given characters of the acid for containing elements which does not belong to the RNA or DNA.
                if acid[0] == "A" or acid[0] == "U" or acid[0] == "G" or acid[0] == "C" or acid[0] == "T":
                        return 0 + valid_acid(acid[1:])
                else: 
                    return 1 
    #If acid valid funtion returns 0.
    control = valid_acid(acid)
    if control == 0:
        return "valid"
    else:
        return "invalid"
    
def dna_or_rna_or_invalid(acid):
    #Checks the funcion is valid or not.
    control = valid_or_invalid(acid)
    
    def dna_or_rna(acid):
        if len(acid) == 0:
            return 0
        
        else:
            if acid[0] == "T":
                #If acid involves T it returns 1.
                return 1 
            elif acid[0] == "G":
                #If acid involves G it returns 0.
                return 0 + dna_or_rna(acid[1:])
            else:
                return 0 + dna_or_rna(acid[1:])
    
    if control == "valid" :
        if dna_or_rna(acid) == 0:
            return "RNA"
        else :
            return "DNA"
    else:
        return "invalid"
    
def pair_some_dna(acid):
    #It decides wheter fiven acid is DNA or NOT.
    acid_type = dna_or_rna_or_invalid(acid)
    pair_of_dna = []
    def pair_dna(acid):
        #If acid length is 0 recursion stops.
        if len(acid) == 0:
            return ""
        else: 
            #It appends the correct pair to the pair_of_dna list.
            if acid[0] == "A":
                pair_of_dna.append("T")
                pair_dna(acid[1:])
            elif acid[0] == "T":
                pair_of_dna.append("A")
                pair_dna(acid[1:])
            elif acid[0] == "G":
                pair_of_dna.append("C")
                pair_dna(acid[1:])
            elif acid[0] == "C":
                pair_of_dna.append("G")
                pair_dna(acid[1:])
            
        return pair_of_dna
    if acid_type == "DNA":
        #it returns the pair of the given DNA.
        pair_of_dna = ''.join(pair_dna(acid))
        
        return pair_of_dna
    else:
        print("It is not a DNA")
        

def find_the_difference_between_two_acid(acid1,acid2):
    
    difference = []
    #It adds the length difference to the list.
    difference.append(str(abs(len(acid1)-len(acid2))))
    difference_number = 0
    def find_the_difference(acid1,acid2):
        #If one of the acids lenght is 0 it stops the recursion.
        if len(acid1) == 0 or len(acid2) == 0 :
            return ""
        else: 
            #Every different element adds "1" to the list.
            if acid1[0] != acid2[0] :
                difference.append(str(1))
                find_the_difference(acid1[1:],acid2[1:])
            #Every same element adds "0" to the list.
            else :
                find_the_difference(acid1[1:],acid2[1:])
                difference.append(str(0))
    find_the_difference(acid1,acid2)
    #It summs all elements of the list.
    for number in difference:
        difference_number += int(number)
    
    return difference_number



        
        
                
        



























        

        
                
            
                

        
        
        
    

    