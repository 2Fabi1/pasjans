from board import *
from os import system

wartosci = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
kolory = ["♥","♠","♦","♣"]
talia, kolumny = stworzenie_talii()
stos_r = talia

def niezakryte_karty(kolumna):
    # Zwraca liczbę niezakrytych kart w kolumnie.
    return sum(1 for karta in kolumna if not karta.zakryta)

def przetasuj_stos_rezerwowy(stos_r, obecna_karta_idx):
    r.shuffle(stos_r)
    obecna_karta_idx = -1  # Resetuje indeks do pierwszej karty
    return stos_r, obecna_karta_idx

def win(kolory_listy):
    if sum(len(kolor) for kolor in kolory_listy) == 52:
        print("Wygrałeś!")
        return True

def wyczysc_konsole():
    print("\033[2J\033[H", end='') #czyszczenie ekranu dzieki formatowaniu ANSI

def weryfikacja_ruchu(karta1, karta2):
    if kolory.index(karta1.kolor) % 2 == kolory.index(karta2.kolor) % 2:
        return False
    if wartosci.index(karta1.wartosc) + 1 != wartosci.index(karta2.wartosc):
        return False
    return True

def ruch(karty_przenoszone, droga, kolumny, numer_kolumny=0, niezakryte=0, cel_kolumna=0, obecna_karta_idx=0):
    if droga == "kol-kol":
        if numer_kolumny == cel_kolumna:
            wyczysc_konsole()
            print("Nie można przenieść kart do tej samej kolumny.")
        else:
            for i in range(len(karty_przenoszone)):
                if len(kolumny[cel_kolumna-1]) == 0 and karty_przenoszone[0].wartosc == "K":
                    kolumny[cel_kolumna-1].append(karty_przenoszone[0])
                    kolumny[numer_kolumny-1].remove(karty_przenoszone[0])
                elif weryfikacja_ruchu(karty_przenoszone[i], kolumny[cel_kolumna-1][-1]):
                    kolumny[cel_kolumna-1].append(karty_przenoszone[i])
                    kolumny[numer_kolumny-1].remove(karty_przenoszone[i])
                else:
                    wyczysc_konsole()
                    print(f"Nie można przenieść {karty_przenoszone[0]} na {kolumny[cel_kolumna-1][-1]}.")
                    return kolumny
                wyczysc_konsole()
            if niezakryte == len(karty_przenoszone) and len(kolumny[numer_kolumny-1]) > 0:
                kolumny[numer_kolumny-1][-1].zakryta = False
    elif droga == "kol-koń":
        lista_koloru = kolory_listy[kolory.index(karty_przenoszone.kolor)]
        if len(kolory_listy[kolory.index(karty_przenoszone.kolor)]) == wartosci.index(karty_przenoszone.wartosc):
            lista_koloru.append(karty_przenoszone)
            kolumny[numer_kolumny-1].remove(karty_przenoszone)
            if niezakryte == 1 and len(kolumny[numer_kolumny-1]) > 0:
                kolumny[numer_kolumny-1][-1].zakryta = False
            wyczysc_konsole()
        else:
            wyczysc_konsole()
            print(f"Nie można przenieść {karty_przenoszone} do tej kolumny.")
    elif droga == "rez-kol":
        if len(kolumny[cel_kolumna-1]) == 0:
            if karty_przenoszone.wartosc == "K":
                kolumny[cel_kolumna-1].append(karty_przenoszone)
                stos_r.remove(karty_przenoszone)
                obecna_karta_idx -= 1
                wyczysc_konsole()
            else:
                wyczysc_konsole()
                print("Do pustej kolumny można przenieść tylko króla.")
        elif weryfikacja_ruchu(karty_przenoszone, kolumny[cel_kolumna-1][-1]):
            kolumny[cel_kolumna-1].append(karty_przenoszone)
            stos_r.remove(karty_przenoszone)
            obecna_karta_idx -= 1
            wyczysc_konsole()
        else:
            wyczysc_konsole()
        return kolumny, obecna_karta_idx
    elif droga == "rez-koń":
        lista_koloru = kolory_listy[kolory.index(karty_przenoszone.kolor)]
        if len(kolory_listy[kolory.index(karty_przenoszone.kolor)]) == wartosci.index(karty_przenoszone.wartosc):
            lista_koloru.append(karty_przenoszone)
            stos_r.remove(karty_przenoszone)
            obecna_karta_idx -= 1
        wyczysc_konsole()
        return kolumny, obecna_karta_idx
    elif droga == "koń-kol":
        if len(kolumny[cel_kolumna-1]) == 0 and karty_przenoszone.wartosc == "K":
            kolumny[cel_kolumna-1].append(karty_przenoszone)
            wyczysc_konsole()
        elif weryfikacja_ruchu(karty_przenoszone, kolumny[cel_kolumna-1][-1]):
            kolumny[cel_kolumna-1].append(karty_przenoszone)
            kolory_listy[kolory.index(karty_przenoszone.kolor)].remove(karty_przenoszone)
            wyczysc_konsole()
            return kolumny, kolory_listy
        else:
            wyczysc_konsole()
            print("Nie można przenieść karty do tej kolumny.")
    return kolumny

