# 1
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

count_pages = 0
book_8 = 0
for book in books:
    count_pages += book['pages']

    if book['rating'] >= 8:
        book_8 += 1

# print(count_pages)
# print(book_8)

# 2
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

sum_marks = 0
subjects = []
for subject, mark in schoolReport.items():
    sum_marks += mark

    if mark == 1:
        subjects.append(subject)

# print(', '.join(subjects))
# print(sum_marks/len(schoolReport))
# print(sum(schoolReport.values())/len(schoolReport))


# 3
plates = {
  "4A2 3000": "František Novák",
  "6P5 4747": "Jana Pilná",
  "3B7 3652": "Jaroslav Sečkár",
  "1P5 5269": "Marta Nováková",
  "37E 1252": "Martina Matušková",
  "2A5 2241": "Jan Král"
}

for spz, majitel in plates.items():
    if spz[1] == 'P':
        print(majitel)
