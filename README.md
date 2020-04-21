running from command line: 


running from docker:

```
docker build -t mongo mongo
docker build -t book_request .
docker-compose up
```

comment out the following line in `book_request/__init__.py`

(should really use a different config file for docker, or detect environment or something)

```
    app.config['MONGODB_HOST'] = 'mongo'
```

then run
```
cd book_request
FLASK_ENV=development FLASK_APP=. flask run
```
