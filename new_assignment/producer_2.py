from kafka import KafkaProducer
import json
from data import get_registered_user
import time
import argparse
import couchdb

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--topic', default='registered_user', help='publisher topic and couchdb document name; default registered_user')
    args = parser.parse_args()
    return args

producer = KafkaProducer(bootstrap_servers='54.158.65.224:9092,3.217.42.101:9092',
                         value_serializer=json_serializer)

if __name__ == "__main__":
    parsed_args = parse_args()

    try:
        couch = couchdb.Server('http://54.158.65.224:5984/')
        couch.resource.credentials = ('admin', 'Mygrade9')
        db = couch[parsed_args.topic]
    except:
        db = couch.create(parsed_args.topic)

    while True:
        
        registered_user = get_registered_user()
        print(registered_user)
        producer.send(parsed_args.topic, registered_user)
        time.sleep(5)


