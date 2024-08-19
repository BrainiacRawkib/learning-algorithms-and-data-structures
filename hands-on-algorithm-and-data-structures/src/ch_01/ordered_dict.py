from collections import OrderedDict


ord_dict = OrderedDict({
    'a': 1, 'b': 2, 'd': 4, 'e': 5, 'c': 3, 'f': 6
})

ord_dict['g'] = 7


if __name__ == '__main__':
    print(ord_dict)
