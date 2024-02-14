#!/usr/bin/python3
# test every code i write

print('start')

from book import Book

b = Book('made easy physics', 'Akintola')
b.category = 'school book'
print(b.__dict__)
print()
print(b.to_dict())
# print(k)
