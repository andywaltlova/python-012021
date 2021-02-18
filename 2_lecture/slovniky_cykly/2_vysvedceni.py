# Uvažujme vysvědčení, které máme zapsané jako slovník.
#
# Napiš program, který spočte průměrnou známku ze všech předmětů.
# Uprav program, aby vypsal všechny předměty, ve kterých získal student
# známku 1.

schoolReport = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělešná výchova": 3,
    "Chemie": 4,
}

soucet_znamek = 0
for predmet, znamka in schoolReport.items():
    if znamka == 1:
        print(predmet)
    soucet_znamek += znamka

print('Average:', soucet_znamek // len(schoolReport))

# Pro zvedave prumer bez explicitniho cyklu
# print('Average:', sum(schoolReport.values()) // len(schoolReport))
