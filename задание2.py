list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_2 = []
for el in list:
    if el.isdigit():
        num = int(el)
        list_2.extend(['"', f'{num:02d}', '"'])
    elif (el.startswith('-') or el.startswith('+')) and el[1:].isdigit():
        num = int(el[1:])
        list_2.extend(['"', f'{el[0]}{num:02d}', '"'])
    else:
        list_2.append(el)
    list_2.append(' ')
print(list_2)
list = ' '.join(list_2).strip()
print(list)
