from collections import UserDict


class MyDict(UserDict):

    def push(self, key, value):
        raise RuntimeError('cannot insert!')


if __name__ == '__main__':
    d = MyDict({'ab': 1, 'bc': 2, 'cd': 3})
    d.push('ef', 5)
