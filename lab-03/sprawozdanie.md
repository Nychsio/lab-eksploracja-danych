# Sprawozdanie – Laboratorium 3

Skrypt `skrypt.py` wczytuje plik CSV (podany jako argument, domyślnie `dane.csv`) i wypisuje liczbę wierszy oraz nazwy kolumn.

## Opis commitów

- `d165ffc` – dodano skrypt wczytujący CSV: pierwsza wersja, która wczytuje plik przez pandas i wypisuje liczbę wierszy.
- `44f4d09` – dodano wypisanie nazw kolumn: od razu widać strukturę wczytanych danych.
- `e7a0939` – poprawiono czytelność wyniku: liczba wierszy i kolumny są opisane etykietami zamiast surowych wartości.
- `261631c` – dodano sprawdzenie istnienia pliku: brak pliku kończy działanie czytelnym komunikatem zamiast błędu pandas.
- `f5568b0` – dodano komentarze opisujące kolejne kroki skryptu: ścieżkę, sprawdzenie pliku, wczytanie danych i wypisanie wyników.
- `58e75b1` – dodano komentarz `#dodatkowa liniaO` (bez wpływu na działanie) oraz zrzut ekranu wyniku `git status` i `git diff`.
- `275d1cc` – dodano `.gitignore` z regułami dla plików tymczasowych, przeniesiono zrzut `status-diff.png` do katalogu `screenshots/` i dodano kolejne zrzuty ekranu.

## Zadania samodzielne

### Zadanie 1: Konflikt scalania

Na dwóch branchach zmieniono tę samą linię `README.md` w różny sposób (commity `31c3583` i `210f089`). Przy próbie scalenia Git nie mógł sam wybrać wersji, więc zgłosił konflikt. Rozwiązanie zostało zapisane w commicie `c89ac28`.

### Zadanie 2: Plik .gitignore

Utworzono `.gitignore` z regułami `*.log`, `__pycache__/` i `.ipynb_checkpoints/`, dzięki czemu plik `lab-03/debug.log` przestał pojawiać się w `git status`. Reguły zostały zapisane w commicie `275d1cc`, a różnice w skrypcie sprawdzono poleceniem `git diff`.

### Zadanie 3: Historia i cofanie

Na branchu `lab-03-historia` dodano błędną linię `print(f"zle dane")` w commicie `d96db43`. Następnie cofnięto ją poleceniem `git revert`, który utworzył commit `49a79b4` zamiast kasować historię. Dzięki temu błędna linia zniknęła z pliku, a w `git log` widać obie zmiany.
