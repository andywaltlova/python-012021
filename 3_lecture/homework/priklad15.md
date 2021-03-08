# Prodej vstupenek

Vytvoř program na prodej vstupenek do letního kina. Ceny vstupenek jsou v tabulce níže.

| Datum | Cena |
| ------------- |-------------:| 
| 1. 7. 2021 - 10. 8. 2021 | 250 Kč | 
| 11. 8. 2021 - 31. 8. 2021 | 180 Kč |

Mimo tato data je středisko zavřené.

Tvůj program se nejprve zeptá uživatele na datum a počet osob, pro které uživatel chce vstupenky koupit. Uživatel zadá datum ve středoevropském formátu. Převeď řetězec zadaný uživatelem na datum pomocí funkce `datetime.strptime()`. Následně se zeptej na počet osob, 

Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že letní kino je v té době uzavřené. Pokud je letní kino otevřené, spočítej a vypiš cenu za ubytování.

Data lze porovnávat pomocí známých operátorů `<`, `>`, `<=`, `>=`, `==`, `!=`. Tyto operátory můžeš použít v podmínce `if`. Níže vidíš příklad porovnání dvou dat. Program vypíše text `"První datum je dřívější než druhé datum."`.

```python
from datetime import datetime
prvni_udalost = datetime(2021, 7, 1)
druha_udalost = datetime(2021, 7, 3)
if prvni_datum < druhe_datum:
  print("Druhá událost se stala po první události")
```

