# ---------- writing
# with open('./single/example1.txt', 'w') as file1:
#     file1.write('This is a line')

# #-----------------------
# Lines = ["This is line 1", "This is line 2", "This is line 3"]

# with open('./single/example1.txt', 'w') as file2:
#   for line in Lines:
#      file2.write(line)

# with open('./single/example1.txt', 'a') as file3:
#    file3.write('this is line D')

# with open('./single/example1.txt', 'w') as file2:
#   for line in Lines:
#       file2.write(line + "\n")

# #------------------------ copying
# with open('./single/example1.txt', "r") as readfile:
#    with open('./single/example2.txt', "w") as writefile:
#       for line in readfile:
#          writefile.write(line)

# ------------ appending
new_data = "This is line C"
# Open an existing file Example2.txt for appending
with open('./single/example2.txt', 'a') as file1:
    file1.write(new_data + "\n")