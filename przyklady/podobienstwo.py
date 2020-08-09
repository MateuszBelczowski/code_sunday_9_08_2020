import difflib

napis1 = 'coldplay'
napis2 = 'coldplxys'

wspolczynnik = difflib.SequenceMatcher(None, napis1, napis2).ratio()
print(wspolczynnik)

napis1 == napis2
if wspolczynnik > 0.8:
    print("napisy są podobne")
else:
    print("błędna odpowiedź")