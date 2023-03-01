my_list = {
    "tomatoes": "200frs",
    "onion": "100frs",
    "green_spicies": "50frs",
    "rice": "900frs",
    "maggi": "50frs",
    "salt": "50frs"}
print (my_list["maggi"])
print (len(my_list))
print (type(my_list))

#another methos of declaring a dictionary 
my_list2 = dict(
    tomatoes = "200frs",
    onion = "100frs",
    green_spicies ="50frs",
    rice ="900frs",
    maggi ="50frs",
    salt = "50frs"
)
print (my_list2)
#acessing an element in a dictionary
this = my_list2.get("salt")
print (this)
