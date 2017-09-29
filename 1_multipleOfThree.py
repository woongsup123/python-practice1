import sys


def isint(x):
    try:
        a = int(x)
    except ValueError:
        return False
    return True


number = input('수를 입력하세요: ')
if isint(number):
    if int(number) % 3 == 0:
        print('3의 배수입니다.')
    else:
        print('3의 배수가 아닙니다.')
else:
    print('정수가 아닙니다.')