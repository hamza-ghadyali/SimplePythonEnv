# Amortize a 5% loan of $1000 with 10 annual payments of $90
from itertools import accumulate, repeat
account_update = lambda bal, pmt: round(bal * 1.05) + pmt

r = list(accumulate(repeat(-90,10), account_update, initial=1000))

print(r)