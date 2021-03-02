# https://docs.python.org/3/library/datetime.html
from datetime import datetime


orbiter_start = datetime(2020, 2, 10, 5, 3)
print(orbiter_start.isoweekday())

cas_od_startu = datetime.now() - orbiter_start
print(type(cas_od_startu))
print(cas_od_startu)
