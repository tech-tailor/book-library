#!/usr/bin/python3
# test every code i write

print('start')

from book import Book, Library

b = Book('Akin', 'how to code', 873786378)

l = Library()

add_book = l.add_book(b)
print(add_book)
k = Library()
d = k.display_book(title='how code')
print(d)
#l.delete_all()
print()

# print(k)
