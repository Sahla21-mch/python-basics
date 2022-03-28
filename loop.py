import math
def square_root(number):                        #function declaration
    if number<0:                                #checking the state of the number
        return ("no answer")
    else:
        return(math.sqrt(number))               #calculating the square root
answer=square_root(int(input("enter a number")))    #calling the function
print(answer)

