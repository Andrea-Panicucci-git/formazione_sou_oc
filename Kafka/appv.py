from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'foobar',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # legge dall'inizio del topic
    group_id='my-group'            # identificatore del gruppo consumer
)

print("In ascolto sul topic 'foobar'...")

for message in consumer:
    print(f"Ricevuto: {message.value.decode('utf-8')}")
