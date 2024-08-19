from collections import ChainMap


dict1: dict = {'data': 1, 'structure': 2}

dict2: dict = {'python': 3, 'language': 4}

dict3: dict = {'django': 3, 'language': 5}


if __name__ == '__main__':
    chain = ChainMap(dict1, dict2, dict3)
    print(list(chain.keys()))
    print(list(chain.values()))
    print(chain)
    print(chain['data'])
    print(chain['language'])
