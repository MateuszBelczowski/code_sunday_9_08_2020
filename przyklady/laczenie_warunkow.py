zaliczenie_teoria = 60
zaliczenie_praktyka = 50
wynik_teoria = int(input("Jaki miałeś wynik z teorii? "))
wynik_praktyka = int(input("Jaki miałeś wynik z praktyki? "))
if wynik_teoria > zaliczenie_teoria and wynik_praktyka > zaliczenie_praktyka:
    print("CONGRATULATIONS, YOU PASSED!")
elif wynik_teoria < zaliczenie_teoria and wynik_praktyka > zaliczenie_praktyka:
    print("You have passed theory, but practics is much worse")
elif wynik_teoria > zaliczenie_teoria and wynik_praktyka < zaliczenie_praktyka:
    print("You can only do some practics, go learn theory!!!")
elif wynik_teoria < zaliczenie_teoria and wynik_praktyka < zaliczenie_praktyka:
    print("Stop driving")