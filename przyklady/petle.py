# for i in range(10):
#     wiek = input("Ile masz lat?")
#     print(i)

lista = ['kot', 'pies', 'mysz', 'koń', 'chomik', "fretka", "wąż", "kanarek"]
for zwierze in lista:
    print(f"{zwierze} ma {len(zwierze)}")

lista_osob = [
    {"imie": "Jan", "nazwisko": "Kowalski"},
    {"imie": "Karol", "nazwisko": "Karolski"},
    {"imie": "Adam", "nazwisko": "Nowak"},
    {"imie": "Michał", "nazwisko": "Dębowski"},
]
for osoba in lista_osob:
    print(osoba['nazwisko'])