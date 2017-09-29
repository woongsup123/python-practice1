sum_of_nums = 0

def add_to_sum(num):
    global sum_of_nums
    sum_of_nums += num

while True:
    num = int(input())
    add_to_sum(num)
    print(sum_of_nums)
