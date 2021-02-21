volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}

hodina = int(input("Zadej hodinu, na ktero uchces mistnost zamluvit: "))

if hodina in volnePokoje:
    print('K dizpozici', len(volnePokoje[hodina]), 'mistnosti.')
else:
    print('V dany cas neni dostupna mistnost')

# Pripadne lze vynechat podminku, pokud predpokladame, ze hodina zadana
# uzivatelem ve slovniku je


# Advanced reseni
mistnosti = len(volnePokoje.get(hodina, []))
print('Dostupne mistnosti: ' + str(mistnosti))
