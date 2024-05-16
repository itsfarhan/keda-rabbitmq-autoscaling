import pika

# Connect to RabbitMQ server (replace 'localhost' with the RabbitMQ server hostname if needed)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a durable queue named 'hello_queue' (matching the existing queue settings)
channel.queue_declare(queue='hello_queue', durable=True)

# Send 'Hello, world!' message to the queue 50 times
for _ in range(50):
    channel.basic_publish(exchange='', routing_key='hello_queue', body='Hello, world!', properties=pika.BasicProperties(delivery_mode=2))
    print(" [x] Sent 'Hello, world!'")

# Close the connection
connection.close()
