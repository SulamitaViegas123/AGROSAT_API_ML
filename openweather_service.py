import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def buscar_localidade(latitude, longitude):
    url_geo = "https://api.openweathermap.org/geo/1.0/reverse"

    params_geo = {
        "lat": latitude,
        "lon": longitude,
        "limit": 1,
        "appid": API_KEY
    }

    response_geo = requests.get(url_geo, params=params_geo)
    response_geo.raise_for_status()

    dados_geo = response_geo.json()

    if not dados_geo:
        return "Não identificado"

    cidade = dados_geo[0].get("name", "")
    estado = dados_geo[0].get("state", "")
    pais = dados_geo[0].get("country", "")

    partes = []

    if cidade:
        partes.append(cidade)

    if estado:
        partes.append(estado)

    if pais:
        partes.append(pais)

    if partes:
        return " - ".join(partes)

    return "Não identificado"


def buscar_chance_chuva(latitude, longitude):
    url_previsao = "https://api.openweathermap.org/data/2.5/forecast"

    params_previsao = {
        "lat": latitude,
        "lon": longitude,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    response_previsao = requests.get(url_previsao, params=params_previsao)
    response_previsao.raise_for_status()

    dados_previsao = response_previsao.json()

    primeira_previsao = dados_previsao["list"][0]

    chance_chuva = round(primeira_previsao.get("pop", 0) * 100)

    return chance_chuva


def buscar_clima(latitude, longitude):
    if not API_KEY:
        raise ValueError("API Key da OpenWeather não encontrada. Verifique o arquivo .env.")

    url_clima_atual = "https://api.openweathermap.org/data/2.5/weather"

    params_clima = {
        "lat": latitude,
        "lon": longitude,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    response_clima = requests.get(url_clima_atual, params=params_clima)
    response_clima.raise_for_status()

    dados_clima = response_clima.json()

    temperatura = dados_clima["main"]["temp"]
    umidade = dados_clima["main"]["humidity"]
    velocidade_vento = dados_clima["wind"]["speed"]
    descricao = dados_clima["weather"][0]["description"]

    localidade = buscar_localidade(latitude, longitude)
    chance_chuva = buscar_chance_chuva(latitude, longitude)

    return {
        "localidade": localidade,
        "temperatura": temperatura,
        "umidade": umidade,
        "chance_chuva": chance_chuva,
        "velocidade_vento": velocidade_vento,
        "descricao": descricao
    }