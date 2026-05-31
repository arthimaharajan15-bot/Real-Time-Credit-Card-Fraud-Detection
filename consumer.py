import json
import pickle
import numpy as np
from kafka import KafkaConsumer

# Load the trained machine learning model from pickle file
with open('fraud_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Initialize Kafka Consumer to listen to the real-time transaction stream
# Fixed configuration error by changing value_serializer to value_deserializer
consumer = KafkaConsumer(
    'ml-transactions',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Kafka Consumer is ready... Monitoring live transactions...")

# Continuously fetch and process incoming messages from the stream
for message in consumer:
    transaction = message.value
    
    # Drop the target label 'Class' if it exists in the incoming stream data
    if 'Class' in transaction:
        del transaction['Class']
        
    # Extract values and reshape the array to match model input requirements
    input_data = np.array(list(transaction.values())).reshape(1, -1)
    
    # Perform real-time inference using the trained model
    prediction = model.predict(input_data)[0]
    
    # Output the prediction results dynamically
    if prediction == 1:
        print(f"⚠️ ALERT: Fraudulent Transaction Detected! Amount: {transaction['Amount']}")
    else:
        print(f"✅ SUCCESS: Genuine Transaction Approved. Amount: {transaction['Amount']}")