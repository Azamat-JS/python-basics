person = {"name": "Umar", "age": 12, "job": "developer"}
print(person.keys())
print(person.values())
print(person["age"])
del(person["age"])
print(person)
person["address"] = "Al-Beruniy 27"
print(person)
print(list(person.keys()))

dict_name = {} #Creates an empty dictionary
person = { "name": "John",  "age": 30, "city": "New York"}
Value = dict_name["key_name"] # syntax
#-- examples 
name = person["name"]
age = person["age"]


# -  syntax -> dict_name[key] = value
#examples
person["Country"] = "USA" # A new entry will be created.
person["city"] = "Chicago"


del person["Country"]

person.update({"Profession": "Doctor"})
person.clear()
if "name" in person:
    print("Name exists in the dictionary.")

    new_person = person.copy()
new_person = dict(person) # 


info = list(person.items())