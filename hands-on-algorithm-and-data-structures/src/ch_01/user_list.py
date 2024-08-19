from collections import UserList


class MyList(UserList):

    def push(self, key):
        raise RuntimeError('cannot insert in the list!')


if __name__ == '__main__':
    d = MyList([11, 12, 13, 14])
    d.push(2)
