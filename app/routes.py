from flask import Blueprint, jsonify

books_bp = Blueprint("books", __name__, url_prefix="/books")

# temporary hard-coded instances
class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Harry Potter", "A boy with glasses is a wizard and goes to school."),
    Book(2, "And Then There Were None", "10 people go to an island. Then they start dropping like flies."),
    Book(3, "Tidying Up", "This is your chance to declutter and truly appreciate the items that spark joy.")
]

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)