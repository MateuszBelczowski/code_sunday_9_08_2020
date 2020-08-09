stan_konta = 1000
bankomat_czynny = True

wyplata = int(input("Ile chcesz wypłacić?"))

if wyplata > stan_konta:
    print("nie masz tyle pieniędzy")
elif bankomat_czynny:
    print("ok, tutaj Twoja kasa")
