import os
from datetime import datetime

import pandas as pd
import streamlit as st

from openweather_service import buscar_clima
from predict import prever_risco


st.set_page_config(
    page_title="AgroSat ML",
    page_icon="🌱",
    layout="wide"
)


HISTORICO_ARQUIVO = "historico.csv"


def salvar_historico(latitude, longitude, clima, risco_formatado, recomendacao, prioridade):
    novo_registro = pd.DataFrame([{
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "localidade": clima.get("localidade", "Não informado"),
        "latitude": latitude,
        "longitude": longitude,
        "temperatura": clima["temperatura"],
        "umidade": clima["umidade"],
        "chance_chuva": clima["chance_chuva"],
        "velocidade_vento": clima["velocidade_vento"],
        "descricao": clima["descricao"],
        "risco": risco_formatado,
        "prioridade": prioridade,
        "recomendacao": recomendacao
    }])

    if os.path.exists(HISTORICO_ARQUIVO):
        historico = pd.read_csv(HISTORICO_ARQUIVO)
        historico = pd.concat([historico, novo_registro], ignore_index=True)
    else:
        historico = novo_registro

    historico.to_csv(HISTORICO_ARQUIVO, index=False)


def carregar_historico():
    if os.path.exists(HISTORICO_ARQUIVO):
        return pd.read_csv(HISTORICO_ARQUIVO)

    return pd.DataFrame()


st.title("🌱 AgroSat ML")
st.subheader("Sistema inteligente de previsão de risco agrícola com Machine Learning")

st.markdown("""
O **AgroSat ML** utiliza dados climáticos reais da OpenWeather e um modelo de Machine Learning
para classificar o risco climático de uma propriedade agrícola.

A solução simula a integração com as tabelas do banco do projeto AgroSat, como
`agro_dados_climaticos`, `agro_alertas` e `agro_recomendacoes_ia`.
""")

st.caption("🌦️ Fonte dos dados climáticos: OpenWeather API")
st.caption("🤖 Modelo de Machine Learning: Random Forest Classifier | Acurácia aproximada: 86%")

st.divider()

st.header("📍 Localização da propriedade")

col_lat, col_lon = st.columns(2)

with col_lat:
    latitude = st.number_input(
        "Latitude da propriedade",
        value=-23.5505,
        format="%.6f"
    )

with col_lon:
    longitude = st.number_input(
        "Longitude da propriedade",
        value=-46.6333,
        format="%.6f"
    )


