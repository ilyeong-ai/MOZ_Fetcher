#!/bin/bash

# MongoDB restore
mongorestore --uri $MONGODB_URI /backup/mongodb_$1

# Redis restore
systemctl stop redis
rm /data/dump.rdb
cp /backup/redis_$1.rdb /data/dump.rdb
systemctl start redis

# RabbitMQ restore
rabbitmqctl stop_app
rabbitmqctl reset
rabbitmqctl start_app
rabbitmqctl import_definitions /backup/rabbitmq_$1.json