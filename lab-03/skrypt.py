import sys

import pandas as pd

path = sys.argv[1] if len(sys.argv) > 1 else "dane.csv"
df = pd.read_csv(path)
print(len(df))
