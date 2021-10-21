#!/usr/bin/env python
import pika
def main():
    
    # Part 1 - Connect to rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Part 2 - Check the channel exist with the command declare. It does not create multiple, is "indempotent"
    channel.queue_declare(queue='hello')

    
    def callback(ch, method, properties, body):
        # function to be called from by the rabbitmq SKD library. 
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)