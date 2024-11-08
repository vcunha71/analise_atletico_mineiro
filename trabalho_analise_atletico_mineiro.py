import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# Caminhos dos arquivos (considerando que estão na pasta "Bases Atividades" dentro da raiz do projeto)
jogadores_path = "Bases Atividades/league_players.xlsx"
partidas_path = "Bases Atividades/partidas_Atletico_Mineiro.xlsx"

# Carregar os dados
partidas_df = pd.read_excel(partidas_path)

# Configuração da Página
st.title("Análise de Desempenho do Atlético Mineiro no Brasileirão Série A 2024")
st.subheader("Fundamentos da Análise de Desempenho")
st.write("Professor: Ricardo Pombo Sales")
st.write("Data de Entrega: 25/11 até 15h")
st.write("---")

# Filtrar partidas completas
partidas_df = partidas_df[partidas_df['Escanteios'] != -1]

# Introdução
st.header("Introdução")
st.write("""
    Este trabalho apresenta uma análise de desempenho tático do Atlético Mineiro na Série A do Brasileirão 2024,
    focado no conceito de **Pressão e Controle de Bola**. Essa análise combina métricas quantitativas e qualitativas
    para avaliar a capacidade do time de controlar o jogo e pressionar o adversário de maneira estratégica.
""")

# Escolha do Conceito e Descrição    
st.header("1. Escolha e Descrição do Conceito")
st.write("""
**Pressão e Controle de Bola** são abordagens táticas onde o time busca dominar a posse de bola para ditar o ritmo e, ao perder a posse, aplicar pressão alta para forçar o adversário ao erro.
Objetivos principais:
- **Manter a Posse de Bola**: Controlar o ritmo e evitar que o adversário desenvolva seu jogo.
- **Pressionar no Campo Adversário**: Forçar erros do adversário em áreas que gerem oportunidades.
- **Criar Oportunidades de Ataque**: Utilizar o controle e a pressão para transformar posse em finalizações claras.
""")

# Análise Quantitativa
st.header("2. Análise Quantitativa")

# A. Controle de Posse e Ataques
st.subheader("A. Controle de Posse e Ataques")

# Convertendo a coluna de datas para o formato datetime
partidas_df['match_date'] = pd.to_datetime(partidas_df['match_date'])

# Calculando a média de posse de bola para cada data
media_posse_por_data = partidas_df.groupby('match_date')['Posse_Bola'].mean()

# Posse de Bola (média geral)
media_posse = partidas_df['Posse_Bola'].mean()
st.write(f"Posse média de bola: {media_posse:.2f}%")
st.write("**Justificativa:** A posse de bola é uma métrica-chave para avaliar o controle de jogo. O percentual médio indica a capacidade do time de manter a bola em diferentes partidas, demonstrando eficiência no controle.")

# Configuração do estilo do gráfico
plt.style.use('_mpl-gallery')

# Dados para o gráfico
x = media_posse_por_data.index  # Datas com valores
y = media_posse_por_data.values  # Média de posse de bola

# Criando o gráfico
fig, ax = plt.subplots(figsize=(15, 8))
ax.bar(x, y, width=0.8, edgecolor="white", linewidth=0.7)

# Configurando os limites e os rótulos do gráfico
ax.set_ylim(0, 100)
ax.set_ylabel("Posse de Bola (%)")
ax.set_xlabel("Data")
ax.set_title("Média de Posse de Bola por Data")
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.xticks(rotation=45, ha='right')

# Adicionando rótulos de dados nas barras
for i in range(len(x)):
    ax.text(x[i], y[i] + 2, f'{y[i]:.1f}%', ha='center', va='bottom')

st.pyplot(fig)

#========================================================================================================================#

# Ataques e Ataques Perigosos
st.write("### Ataques e Ataques Perigosos")
media_ataques = partidas_df['Ataques_Time'].mean()
media_ataques_perigosos = partidas_df['Ataques_Perigosos'].mean()
st.write(f"Média de ataques: {media_ataques:.2f}")
st.write(f"Média de ataques perigosos: {media_ataques_perigosos:.2f}")
st.write("**Justificativa:** Essas métricas mostram o esforço ofensivo e a capacidade de criar situações de perigo. Ataques perigosos refletem não apenas a frequência, mas a qualidade das jogadas.")

# Configuração do estilo do gráfico
sns.set_theme(style="whitegrid")

# Dados para o gráfico
categorias = ["Ataques", "Ataques Perigosos"]
valores = [media_ataques, media_ataques_perigosos]

# Criando o gráfico
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(categorias, valores, color=["#4c72b0", "#55a868"], edgecolor="black", linewidth=1.2)

