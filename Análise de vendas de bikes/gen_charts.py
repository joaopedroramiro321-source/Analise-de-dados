"""
gen_charts.py
Gera os 4 gráficos da apresentação Bike Sales a partir do Excel de dados.
Saída: pasta assets/ com chart_country.png, chart_timeline.png,
       chart_demographics.png e chart_products.png
"""

import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# ── Configuração ─────────────────────────────────────────────────────────────
DATA_FILE = 'Bike_Sales_Pivot_Lab.xlsx'
OUT_DIR   = 'assets'

BG    = '#0F1629'
TEXT  = '#F1F5F9'
MUTED = '#94A3B8'
GRID  = '#1E2D50'
GREEN = '#10C97B'
BLUE  = '#3B82F6'
AMBER = '#F59E0B'
DARK  = '#2A3F6A'

os.makedirs(OUT_DIR, exist_ok=True)

plt.rcParams.update({
    'font.family':      'DejaVu Sans',
    'axes.facecolor':   'none',
    'figure.facecolor': 'none',
    'text.color':       TEXT,
    'axes.labelcolor':  MUTED,
    'xtick.color':      MUTED,
    'ytick.color':      MUTED,
    'axes.edgecolor':   GRID,
    'axes.spines.top':  False,
    'axes.spines.right':False,
})

# ── Carregar dados ────────────────────────────────────────────────────────────
df = pd.read_excel(DATA_FILE)
df.columns = df.columns.str.strip()
df['Country'] = df['Country'].str.strip()


# ── 1. Receita por país ───────────────────────────────────────────────────────
def chart_country():
    countries = df.groupby('Country')['Revenue'].sum().sort_values().tail(6)
    labels = list(countries.index)
    vals   = countries.values / 1000
    colors = ['#1A2E4A'] * len(vals)
    colors[-1] = GREEN
    colors[-2] = BLUE

    fig, ax = plt.subplots(figsize=(7, 3.8), facecolor='none')
    bars = ax.barh(range(len(labels)), vals, color=colors, height=0.55, zorder=3)
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel('Receita (USD mil)', fontsize=9, labelpad=8)
    ax.xaxis.grid(True, color=GRID, linewidth=0.5, zorder=0)
    ax.set_axisbelow(True)
    for i, (bar, v) in enumerate(zip(bars, vals)):
        ax.text(v + 1.5, i, f'${v:.0f}K', va='center', fontsize=9,
                color=TEXT if i >= len(vals) - 2 else MUTED)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color(GRID)
    plt.tight_layout(pad=1.2)
    fig.savefig(f'{OUT_DIR}/chart_country.png', dpi=150, bbox_inches='tight', transparent=True)
    plt.close()
    print('✓ chart_country.png')


# ── 2. Receita por dia ────────────────────────────────────────────────────────
def chart_timeline():
    days = df.groupby('Day')['Revenue'].sum().sort_index().dropna().reset_index()
    x = days['Day'].astype(int)
    y = days['Revenue'] / 1000

    fig, ax = plt.subplots(figsize=(7, 3.2), facecolor='none')
    ax.fill_between(x, y, alpha=0.15, color=GREEN, zorder=2)
    ax.plot(x, y, color=GREEN, linewidth=2, zorder=3)
    peak = y.idxmax()
    ax.scatter(x[peak], y[peak], color=AMBER, s=80, zorder=5)
    ax.annotate(f'Pico: $70K\nDia {x[peak]}',
                xy=(x[peak], y[peak]), xytext=(x[peak] - 5, y[peak] - 15),
                color=AMBER, fontsize=8,
                arrowprops=dict(arrowstyle='->', color=AMBER, lw=1))
    ax.set_xlabel('Dia do mês', fontsize=9, labelpad=6)
    ax.set_ylabel('Receita (USD mil)', fontsize=9, labelpad=6)
    ax.yaxis.grid(True, color=GRID, linewidth=0.5)
    ax.set_axisbelow(True)
    plt.tight_layout(pad=1.2)
    fig.savefig(f'{OUT_DIR}/chart_timeline.png', dpi=150, bbox_inches='tight', transparent=True)
    plt.close()
    print('✓ chart_timeline.png')


