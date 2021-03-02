### 1 Balík

Pokračuj ve své práci pro zásilkovou společnost. Společnost nově doručuje i cenné balíky, které mají zadanou určitou hodnotu.

- Vytvoř třídu `ValuablePackage`, která dědí od třídy `Package`. `ValuablePackage` má navíc atribut `value`, ostatní atributy dědí od třídy `Package`.
- Atribut value nastav pomocí funkce `__init__`. Ostatní parametry předej funkci `__init__` třídy Package.
- Vytvoř si alespoň jeden objekt a zkus volání jeho funkcí.

### 2 Částečný úvazek

Naše firma se rozhodla zaměstnávat i pracovníky na částečné úvazky, pro které bude vytvořena zvláštní třída. Vytvoř novou třídu `PartTimeEmployee`, která bude dědit od třídy `Employee` a bude mít navíc atribut `workload` (float), který reprezentuje velikost úvazku oproti plnému. Přidej informaci o úvazku k výpisu informací do funkce `getInfo`.

### 3 Řidič

Pokračuj ve své práci pro zásilkovou společnost. Společnost nyní eviduje jednotlivé řidiče a eviduje balíky, které má každý řidič doručit.

- Vytvoř třídu `Driver`, která má dva atributy: `name` (jméno řidiče) a `packageList` (seznam balíků k doručení, na začátku je prázdný).
- Přidej třídě funkci `assignPackage`, která bude mít jeden parametr - `package` (balík k doručení, může se jednat i o cenný balík). 
- Funkce nejprve zkontroluje, zda balík již nebyl doručen. Pokud ano, vypíše funkce text: "Nelze přiřadit, balík již byl doručen."
- Pokud balík ještě nebyl doručen, je přidán do seznamu balíků `packageList` (použij funkci append).
- U řidiče chceme sledovat, kolik by měl ještě doručit balíků. Napiš funkci `remainingPackages`, která vrátí počet balíků, které má řidič přiřazené a ještě je nedoručil.