import seaborn as sns
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# !) load & clean
penguins = sns.load_dataset("penguins")
cols = ["bill_length_mm", "flipper_length_mm", "species"]
df = penguins(cols).dropna()

X = df[["bill_length_mm", "flipper_length_mm"]]
y = df['species']

# 2 ) split(80/20), stratify to preserve class balance
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42,stratify=y)

# 3) Build pipeline
pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter = 1000))
])

# 4) fit on TRAIN only
pipe.fit(X_train, y_train)

# 5) evaluate on TEST
y_pred = pipe.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Test Accuracy (TRAIN -TEST): {acc:.3f}")

# 6) Save the TRAIN-fitted model
joblib.dump(pipe, "penguin_model.pkl")

# 7) save slider metadeta from TRAIN ranges, (keeps UI consistent with training dist)

meta = {
    "bill_length_mm": (float(X_train.bill_length_mm.min()), float(X_train.bill_length_mm.max())),
    "flipper_length_mm": (float(X_train.flipper_length_mm.min()), float(X_train.flipper_length_mm.max())),
    "bill_length_default": (float(X_train.bill_length_mm.mean())),
    "flipper_length_default": (float(X_train.flipper_length_mm.mean())),
    "classes": pipe.classes_.tolist(),
    "test_accuracy": float(acc)
}

pd.Series(meta).to_json("penguin_meta.json")

print("Saved penguin_model.pkl and penguin_meta.json")