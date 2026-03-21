# 🚲 Bike Sales Dashboard

Apresentação interativa de análise de vendas de Mountain Bikes gerada a partir de dados reais em Excel, combinando **Python** para processamento de dados e geração de gráficos com **HTML/CSS/JavaScript** para uma apresentação navegável no navegador.

---

## 📊 Sobre o projeto

O projeto transforma uma planilha de vendas (`Bike_Sales_Pivot_Lab.xlsx`) em uma apresentação visual completa de 8 slides com:

- KPIs de desempenho (receita, lucro, ticket médio)
- Gráficos gerados com Matplotlib e embutidos no HTML
- Navegação lateral interativa
- Design responsivo com tema escuro

**Dados analisados:** 88 pedidos · Dezembro 2021 · 8 países · Mountain Bikes

---

## 🗂️ Estrutura do repositório

```
bike-sales-dashboard/
├── bike_sales_presentation.html   # Apresentação final (arquivo único autocontido)
├── Bike_Sales_Pivot_Lab.xlsx      # Dados brutos de vendas
├── gen_charts.py                  # Script Python para geração dos gráficos
└── README.md
```

> **Nota:** o arquivo HTML é totalmente autocontido — todos os gráficos estão embutidos como Base64, sem dependências externas. Basta abrir no navegador.

---

## 🛠️ Tecnologias utilizadas

| Camada | Tecnologia |
|--------|-----------|
| Processamento de dados | Python 3 · Pandas |
| Geração de gráficos | Matplotlib |
| Interface | HTML5 · CSS3 · JavaScript (vanilla) |
| Fontes | Google Fonts (Inter · Space Grotesk) |
| Dados | Excel (.xlsx) via openpyxl |

---

## 📦 Como executar localmente

### Pré-requisitos

```bash
python3 -m pip install pandas matplotlib openpyxl
```

### 1. Gerar os gráficos

```bash
python3 gen_charts.py
```

Isso cria a pasta `assets/` com os 4 gráficos em PNG:

- `chart_country.png` — receita por país
- `chart_timeline.png` — receita por dia
- `chart_demographics.png` — gênero e faixa etária
- `chart_products.png` — top produtos

### 2. Abrir a apresentação

Abra o arquivo `bike_sales_presentation.html` diretamente no navegador:

```bash
# Linux / macOS
open bike_sales_presentation.html

# Windows
start bike_sales_presentation.html
```

Não é necessário servidor local — o arquivo é totalmente autocontido.

---

## 🖥️ Slides da apresentação

| # | Slide | Conteúdo |
|---|-------|----------|
| 1 | **Capa** | Visão geral com os 4 KPIs principais |
| 2 | **Métricas** | Receita, lucro, ticket médio e custo |
| 3 | **Por País** | Gráfico de barras com insights geográficos |
| 4 | **Timeline** | Curva de receita por dia com pico destacado |
| 5 | **Clientes** | Distribuição por gênero e faixa etária |
| 6 | **Produtos** | Ranking dos top 6 modelos por receita |
| 7 | **Insights** | 6 conclusões estratégicas |
| 8 | **Conclusão** | Recomendações de próximos passos |

---

## 🧭 Navegação

| Ação | Como fazer |
|------|-----------|
| Abrir menu lateral | Clicar no botão ☰ na borda esquerda |
| Ir para um slide | Clicar no item desejado na sidebar |
| Próximo slide | Tecla `→` ou `↓` |
| Slide anterior | Tecla `←` ou `↑` |

---

## 📈 Principais insights dos dados

- **EUA + Austrália** concentram 66% da receita total ($240K de $361K)
- **Clientes femininas** geram 48,5% mais receita que masculinos
- **Adultos (35–64 anos)** representam 57% do faturamento
- **Dias 18–20** concentraram 36% da receita mensal (risco de sazonalidade)
- **Mountain-200 Black, 46** é o produto líder com $71K isolados
- **Margem uniforme de 45,4%** em todos os países e segmentos

---

## 🔄 Regenerando a apresentação com novos dados

1. Substitua o arquivo `Bike_Sales_Pivot_Lab.xlsx` pelos novos dados
2. Execute `python3 gen_charts.py` novamente
3. O script `embed_charts.py` reembute as imagens no HTML automaticamente

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e de portfólio.
