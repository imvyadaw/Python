my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
my_dict2 = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

for key in my_dict:
    print(key)



# print(my_dict.get("name"))

# my_dict2["age"]=45
# my_dict2["name"]="nisha"

# my_dict["name"]="Vishal yadaw"
# my_dict["age"]=21
# my_dict["city"]='Motihari'

# print(my_dict["age"])
# print(my_dict["name"])
# print(my_dict["city"])

# print(my_dict2["age"])
# print(my_dict2["name"])

# my_dict["Job"]="Ethical hacker"  # new dict add

# print(my_dict["Job"])    

# merge={**my_dict,**my_dict2}

# print(merge)
if "age" in my_dict:
    print("age is present in dict",my_dict["age"])
else:
    print("not found",my_dict["age"])


# my_dict = {
#     "name": "Alice",
#     "age": 30
# }

# print(my_dict.get("name"))  # Outputs: Alice
# print(my_dict.get("city", "Not Found"))  # Outputs: Not Found (since "city" is not in the dictionary)


