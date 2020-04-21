FROM mongo
COPY dump/ /tmp/dump
CMD mongod --fork --logpath /var/log/mongodb.log; \
    mongorestore --drop /tmp/dump/; \
    mongod --shutdown; \
    docker-entrypoint.sh mongod
