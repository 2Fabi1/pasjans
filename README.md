# pasjans

Biblioteki potrzebne do kodu: -

Aby rozpocząć grę, należy uruchomić plik main.py

Jak grać?
Użytkownik może wykonać 7 komend:
- "Liczba-Liczba": Przenosi kartę z kolumny o numerze pierwszej podanej liczby do kolumny o numerze drugiej podanej liczby, przykład: 5-3  
- "Liczba-K": Przenosi kartę z kolumny o numerze podanej liczby do stosu końcowego, przykład: 7-K
- "R-Liczba": Przenosi kartę z stosu rezerwowego do kolumny o numerze podanej liczby, przykład: R-3
- "R-K": Przenosi kartę z stosu rezerwowego do stosu końcowego
- "R": Dobiera kartę z stosu rezerwowego
- "KLiczba-Liczba": Przenosi kartę z stosu końcowego o podanym numerze do kolumnie o numerze podanej liczby, przykład: K2-4

Plik board.py:
        Klasa Karta:
        Klasa wszystkich kart, zawiera właściwości "kolor","wartosc" oraz "zakryta".
        Klasa ta także definiuje sposób drukowania kart
        
