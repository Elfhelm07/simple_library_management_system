from flask import Flask, request, jsonify
from models import Book, Member
from auth import token_required
from utils import paginate

app = Flask(__name__)

books = []
members = []

@app.route('/books', methods=['POST'])
@token_required
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'])
    books.append(new_book)
    return jsonify({"message": "Book added successfully!"}), 201

@app.route('/books', methods=['GET'])
@token_required
def get_books():
    title = request.args.get('title')
    author = request.args.get('author')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    filtered_books = [
        book for book in books 
        if (title is None or title in book.title) or (author is None or author in book.author)
    ]
    
    paginated_books = paginate(filtered_books, page, per_page)

    return jsonify({
        "books": [{"title": book.title, "author": book.author} for book in paginated_books],
        "total": len(filtered_books),
        "page": page,
        "per_page": per_page
    })

@app.route('/members', methods=['POST'])
@token_required
def add_member():
    data = request.json
    new_member = Member(name=data['name'])
    members.append(new_member)
    return jsonify({"message": "Member added successfully!"}), 201

@app.route('/members', methods=['GET'])
@token_required
def get_members():
    return jsonify([{"name": member.name} for member in members])

if __name__ == '__main__':
    app.run(debug=True)