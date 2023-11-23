# Задача 8
# Компанії платять податки. При чому розмір податку, найчастіше залежить від прибутку (податок на прибуток). Припустимо
# гіпотетично, що якщо прибуток компанії склав до 100000 (сто тисяч), компанія повинна заплатити 5% від нього,
# якщо прибуток до 1000000 (мільйон), податок становить 8%, якщо виторг більший за 10000000 (десять мільйонів),
# компанія платить 15% податок. Використовуйте функцію з сьо завдання, щоб порахувати, який буде прибуток компанії
# після сплати податків

MASTER_WORK = 75
HUNDRED_PAPER_PRICE = 120
INK_PRICE = 20

TAX_MIN = 0.05
TAX_MID = 0.10
TAX_MAX = 0.15


def profit(p, n):
    if n % 100 != 0:
        return 'Error, not devide by 100'

    hundreds = n // 100
    return n * p - hundreds * (MASTER_WORK + HUNDRED_PAPER_PRICE + INK_PRICE)


def profit_after_tax(p, n):
    profit_before_tax = profit(p, n)
    if profit_before_tax < 1000_000:
        return profit_before_tax * (1 - TAX_MIN)
    elif profit_before_tax < 1_000_000:
        return profit_before_tax * (1 - TAX_MID)
    else:
        return profit_before_tax * (1 - TAX_MAX)


print(profit(2.5, 500000))
print(profit(2.5, 5000000))
