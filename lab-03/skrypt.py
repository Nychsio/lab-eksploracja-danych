import os
import sys

import pandas as pd

# Ścieżka do pliku CSV: z argumentu wiersza poleceń, domyślnie dane.csv
path = sys.argv[1] if len(sys.argv) > 1 else "dane.csv"

# Przerwij z czytelnym komunikatem, jeśli pliku nie ma
if not os.path.exists(path):
    sys.exit(f"Nie znaleziono pliku: {path}")

# Wczytaj dane do DataFrame
df = pd.read_csv(path)

# Wypisz liczbę wierszy i nazwy kolumn
print(f"Liczba wierszy: {len(df)}")
print(f"Kolumny: {list(df.columns)}")
