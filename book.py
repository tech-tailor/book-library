#!/usr/bin/env bash
# book module
import json

class Book:

    def __init__(self, author, title, isbn=None):
        self.author = author
        self.title = title
        self.isbn =  isbn

    
    # def __str__(self):
        # return f"{self.title, self.author, self.ISBN}"
    
    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn
        }
    
class Library:
    _file = 'file.json'

    def __init__(self):
        self.books = []
        self.load_data()


    def load_data(self):
        try:
            with open('file.json', 'r', encoding="utf-8") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            pass

    def save(self):
        with open('file.json', 'w', encoding="utf-8") as f:
            json.dump(self.books, f, indent=3)

    def add_book(self, book):
        self.books.append(book.to_dict())
        self.save()
        title = book.to_dict()['title']
        return f"'{title}' book is now added"

    def display_all(self):
        return self.books
    
    def display_book(self, title=None, author=None, isbn=None):
        for book in self.books:
            if book['title'] == title or book['author'] == author:
                return book
        return 'Not match'

    def total_books(self, title=None, author=None, isbn=None):
        no_of_books = 0
        for book in self.books:
            if book['title'] == title:
                no_of_books += 1
                return book
        return 'Not match'
            
    def delete_all(self):
        self.books.clear()
        self.save()
        return 'the list of book is empty'

            
