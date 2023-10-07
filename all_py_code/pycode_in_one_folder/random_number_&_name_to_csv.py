import random
import csv
import string


just_rand_str = [str(random.randint(0 , 1)) for _ in range(100)]

def generate_random_name(length):
    chars = string.ascii_letters
    return ''.join(random.choice(chars) for _ in range(length))

min_num = 100000000000000
max_num = 999999999999999
random_numbers = ["TCEA-CN-" + str(random.randint(min_num, max_num)) for _ in range(100)]
# print(random_numbers)

num_names = 100
name_length = 15
random_names = [generate_random_name(name_length) for _ in range(num_names)]
# print(random_names)

data = list(zip(random_names, random_numbers, just_rand_str))

with open("numbers_and_names.csv", "w", newline="") as csvfile:
    file = csv.writer(csvfile)
    file.writerow(["Name", "Number", "Action"])
    for name, number, action in data:
        file.writerow([name, number, action])

print("Done")