def wypisz_bledna_konstrukcje():
    wyczysc_konsole()
    print("Nieprawidłowa konstrukcja komendy. Wybierz jedną z dostępnych opcji: Liczba kolumny-Liczba kolumny, Liczba kolumny-K, R-Liczba kolumny, R-K, R, K+Liczba stosu końcowego-Liczba kolumny, E")

def main(kolumny, obecna_karta_idx, kolory_listy, stos_r, talia):
    # przesuń kartę z kolumny do kolumny, przesuń kartę z kolumny do stosu końcowego, przesuń kartę ze stosu rezerwowego do kolumny, przesuń kartę ze stosu rezerwowego do stosu końcowego, przesuń kartę ze stosu końcowego do kolumny
    while True:
        wyswietl_plansze_gry(kolumny, stos_r, kolory, kolory_listy, obecna_karta_idx)
        print("===============================================")
        wybor = input("Wpisz komendę: ")
        if not wybor:
            wyczysc_konsole()
            print("Nie wpisano żadnej komendy.")
            continue
        else:
            if wybor[0].upper() == 'R' and len(wybor) == 1:
                if obecna_karta_idx == len(stos_r)-1:
                    stos_r, obecna_karta_idx = przetasuj_stos_rezerwowy(stos_r, obecna_karta_idx)
                else:
                    obecna_karta_idx += 1
                wyczysc_konsole()
            elif wybor[0].upper() == 'E' and len(wybor) == 1:
                # resetowanie gry
                wyczysc_konsole()
                for i in kolumny:
                    i.clear()
                talia.clear()
                talia, kolumny = stworzenie_talii()
                stos_r = talia
                for i in kolory_listy:
                    i.clear()
                obecna_karta_idx = -1  # Resetuje indeks do pierwszej karty
                print("Gra została zresetowana.")
            elif len(wybor) == 3: #ochrona przed błędami
                if wybor[0].isdigit() and wybor[1] == "-" and wybor[2].isdigit():   
                    if 1 <= int(wybor[0]) <= 7:
                        kolumna = kolumny[int(wybor[0])-1]
                        if kolumna:
                            niezakryte_count = niezakryte_karty(kolumna)
                            karty_przenoszone = []
                            karty_przenoszone.append(kolumna[-1])
                            kolumny = ruch(karty_przenoszone, "kol-kol", kolumny, int(wybor[0]), niezakryte_count, int(wybor[2]))  # Przeniesienie ostatniej karty
                        else:
                            wyczysc_konsole()
                            print("Kolumna jest pusta.")
                    else:
                        wyczysc_konsole()
                        print("Nieprawidłowy wybór kolumny.")
                elif wybor[0].isdigit() and wybor[1] == "-" and wybor[2].upper() == 'K':
                    kolumna = int(wybor[0])
                    if 1 <= kolumna <= 7:
                        kolumna = kolumny[kolumna-1]
                        if kolumna:
                            karty_przenoszone = kolumna[-1]  # Przenieś ostatnią kartę
                            kolumny = ruch(karty_przenoszone, "kol-koń", kolumny, int(wybor[0]), niezakryte_karty(kolumna))
                        else:
                            wyczysc_konsole()
                            print("Kolumna jest pusta.")
                    else:
                        wyczysc_konsole()
                        print("Nieprawidłowy wybór kolumny.")
                
                elif wybor[0].upper() == 'R' and wybor[1] == "-" and wybor[2].isdigit():
                    if obecna_karta_idx == -1:
                        wyczysc_konsole()
                        print("Nie ma odkrytej karty w stosie rezerwowym.")
                    else:
                        wybor = int(wybor[2])
                        if 1 <= wybor <= 7:
                            kolumna = kolumny[wybor-1]
                            karta_przenoszona = stos_r[obecna_karta_idx]  # Przenieś ostatnią kartę
                            kolumny, obecna_karta_idx = ruch(karta_przenoszona, "rez-kol", kolumny, 0, niezakryte_karty(kolumna), wybor, obecna_karta_idx)
                        else:
                            wyczysc_konsole()
                            print("Nieprawidłowy wybór kolumny.")
                elif wybor[0].upper() == 'R' and wybor[1] == '-' and wybor[2].upper() == 'K':
                    if obecna_karta_idx == -1:
                        wyczysc_konsole()
                        print("Nie ma odkrytej karty w stosie rezerwowym.")
                    else:
                        kolumny, obecna_karta_idx = ruch(stos_r[obecna_karta_idx], "rez-koń", kolumny, 0, 0, 0, obecna_karta_idx)
                else:
                    wypisz_bledna_konstrukcje()
            elif len(wybor) == 4: #ochrona przed błędami
                if wybor[0].upper() == 'K' and wybor[1].isdigit() and wybor[2] == "-" and wybor[3].isdigit():
                    wybor = int(wybor[1])
                    wybor_kolumny = int(wybor[3])
                    if 1 <= wybor_kolumny <= 7 and len(kolory_listy[wybor-1]) != 0:
                        kolumna = kolumny[wybor-1]
                        kolumny, kolory_listy = ruch(kolory_listy[wybor-1][-1], "koń-kol", kolumny, 0, 0, wybor_kolumny)
                    elif len(kolory_listy[wybor-1]) == 0:
                        wyczysc_konsole()
                        print("Nie ma kart w tym stosie końcowym.")
                    elif 1 > wybor_kolumny or wybor_kolumny > 7:
                        wyczysc_konsole()
                        print("Nieprawidłowy wybór kolumny.")
                else:
                    wypisz_bledna_konstrukcje()
            elif len(wybor) == 5 or len(wybor) == 6: #ochrona przed błędami
                if wybor[0].isdigit() and wybor[1] == "-" and wybor[2].isdigit() and wybor[3] == "-":   
                    if 1 <= int(wybor[0]) <= 7:
                        kolumna = kolumny[int(wybor[0])-1]
                        if kolumna:
                            niezakryte_count = niezakryte_karty(kolumna)
                            if wybor[4] == '1':
                                wartosc_karty = '10'
                            else:
                                wartosc_karty = wybor[4]
                            wybor_karty = 0
                            for i in range(niezakryte_count):
                                if kolumna[i+len(kolumna)-niezakryte_count].wartosc == wartosc_karty.upper():
                                    wybor_karty = i+1
                            if wybor_karty <= niezakryte_count and wybor_karty > 0:
                                karty_przenoszone = kolumna[-1*(niezakryte_count-wybor_karty+1):]
                                wybor_kolumny = int(wybor[2])
                                kolumny = ruch(karty_przenoszone, "kol-kol", kolumny, int(wybor[0]), niezakryte_count, wybor_kolumny)
                            else:
                                wyczysc_konsole()
                                print("Nieprawidłowy wybór karty.")
                        else:
                            wyczysc_konsole()
                            print("Kolumna jest pusta.")
                    else:
                        wyczysc_konsole()
                        print("Nieprawidłowy wybór kolumny.")
            else:
                wypisz_bledna_konstrukcje()
            if win(kolory_listy):
                wyswietl_stos_rezerwowy(stos_r, obecna_karta_idx)
                wyswietl_stos_koncowy(kolory, kolory_listy)
                break

if __name__ == "__main__":
    main(kolumny, obecna_karta_idx, kolory_listy, stos_r, talia) 
