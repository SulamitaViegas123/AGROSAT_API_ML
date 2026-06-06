# 🌱 AGROSAT ML

Sistema inteligente de previsão de risco agrícola utilizando **OpenWeather API** e **Machine Learning**.

---

## 📌 Objetivo

O **AgroSat ML** tem como objetivo auxiliar produtores rurais na identificação de riscos climáticos que possam afetar suas plantações.

A aplicação coleta dados climáticos reais a partir da latitude e longitude de uma propriedade agrícola, processa essas informações com um modelo de Machine Learning e retorna uma classificação de risco climático.

---

## 🚀 Tema da Global Solution

O projeto está conectado à proposta da Global Solution por aplicar tecnologia, dados, APIs, automação e inteligência artificial em um problema real do agronegócio: o monitoramento climático de áreas agrícolas.

---

## 🧠 Trilha escolhida

A trilha escolhida foi:

**Machine Learning**

O sistema utiliza um modelo treinado para classificar o risco climático em três níveis:

* 🟢 Baixo risco climático
* 🟡 Médio risco climático
* 🔴 Alto risco climático

---

## 🛠️ Tecnologias utilizadas

* Python
* Streamlit
* Pandas
* Scikit-learn
* Joblib
* Requests
* OpenWeather API
* Random Forest Classifier
* CSV para histórico local

---

## 🔄 Como funciona o projeto

O fluxo da solução é:

```txt
dataset.csv
↓
train_model.py
↓
modelo_risco.pkl
↓
app.py
↓
OpenWeather API
↓
predict.py
↓
Resultado da IA
↓
historico.csv
```

Explicando de forma simples:

1. O arquivo `dataset.csv` contém dados climáticos simulados usados para treinar o modelo.
2. O arquivo `train_model.py` treina o modelo de Machine Learning.
3. Após o treinamento, é gerado o arquivo `modelo_risco.pkl`.
4. O dashboard é executado pelo arquivo `app.py`.
5. O usuário informa latitude e longitude da propriedade agrícola.
6. O sistema consulta a OpenWeather API.
7. Os dados climáticos reais são enviados para o modelo.
8. O modelo retorna o nível de risco climático.
9. O resultado é exibido no dashboard.
10. A análise é salva no arquivo `historico.csv`.

---

## 🌦️ Integração com OpenWeather

A integração com a OpenWeather acontece no arquivo:

```txt
openweather_service.py
```

A aplicação envia:

* Latitude
* Longitude
* API Key

E recebe dados reais como:

* Temperatura
* Umidade
* Velocidade do vento
* Descrição climática

---

## 🤖 Machine Learning

O modelo utilizado foi o:

```txt
Random Forest Classifier
```

Ele foi treinado com os seguintes dados:

* Temperatura
* Umidade
* Chance de chuva
* Velocidade do vento
* Risco climático

Classificação:

```txt
0 = Baixo risco
1 = Médio risco
2 = Alto risco
```

A acurácia obtida no treinamento foi de aproximadamente:

```txt
86%
```

---

## 🗄️ Integração com o banco AgroSat

Nesta versão, os dados das análises são armazenados localmente no arquivo:

```txt
historico.csv
```

O projeto também simula a integração com as tabelas do banco relacional do AgroSat:

* `agro_dados_climaticos`
* `agro_alertas`
* `agro_recomendacoes_ia`

Essas tabelas representam, respectivamente:

* Armazenamento dos dados climáticos coletados
* Registro dos alertas gerados pela IA
* Registro das recomendações inteligentes

---

## ▶️ Como executar o projeto

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Treinar o modelo

```bash
python train_model.py
```

Esse comando gera o arquivo:

```txt
modelo_risco.pkl
```

### 3. Executar o dashboard

```bash
python -m streamlit run app.py
```

### 4. Acessar no navegador

O Streamlit abrirá automaticamente. Caso não abra, acesse:

```txt
http://localhost:8501
```

---

## 🔑 Configuração da API Key

No arquivo `openweather_service.py`, insira sua chave da OpenWeather:

```python
API_KEY = "SUA_CHAVE_AQUI"
```

---

## ✅ Resultado esperado

Após informar latitude e longitude, o sistema exibe:

* Dados climáticos reais
* Gráfico dos indicadores
* Resultado da IA
* Recomendação automática
* Histórico das análises
* Simulação de integração com banco de dados

---

## 👨‍💻 Status do projeto

Projeto funcional com:

* ✅ Consulta real à OpenWeather API
* ✅ Modelo de Machine Learning treinado
* ✅ Dashboard interativo
* ✅ Histórico de análises
* ✅ Simulação de integração com banco relacional
* ✅ Diagrama de arquitetura
* ✅ Documentação de execução

---

## 📚 Disciplina

Projeto desenvolvido para a disciplina:

**Disruptive Architectures: IoT, IoB & Generative IA**

Dentro da **Global Solution - FIAP**.

---

# 👥 Integrantes

| RM | Nome |
|---|---|
| RM560914 | Lucas Siqueira de Almeida |
| RM561090 | Matteus Viegas dos Santos |
| RM561089 | Sulamita Viegas dos Santos |
