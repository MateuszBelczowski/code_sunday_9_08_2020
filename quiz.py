import random

lista_piosenek = [
    {
        "artysta": "Bajm",
        "tytul": "Biała armia",
        "rok": 1978,
        "tekst_piosenki": """To Twoja flaga, nasz młody przyjacielu
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
    },
    {
        "artysta": "Lady Pank",
        "tytul": "Kryzysowa Narzeczona",
        "rok": 1978,
        "tekst_piosenki": """Mogłaś moją być
Kryzysową narzeczoną
Razem ze mną pić
To, co nam tu nawarzono
Mogłaś moją być
Przy zgłuszonym odbiorniku
Aż po blady świt
Słuchać nowin i uderzać w gaz
Nie jeden raz
Nie jeden raz
Nie jeden raz

Mogłaś być już na dnie
A nie byłaś
Nigdy nie dowiesz się
Co straciłaś

Mogłaś moją być
Kryzysową narzeczoną
Pomalutku żyć
Tak jak nam tu naznaczono
Mogłaś moją być
Jakoś ze mną przebiedować
Zamiast życzyć mi
Na pocztówce nie wiadomo skąd
Wesołych świąt
Wesołych świąt
Wesołych świąt

Mogłaś być już na dnie
A nie byłaś
Nigdy nie dowiesz się
Co straciłaś
Mogłaś być już na dnie
A nie byłaś
Nigdy... Nigdy nie dowiesz się

Mogłaś moją być
Zamiast życzyć mi
Wesołych świąt
Wesołych świąt
Wesołych świąt

Mogłaś być już na dnie
A nie byłaś
Nigdy nie dowiesz się
Co straciłaś
Mogłaś być już na dnie
A nie byłaś
Nigdy... Nigdy nie dowiesz się """
    },
    {
        "artysta": "Perfect",
        "tytul": "Nie płacz Ewka",
        "rok": 1978,
        "tekst_piosenki": """Nie płacz, Ewka, bo tu miejsca brak na twe babskie łzy
Po ulicy miłość hula wiatr wśród rozbitych szyb
Patrz, poeci śliczni prawdy sens roztrwonili w grach
W półlitrówkach pustych SOS wysyłają w świat

Żegnam was, już wiem
Nie załatwię wszystkich pilnych spraw
Idę sam, właśnie tam, gdzie czekają mnie
Tam przyjaciół kilku mam od lat
Dla nich zawsze śpiewam, dla nich gram
Jeszcze raz żegnam was, nie spotkamy się

Proza życia to przyjaźni kat, pęka cienka nić
Telewizor, meble, mały fiat: oto marzeń szczyt
Hej, prorocy moi z gniewnych lat, obrastacie w tłuszcz
Już was w swoje szpony dopadł szmal, zdrada płynie z ust

Żegnam was, już wiem
Nie załatwię wszystkich pilnych spraw
Idę sam, właśnie tam, gdzie czekają mnie
Tam przyjaciół kilku mam od lat
Dla nich zawsze śpiewam, dla nich gram
Jeszcze raz żegnam was, nie spotkamy się (x2) """
    },
]
imie = input("Podaj swoje imię: ")
print(f"Cześć {imie}, witamy w najlepszym quizie")
for piosenka in random.sample(lista_piosenek, 3):
    print(f"Utwór {piosenka['tytul']} wykonawcy {piosenka['artysta']}")
    print(piosenka['rok'])
    liczba_znakow = int(input("Podaj liczbę znaków: "))
    print(piosenka['tekst_piosenki'][:liczba_znakow])

    tytul_uzytkownika = input("Jaki jest tytuł tej piosenki?")
    artysta_uzytkownika = input("Jaki jest wykonawca tej piosenki?")
    zgadl_tytul = tytul_uzytkownika.lower() == piosenka['tytul'].lower()
    zgadl_artyste = artysta_uzytkownika.lower() == piosenka['artysta'].lower()
    if zgadl_tytul and zgadl_artyste:
        print("Brawo, zgadłeś")
    elif zgadl_tytul and not zgadl_artyste:
        print(f"Prawidłowy tytuł, ale błędny wykonawca -> {piosenka['artysta']}")
    elif zgadl_artyste and not zgadl_tytul:
        print(f"Prawidłowy artysta, ale błędny tytuł -> {piosenka['tytul']}")
    else:
        print(f"Niepoprawna odpowiedź, prawidłowy tytuł to {piosenka['tytul']}, a artysta to {piosenka['artysta']}")

# Stwórz listę przechowującą 3 słowniki zawierające informacje o piosenkach (artysta, tytul, tekst).
# Zapytaj użytkownika, żeby odgadł wszystkie 3 piosenki,
# dostęp do konkretnej piosenki powinien odbyć się poprzez indeks listy (np. lista_piosenek[0])