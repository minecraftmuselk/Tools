cart = {}
action = input('What do you want to do your cart? ')


def add_item():
    item = input('What item do you want to buy? ')
    num = int(input('How many of this item do you need? '))
    cart[item] = num


def remove_item():
    obj = input('What item to remove? ')
    #quant = int(input('How many of this item do you need to remove? '))
    del cart[obj]


def main():
    while action != 'save':
        if action == 'add':
            add_item()
        elif action == 'remove':
            remove_item()


main()
