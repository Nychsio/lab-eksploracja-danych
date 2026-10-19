import os
import sys

import pandas as pd

path = sys.argv[1] if len(sys.argv) > 1 else "dane.csv"
if not os.path.exists(path):
    sys.exit(f"Nie znaleziono pliku: {path}")
df = pd.read_csv(path)
print(f"Liczba wierszy: {len(df)}")
print(f"Kolumny: {list(df.columns)}")
