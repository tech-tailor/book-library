#!/usr/bin/env bash
# book module
import json

class Book:

    def __init__(self, author, title, ISBN=None):
        self.author = author
        self.title = title
        self.ISBN =  ISBN

    
    def __str__(self):
        return f"{self.title, self.author, self.ISBN}"
    
    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'ISBN': self.ISBN
        }
    
    class Library:
        _file = 'file.json'

        def __init__(self):
            self.books = []


        def load_data(self):
            with open('file.json', 'r,', encoding="utf-8") as f:
                json.load(self.books, f)

                
            
