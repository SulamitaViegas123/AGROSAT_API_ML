import joblib
import pandas as pd

modelo = joblib.load("modelo_risco.pkl")


def gerar_motivos(temperatura, umidade, chance_chuva, velocidade_vento):
    motivos = []

    if temperatura >= 35:
        motivos.append("Temperatura muito elevada pode causar estresse térmico na plantação.")
    elif temperatura >= 30:
        motivos.append("Temperatura acima do ideal exige atenção ao manejo da cultura.")

    if umidade >= 85:
        motivos.append("Umidade muito alta pode favorecer fungos e doenças nas plantas.")
    elif umidade <= 40:
        motivos.append("Umidade baixa pode indicar risco de ressecamento do solo.")

    if chance_chuva >= 70:
        motivos.append("Alta possibilidade de chuva pode exigir atenção à drenagem da área.")
    elif chance_chuva <= 15:
        motivos.append("Baixa chance de chuva pode exigir monitoramento da irrigação.")

    if velocidade_vento >= 20:
        motivos.append("Ventos fortes podem danificar culturas mais sensíveis.")
    elif velocidade_vento >= 12:
        motivos.append("Vento moderado pode afetar pulverização e manejo agrícola.")

    if not motivos:
        motivos.append("Os indicadores climáticos estão dentro de uma faixa considerada estável.")

    return motivos


def prever_risco(temperatura, umidade, chance_chuva, velocidade_vento):
    entrada = pd.DataFrame([{
        "temperatura": temperatura,
        "umidade": umidade,
        "chance_chuva": chance_chuva,
        "velocidade_vento": velocidade_vento
    }])

    resultado = modelo.predict(entrada)[0]
    probabilidades = modelo.predict_proba(entrada)[0]

    confianca = round(max(probabilidades) * 100, 2)

    motivos = gerar_motivos(
        temperatura,
        umidade,
        chance_chuva,
        velocidade_vento
    )

    if resultado == 0:
        risco = "Baixo risco"
    elif resultado == 1:
        risco = "Médio risco"
    else:
        risco = "Alto risco"

    return {
        "risco": risco,
        "confianca": confianca,
        "motivos": motivos,
        "probabilidades": {
            "Baixo risco": round(probabilidades[0] * 100, 2),
            "Médio risco": round(probabilidades[1] * 100, 2),
            "Alto risco": round(probabilidades[2] * 100, 2)
        }
    }