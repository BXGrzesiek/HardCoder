# operations:
# - I/O
# - read
# - write
# - append
# -
# filename = name or path
# mode = r(read) w(write) a(add content) x(create file) + else
# my_file = open(filename, mode)

my_file = open("demo.txt", "r")
# print(my_file)

# read() - whole content
# read(n)
# readline() - one line
# readlines(n) - all lines

# print(my_file.read())
# read przestawia kursor na koniec pliku kolejny print z read nic nie wyświetli
# print(my_file.read())

# for i in range(3):
#     print(my_file.readline())
    # new lines? why?
    # because print is giving new lines + next line invisible character

# lines = my_file.readlines()
# print(lines)  # - - \n are visible in list
# print(lines[1].lstrip(1)) # usuwa biały znak z prawej

# wee need to close file, because it will be still in use
# my_file.close()