number_list = []

for i in range(1, 30):
    number_list.append(i)

num = 0
sum_of_nums = 0

for number in number_list:
    if number % 3 == 0:
        num += 1
        sum_of_nums += number

print(num)
print(sum_of_nums)
