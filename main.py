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

def weryfikacja_ruchu(karta1, karta2):
    if kolory.index(karta1.kolor) % 2 == kolory.index(karta2.kolor) % 2:
        return False
    if wartosci.index(karta1.wartosc) + 1 != wartosci.index(karta2.wartosc):
        return False
    return True

def ruch(karty_przenoszone, droga, kolumny, numer_kolumny=0, niezakryte=0, cel_kolumna=0, obecna_karta_idx=0):
    if droga == "kol-kol":
        if numer_kolumny == cel_kolumna:
            system("cls")
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
                    system("cls")
                    print(f"Nie można przenieść {karty_przenoszone[0]} na {kolumny[cel_kolumna-1][-1]}.")
                    return kolumny
                system("cls")
                print(f"Przeniesiono {', '.join(str(karta) for karta in karty_przenoszone)} do kolumny {cel_kolumna}.")

            if niezakryte == len(karty_przenoszone) and len(kolumny[numer_kolumny-1]) > 0:
                kolumny[numer_kolumny-1][-1].zakryta = False
    elif droga == "kol-koń":
        lista_koloru = kolory_listy[kolory.index(karty_przenoszone.kolor)]
        if len(kolory_listy[kolory.index(karty_przenoszone.kolor)]) == wartosci.index(karty_przenoszone.wartosc):
            lista_koloru.append(karty_przenoszone)
            kolumny[numer_kolumny-1].remove(karty_przenoszone)
            if niezakryte == 1 and len(kolumny[numer_kolumny-1]) > 0:
                kolumny[numer_kolumny-1][-1].zakryta = False
            system("cls")
            if karty_przenoszone.kolor in ["♥", "♦"]:
                print(f"Przeniesiono kartę {karty_przenoszone} do stosu końcowego \033[91m{karty_przenoszone.kolor}\033[00m.")
            else:
                print(f"Przeniesiono kartę {karty_przenoszone} do stosu końcowego \033[96m{karty_przenoszone.kolor}\033[00m.")
        else:
            system("cls")
            print(f"Nie można przenieść {karty_przenoszone} do tej kolumny.")
    elif droga == "rez-kol":
        if len(kolumny[cel_kolumna-1]) == 0:
            if karty_przenoszone.wartosc == "K":
                kolumny[cel_kolumna-1].append(karty_przenoszone)
                stos_r.remove(karty_przenoszone)
                obecna_karta_idx -= 1
                system("cls")
                print(f"Przeniesiono kartę {karty_przenoszone} do pustej kolumny {cel_kolumna}.")
            else:
                system("cls")
                print("Do pustej kolumny można przenieść tylko króla.")
        elif weryfikacja_ruchu(karty_przenoszone, kolumny[cel_kolumna-1][-1]):
            kolumny[cel_kolumna-1].append(karty_przenoszone)
            stos_r.remove(karty_przenoszone)
            obecna_karta_idx -= 1
            system("cls")
            print(f"Przeniesiono kartę {karty_przenoszone} do kolumny {cel_kolumna}.")
        else:
            system("cls")
            print(f"Nie można przenieść {karty_przenoszone} na {kolumny[cel_kolumna-1][-1]}.")
        return kolumny, obecna_karta_idx
    elif droga == "rez-koń":
        lista_koloru = kolory_listy[kolory.index(karty_przenoszone.kolor)]
        if len(kolory_listy[kolory.index(karty_przenoszone.kolor)]) == wartosci.index(karty_przenoszone.wartosc):
            lista_koloru.append(karty_przenoszone)
            stos_r.remove(karty_przenoszone)
            obecna_karta_idx -= 1
            system("cls")
            if karty_przenoszone.kolor in ["♥", "♦"]:
                print(f"Przeniesiono kartę {karty_przenoszone} do stosu końcowego \033[91m{karty_przenoszone.kolor}\033[00m.")
            else:
                print(f"Przeniesiono kartę {karty_przenoszone} do stosu końcowego \033[96m{karty_przenoszone.kolor}\033[00m.")
        else:
            system("cls")
            print(f"Nie można przenieść {karty_przenoszone} do stosu końcowego.")
        return kolumny, obecna_karta_idx
    elif droga == "koń-kol":
        if len(kolumny[cel_kolumna-1]) == 0 and karty_przenoszone.wartosc == "K":
            kolumny[cel_kolumna-1].append(karty_przenoszone)
            system("cls")
            print(f"Przeniesiono kartę {karty_przenoszone} do kolumny {cel_kolumna}.")
        elif weryfikacja_ruchu(karty_przenoszone, kolumny[cel_kolumna-1][-1]):
            kolumny[cel_kolumna-1].append(karty_przenoszone)
            kolory_listy[kolory.index(karty_przenoszone.kolor)].remove(karty_przenoszone)
            system("cls")
            print(f"Przeniesiono kartę {karty_przenoszone} do kolumny {cel_kolumna}.")
            return kolumny, kolory_listy
        else:
            system("cls")
            print("Nie można przenieść karty do tej kolumny.")
    return kolumny

