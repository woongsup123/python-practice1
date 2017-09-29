import random

flag = True

while flag:
    min_num = 1
    max_num = 100
    num = random.randint(min_num, max_num)
    guess = -1
    counter = 1
    print('수를 결정하였습니다. 맞추어 보세요')

    while guess != num:
        print(str(min_num) + '-' + str(max_num))
        guess = int(input(str(counter) + '>> '))
        if guess < num:
            print('더 높게')
            min_num = guess
        elif guess > num:
            print('더 낮게')
            max_num = guess

    print('맞았습니다.')
    retry = ''
    while retry != 'y' and retry != 'n':
        retry = input('다시 하시겠습니까(y/n)>> ')
    if retry == 'n':
        flag = False

