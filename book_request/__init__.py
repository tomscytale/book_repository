from flask import Flask
from flask_mongoengine import MongoEngine


db = MongoEngine()


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['MONGODB_DB'] = 'library'
    # comment out this line if not running in a container
    app.config['MONGODB_HOST'] = 'mongo'
    app.config['SECRET_KEY'] = '<replace with a secret key>'
    db.init_app(app)

    @app.route('/test')
    def test():
        return 'test'

    from . import book_request
    app.register_blueprint(book_request.bp)

    return app

