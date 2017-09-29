# identifies if one digit numeric variable, num is divisible by 3
def clap(num):
    if num != 0 and num % 3 == 0:
        return True


for i in range(1, 99):
    clap_sum = ''
    div = divmod(i, 10)
    for val in div:
        if clap(val):
            clap_sum += '짝'
    if clap_sum != '':
        print(str(i) + ' ' + clap_sum)
