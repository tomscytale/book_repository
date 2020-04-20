import book_request

if __name__ == '__main__':
    app = book_request.create_app()
    app.run(host='0.0.0.0')
