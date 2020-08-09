artysta = "Bajm"
tytul = "Biała Armia"
rok = 1978
tekst_piosenki = """To Twoja flaga, nasz młody przyjacielu
Nie musisz kochać jej barw, o nie
To Twoja armia i życie w ciągłym biegu
Nigdy nie będziesz już sam
Możesz wreszcie zachłysnąć się powietrzem
I unieść do góry jak ptak, he-hej
Możesz wreszcie zabłądzić w wielkim mieście
Urodziłeś się, by służyć nam

Właśnie nadszedł ten czas
Whoah, to jest właśnie ten czas

Ref.:
Jesteś sterem, białym żołnierzem
Nosisz spodnie, więc walcz
Jesteś żaglem, szalonym wiatrem
Twoja siła to skarb

Bóg jest z nami, jego prawda
Jak tarcza Cię ocali
Czekałeś na ten dzień tyle lat
Ruszaj z nami, z wątłymi marzeniami
Z ufnością, którą jeszcze masz

Właśnie nadszedł ten czas
Whoah, to jest właśnie ten czas

Jesteś sterem, białym żołnierzem
Nosisz spodnie, więc walcz
Jesteś żaglem, szalonym wiatrem
Twoja siła to skarb

Jesteś sterem, białym żołnierzem
Nosisz spodnie, więc walcz
Jesteś żaglem, szalonym wiatrem
Twoja siła to skarb

Jesteś sterem, białym żołnierzem
Nosisz spodnie, więc walcz
Jesteś żaglem, szalonym wiatrem
Twoja siła to skarb

Jesteś sterem, białym żołnierzem
Nosisz spodnie, więc walcz
Jesteś żaglem, szalonym wiatrem
Twoja siła to skarb

Jesteś sterem, białym żołnierzem
Nosisz spodnie, więc walcz
Jesteś żaglem, szalonym wiatrem
Twoja siła to skarb

Jesteś sterem, białym żołnierzem
Nosisz spodnie, więc walcz
Jesteś żaglem, szalonym wiatrem
Twoja siła to skarb"""

print(f"Utwór {tytul} wykonawcy {artysta}")
print(rok)
imie = input("Podaj swoje imię: ")
print(f"Cześć {imie}, witamy w najlepszym quizie")
liczba_znakow = int(input("Podaj liczbę znaków: "))
print(tekst_piosenki[:liczba_znakow])

"""
Zapytaj użytkownika, jaki tytuł ma dana piosenka, dla której wyświetlamy tekst.
W przypadku prawidłowej odpowiedzi wyświetl komunikat z gratulacjami,
w przypadku błędnej odpowiedzi poinformuj użytkownika,
jaka jest prawidłowa odpowiedź
"""
