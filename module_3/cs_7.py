MASTER_WORK = 75
HUNDRED_PAPER_PRICE = 120
INK_PRICE = 20

def profit(p, n):
    if n % 100 != 0:
        return 'Error, not devide by 100'

    hundreds = n // 100
    return n * p - hundreds * (MASTER_WORK + HUNDRED_PAPER_PRICE + INK_PRICE)

print(profit(2.5, 1000))
print(profit(5, 2567))