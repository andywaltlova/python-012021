purchaseList = [
    {"person": "Petr", "item": "Prací prášek", "value": 399},
    {"person": "Ondra", "item": "Savo", "value": 80},
    {"person": "Petr", "item": "Toaletní papír", "value": 65},
    {"person": "Libor", "item": "Pivo", "value": 124},
    {"person": "Petr", "item": "Pytel na odpadky", "value": 75},
    {"person": "Míša", "item": "Utěrky na nádobí", "value": 130},
    {"person": "Ondra", "item": "Toaletní papír", "value": 120},
    {"person": "Míša", "item": "Pečící papír", "value": 30},
    {"person": "Zuzka", "item": "Savo", "value": 80},
    {"person": "Pavla", "item": "Máslo", "value": 50},
    {"person": "Ondra", "item": "Káva", "value": 300}
]

sumPerPerson = {}
for item in purchaseList:
    person = item["person"]
    value = item["value"]
    if person in sumPerPerson:
        sumPerPerson[person] += value
    else:
        sumPerPerson[person] = value

totalValue = 0
for person, value in sumPerPerson.items():
    totalValue += value
    print(f"{person} utratil(a) za společné nákupy {value} Kč.")

averageValue = totalValue / len(sumPerPerson)
print(f"Průměrná hodnota na osobu je {round(averageValue)} Kč.")

# Dopiš cyklus, který projde slovník sumPerPerson a pro každého ze
# spolubydlících vypíše, kolik by měl doplatit (pokud utratil(a) méně než
# průměr), případně kolik by měl obdržet (pokud utratil(a) více než průměr).

for person, value in sumPerPerson.items():
    if value > averageValue:
        print(f'{person:<6} | Vratka: {round(value - averageValue, 2)} Kč.')
    elif value < averageValue:
        print(f'{person:<6} | Doplatek: {round(averageValue - value, 2)} Kč.')
    else:
        print(f'{person:<6} | Utratil presne prumernou utratu.')
