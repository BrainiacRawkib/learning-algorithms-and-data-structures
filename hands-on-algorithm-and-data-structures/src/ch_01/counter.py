from collections import Counter


inventory = Counter('hello!')

c = Counter({'a': 4, 'b': 2})

if __name__ == '__main__':
    print(inventory)
    print(inventory['h'])
    print(inventory['l'])
    print(c)
