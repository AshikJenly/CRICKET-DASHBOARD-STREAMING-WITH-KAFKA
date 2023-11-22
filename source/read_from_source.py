from confluent_kafka import Consumer, KafkaError
import json
import time
import threading

conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'cricket_group_a',
    'auto.offset.reset': 'earliest',
    'enable.auto.commit': True,
    'auto.commit.interval.ms': 1000,
}

consumer = Consumer(conf)
consumer.subscribe(['mysql_live_cricket_match_data_live'])


shared_data = []

def get_data(shared_data):
    try:
        print("Started consuming")
        while True:
            msg = consumer.poll(1)
            if msg is None:
                print("waiting")
                continue
            elif msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            else:
                byte_data = msg.value()
                str_data = byte_data.decode('utf-8')
                my_dict = json.loads(str_data)
                payload = my_dict["payload"]
                shared_data.append(payload)
                print("appending")
    except KeyboardInterrupt:
        consumer.close() 
    finally:
        print("closed consumer")
        consumer.close()

# Start Kafka consumer thread
consumer_thread = threading.Thread(target=get_data, args=(shared_data,))
consumer_thread.start()