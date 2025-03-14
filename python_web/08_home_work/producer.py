import pika
from faker import Faker
from models import Users

class Producer:
    def __init__(self):
        self.credentials = pika.PlainCredentials('guest', 'guest')
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost', port=5672, credentials=self.credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='email')
        self.channel.queue_declare(queue='phone')
        self.faker = Faker('en_GB')


    def generate(self, n:int=20):
        for i in range(n):
            user = Users(name=self.faker.name(), email=self.faker.email(), phone_number=self.faker.phone_number(),
                         preferred_method=self.faker.random_element(elements=("email", "phone")))
            user.save()
        print(f"Generated {n} users")

    def send(self):
        users:list[Users] = Users.objects(is_send=False) # пошук юзера
        print(len(users))
        for user in users:
            self.channel.basic_publish(exchange='', routing_key=user.preferred_method, body=str(user.pk).encode())

        # self.connection.close()
def main():
    producer = Producer()
    producer.generate(5)
    producer.send()

if __name__ == '__main__':
    main()
