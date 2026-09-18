# 💧 Calculadora de Consumo de Água

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)

## 📋 Sobre o programa
Sistema desenvolvido em Python que tem como objetivo permitir que o usuário calcule o consumo mensal de água (em m³) do seu imóvel e receba alertas educativos, indicando se o consumo está dentro do padrão, econômico ou excessivo — incentivando o uso consciente da água.

## ⚙️ Funcionalidades
- Identifica o tipo de imóvel (apartamento, casa ou comercial)
- Valida entradas inválidas (texto, números negativos)
- Classifica o consumo com base em regras específicas para cada tipo de imóvel
- Exibe mensagens educativas sobre economia de água

## 📐 Regras de classificação
| Tipo de imóvel | Consumo | Resultado |
|---|---|---|
| Comercial | — | Tarifa comercial aplicada |
| Apartamento | < 10 m³ | Consumo econômico |
| Apartamento ou Casa | até 25 m³ | Consumo moderado |
| Qualquer tipo | acima de 25 m³ | Consumo excessivo |

## 🛠️ Tecnologias utilizadas
- Python 3.14
- Visual Studio Code