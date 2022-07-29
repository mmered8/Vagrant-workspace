from kafka import KafkaConsumer
import json
import couchdb  # importing couchdb  
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--topic', default='registered_user', help='publisher topic and couchdb document name; default registered_user')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    parsed_args = parse_args()
    consumer = KafkaConsumer(
        parsed_args.topic,
        bootstrap_servers='54.158.65.224:9092,3.217.42.101:9092',
        group_id = None
        # group_id=f'consumer-group-{parsed_args.topic}'
        )
    print("starting the consumer")

    couch = couchdb.Server('http://admin:Mygrade9@54.158.65.224:5984')

    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value)))
        # db = couch[f'{parsed_args.topic}']
        db = couch[parsed_args.topic]
        print(db.name)
        doc = msg
        print(doc)
        db.save(json.loads(msg.value))
        print("Saved registered User = {}".format(json.loads(msg.value)))


