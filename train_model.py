import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv("dataset.csv")

X = df[["temperatura", "umidade", "chance_chuva", "velocidade_vento"]]
y = df["risco"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

previsoes = modelo.predict(X_test)
acuracia = accuracy_score(y_test, previsoes)

print(f"Acurácia do modelo: {acuracia:.2f}")

joblib.dump(modelo, "modelo_risco.pkl")

print("Modelo salvo como modelo_risco.pkl")