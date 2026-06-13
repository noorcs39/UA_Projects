import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split

DATA_PATH = Path(__file__).resolve().parent / "dataset" / "Cleaned_data_after_processing.csv"
df = pd.read_csv(DATA_PATH)

print(df.columns)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=0)

print(y_test)
