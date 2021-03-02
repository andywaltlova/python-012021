"""
%d	den
%m	měsíc
%Y	rok (nezkrácený)
%H	hodina (rozsah 0-23)
%M	minuta
%S	sekunda
"""
# https://docs.python.org/3/library/datetime.html
from datetime import datetime, timedelta

# 1
apolloStart = datetime(1969, 7, 16, 14, 32)
# print(apolloStart.strftime('%m/%d/%Y'))

# 2
# orbiter_start = datetime(2020, 2, 10, 5, 3)
# print(orbiter_start.isoweekday())
#
# cas_od_startu = datetime.now() - orbiter_start
# print(type(cas_od_startu))
# print(cas_od_startu)

# 3
cas_objednavky = datetime(2020, 11, 13, 19, 47)
prevzeti = timedelta(minutes=8, seconds=35)
priprava = timedelta(minutes=30)
doprava = timedelta(minutes=25, seconds=30)

print(cas_objednavky + prevzeti + priprava + doprava)
