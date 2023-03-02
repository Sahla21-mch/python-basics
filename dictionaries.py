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
this = my_list2.values()
this = my_list2.keys()
print (this)

my_list = {
    "tomatoes": "200frs",
    "onion": "100frs",
    "green_spicies": "50frs",
    "rice": "900frs",
    "maggi": "50frs",
    "salt": "50frs"}
my_list.update({"oil": "1500"})
print(my_list)
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
my_list2["rice"] = 1200
print (my_list2)
this = my_list2.values()
this = my_list2.keys()
print (this)
tuples = my_list2.items()
print (tuples)
if "magg" in my_list2:
    print("yes, there's maggi")
else:
    print("NO! doesn't exist")
#looping in dics
for x, y in my_list2.items():
    print(x, y)
# dictionaries in dictionaries 
my_list = {
    "tomatoes": {"fresh": "500frs","dry": "200frs"},
    "onion": "100frs",
    "green_spicies": "50frs",
    "rice": "900frs",
    "maggi": "50frs",
    "salt": "50frs"}
my_list.update({"oil": "1500"})
print(my_list)

