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
        bootstrap_servers='54.205.194.42:9092,44.199.112.155:9092',
        group_id = None
        # group_id=f'consumer-group-{parsed_args.topic}'
        )
    print("starting the consumer")

    couch = couchdb.Server('http://admin:Mygrade9@54.205.194.42:5984')

    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value)))
        db = couch[parsed_args.topic]
        print(db.name)
        doc = msg
        print(doc)
        db.save(json.loads(msg.value))
        print("Saved registered User = {}".format(json.loads(msg.value)))


