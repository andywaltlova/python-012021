# # 1. Nabídky práce Stáhni si soubor DataAnalyst.csv se seznamem nabídek
# práce pro datové analytiky. Soubor byl stažen z webu Kaggle.com, kde najdeš
# spoustu zajímavých dat, na kterých se můžeš učit, jak analyzovat data.
#
# Ale zpět k našim úkolům.
#
# - Načti data do DataFrame, který si pojmenuj jobs.
# - Nech si zobrazit názvy sloupců, které jsou v souboru uloženy.
# - Podívej se, kolik má soubor řádek.
# - Zjisti všechny informace o pracovní pozici na desátém řádku.
# - Podívej se, kde budou pracovat zájemci vybraní na 12-20.

import pandas as pd

jobs = pd.read_csv('DataAnalyst.csv', index_col=0)
print(jobs.shape)
print(jobs.columns)
