slownik = {}
# lub
# slownik = dict()
print(slownik)
# dodanie elementu do słownika
slownik["imie"] = "Mateusz"
print(slownik)
# odczyt ze słownika
print(slownik["imie"])
slownik2 = {
    "imie": "Jan",
    "nazwisko": "Kowalski",
    "adres": """
    Konwaliowa 123, Gdańsk"""
}
print(slownik2["imie"])
slownik2["imie"] = "Krzysztof"
print(slownik2["imie"])
print(f"Nazywam {slownik2['imie']} {slownik2['nazwisko']} i mieszkam pod adresem {slownik2['adres']}")