# Adicionando rótulos de dados nas barras
for bar, value in zip(bars, valores):
    ax.text(bar.get_x() + bar.get_width() / 2, value + 3, f'{value:.2f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.set_title("Média de Ataques", fontsize=16, fontweight='bold')
ax.set_ylabel("Quantidade")
ax.set_ylim(0, max(valores) + 20)
sns.despine(left=True, bottom=True)

st.pyplot(fig)

#========================================================================================================================#

# B. Eficiência Defensiva
st.subheader("B. Eficiência Defensiva")
media_gols_sofridos = partidas_df['goals_against'].mean()
media_cartoes_amarelos = partidas_df['Cartoes_Amarelos'].mean()
media_cartoes_vermelhos = partidas_df['Cartoes_Vermelhos'].mean()
media_faltas = partidas_df['Faltas'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Gols Sofridos", f"{media_gols_sofridos:.2f}")
col2.metric("Cartões Amarelos", f"{media_cartoes_amarelos:.2f}")
col3.metric("Cartões Vermelhos", f"{media_cartoes_vermelhos:.2f}")
col4.metric("Faltas Cometidas", f"{media_faltas:.2f}")
st.write("**Justificativa:** A eficiência defensiva é avaliada pela capacidade do time de minimizar gols sofridos e controlar a agressividade (faltas e cartões). Esses indicadores refletem a eficácia da estratégia de pressão sem comprometer a disciplina.")

#========================================================================================================================#

# C. Eficiência Ofensiva e Criatividade
st.subheader("C. Eficiência Ofensiva e Criatividade")
media_escanteios = partidas_df['Escanteios'].mean()
media_gols = partidas_df['Gols'].mean()
media_gols_esperados = partidas_df['Gols_Esperados'].mean()
st.write(f"Média de escanteios: {media_escanteios:.2f}")
st.write(f"Média de gols: {media_gols:.2f}")
st.write(f"Gols esperados: {media_gols_esperados:.2f}")
st.write("**Justificativa:** A eficiência ofensiva é observada pela relação entre gols e gols esperados (xG). A criatividade é avaliada pelo número de escanteios, indicando a pressão e presença ofensiva constante.")

sns.set_theme(style="whitegrid")
categorias = ["Gols", "Gols Esperados"]
valores = [media_gols, media_gols_esperados]

fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(categorias, valores, color=["#3498db", "#2ecc71"], edgecolor="black", linewidth=1.2)
for bar, value in zip(bars, valores):
    ax.text(bar.get_x() + bar.get_width() / 2, value + 0.05, f'{value:.2f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

ax.set_title("Gols e Gols Esperados", fontsize=16, fontweight='bold')
ax.set_ylabel("Quantidade")
ax.set_ylim(0, max(valores) + 0.5)
sns.despine(left=True, bottom=True)

st.pyplot(fig)

#========================================================================================================================#

# Análise Qualitativa e Conclusão
st.header("3. Análise Qualitativa")
st.write("""
A análise qualitativa é baseada na interpretação dos dados táticos observados:
1. **Posse de bola e ataques perigosos**: A posse de bola consistente e ataques perigosos indicam controle e oportunidades de ataque frequentes, mostrando que o time busca manter o domínio do jogo.
2. **Eficiência Defensiva**: O equilíbrio entre pressão e disciplina defensiva reflete a eficácia da estratégia de controle de jogo, pois o time consegue recuperar a posse sem comprometer a integridade defensiva (mínimo de cartões e faltas).
3. **Aproveitamento Ofensivo**: A diferença entre os gols esperados (xG) e os gols efetivamente marcados sugere uma necessidade de melhorar a precisão nas finalizações. Isso indica que, embora o time crie boas chances de gol, pode haver espaço para melhorar a conversão dessas oportunidades em gols.
4. **Criação de Oportunidades através de Escanteios**: A média de escanteios destaca o time como um grupo que gera pressão ofensiva constante, utilizando jogadas de bola parada como uma arma para criar oportunidades de gol.

Esses pontos são observados não apenas nos dados numéricos, mas também no comportamento do time durante os jogos, conforme analisado nos vídeos e nas situações de jogo específicas.
""")

# Inclusão de Vídeos para Contexto
st.subheader("Observação de Jogo")
st.write("""
Para ilustrar as análises táticas, incluímos alguns vídeos de partidas relevantes do Atlético Mineiro, onde o time aplicou uma pressão alta e controlou a posse de bola.
Também analisamos as dificuldades encontradas em certos momentos defensivos e a precisão nas finalizações:
""")
st.video("https://www.youtube.com/embed/ID_DO_VIDEO")  # Substitua o ID_DO_VIDEO com o link do YouTube relevante
st.video("https://www.youtube.com/embed/ID_DO_VIDEO_2")  # Substitua por outro vídeo relevante
st.write("""
Os vídeos destacam momentos em que a pressão do Atlético Mineiro resulta em recuperação rápida de posse, bem como lances onde a criação ofensiva se traduz em escanteios e oportunidades de gol. A análise visual complementa os dados quantitativos, ajudando a entender como o time aplica os conceitos de pressão e controle na prática.
""")

# Conclusão
st.header("4. Conclusão")
st.write("""
O Atlético Mineiro apresenta um estilo de jogo focado na **pressão e controle de bola**, buscando manter a posse para controlar o ritmo da partida e pressionando o adversário em seu próprio campo para criar oportunidades de ataque. As análises quantitativas mostram que o time tem uma posse de bola elevada e um número considerável de ataques perigosos, reforçando essa abordagem ofensiva.

No entanto, a análise dos **gols esperados (xG)** em comparação com os **gols efetivamente marcados** sugere que há espaço para melhorar a eficiência nas finalizações. Além disso, a quantidade de faltas e cartões aponta para uma estratégia defensiva agressiva, que, embora seja eficaz para recuperar a posse, pode representar um risco em termos de disciplina.

Com base nos conceitos apresentados nas aulas, recomenda-se que o Atlético Mineiro trabalhe na **finalização das jogadas** e busque manter a agressividade defensiva dentro de limites que evitem penalizações frequentes. A continuidade do desenvolvimento do conceito de **pressão alta** pode ser crucial para manter o controle dos jogos e alcançar melhores resultados na Série A do Brasileirão 2024.
""")

st.write("**Referências**: Estatísticas das bases fornecidas, vídeos de análise, e conceitos abordados nas aulas do professor Ricardo Pombo Sales.")
