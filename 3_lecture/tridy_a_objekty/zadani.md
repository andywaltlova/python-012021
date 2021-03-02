### 1 Kniha
Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu `Book`, která reprezentuje knihu. Každá kniha bude mít atributy `title`, `pages` a `price`. Hodnoty nastav ve funkci `__init__`.

- Přidej knize funkci `getInfo`, která vypíše informace o knize v nějakém pěkném formátu.
- Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou. Přidej funkci `discount`, která bude mít jeden parametr - velikost slevy v procentech. Funkce sníží cenu knihy o dané procento.
### 2 Balík
Uvažuj, že navrhuješ software pro zásilkovou společnost.

- Vytvoř třídu `Package`, která bude mít tři atributy - `address`, `weightInKilos` a `delivered`. První dva atributy nastav pomocí parametrů funkce `__init__`. Parametr delivered nastav na začátku jako `False`.
- Připoj ke třídě funkci `deliver`, která změní hodnotu parametru `delivered` na `True`.
- Přidej funkci `getInfo`, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.
- Zkus si vytvořit nějaké objekty ze třídy `Package` a ověř, že vše funguje.

### 3 Zkušební doba

U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.

- Rozšiř funkci `__init__` třídy Employee o parametr probation, který bude typu bool. Tuto hodnotu ulož jako atribut třídy Employee.
- Uprav funkci getInfo. Pokud je zaměstnanec ve zkušební době, přidej k jeho/jejímu výpisu text Je ve zkušební době.