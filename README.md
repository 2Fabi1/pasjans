## Wymagania

- Brak zależności zewnętrznych - Python 3.10+

## Uruchomienie gry

Grę należy otworzyć w terminalu obsługującym formatowanie ANSI, np: Visual Studio Code lub Powershell 7+

## Komendy

Wpisuj poniższe komendy, aby grać:

- Liczba-Liczba - Przenieś kartę z jednej kolumny do drugiej, przykład: 5-3

- Liczba-Liczba-Wartość - Przenieś ciąg kart od danej wartości między kolumnami o pierwszej podanej liczbie i drugiej podanej liczbie, przykład: 4-7-Q

- Liczba-K - Przenieś kartę z kolumny o numerze podanej liczby do stosu końcowego, przykład: 2-K

- R - Dobierz kartę ze stosu rezerwowego

- R-Liczba - Przenieś kartę z stosu rezerwowego do kolumny przykład: R-3 

- R-K - Przenieś kartę ze stosu rezerwowego do stosu końcowego 

- KX-Liczba - Przenieś kartę ze stosu końcowego X do kolumny, przykład: K1-5 

- E - Zresetuj grę

## Zawartość `board.py`

- Karta - Klasa representująca pojedynczą kartę (kolor, zakryta/odkryta, wartość)
- stworzenie_talii() - Inicjalizacja potasowanej talii, kolumn i stosu rezerwowego
- wyswietl_stos_rezerwowy() - Rysuje stos rezerwowy w terminalu Rysuje Stosy
- wyswietl_stos_koncowy() - 
- wyswietl_plansze() – Rysuje planszę w terminalu (kolumny)
- wyswietl_plansze_gry() – Rysuje całą planszę w terminalu (kolumny + stosy)

## Zawartość `main.py`

Obsługuje interakcje użytkownika oraz implementuje wszystkie możliwe ruchy:

- main(...) – Główna pętla gry
- ruch(...) – Przetwarza ruchy kart między kolumnami, stosami i rezerwą
- niezakryte_karty(...) – Zlicza odkryte karty w kolumnie
- weryfikacja_ruchu(...) – Sprawdza poprawność ruchu wg zasad pasjansa
- przetasuj_stos_rezerwowy(...) – Tasuje zużyty stos rezerwowy
- win(...) – Sprawdza warunek zwycięstwa
- wypisz_bledna_konstrukcje() – Pokazuje poprawne formaty komend

## Zakończenie gry

Gra kończy się automatycznie po przeniesieniu wszystkich 52 kart na stosy końcowe.



