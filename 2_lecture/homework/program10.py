def sance_na_uspech_zakazky(odvetvi, obrat, zeme, konference=False, newsletter=False):
    body = 0
    # tady by sel udelat i slovnik s hodnotami jako body
    if odvetvi == 'automotive':
        body += 3
    if odvetvi == 'retail':
        body += 2

    if 10000000 <= obrat <= 1000000000:
        body += 3
    elif obrat > 10000000:
        body += 1

    if zeme in ['Česko', 'Slovensko']:
        body += 2
    elif zeme in ['Německo', 'Francie']:
        body += 1

    if konference:
        body += 1
    if newsletter:
        body += 1

    if body < 5:
        return 'Mala'
    if body <= 8:
        return 'Stredni'
    return 'Vysoka'
