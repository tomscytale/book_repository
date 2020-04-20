from flask import Blueprint, abort, jsonify, make_response, request as http_request
import mongoengine

from .documents import Book, Request

bp = Blueprint('book_request', __name__, url_prefix='/request')


def format_request(req):
    return {
        "email": req.email,
        "title": req.book.title,
        "id": str(req.id),
        "timestamp": req.timestamp,
    }


def jsonify_request(req):
    return jsonify(format_request(req))


def jsonify_requests(requests):
    return jsonify([format_request(x) for x in requests])


def json_abort(message="Invalid data", code=400):
    return abort(make_response(jsonify({"message": message}), code))


@bp.route('/', methods=['GET', 'POST'])
def request_book():
    if http_request.method == 'GET':
        return jsonify_requests(Request.objects.all())

    elif http_request.method == 'POST':
        if not http_request.json or 'title' not in http_request.json or 'email' not in http_request.json:
            json_abort('Request must include "email" and "title"')

        title = http_request.json['title']
        email = http_request.json['email']

        try:
            book = Book.objects.get(title=title)
        except Book.DoesNotExist:
            json_abort(f'could not find the book with the title "{title}"', 404)

        book_request = Request(email=email, book=book)

        try:
            book_request.save()
        except mongoengine.errors.NotUniqueError:
            json_abort(f'There is already a request from the user {email} for the book "{title}"')
        except mongoengine.errors.ValidationError as e:
            json_abort(str(e.errors))

        return jsonify_request(book_request)


@bp.route('/<id>', methods=['GET', 'DELETE'])
def request_by_id(id):
    try:
        request = Request.objects.get(id=id)
    except (Request.DoesNotExist, mongoengine.errors.ValidationError):
        json_abort(f"could not find a request with id {id}", 404)

    if http_request.method == 'GET':
        return jsonify_request(request)
    elif http_request.method == 'DELETE':
        request.delete()
        return jsonify(success=True)
