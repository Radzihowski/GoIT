def greeting(variable):
    print(f"Function gretting with variable {variable}")


def bot(func):
    def inner(*args, **kwargs):
        print('Hello')
        result = func(*args, **kwargs)
        print('Goodbye')
        return result
    return inner

greeting('Bots')

bot_says = bot(greeting)
bot_says('Bot')
print(bot_says('Bot'))