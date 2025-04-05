dict = {"name":"sharathi","name":"xyz","name":"abc", "age":25}
print(dict)
print(dict["name"])
# adding values in the dict
dict["email"] = "sharathir25@gmail.com"
print(dict)

# remove the value form dict
dict.pop("name")
print(dict)

del dict["email"]
print(dict)

#  this is for clearing the key values at the end
dict.clear()
print(dict)