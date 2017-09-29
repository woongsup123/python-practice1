menu_dict = {'오뎅': 300, '순대': 400, '만두': 500}

menu = input('메뉴: ')

if menu in menu_dict:
    print(str(menu_dict[menu]) + '원')
