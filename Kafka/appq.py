from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

topic = 'foobar'

for i in range(10):
    message = f'Messaggio {i}'
    producer.send(topic, message.encode('utf-8'))
    print(f'Inviato: {message}')
    time.sleep(1)

producer.flush()
producer.close()
