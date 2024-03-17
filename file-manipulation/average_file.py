num_file = open("./nums.txt", "r")
num_list = num_file.readlines()
count_num = 0
total = 0

for num in num_list:
    try:
        total += float(num)
        count_num += 1
    except:
        pass


avg = total/count_num

print(avg)
