# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 15:43:02 2018

@author: Eray Okutay
Number = 260201058
"""
#Firtly, program asks an input.
print("Press 1 to product and price list")
print("Press 2 to total revenue and most selling product(s) in total")
print("Press 3 to daily revenue and most selling product(s) in a day")
print("Press 4 to total payment for a student")
print("Press 0 to exit")
choice = input("")

#If user enters different input than given values, user will encounter this: 
while choice != "1" and choice != "2" and choice != "3" and choice !="4" and choice !="0" :
    print("Please enter 1,2,3,4 or 0(exit)")
    print("Enter 5 to see your choices again")
    choice = input("")
    if choice == "5" :
        print("Press 1 to product and price list")
        print("Press 2 to total revenue and most selling product(s) in total")
        print("Press 3 to daily revenue and most selling product(s) in a day")
        print("Press 4 to total payment for a student")
        print("Press 0 to exit")
        choice = input("")
        print(" ")
#While user enters the right input, the loop starts.        
while choice == "1" or choice =="2" or choice == "3" or choice =="4":
    

    if choice == "1" :
     

        #To print the output correctly I've done this.
        print("PRODUCT               PRICES")
        print(" ")
        #Program opens our first file.
        a = open("PriceList.txt",'r+')
        #program transforms text file to a list and splits them by "#"
        for lines in a.readlines():
            info = lines.split("#")
            
            #Every items has a different character length.Thus, I've had to do an extraction funtion for needed spaces...
            print(info[0],(" ")*(20-len(info[0])) ,info[1])
        #I've encountered some bugs so I closed the file until next turn of the loop.
        a.close()
        #Another input addition to stop the loop from being infinite.
        print("Press 1 to product and price list")
        print("Press 2 to total revenue and most selling product(s) in total")
        print("Press 3 to daily revenue and most selling product(s) in a day")
        print("Press 4 to total payment for a student")
        print("Press 0 to exit")
        choice = input("")
        print(" ")
        
        #Another character check.
        while choice != "1" and choice != "2" and choice != "3" and choice !="4" and choice !="0" :
            print("Please enter 1,2,3,4 or 0(exit)")
            print("Enter 5 to see your choices again")
            choice = input("")
            if choice == "5" :
                print("Press 1 to product and price list")
                print("Press 2 to total revenue and most selling product(s) in total")
                print("Press 3 to daily revenue and most selling product(s) in a day")
                print("Press 4 to total payment for a student")
                print("Press 0 to exit")
                choice = input("")
                print(" ")
    #I've seperated choice 1 and others because of some bugs.    
    elif choice == "2" or choice == "3" or choice == "4" :
        b=0
        d=0
        a = open("PriceList.txt",'r+')
        b = a.readlines()
        f= 0
        gum = 0
        ben=0
        sen=0
        o = 1
        biz = 0
        siz=0
        giz = 0
        harry = 0
        potter = 0
        selam=0
        portal = 0
        gezgin = 0
        ppp= -1
        c = open("PurchaseHistory.txt",'r+')
        d = c.readlines()
        A= []
        C = []
        G = []
        Z = []
        L = []
        P = []
        
        if choice == "2" :
            for i in range(len(b)):
                b[i] = b[i].split("#")
     
            #A function written for seperating STUDENT's ids as a different element of a list.
            for i in range(len(d)):
                d[i] = d[i].replace("-",",")
            for i in range(len(d)):
                d[i] = d[i].split(",")
            #Comparing the lists and if there is a match it adds item's price to sum.
            for i in d:
                for f in i:
                    f= f.strip()
                    for m in b:
                        m[0]= m[0].strip()
                        m[1]= m[1].strip()
                        
                        if f==m[0]:
                            gum+=int(m[1])
            #Creates a list of items with number of how much they sold.                
            for m in b :
                m[0]= m[0].strip()
                m[1]= m[1].strip()
                for i in d:
                    for f in i:
                        f= f.strip()
                        if f==m[0]:
                            ben+=1
                ben = str(ben)
                A.append(m[0]+"#"+ben)
                ben=0
            #Determines which items sold most and adds them to a list and determines how much they sold.
            for i in range(len(A)):
                A[i] = A[i].split("#")
            food = A[0][0]
            maximum = A[0][1]    
            for i in range(len(A)-1):
                if int(A[i+1][1]) >=  int(maximum):
                    food = A[i+1][0]
                    maximum= A[i+1][1]
            for i in range(len(A)-1):
                if int(A[i][1]) ==  int(maximum):
                    P.append(A[i][0])
                    
            print("Total revenue = ",gum,"")
            print("Most selling product(s) in TOTAL (",maximum,"sales)")
            #Printing most selling items.
            for i in P:
                print(i)
            #Another character check.
            while choice != "1" and choice != "2" and choice != "3" and choice !="4" and choice !="0" :
                print("Please enter 1,2,3,4 or 0(exit)")
                print("Enter 5 to see your choices again")
                choice = input("")
            if choice == "5" :
                print("Press 1 to product and price list")
                print("Press 2 to total revenue and most selling product(s) in total")
                print("Press 3 to daily revenue and most selling product(s) in a day")
                print("Press 4 to total payment for a student")
                print("Press 0 to exit")
                choice = input("")
                print(" ")
                
                    
        elif choice== "3" :
            
            for i in range(len(b)):
                b[i] = b[i].split("#")
     

            for i in range(len(d)):
                d[i] = d[i].replace("-",",")
            for i in range(len(d)):
                d[i] = d[i].split(",")
            
            for m in b :
                m[0]= m[0].strip()
                m[1]= m[1].strip()
            #Creates a list for extracting information later.    
            for i in d:
                for p in i:
                    p= p.strip()
                    
                    C.append(p)
            #Determines how many days are there for asking.    
            for i in range(1,len(d)):
                for x in C:
                    if "DAY"+"#"+str(i) == x:
                        selam = i                    

                
            
                
            #If user enters a day out of range.    
            print("Select day between 1 and ",selam,": ")
            g= input()
            while int(g)<1 or int(g)>selam :
                print("Select day between 1 and ",selam,": ")
                g= input()
                
                
            
                    
            
                    
            f=0 
            #Finding which line on given DAY.
            Q = C.index("DAY"+"#"+g)   
            
            #I use try and except because when user enters last day try code doesn't work.
            try:
                #Calculating day's revenue.
                R = C.index("DAY"+"#"+str(int(g)+1))
                for f in range(Q,R):
                
                    for m in b:
                        m[0]= m[0].strip()
                        m[1]= m[1].strip()
                        if C[f]==m[0]:
                            siz+=int(m[1])
                            
                                
                
                #Matching item and how much that item sold in a list.
                for m in b :
                    m[0]= m[0].strip()
                    m[1]= m[1].strip()
                    for i in range(Q,R):
                        if C[i] == m[0]:
                            giz+=1
                    giz = str(giz)
                    Z.append(m[0]+"#"+giz)
                    giz= 0 
                for i in range(len(Z)):
                    Z[i] = Z[i].split("#")
                harry = Z[0][0]
                potter = Z[0][1]
                #Finding most sold item and how many sold.
                for i in range(len(Z)-1):
                    if int(Z[i+1][1]) >=  int(potter):
                        harry = Z[i+1][0]
                        potter = Z[i+1][1]
                #Appending most sold items to a list.
                for i in range(len(Z)-1):
                    if int(Z[i][1]) ==  int(potter):
                        L.append(Z[i][0])
            #This function is valid for the last day on list (It is pretty much same with the try.
            except ValueError :
                
                for f in range(Q,len(C)):
                
                    for m in b:
                        m[0]= m[0].strip()
                        m[1]= m[1].strip()
                        if C[f]==m[0]:
                            siz+=int(m[1])
                                
                
                
                for m in b :
                    m[0]= m[0].strip()
                    m[1]= m[1].strip()
                    for i in range(Q,len(C)):
                        if C[i] == m[0]:
                            giz+=1
                    giz = str(giz)
                    Z.append(m[0]+"#"+giz)
                    giz= 0 
                for i in range(len(Z)):
                    Z[i] = Z[i].split("#")
                harry = Z[0][0]
                potter = Z[0][1]
                for i in range(len(Z)-1):
                    if int(Z[i+1][1]) >=  int(potter):
                        harry = Z[i+1][0]
                        potter = Z[i+1][1]
                
                for i in range(len(Z)-1):
                    if int(Z[i][1]) ==  int(potter):
                        L.append(Z[i][0])
                
            #Printing data.
            print("Day",g,"total revenue = ",siz,"")
            print("Most selling product(s) (",potter,"sales)")
            #printing the most sold items list.
            for i in L:
                print(i)
        elif choice == "4":
            for i in range(len(b)):
                b[i] = b[i].split("#")
                 
            
            for i in range(len(d)):
                d[i] = d[i].replace("-",",")
            for i in range(len(d)):
                d[i] = d[i].split(",")
            #Finding how many student ids there are.    
            for i in range(len(d)):
                if "STUDENT"+str(i)== d[i][0]:
                    gezgin=i
            print("Select student is between 1 and ",gezgin,": ")
            q = input()
            while int(q)<1 or int(q)>int(gezgin):
                print("Select student is between 1 and ",gezgin,": ")
                q = input()
            
            for m in b :
                m[0]= m[0].strip()
                m[1]= m[1].strip()
            
            for i in range(len(d)):
                
            
                #Finds which lines have given student ids in it and appends to P list.
                if d[i][0] == "STUDENT"+q: 
                    P.append(str(i))
            
            #Calculating the total expenses of given lines in list P.    
            for i in P:
                for l in d[int(i)]:
                    l= l.strip()
                    for m in b:
                        if m[0]==l:
                            portal+=int(m[1])
                            
            print("Student id=",q,"")
            print("Total payment of student",q,"=",portal,"")
        
        
        
        
        
        
        
        
        
        #Asking input.
        print("Press 1 to product and price list")
        print("Press 2 to total revenue and most selling product(s) in total")
        print("Press 3 to daily revenue and most selling product(s) in a day")
        print("Press 4 to total payment for a student")
        print("Press 0 to exit")
        choice = input("")
        print(" ")
        
        #Another character check.
        while choice != "1" and choice != "2" and choice != "3" and choice !="4" and choice !="0" :
            print("Please enter 1,2,3,4 or 0(exit)")
            print("Enter 5 to see your choices again")
            choice = input("")
            if choice == "5" :
                print("Press 1 to product and price list")
                print("Press 2 to total revenue and most selling product(s) in total")
                print("Press 3 to daily revenue and most selling product(s) in a day")
                print("Press 4 to total payment for a student")
                print("Press 0 to exit")
                choice = input("")
                print(" ")
                        
        
           
                    
                    
                    
                    
                    
                
                
                
                
                
            #Closing the lists.    
            a.close()
            c.close()
    #breaking the function.        
    elif choice == "0":
        break
    
                        
        
        
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
            
            