if st.button("🔍 Analisar risco agrícola"):
    with st.spinner("Consultando OpenWeather e analisando dados com Machine Learning..."):
        clima = buscar_clima(latitude, longitude)

        resultado_ia = prever_risco(
            clima["temperatura"],
            clima["umidade"],
            clima["chance_chuva"],
            clima["velocidade_vento"]
        )

    risco = resultado_ia["risco"]

    if risco == "Baixo risco":
        risco_formatado = "🟢 Baixo risco climático para a plantação"
        recomendacao = (
            "Condição climática favorável para o cultivo. "
            "Recomenda-se manter o monitoramento periódico da propriedade."
        )
        prioridade = 1

    elif risco == "Médio risco":
        risco_formatado = "🟡 Médio risco climático para a plantação"
        recomendacao = (
            "Monitorar a umidade, o vento e a possibilidade de chuva nas próximas horas. "
            "A plantação pode exigir atenção preventiva."
        )
        prioridade = 2

    else:
        risco_formatado = "🔴 Alto risco climático para a plantação"
        recomendacao = (
            "Recomenda-se verificar irrigação, drenagem, proteção da cultura "
            "e possibilidade de perdas agrícolas."
        )
        prioridade = 3

    salvar_historico(
        latitude,
        longitude,
        clima,
        risco_formatado,
        recomendacao,
        prioridade
    )

    st.divider()

    st.header("📊 Dados climáticos coletados")

    st.write(f"**Localidade identificada:** {clima.get('localidade', 'Não informado')}")
    st.write(f"**Descrição climática:** {clima['descricao']}")

    card1, card2, card3, card4 = st.columns(4)

    card1.metric("Temperatura", f"{clima['temperatura']} °C")
    card2.metric("Umidade", f"{clima['umidade']}%")
    card3.metric("Chance de chuva", f"{clima['chance_chuva']}%")
    card4.metric("Vento", f"{clima['velocidade_vento']} m/s")

    dados_grafico = pd.DataFrame({
        "Indicador": [
            "Temperatura",
            "Umidade",
            "Chance de chuva",
            "Vento"
        ],
        "Valor": [
            clima["temperatura"],
            clima["umidade"],
            clima["chance_chuva"],
            clima["velocidade_vento"]
        ]
    })

    st.subheader("📈 Visualização dos indicadores")
    st.bar_chart(dados_grafico.set_index("Indicador"))

    st.divider()

    st.header("🤖 Resultado da IA")

    if prioridade == 1:
        st.success(risco_formatado)
    elif prioridade == 2:
        st.warning(risco_formatado)
    else:
        st.error(risco_formatado)

    st.info(f"**Recomendação da IA:** {recomendacao}")

    st.subheader("🔍 Motivos analisados pela IA")

    for motivo in resultado_ia["motivos"]:
        st.write(f"• {motivo}")

    st.subheader("📌 Probabilidade por classe")

    probabilidades_df = pd.DataFrame({
        "Classe": list(resultado_ia["probabilidades"].keys()),
        "Probabilidade (%)": list(resultado_ia["probabilidades"].values())
    })

    st.bar_chart(probabilidades_df.set_index("Classe"))

    st.divider()

    st.header("🗄️ Integração com o banco AgroSat")

    st.markdown(f"""
    A análise realizada seria registrada no banco de dados do AgroSat da seguinte forma:

    **Tabela `agro_dados_climaticos`**
    - Localidade: `{clima.get("localidade", "Não informado")}`
    - Temperatura: `{clima["temperatura"]}`
    - Umidade: `{clima["umidade"]}`
    - Chance de chuva: `{clima["chance_chuva"]}`
    - Velocidade do vento: `{clima["velocidade_vento"]}`
    - Descrição: `{clima["descricao"]}`

    **Tabela `agro_alertas`**
    - Tipo de alerta: `Risco climático agrícola`
    - Descrição: `{risco_formatado}`
    - Nível de risco: `{prioridade}`

    **Tabela `agro_recomendacoes_ia`**
    - Recomendação: `{recomendacao}`
    - Prioridade: `{prioridade}`
    """)

st.divider()

st.header("📚 Histórico de análises")

historico = carregar_historico()

if historico.empty:
    st.info("Nenhuma análise foi realizada ainda.")
else:
    st.dataframe(historico, use_container_width=True)

    st.divider()

st.header("🧪 Simulador técnico do modelo")

st.markdown("""
Esta área permite testar o comportamento do modelo com valores controlados,
sem consultar a OpenWeather. Ela serve para demonstrar que o modelo também
classifica cenários de médio e alto risco.
""")

sim_temp = st.slider("Temperatura simulada", 10, 45, 35)
sim_umidade = st.slider("Umidade simulada", 0, 100, 85)
sim_chuva = st.slider("Chance de chuva simulada", 0, 100, 80)
sim_vento = st.slider("Velocidade do vento simulada", 0, 40, 25)

if st.button("🧠 Testar modelo com dados simulados"):
    resultado_simulado = prever_risco(
        sim_temp,
        sim_umidade,
        sim_chuva,
        sim_vento
    )

    risco_simulado = resultado_simulado["risco"]

    if risco_simulado == "Baixo risco":
        st.success("🟢 Baixo risco climático")
    elif risco_simulado == "Médio risco":
        st.warning("🟡 Médio risco climático")
    else:
        st.error("🔴 Alto risco climático")

    st.write("**Motivos analisados:**")
    for motivo in resultado_simulado["motivos"]:
        st.write(f"• {motivo}")