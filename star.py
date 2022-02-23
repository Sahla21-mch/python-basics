number =  int(input("Enter an odd number "))
if(number>3 and number % 2!= 0 ):
    for i in range(number//2): #loop in ascending values of n
        print(" " * (number-i*2+1-2), "* " * (i*2+1))#(i*2+1) is to print odd stars (*, ***, *****.......)
    for i in range(number//2, -1, -1): #loop in reverse order
        if (i == number//2):
            print(" " * (number-i-4), "* " * (i*2+1))
        else:
            print(" "*(number-i*2-2), " *" *(i*2+1))
elif(number<3 and number % 2==0 ):
    print("number must be greater 3")
else:
    print("number must be odd")



