# print("salom python")
# print(int(3.1))
# print(bool(1))
# print(float(3))
# name = "Azamat Abdullayev"
# # print(name[1]) # z
# # print(name[-2]) # e

# # print(name[0:4]) # Azam
# # print(name[9:12]) # dul
# # print(name[::2]) # Aaa bulyv
# # print(len(name)) #17
# # role = " developer"
# # print(name + role) #Azamat Abdullayev developer
# # print(3 * name) #Azamat AbdullayevAzamat AbdullayevAzamat Abdullayev
# A="email.com"
# # B=A.upper()
# # print(B) #EMAIL.COM
# C="Bu archa"
# D=C.replace("Bu", "Chiroyli")
# print(D) # Chiroyli archa
# print(C.find("rch")) #4
# print(C.find("ge")) # -1
# ---------------------------------------

# name = "John"
# age = 30

# print(f"His name is {name} his age is {age}")
# print("Your name is {} and your age is {}".format(name, age))
# x=2/2
# print(x) # 1.0

# --------------------- tuples - immutable

# ratings = (12, 11, 4, 33, 9)
# ratingsSorted = sorted(ratings)
# print(ratingsSorted) #[4, 9, 11, 12, 33]

# -------------- Lists - mutable

# L = ["Hi", 1.32, 10]
# # # print(L[0]) # Hi
# # L1 = L+["pop", 11]
# # print(L1) # ['Hi', 1.32, 10, 'pop', 11]
# # L.extend(["yu", 13])
# # print(L) #['Hi', 1.32, 10, 'yu', 13]
# # L.append([12, "pol"])
# # print(L) #['Hi', 1.32, 10, 'yu', 13, [12, 'pol']]
# del(L[0])
# print(L) # [1.32, 10]
# new_list = L.copy()
# print(new_list) # [1.32, 10]

# B = [1, 1, 1, 3, 3, 4, 11, 1]
# count = B.count(1)
# print(count) # 4

C=['we', 'are', 12, 'friends']
new_list = C.insert(2, "twelve")
print(C) # ['we', 'are', 'twelve', 12, 'friends']

my_list = [1, 2, 3, 4, 5] 
print(my_list[1:4]) 
# Output: [2, 3, 4] (elements from index 1 to 3)
print(my_list[:3]) 
# Output: [1, 2, 3] (elements from the beginning up to index 2) 
print(my_list[2:]) 
# Output: [3, 4, 5] (elements from index 2 to the end) 
print(my_list[::2]) 
# Output: [1, 3, 5] (every second element)

print([1, 1, 1] + [2, 3])