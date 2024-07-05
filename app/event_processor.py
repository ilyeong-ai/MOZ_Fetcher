import json
import logging
from app.database import events_collection
from app.blockchain import get_transfer_events
import redis
import pika
from app.config import REDIS_URL, RABBITMQ_URL
from app.monitoring import EVENTS_PROCESSED, TimerContextManager
from app.error_handler import CustomException

import socket
socket.gethostbyname("")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

redis_client = redis.Redis.from_url(REDIS_URL)

connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
channel = connection.channel()
channel.queue_declare(queue='tether_events')

def process_events(from_block, to_block):
    try:
        with TimerContextManager():
            events = get_transfer_events(from_block, to_block)
            for event in events:
                event_data = {
                    'from': event['args']['from'],
                    'to': event['args']['to'],
                    'value': event['args']['value'],
                    'block_number': event['blockNumber'],
                    'transaction_hash': event['transactionHash'].hex()
                }
                
                events_collection.insert_one(event_data)
                redis_client.set(f"event:{event['transactionHash'].hex()}", json.dumps(event_data))
                channel.basic_publish(exchange='',
                                      routing_key='tether_events',
                                      body=json.dumps(event_data))
                
                logger.info(f"Processed event: {event_data}")
                EVENTS_PROCESSED.inc()
    except Exception as e:
        logger.error(f"Error processing events: {str(e)}")
        raise CustomException(status_code=500, detail=f"Failed to process events: {str(e)}")