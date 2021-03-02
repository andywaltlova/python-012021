# https://docs.python.org/3/library/datetime.html
from datetime import datetime, timedelta

cas_objednavky = datetime(2020, 11, 13, 19, 47)
prevzeti = timedelta(minutes=8, seconds=35)
priprava = timedelta(minutes=30)
doprava = timedelta(minutes=25, seconds=30)

print(cas_objednavky + prevzeti + priprava + doprava)
