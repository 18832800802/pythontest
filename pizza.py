def make(size,*toppings):
    print('\n制作一个' + str(size) + '寸的pizza所需要的配料： ')
    for topping in toppings:
        print('-' + topping)
make(16,'黄油','芝士','虾')