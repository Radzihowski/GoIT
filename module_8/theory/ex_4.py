import json

class UserManagerSystem:
    def __init__(self, json_file, database_file):
        self.database_file = database_file

    def load_users(self):
        user = self.load_users()
        try:
            with open(self.database_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_user(self, users):
        with open(self.database_file, 'w', encoding='utf-8') as file:
            json.dump(users, file)

    def add_user(self, user):
        user = self.load_users()
        user.append(user)
        self.save_user(users)
        print('User was added')

    def view_users(self):
        users = self.load_users()
        if users:
            print('List of users')
            for user in users:
                print(user)
        else:
            print('User not found')

    def delete_ser(self, user_id):
        user = self.load_users()
        for user in users:
            if user['id'] == user_id:
                users.remove(user)
                print('')
                self.save_user(users)
                return
        print(f'User with if not found', format(user_id))

    def clean_users(self):
        pass

if __name__ == '__main__':
    user_managment = UserManagerSystem('users.json')

    user_managment.add_user({'id': 1, 'name': 'Iavan', 'email': 'aasdfa@gmail@com' })