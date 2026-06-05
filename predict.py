import joblib
import pandas as pd

modelo = joblib.load("modelo_risco.pkl")

def prever_risco(temperatura, umidade, chance_chuva, velocidade_vento):
    entrada = pd.DataFrame([{
        "temperatura": temperatura,
        "umidade": umidade,
        "chance_chuva": chance_chuva,
        "velocidade_vento": velocidade_vento
    }])

    resultado = modelo.predict(entrada)[0]

    if resultado == 0:
        return "Baixo risco"
    elif resultado == 1:
        return "Médio risco"
    else:
        return "Alto risco"