# -*- coding: utf-8 -*-

import json

filePath = r'D:\OneDrive\python\DB_library\flask_library\APP\blueprints\books.json'
with open(filePath, encoding='utf-8') as f:
    js = json.load(f)
    print(js[1])

for book in js:
    # b = Book()
    # b.bName = book['name']
    # b.ISBN = book['ISBN']
    # b.author = book['author']
    # b.publicationDate = book['date'] + '-1'
    # b.press = book['press']
    # b.sum = 10
    # b.currNum = 10
    # b.price = book['price']
    # b.score = book['score']
    # b.link = book['link']
    # b.page = book['page']
    # db.session.add(b)
    print(book['ISBN'])
