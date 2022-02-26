# using the AND method to determine if number is odd or even
def is_even(num):
    return not(num & 1) and True or False #  perform the and gate operation and return its output


n= int(input("enter the number you wish to check : "))
print(is_even(n))

 