from input_utils import input_int


num_file = open("./nums.txt", "r+")
num_list = num_file.readlines()
adding_num = input_int("Please insert a number: ")
adding_pos = input_int("Please insert the line: ")

num_list.insert(adding_pos, str(adding_num)+"\n")

num_file = open("./nums.txt", "w")
num_file.write("".join(num_list))


