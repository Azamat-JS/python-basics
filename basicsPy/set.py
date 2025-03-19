# syntax set_name.add(element) 
fruits = {"pear", "apple", "banana"}

fruits.add("mango")
fruits.clear()
new_fruits = fruits.copy()
empty_set = set() #Creating an Empty 
fruits = {"apple", "banana", "orange"}
fruits.discard("apple") # removes apple
colors = {"kiwi", "peach"}
is_subset = fruits.issubset(colors) # true
is_superset = colors.issuperset(fruits) # check all elements are available in other set

removed_fruit = fruits.pop()
fruits.remove("banana")

combined = fruits.union(colors) 
common = fruits.intersection(colors) 
unique_to_fruits = fruits.difference(colors) 
sym_diff = fruits.symmetric_difference(colors)
