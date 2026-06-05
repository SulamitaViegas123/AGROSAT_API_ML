import requests

API_KEY = "0633da7f24dc99236075364764a483fb"

def buscar_clima(latitude, longitude):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    dados = response.json()

    temperatura = dados["main"]["temp"]
    umidade = dados["main"]["humidity"]
    velocidade_vento = dados["wind"]["speed"]
    descricao = dados["weather"][0]["description"]

    chance_chuva = 0

    if "rain" in dados:
        chance_chuva = 80
    elif "clouds" in dados and dados["clouds"]["all"] > 70:
        chance_chuva = 50
    else:
        chance_chuva = 20

    return {
        "temperatura": temperatura,
        "umidade": umidade,
        "chance_chuva": chance_chuva,
        "velocidade_vento": velocidade_vento,
        "descricao": descricao
    }