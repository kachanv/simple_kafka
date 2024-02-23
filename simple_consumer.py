from confluent_kafka import Consumer, KafkaError, KafkaException

my_consumer_config = {
    'brokers': 'localhost:29092,localhost:29093',
    'consumer_group': 'my_group',
    'autoreset_policy': 'earliest',
    'protocol': 'PLAINTEXT'
}


def init_consumer(config: dict) -> Consumer:
    return Consumer({
        'bootstrap.servers': config['brokers'],
        'group.id': config['consumer_group'],
        'auto.offset.reset': config['autoreset_policy'],
        'security.protocol': config['protocol']
    })


def simple_consumer(consumer: Consumer, topic: str, message_count_limit: int = 20) -> bool:
    consumer.subscribe([topic])
    print('Reading topic: ' + topic)

    for _ in range(message_count_limit):
        msg = consumer.poll(timeout=2.5)
        if msg is None:
            print("Message is None | info: {}".format(consumer.position(consumer.assignment())))
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('%% %s [%d] reached end at offset %d\n' % (msg.topic(), msg.partition(), msg.offset()))
            elif msg.error():
                consumer.close()
                raise KafkaException(msg.error())
        else:
            print('read topic: {} | partition: {} | offset: {} | value: {}'.format(msg.topic(),
                                                                                   msg.partition(),
                                                                                   msg.offset(),
                                                                                   msg.value().decode('utf-8')))
    consumer.close()
    return True


#c = init_consumer(config=my_consumer_config)
#simple_consumer(consumer=c, topic='MyTestTopic2')
