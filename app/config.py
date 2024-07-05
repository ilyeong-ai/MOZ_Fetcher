import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB = os.getenv("MONGODB_DB")
REDIS_URL = os.getenv("REDIS_URL")
RABBITMQ_URL = os.getenv("RABBITMQ_URL")
SENTRY_DSN = os.getenv("SENTRY_DSN")
EVM_RPC_URL = os.getenv("EVM_RPC_URL")
TETHER_CONTRACT_ADDRESS = os.getenv("TETHER_CONTRACT_ADDRESS")
SECRET_KEY = os.getenv("SECRET_KEY")
PROMETHEUS_PORT = int(os.getenv("PROMETHEUS_PORT", 9090))

if not all([MONGODB_URI, MONGODB_DB, REDIS_URL, RABBITMQ_URL, SENTRY_DSN, EVM_RPC_URL, TETHER_CONTRACT_ADDRESS, SECRET_KEY]):
    raise ValueError("Missing required environment variables. Please check your .env file.")