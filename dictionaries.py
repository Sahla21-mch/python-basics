# defining a dictionary
dicts = { "class" : "form 1, form 2, form 3", "gender":"frmale, male"}
print(dicts)
for key , value in dicts.items():
    print("key \n", key)
    print("value \n", value)
dicts["color"] = "blue,red,pink"
print(dicts)
for key, value in dicts.items():
    print("key    value \n", key,  value )
    print(dicts["class"])