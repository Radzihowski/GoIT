# Структурні патерни
#
# Фасад (Facade)
# Паттерн проектування, який надає простий інтерфейс до складної системі класів, бібліотеки або фреймворку.

# Паттерн вирішує проблему, коли бізнес-логіка ваших класів тісно починає переплітатися з деталями реалізації сторонніх
# бібліотек. Код стає заплутаним, а заплутаний код стає важче підтримувати. Для таких цілей і використовують патерн Фасад.
# Простими словами, всю складну логіку ми ховаємо за простим інтерфейсом.

# Прикладом може бути замовлення в інтернет-магазині. У вас є фасад – це сайт, на якому ви робите замовлення. Від вас
# захована вся функціональність, ви не телефонуєте на склад, не виписуєте накладну тощо. Все просто – є фасад сайту,
# де мінімум необхідного функціоналу для роботи.

# Якщо коротко підбити підсумок – ми використовуємо патерн Фасад, замість прямої роботи з об'єктами складної форми.
class FacadeNewsLetter:
    def __init__(self, users_system, email_system) -> None:
        self._users_system = users_system
        self._email_system = email_system

    def sending(self) -> str:
        users = self._users_system.get_users()
        male, female = self._users_system.separate_users(users)
        text_for_male = self._email_system.get_text_email("male")
        text_for_female = self._email_system.get_text_email("female")
        self._email_system.send_emails(male, text_for_male)
        self._email_system.send_emails(female, text_for_female)
        return "Done"

class UserSystem:
    def get_users(self) -> list:
        users = [
            {
                "name": "Allen Raymond",
                "email": "nulla.ante@vestibul.co.uk",
                "gender": "male",
            },
            {
                "name": "Chaim Lewis",
                "email": "dui.in@egetlacus.ca",
                "gender": "male",
            },
            {
                "name": "Kennedy Lane",
                "email": "mattis.Cras@nonenimMauris.net",
                "gender": "female",
            },
            {
                "name": "Wylie Pope",
                "email": "est@utquamvel.net",
                "gender": "female",
            }
        ]
        return users

    def separate_users(self, users) -> tuple:
        male = []
        female = []
        for person in users:
            if person.get("gender", None) == "male":
                male.append(person)
            else:
                female.append(person)
        return male, female

class EmailSystem:
    def get_text_email(self, gender) -> str:
        text = "Default text"
        if gender == "male":
            text = "Male text email"
        if gender == "female":
            text = "Female text email"
        return text

    def send_emails(self, users, text) -> str:
        for person in users:
            print(f"Send {person.get('name')} email: {text}")
        return "Done"

def client_code(newsletter) -> None:
    print(newsletter.sending(), end="")

if __name__ == "__main__":
    facade = FacadeNewsLetter(UserSystem(), EmailSystem())
    client_code(facade)

# Виведення:
# Send Allen Raymond email: Male text email
# Send Chaim Lewis email: Male text email
# Send Kennedy Lane email: Female text email
# Send Wylie Pope email: Female text email
# Done