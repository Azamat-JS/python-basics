# age = 12
# if age > 18:
#     print('you will enter')
# elif age==18:
#     print('go to computer room')
# else:
#     print('go see meat loaf')

# # or operatot

# birth_year = 2008

# if(birth_year < 1990) or (birth_year > 2000):
#     print('You was born before 1990 or after 2000')
# else:
#     print('You was born in the 1990s')

# and operator

# if(birth_year > 1990) and (birth_year < 2000):
#     print('You was born between 1990 and 2000')
# else:
#     print('You was born before 1990 or after 2000')

# not operator

# is_do_not_disturb = True
# if not is_do_not_disturb:
#     print("New message received")

#     friend1_likes_comedy = True
# friend2_likes_action = False
# friend3_likes_drama = False
# if friend1_likes_comedy or friend2_likes_action or friend3_likes_drama:
#     print('good')

#_-----------

# c = "Ok"
# if(c=="Okgs"):
#     print('go')
# else:
#     print('stop')
# print('mike')
#----------

def add(a, b):
    return (sum((a,b)))
print(add(1,2))

with open('./single/example1.txt', 'r') as file1:
  file_stuff=file1.readline()
  print(file_stuff)

# print(file1.closed)
# print(file_stuff)