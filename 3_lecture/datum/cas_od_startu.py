# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# 1
apolloStart = datetime(1969, 7, 16, 14, 32)
print(apolloStart.strftime('%m/%d/%Y'))
