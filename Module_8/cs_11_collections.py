import collections

bank = (2234, 789, 176)
print(type(bank), bank)
print(bank[2])

Bank = collections.namedtuple('Bank', ['cash', 'percentage', 'NMT'])
bank_col = Bank(cash=2233, percentage=788, NMT=175)
bank_cols = Bank(223, 175, 788)
print(bank_cols)
print(type(bank_col), bank_col)
print(bank_col.cash, bank_col.NMT, bank_col.percentage, sep='\t')