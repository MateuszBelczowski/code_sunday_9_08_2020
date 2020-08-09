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

tytul_uzytkownika = input("Jaki jest tytuł tej piosenki?")
artysta_uzytkownika = input("Jaki jest wykonawca tej piosenki?")
zgadl_tytul = tytul_uzytkownika.lower() == tytul.lower()
zgadl_artyste = artysta_uzytkownika.lower() == artysta.lower()
if zgadl_tytul and zgadl_artyste:
    print("Brawo, zgadłeś")
elif zgadl_tytul and not zgadl_artyste:
    print(f"Prawidłowy tytuł, ale błędny wykonawca -> {artysta}")
elif zgadl_artyste and not zgadl_tytul:
    print(f"Prawidłowy artysta, ale błędny tytuł -> {tytul}")
else:
    print(f"Niepoprawna odpowiedź, prawidłowy tytuł to {tytul}, a artysta to {artysta}")

"""
Zapytaj użytkownika również o artystę:
- tylko w przypadku poprawnych obu odpowiedzi, uznajemy, że zgadł
"""
