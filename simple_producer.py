import csv
from confluent_kafka import Producer, SerializingProducer
from confluent_kafka.serialization import StringSerializer

my_producer_config = {
    'brokers': 'localhost:29092,localhost:29093',
    'client.id': 'my_client',
    'protocol': 'PLAINTEXT',
    'acks': 'all'
}


def init_producer(config: dict) -> Producer:
    return SerializingProducer({
        'bootstrap.servers': config['brokers'],
        'client.id': config['client.id'],
        'security.protocol': config['protocol'],
        'acks': config['acks'],
        'key.serializer': StringSerializer('utf-8'),
        'value.serializer': StringSerializer('utf-8')
    })


# function read file:
# key_1;value_1
# key_2;value_2
# key_3;value_3
def read_file(file_name: str) -> list:
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            try:
                yield row
            except IndexError:
                continue


# callback function
def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


# simple async producer
def simple_producer(producer: Producer, file_name: str, topic: str) -> bool:
    for row in read_file(file_name):
        # put roes into delivery buffer
        producer.produce(topic, key=row[0], value=row[1], on_delivery=acked)
        # get a callback
        producer.poll(1)
    # waiting for delivery
    producer.flush()
    return True


simple_producer(producer=init_producer(my_producer_config), file_name='my_test_data.csv', topic='MyTestTopic2')
