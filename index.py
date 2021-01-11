states = {
    "ny": 0.3,
    "la": 0.5,
    "man": 0.2,
    "org": 1.4,
    "pen": 1.1
}


state = input('Введите код штата(например ny): ')
sku = int(input('Введите количество единиц товара: '))
price = int(input('Ввидите цену товара: '))
summ = sku*price
sum_tax = summ + sku*price*states[state]
your_discount = 0


if summ >= 1000:
    your_discount = summ * 0.03
elif summ >= 5000:
    your_discount = summ * 0.05
elif summ >= 7000:
    your_discount = summ * 0.07
elif summ >= 10000:
    your_discount = summ * 0.1
elif summ >= 15000:
    your_discount = summ * 0.15
final_summ = sum_tax - your_discount

print('Ваша скидка - ' + str(your_discount))
print('Стоимость вашего заказа без налогов - ' + str(summ))
print('Стоимость вашего заказа c учетом налога штата и учетом вашей скидки - ' + str(final_summ))
