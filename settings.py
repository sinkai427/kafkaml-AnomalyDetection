import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DELAY = 0.1

KAFKA_BROKER = "localhost:9092"
TRANSACTIONS_TOPIC = "transactions"
TRANSACTIONS_CONSUMER_GROUP = "transactions"
ANOMALIES_TOPIC = "anomalies"
ANOMALIES_CONSUMER_GROUP = "anomalies"

SLACK_API_TOKEN = os.environ.get("SLACK_API_TOKEN")
SLACK_CHANNEL = "anomalies-alerts"
