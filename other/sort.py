#get n numbers as input and print them in order

amount = int(input("How many numbers?: "))
nums = []
for i in range(amount):
    nums.append(int(input("insert the number: ")))

print(sorted(nums))
    

