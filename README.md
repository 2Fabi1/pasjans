# 🃏 Pasjans (Solitaire) – Gra tekstowa w Pythonie

Gra pasjans (klasyczny Solitaire) zaimplementowana w czystym Pythonie. W pełni tekstowy interfejs w terminalu, bez użycia zewnętrznych bibliotek graficznych.

---

## 📁 Struktura projektu

```
.
├── board.py        # Logika gry, klasa Karta, funkcje do tworzenia i wyświetlania planszy
├── main.py         # Główna pętla gry, obsługa komend użytkownika
└── README.md       # Dokumentacja
```

---

## Wymagania

- Python 3.10+
- Brak zależności zewnętrznych

---

## Uruchomienie gry

Grę należy otworzyć w terminalu obsługującym formatowanie ANSI, np. Visual Studio Code lub Powershell 7+

---

## Zasady i komendy

Wpisuj poniższe komendy, aby grać:

- `Liczba-Liczba` – Przenieś kartę z jednej kolumny do drugiej  
  **np.** `5-3`

- `Liczba-Liczba-Wartość` – Przenieś ciąg kart od danej wartości między kolumnami  
  **np.** `4-7-Q`

- `Liczba-K` – Przenieś kartę z kolumny do stosu końcowego  
  **np.** `2-K`

- `R` – Dobierz nową kartę ze stosu rezerwowego

- `R-Liczba` – Przenieś kartę z rezerwy do kolumny  
  **np.** `R-3`

- `R-K` – Przenieś kartę z rezerwy do stosu końcowego

- `KX-Liczba` – Przenieś kartę ze stosu końcowego `X` do kolumny  
  **np.** `K1-5`

- `E` – Zresetuj grę

---

## Zawartość `board.py`

- `Karta` – Klasa reprezentująca pojedynczą kartę (wartość, kolor, zakryta/odkryta)
- `stworzenie_talii()` – Inicjalizacja potasowanej talii, kolumn i stosu rezerwowego
- `wyswietl_stos_rezerwowy()` – Rysuje stos rezerwowy w terminalu
  `wyswietl_stos_koncowy()` – Rysuje stosy końcowe w terminalu
- `wyswietl_plansze()` – Rysuje planszę w terminalu (kolumny)
- `wyswietl_plansze_gry()` – Rysuje całą planszę w terminalu (kolumny + stosy)

---

## Zawartość `main.py`

Obsługuje interakcje użytkownika oraz implementuje wszystkie możliwe ruchy:

- `main(...)` – Główna pętla gry
- `ruch(...)` – Przetwarza ruchy kart między kolumnami, stosami i rezerwą
- `niezakryte_karty(...)` – Zlicza odkryte karty w kolumnie
- `weryfikacja_ruchu(...)` – Sprawdza poprawność ruchu wg zasad pasjansa
- `przetasuj_stos_rezerwowy(...)` – Tasuje zużyty stos rezerwowy
- `win(...)` – Sprawdza warunek zwycięstwa
- `wypisz_bledna_konstrukcje()` – Pokazuje poprawne formaty komend

---

## Zakończenie gry

Gra kończy się automatycznie po przeniesieniu wszystkich 52 kart na stosy końcowe.
---