def wypisz_bledna_konstrukcje():
    system("cls")
    print("Nieprawidłowa konstrukcja komendy. Wybierz jedną z dostępnych opcji: Liczba kolumny-Liczba kolumny, Liczba kolumny-K, R-Liczba kolumny, R-K, R, K+Liczba stosu końcowego-Liczba kolumny, E")

def main(kolumny, obecna_karta_idx, kolory_listy, stos_r, talia):
    # przesuń kartę z kolumny do kolumny, przesuń kartę z kolumny do stosu końcowego, przesuń kartę ze stosu rezerwowego do kolumny, przesuń kartę ze stosu rezerwowego do stosu końcowego, przesuń kartę ze stosu końcowego do kolumny
    while True:
        wyswietl_plansze_gry(kolumny, stos_r, kolory, kolory_listy, obecna_karta_idx)
        print("===============================================")
        wybor = input("Wpisz komendę: ")
        if wybor[0].upper() == 'R' and len(wybor) == 1:
            if obecna_karta_idx == len(stos_r)-1:
                stos_r, obecna_karta_idx = przetasuj_stos_rezerwowy(stos_r, obecna_karta_idx)
            else:
                obecna_karta_idx += 1
            system("cls")
        elif wybor[0].upper() == 'E' and len(wybor) == 1:
            # resetowanie gry
            system("cls")
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
                        if niezakryte_count == 1:
                            karty_przenoszone = []
                            karty_przenoszone.append(kolumna[-1])
                            kolumny = ruch(karty_przenoszone, "kol-kol", kolumny, int(wybor[0]), niezakryte_count, int(wybor[2]))  # Przeniesienie ostatniej karty
                        else:
                            print("Karty do wyboru:")
                            j = 0
                            for i in range(len(kolumna)):
                                if not(kolumna[i].zakryta):
                                    print(f"{j+1} - {kolumna[i]}")
                                    j += 1
                            while True:
                                wybor_karty = int(input(f"Wybierz kartę i wszystkie karty po niej, którą/e chcesz przesunąć (1-{niezakryte_count}): "))
                                if wybor_karty <= niezakryte_count and wybor_karty > 0:
                                    break
                                else:
                                    print("Nieprawidłowy wybór karty.")
                            karty_przenoszone = kolumna[-1*(niezakryte_count-wybor_karty+1):]
                            wybor_kolumny = int(wybor[2])
                            kolumny = ruch(karty_przenoszone, "kol-kol", kolumny, int(wybor[0]), niezakryte_count, wybor_kolumny)
                    else:
                        system("cls")
                        print("Kolumna jest pusta.")
                else:
                    system("cls")
                    print("Nieprawidłowy wybór kolumny.")
            elif wybor[0].isdigit() and wybor[1] == "-" and wybor[2].upper() == 'K':
                kolumna = int(wybor[0])
                if 1 <= kolumna <= 7:
                    kolumna = kolumny[kolumna-1]
                    if kolumna:
                        karty_przenoszone = kolumna[-1]  # Przenieś ostatnią kartę
                        kolumny = ruch(karty_przenoszone, "kol-koń", kolumny, int(wybor[0]), niezakryte_karty(kolumna))
                    else:
                        system("cls")
                        print("Kolumna jest pusta.")
                else:
                    system("cls")
                    print("Nieprawidłowy wybór kolumny.")
            
            elif wybor[0].upper() == 'R' and wybor[1] == "-" and wybor[2].isdigit():
                if obecna_karta_idx == -1:
                    system("cls")
                    print("Nie ma odkrytej karty w stosie rezerwowym.")
                else:
                    wybor = int(wybor[2])
                    if 1 <= wybor <= 7:
                        kolumna = kolumny[wybor-1]
                        karta_przenoszona = stos_r[obecna_karta_idx]  # Przenieś ostatnią kartę
                        kolumny, obecna_karta_idx = ruch(karta_przenoszona, "rez-kol", kolumny, 0, niezakryte_karty(kolumna), wybor, obecna_karta_idx)
                    else:
                        system("cls")
                        print("Nieprawidłowy wybór kolumny.")
            elif wybor[0].upper() == 'R' and wybor[1] == '-' and wybor[2].upper() == 'K':
                if obecna_karta_idx == -1:
                    system("cls")
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
                    system("cls")
                    print("Nie ma kart w tym stosie końcowym.")
                elif 1 > wybor_kolumny or wybor_kolumny > 7:
                    system("cls")
                    print("Nieprawidłowy wybór kolumny.")
            else:
                wypisz_bledna_konstrukcje()
        else:
            wypisz_bledna_konstrukcje()
        if win(kolory_listy):
            wyswietl_plansze_gry(kolumny, stos_r, kolory, kolory_listy, obecna_karta_idx)
            break

if __name__ == "__main__":
    main(kolumny, obecna_karta_idx, kolory_listy, stos_r, talia) 
