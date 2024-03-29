from confluent_kafka import Producer
import socket

my_producer_config = {
        'brokers': 'host1:9092,host2:9092',
        'client.id': 'my_client',
        'protocol': 'PLAINTEXT',
        
       }

producer = Producer(conf)

producer.produce(topic, key="key", value="value")


def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

producer.produce(topic, key="key", value="value", callback=acked)

# Wait up to 1 second for events. Callbacks will be invoked during
# this method call if the message is acknowledged.
producer.poll(1)


#TODO
# есть .csv файлы в которых с разделителем ; лежат данные: key;value
# нужно в цикле вычитать и асинхронно отправить в kafka топик с семантикой доставки в брокер at least once
# key и value сериализовать StringSerializer
