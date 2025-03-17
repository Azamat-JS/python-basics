# def add1(a):
#     b=a+1
#     return b
# print(add1(2))
# # help(add1)

# #///-----

# def Mult(a, b):
#     c=a*b
#     return c

# print(Mult(2, 5)) # 10
# print(Mult(2, "Mike")) # MikeMike
# #--------------
# def add1(a):
#     b=a+1
#     print(a, "plus 1 equals", b)
#     return b

# add1(2)
#-----------

# def print_stuff(ratings):
#     for i, rating in enumerate(ratings):
#         print(f"You {i} Rating is {rating}")  # Using f-string for clarity

# a = [11, 2, 34, 4]
# print_stuff(a)
#------------------------------------
# def WriterNames(*names):
#     for name in names:
#         print(name)

# WriterNames('Olim', 'Ali', "Odil", 'Bek')

#-------------
# def AddDC(y):
#     y = y + 'DC'  # Modify y instead of x
#     print(y)
#     return y

# x = "AC"
# z = AddDC(x)
# print(z)

#-------------------

# def PinkFloyd():
#     global ClaimedSales
#     ClaimedSales = '45 million'
#     return ClaimedSales
# PinkFloyd()
# print(ClaimedSales)

# a = len([sum([1,1,1])])
# print(a)
L=[1, 3, 2]
a=sorted(L)
print(a)