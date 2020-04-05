# Program that asks the user to input any positive integer
# Current value if number is even divide by two
# if number is odd, multiply it by three and add one 
# enter positive integer - 10
# Result 10 5 16 8 4 2 1 


p = float(input("enter positive number "))

if (p % 2) == 0:
    p = p / 2
    print(p)
    # if p has a remainder of 0
    # divide it by two 
    # print P

while (p % 2) != 0:
    p = (p * 3) + 1
    print(p)
while (p % 2) == 0:
    p = p / 2
    print(p)
    # if p is remainder of 1
    # multiple by three and add one
    
print(p, end= '')  #stops the program when answer is 1   


        

        











# while p / 2:
    # if p = 2, 4, 6, 8, 10
    # inspire = / 2
    # if p == 1, 3, 5, 7, 9 
    # inspire = (P * 3) + 1 


    


