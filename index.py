states = {
    "ny": 0.3,
    "la": 0.5,
    "man": 0.2,
    "org": 1.4,
    "pen": 1.1
}


state = input('Введите код штата(например ny): ')
sku = input('Введите количество единиц товара: ')
price = input('Ввидите цену товара: ')
sum = str(int(sku)*int(price))
sum_tax = str(int(sum) + (int(sku)*int(price)*states[state]))

print('Стоимость вашего заказа без налогов - ' + sum)
print('Стоимость вашего заказа c учетом налога штата - ' + sum_tax)
