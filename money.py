amount = input('금액: ')
units = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
numbers = []
for unit in units:
    tup = divmod(int(amount), unit)
    num = tup[0]
    amount = tup[1]
    numbers.append(num)
    print(unit, '원: ', num, '개')
