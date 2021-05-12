from kafka import KafkaProducer, KafkaConsumer
from kafka.errors import kafka_errors
import traceback
import json

def consumer_demo():
    # consumer = KafkaConsumer(
    #     'kafka_demo',
    #     bootstrap_servers='localhost:9092',
    #     group_id='test'
    # )
    consumer = KafkaConsumer(
        'kafka_demo',
        sasl_mechanism='PLAIN',
        security_protocol='SASL_PLAINTEXT',
        sasl_plain_username='admin',
        sasl_plain_password='admin',
        bootstrap_servers=['192.168.90.21:9092'],
        group_id='test')
    for message in consumer:
        print("receive, key: {}, value: {}".format(
            json.loads(message.key.decode()),
            json.loads(message.value.decode())
            )
        )

consumer_demo()