from datetime import datetime

date_reservation = input("Zadej datum, na ktery chces vstupenky zarezervovat: ")
num_of_people = int(input("Kolik vstupenek chces zarezervovat: "))

date_reservation = datetime.strptime(date_reservation,'%d.%m.%Y')

if datetime(2021, 7, 1) <= date_reservation <= datetime(2021, 8, 10):
    cena = num_of_people * 250
    print(f"Cena vstupenek : {cena} Kc.")
elif datetime(2021, 8, 11) <= date_reservation <= datetime(2021, 8, 31):
    cena = num_of_people * 180
    print(f"Cena vstupenek : {cena} Kc.")
else:
    print("Letni kino je v teto dobe uzavrene.")