import pika
import sys
from producer import Producer
from models import Users

class Consumer(Producer):
    def receive(self):
        self.channel.basic_consume(queue='phone', on_message_callback=self.callback, auto_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body): # pk це наша айдішка
        # print(f" [x] Received {ch}")
        # print(f" [x] Received {method}")
        # print(f" [x] Received {properties}") закоментував щоб було чистіше в консолі
        print(f" [x] Received {body}")
        self.mark_as_send(pk=body)

    def mark_as_send(self, pk:bytes):
        user:Users = Users.objects(pk=pk.decode()).first() # знайшли юзера
        print(user)
        user.is_send=True
        user.save()

def main():
    consumer = Consumer()
    consumer.receive()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
