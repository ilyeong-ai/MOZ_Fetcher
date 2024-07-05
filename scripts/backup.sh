# MongoDB backup
mongodump --uri $MONGODB_URI --out /backup/mongodb_$(date +%Y%m%d_%H%M%S)

# Redis backup
redis-cli save
cp /data/dump.rdb /backup/redis_$(date +%Y%m%d_%H%M%S).rdb

# RabbitMQ backup
rabbitmqctl export_definitions /backup/rabbitmq_$(date +%Y%m%d_%H%M%S).json