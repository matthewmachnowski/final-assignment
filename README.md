Przygotowałem bibliotekę umożliwiającą przetwarzanie danych dotyczących dochodów z PIT w polskich jednostkach samorządu terytorialnego. Biblioteka ta zawiera szereg funkcji, które umożliwiają łatwe i efektywne przetwarzanie danych, m.in. filtrowanie, sortowanie, grupowanie i obliczanie statystyk.

Do biblioteki dołączyłem również skrypt demonstrujący jej użycie na konkretnych zbiorach danych. Skrypt ten przedstawia kroki przetwarzania danych przy użyciu biblioteki oraz interpretuje wyniki w sposób prosty i zrozumiały dla użytkownika.

Opis plików/folderów:

- `calculate_income` - biblioteka przetwarzająca dane o dochodach PIT w jednostkach 
samorządu terytorialnego Polski

- `setup.py` - plik przeznaczony do budowania, dystrybucji i instalacji modułów

- `setup.cfg`- plik ini, zawierający domyślne opcje dla poleceń setup.py

- `data` - dane od dochodów budżetowych pobieranych przez urzędy skarbowe na
rzecz jednostek samorządu terytorialnego za rok 2019 i 2020 (dane, na których pokazuję działenie biblioteki) 

- `results` - folder z zapisanymi wynikami w arkuszach Excel

- `config.ini` -  informacje o ścieżkach do danych

- `script.ipynb` - skrypt pokazujący działanie biblioteki

