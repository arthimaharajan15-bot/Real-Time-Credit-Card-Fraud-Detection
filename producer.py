import pandas as pd
import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Kafka Producer is ready! Starting data stream...")

df = pd.read_csv('creditcard.csv')

for index, row in df.iterrows():
    transaction_data = row.to_dict()
    
    producer.send('ml-transactions', value=transaction_data)
    
    print(f"Transaction {index} அனுப்பியாச்சு!")
    time.sleep(1) 