# example from flask_restx website
api.py and hello.py

## test request:
curl http://127.0.0.1:5000/hello
curl http://127.0.0.1:5000/todo1 -d "data=Remember the milk" -X PUT
curl http://127.0.0.1:5000/todo1
curl http://127.0.0.1:5000/todo2 -d "data=Remember the tea" -X PUT
curl http://127.0.0.1:5000/todo2

# example from tube 
file: app.py
resource url: https://www.youtube.com/watch?v=-XuS0cfkvuA

# create db
```
(python38) D:\practice2022\flaskwithswagger>flask shell
D:\practice2022\flaskwithswagger
Python 3.8.13 (default, Mar 28 2022, 06:59:08) [MSC v.1916 64 bit (AMD64)] on win32
App: app [production]
Instance: D:\practice2022\flaskwithswagger\instance
>>> db
<SQLAlchemy engine=sqlite:///D:\practice2022\flaskwithswagger\books.db>
>>> Book
<class 'app.Book'>
>>> db.create_all()
2022-05-02 23:05:02,486 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-05-02 23:05:02,486 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("book")
2022-05-02 23:05:02,487 INFO sqlalchemy.engine.Engine [raw sql] ()
2022-05-02 23:05:02,488 INFO sqlalchemy.engine.Engine COMMIT
>>>
>>> new_book=Book(title='Django for beginners', author='W S Vincent')
>>> new_book2=Book(title='Java', author='Jonathan')
>>> db.session.add(new_book)
>>> db.session.add(new_book2)
>>> db.session.commit()
2022-05-02 23:06:33,197 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-05-02 23:06:33,200 INFO sqlalchemy.engine.Engine INSERT INTO book (title, author, date_added) VALUES (?, ?, ?)
2022-05-02 23:06:33,200 INFO sqlalchemy.engine.Engine [generated in 0.00073s] ('Django for beginners', 'W S Vincent', '2022-05-02 15:04:38.166398')
2022-05-02 23:06:33,226 INFO sqlalchemy.engine.Engine INSERT INTO book (title, author, date_added) VALUES (?, ?, ?)
2022-05-02 23:06:33,227 INFO sqlalchemy.engine.Engine [cached since 0.02778s ago] ('Java', 'Jonathan', '2022-05-02 15:04:38.166398')
2022-05-02 23:06:33,228 INFO sqlalchemy.engine.Engine COMMIT
>>> books=Book.query.all()
2022-05-02 23:06:48,591 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-05-02 23:06:48,594 INFO sqlalchemy.engine.Engine SELECT book.id AS book_id, book.title AS book_title, book.author AS book_author, book.date_added AS book_date_added
FROM book
2022-05-02 23:06:48,595 INFO sqlalchemy.engine.Engine [generated in 0.00039s] ()
>>> books
[Django for beginners, Java]

```
## test request
curl http://127.0.0.1:5000/books