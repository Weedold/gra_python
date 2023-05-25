import random
import os

def wyczysc_ekran():
    os.system('cls' if os.name == 'nt' else 'clear')

def stworz_plansze(wiersze, kolumny):
    plansza = [['_' for _ in range(kolumny)] for _ in range(wiersze)]
    return plansza

def pokaz_plansze(plansza):
    for wiersz in plansza:
        print(' '.join(wiersz))

def wpisz_slowo(plansza, slowo, start_wiersz, start_kolumna, orientacja):
    wiersz_delta = 0
    kolumna_delta = 0

    if orientacja == 'poziomo':
        kolumna_delta = 1
    elif orientacja == 'pionowo':
        wiersz_delta = 1

    for i in range(len(slowo)):
        wiersz = start_wiersz + i * wiersz_delta
        kolumna = start_kolumna + i * kolumna_delta
        plansza[wiersz][kolumna] = slowo[i]

def slowo_kolor(plansza, slowo):
    for wiersz in range(len(plansza)):
        for kolumna in range(len(plansza[wiersz])):
            if plansza[wiersz][kolumna] == slowo[kolumna]:
                plansza[wiersz][kolumna] = '\033[92m' + plansza[wiersz][kolumna] + '\033[0m'

def gra():
    slowa = ["kotek", "domki", "kwiat", "szafa","domki","morze","książ","czasy","klucz","dziad","ptaki",
             "ławka","miska","piłka","krzew","motyl","butla","węgry","akwen","ikona","jacht","lampa","łajba","wyspa","kebab"
             "konto","fotka","cytat","temat","kości","głowa","wyraz","sklep","tosty","cudna","cudny","nudny","kubek","nożyk","łożko",
             "czapa","drzwi","kreda","oczko","taśma","wafel","fotka",
             "ramka","karta","kwiat","baton","trawa","sufit","lampa","ogień","balon","okrąg","żabka","ząbki","serek","filmy","nauka",
             "łyżka","szafa","mięso","obraz","schód","oceny","ferie"]
    haslo = random.choice(slowa)

    liczba_prob = 5
    czy_poprawne = False
    uzyte_slowa = []

    plansza = stworz_plansze(5, 5)

    print("Witaj w grze Odgadnij Słowo!")
    print("Masz 5 prób, aby odgadnąć 5-literowe słowo.")

    while liczba_prob > 0 and not czy_poprawne:
        wyczysc_ekran()
        pokaz_plansze(plansza)

        print(f"\nPróba {6 - liczba_prob}:")

        slowo = input("Podaj słowo (5 liter): ")
        while len(slowo) != 5:
            print("Słowo musi składać się z 5 liter!")
            slowo = input("Podaj słowo (5 liter): ")

        uzyte_slowa.append(slowo)
        wpisz_slowo(plansza, slowo, 5 - liczba_prob, 0, 'poziomo')

        if slowo == haslo:
            czy_poprawne = True
        else:
            liczba_prob -= 1

        wyczysc_ekran()
        pokaz_plansze(plansza)
        slowo_kolor(plansza, haslo)

    wyczysc_ekran()
    pokaz_plansze(plansza)
    print()

    if czy_poprawne:
        print("Gratulacje! Odgadłeś słowo!")
    else:
        print("Przegrałeś! Nie udało ci się odgadnąć słowa.")
        print(f"Prawidłowe słowo to: {haslo}")

    print("\nWykorzystane słowa:")
    for slowo in uzyte_slowa:
        print(slowo)

    wyczysc_ekran()
    print("Plansza z odgadniętym słowem:")
    pokaz_plansze(plansza)

gra()
