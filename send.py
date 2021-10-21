#!/usr/bin/env python
import pika

# Part 1 - Connect to rabbitmq
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Part 2 - Create channel to send and receive msg on 
channel.queue_declare(queue='hello')

# Part 3 - Send to a exchange
for i in range(100):
    msg = 'Hello World!=?!=!'
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=msg)
    print(" [x] Sent {msg1}".format(msg1=msg))
    # Good practice to close channel. (Maybe TCP socket closing?)
connection.close()