from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


gapp = Flask('Books')
gapp.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db = SQLAlchemy(gapp)
migrate = Migrate(gapp, db)

# books = [
#     {'name': 'book_1',
#      'author': 'author_1',
#      'read': True,
#      'id':0},
#     {'name': 'book_2',
#      'author': 'author_2',
#      'read': True,
#      'id':1},
#     {'name': 'book_3',
#      'author': 'author_3',
#      'read': True,
#      'id':2}
#     ]

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    author = db.Column(db.String(500))
    read = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Book {self.id} / <i>{self.name}</i> / <i>{self.author}</i>'
    
    
@gapp.route('/')
def main():
    books = Book.query.all()
    print(books)
    return render_template('index.html',
                            books_list=books)


@gapp.route('/read/<int:book_id>', methods=['PATCH'])
def modify_book(book_id):
    book = Book.query.get(book_id)
    book.read = request.json['ready']
    db.session.commit()
    # global books
    # read = request.json['ready']
    # for book in books:
    #     if book['id'] == book_id:
    #         book.update({'read': read})
    return 'Ok'


@gapp.route('/book', methods=['POST'])
def create_book():
    data = request.json
    book = Book(**data)
    db.session.add(book)
    db.session.commit()
    # last_id = books[-1]['id']
    # new_id = last_id + 1 
    # data['id']= new_id 
    # books.append(data)
    return 'Ok'

if __name__ == '__main__':
    with gapp.app_context():
        db.create_all()
    gapp.run(debug=True)