import pika
import time

# Connect to RabbitMQ server (replace 'localhost' with the RabbitMQ server hostname if needed)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='hello_queue', durable=True)

# Define the number of messages to send
num_messages = 200

# Send messages to the queue
for i in range(num_messages):
    message = f"Message {i+1}"
    channel.basic_publish(exchange='', routing_key='hello_queue', body=message, properties=pika.BasicProperties(delivery_mode=2))
    print(f" [x] Sent '{message}'")
    time.sleep(1)  # Sleep for 1 second between messages

# Close the connection
connection.close()
