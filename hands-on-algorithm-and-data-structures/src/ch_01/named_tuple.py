from collections import namedtuple


Book = namedtuple('Book', ['name', 'ISBN', 'quantity'])

book1 = Book("Hands on Data Structures", "9781788995573", 50)


if __name__ == '__main__':
    print(f'Using index ISBN: {book1[1]}')
    print(f'Using key ISBN: {book1.ISBN}')