# ── 3. Gênero + faixa etária ─────────────────────────────────────────────────
def chart_demographics():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 3.4), facecolor='none')

    # Donut — gênero
    gender = df.groupby('Customer_Gender')['Revenue'].sum()
    sizes  = [gender.get('F', 0), gender.get('M', 0)]
    ax1.pie(sizes, colors=[GREEN, BLUE], startangle=90,
            wedgeprops=dict(width=0.55, edgecolor='none'))
    ax1.set_title('Gênero', fontsize=10, color=TEXT, pad=10)
    pct_f = sizes[0] / sum(sizes) * 100
    ax1.text(0, 0, f'{pct_f:.0f}%\nFem.', ha='center', va='center',
             fontsize=11, color=TEXT, fontweight='bold')
    ax1.legend(['Feminino', 'Masculino'], loc='lower center', ncol=2,
               fontsize=8, facecolor='none', edgecolor='none',
               labelcolor=MUTED, bbox_to_anchor=(0.5, -0.12))

    # Barras — faixa etária
    age     = df.groupby('Age_Group')['Revenue'].sum()
    labels  = ['Adultos\n(35–64)', 'Jovens\n(25–34)', 'Juventude\n(<25)']
    vals    = [age.get('Adults (35-64)', 0),
               age.get('Young Adults (25-34)', 0),
               age.get('Youth (<25)', 0)]
    pcts    = [v / sum(vals) * 100 for v in vals]
    bars    = ax2.bar(labels, pcts, color=[GREEN, BLUE, AMBER], width=0.5, zorder=3)
    ax2.set_ylabel('%', fontsize=8, color=MUTED)
    ax2.yaxis.grid(True, color=GRID, linewidth=0.5)
    ax2.set_axisbelow(True)
    ax2.set_title('Faixa etária', fontsize=10, color=TEXT, pad=10)
    for bar, p in zip(bars, pcts):
        ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
                 f'{p:.0f}%', ha='center', fontsize=9, color=TEXT)

    plt.tight_layout(pad=1.5)
    fig.savefig(f'{OUT_DIR}/chart_demographics.png', dpi=150, bbox_inches='tight', transparent=True)
    plt.close()
    print('✓ chart_demographics.png')


# ── 4. Top produtos ───────────────────────────────────────────────────────────
def chart_products():
    products = df.groupby('Product_Description')['Revenue'].sum()\
                 .sort_values(ascending=False).head(6)
    labels = list(products.index)
    vals   = products.values / 1000
    colors = [GREEN, BLUE, AMBER, DARK, DARK, DARK]

    fig = plt.figure(figsize=(10, 6.2), facecolor=BG)
    ax  = fig.add_axes([0.09, 0.40, 0.88, 0.54], facecolor=BG)

    x    = np.arange(len(labels))
    bars = ax.bar(x, vals, color=colors, width=0.55, zorder=3)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=38, ha='right', fontsize=11.5, color=TEXT)
    ax.tick_params(axis='x', pad=8)
    ax.tick_params(axis='y', labelsize=10)
    ax.set_ylabel('Receita (USD mil)', fontsize=10, labelpad=8, color=MUTED)
    ax.yaxis.grid(True, color=GRID, linewidth=0.6, zorder=0)
    ax.set_axisbelow(True)
    ax.spines['left'].set_color(GRID)
    ax.spines['bottom'].set_color(GRID)
    for bar, v in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.7,
                f'${v:.0f}K', ha='center', fontsize=11, color=TEXT, fontweight='bold')

    fig.savefig(f'{OUT_DIR}/chart_products.png', dpi=160)
    plt.close()
    print('✓ chart_products.png')


# ── Executar todos ────────────────────────────────────────────────────────────
if __name__ == '__main__':
    chart_country()
    chart_timeline()
    chart_demographics()
    chart_products()
    print('\nTodos os gráficos gerados em:', OUT_DIR)
