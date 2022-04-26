**Finalny projekt z przedmiotu Narzędzia programistyczne w Pythonie wspierające analizę danych (NYPD)**

Zadaniem zaliczeniowym jest stworzenie biblioteki do przetwarzania pewnego typu danych.
Do biblioteki powinien być załączony skrypt (może być w formie Jupyter notebooka)
pokazujący użycie biblioteki na konkretnych danych. Własne propozycje zadań również
muszą to spełniać.

Opis plików/folderów:

- `script.ipynb` - skrypt pokazujący działanie biblioteki

- `calculate_income` - biblioteka przetwarzająca dane o dochodach PIT w jednostkach 
samorządu terytorialnego Polski

- `data` - dane, na których pokazuję działenie biblioteki 

- `config.ini` -  Informacje o ścieżkach do danych

UWAGA: zaznaczam, że dane są umieszczone wyłącznie po to, żeby zapewnić sprawdzającemu łatwą możliwość uruchomienia skryptu - zdaję sobię sprawę, że co do zasady umieszczanie danych w repozytorium NIE JEST najlepszym pomysłem (bo np. spowalnia klonowanie i w ogólności niepotrzebnie zwiększa rozmiar repozytorium)

- `profile` - wyniki profilowania (omówię je i opowiem o wnioskach podczas egzaminu)

- `setup.py` i `setup.cfg`- pliki umożliwiający instalację przez pip: bibliotekę instaluje się poleceniem: pip install git+https://github.com/CakePL/NYPD_final_project.git
(wszystkie inne potrzebne biblioteki zostaną zainstalowane automatycznie)
 
- `results` - Wyniki zapisuję w arkuszach Excel w folderze
