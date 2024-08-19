from collections import UserString


class MyString(UserString):

    def append(self, value):
        self.data += value


if __name__ == '__main__':
    s = MyString('data')
    print(f'Original: {s}')
    s.append(' x2 x3')
    print(f'After append: {s}')
