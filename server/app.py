from config import app, db, request, jsonify
from models import *
# import uuid

# configuration
DEBUG = True
# BOOKS = [
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'On the Road',
#         'author': 'Jack Kerouac',
#         'read': True
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Harry Potter and the Philosopher\'s Stone',
#         'author': 'J. K. Rowling',
#         'read': False
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Green Eggs and Ham',
#         'author': 'Dr. Seuss',
#         'read': True
#     }
# ]

# instantiate the app
# app = Flask(__name__)
# app.config.from_object(__name__)

# enable CORS
# CORS(app)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        db.session.add(Books(**post_data))
        db.session.commit()
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = get_posts()
    return jsonify(response_object)

@app.route('/books/<int:book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    mess = ''
    response_object = {'status': 'success'}
    i = db.session.query(Books).get(book_id)
    if request.method == 'PUT':
        post_data = request.get_json()
        # i.title = post_data.get('title')
        # i.author = post_data.get('title')
        # i.read = post_data.get('read')
        i.set(post_data)
        db.session.add(i)
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        if(i):
            db.session.delete(i)
            mess = 'Book removed!'
        else:
            mess = 'Not found book'
        response_object['message'] = mess
    db.session.commit()
    return jsonify(response_object)


def get_posts():
    arr = []
    with app.app_context():
        for book in db.session.query(Books).order_by(Books.id).all():
            arr.append(book.get())
        return arr

if __name__ == '__main__':
    app.run(host="localhost", port=8070, debug=False)
