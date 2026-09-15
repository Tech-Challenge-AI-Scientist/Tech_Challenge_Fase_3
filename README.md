# Tech Challenge Fase 3 - Predição de alfabetização

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

[![Python](https://img.shields.io/badge/python-3.12.6-blue.svg)](https://python.org)

> Modelos de predição de alfabetização de escolas e municipios brasileiros, com base em variáveis educacionais, socioeconômicas e territorial

# Contexto do problema e objetivo analítico

A alfabetização na infância é um dos pilares fundamentais para o desenvolvimento educacional, social e econômico do Brasil. O Compromisso Nacional Criança Alfabetizada mobiliza União, estados e municípios com a meta de garantir que todas as crianças estejam alfabetizadas até o final do 2º ano do ensino fundamental.

O Indicador Criança Alfabetizada - baseado no ponto de corte de 743 pontos na escala SAEB, é o principal termômetro desta política pública. A meta nacional é atingir 100% de alfabetização até 2030.

Este projeto é uma continuação do projeto da Fase 2, no qual foi construída uma pipeline de dados para coletar e tratar dados de indicadores educacionais, disponibilizados gratuitamente pelo governo brasileiro. 

Neste projeto, tais dados serão enriquecidos com variáveis socioeconômicas e territoriais, explorados para obter insights e elencar quais são os fatores de maior impacto na alfabetização das cidades brasileiras, e, por fim, serão construídos dois modelos de predição: um modelo de regressão para prever a porcentagem dos alunos de uma determinada escola serão alfabetizados, e um modelo de classificação para prever se aquela cidade irá atingir a meta de alfabetização ou não.

Com a análise exploratória dos dados, será possível mapear quais são os fatores que mais impactam na probabilidade das crianças de uma determinada localidade ser alfabetizada. A partir dos modelos, por sua vez, será possível compreender quais cidades e escolas estão mais distantes de cumprirem suas metas de alfabetização, para, assim, conseguir redirecionar recursos e políticas públicas para auxiliar no desenvolvimento da educação das mesmas. 

# Organização do Projeto

```text
├── Makefile           <- Comandos de atalho do Makefile (ex: `make data`)
├── README.md          <- O README principal para quem for avaliar ou colaborar no projeto
├── data               <- Pasta para armazenar os conjuntos de dados do projeto
│
├── images             <- Imagens de apoio (arquitetura, prints para este README, etc.)
│
├── notebooks          <- Jupyter notebooks. A convenção de nomenclatura ideal é sequencial
│                         e descritiva (ex: `1.0-exploracao-inicial.ipynb`).
│
├── pyproject.toml     <- Arquivo de configuração do projeto (metadados e ferramentas)
│
├── reports            <- Análises, resultados e relatórios gerados
│
├── setup.cfg          <- Arquivo de configuração para formatação de código (ex: flake8)
│
├── .env               <- Variáveis de ambiente (senhas, chaves) - NÃO enviar para o GitHub
├── .gitignore         <- Lista de arquivos e pastas que o Git deve ignorar
│
└── src                <- Código-fonte principal do projeto
    │
    ├── evaluation     <- Scripts para avaliação de métricas e performance dos modelos
    │
    ├── modeling       <- Scripts para treinar algoritmos e realizar inferências/predições
    │
    ├── preprocessing  <- Scripts para limpeza, tratamento e engenharia de features
    │
    └── visualization  <- Scripts para geração de gráficos estruturados

```
# Configurando o projeto

1. Instale, se ainda não tiver:

- **Python 3.12.6+**
- [Poetry](https://python-poetry.org/) (gerenciador de dependências)

2. Na raiz do projeto, instale as dependências:

```bash
git clone https://github.com/Tech-Challenge-AI-Scientist/Tech_Challenge_Fase_3
cd tech_challenge_fase_3

# Instalar dependências
poetry install
```

3. Adicione no repositório sua chave .json do BigQuery.

4. Crie o arquivo .env e adicione nele a variável GOOGLE_APPLICATION_CREDENTIALS o path da chave.

5. Adicione o path da sua chave do BigQuery no .gitignore

# Dicionário de dados

## Fontes de Dados para Enriquecimento

Para enriquecer a base principal do projeto, foram utilizadas as seguintes fontes públicas:

- **MDS — MI Social / Cadastro Único:** dados socioeconômicos dos anos de **2023 a 2026**. ([Acesso](https://aplicacoes.mds.gov.br/sagi/servicos/misocial/?fl=codigo_ibge%2Canomes_s%20cadun_qtd_familias_atualizadas_i%20cadun_qtd_familias_atualizadas_pobreza_pbf_i%20cadun_qtd_familias_atualizadas_baixa_renda_i%20cadun_qtd_familias_atualizadas_rfpc_ate_meio_sm_i%20cadun_qtd_familias_atualizadas_rfpc_acima_meio_sm_i%20cadun_qtd_familias_atualizadas_renda_zero_i%20cadun_taxa_atualizacao_cadastral_d%20cadun_taxa_atualizacao_cadastral_rfpc_ate_meio_sm_d&fq=cadun_qtd_familias_cadastradas_i%3A*&q=*%3A*&rows=100000&sort=anomes_s%20desc%2C%20codigo_ibge%20asc&wt=csv&fq=anomes_s:2026*))
- **Base dos Dados — Censo Escolar (`br_inep_censo_escolar.escola`):** dados de **2024**. ([Acesso](https://basedosdados.org/dataset/dae21af4-4b6a-42f4-b94a-4c2061ea9de5?table=15e428cb-cce2-41f8-aec5-066d685b5bd5))
- **Base dos Dados — Indicadores Educacionais Brasil (`br_inep_indicadores_educacionais.brasil`):** dados de **2021 a 2026**. ([Acesso](https://basedosdados.org/dataset/63f1218f-c446-4835-b746-f109a338e3a1?table=cd65b1d2-45e8-432b-afe8-c3a706addbe8))
- **Base dos Dados — Indicadores Educacionais por UF (`br_inep_indicadores_educacionais.uf`):** dados de **2021 a 2026**. ([Acesso](https://basedosdados.org/dataset/63f1218f-c446-4835-b746-f109a338e3a1?table=95f49a8d-fb99-416c-ab92-10bcb523b3a3))

## Fontes de dados principais e features

| Base | Caminho | Origem | Função
|---|---|---|---|
| Wide analítica | `data/wide_analitica_alfabetizacao.csv` | Gerada na camada gold do desafio da Fase 2 | Tabela principal da EDA e das features
| Features | `data/features/features.csv` | Feature Engineering | Entrada do modelo de regressão

**Granularidade:** uma linha = município + rede de ensino + ano. Anos 2023 e 2024. Série sempre o **2º ano**.

A wide é a  O `features.csv` parte dela, junta CadÚnico (dezembro de cada ano) e Censo Escolar, aplica dummies/frequency encoding e **remove `id_municipio`** para o modelo não decorar o código IBGE.

---

## Escala dos percentuais (não misturar)

| Campo | Na wide | No features.csv |
|---|---|---|
| `pc_indicador_alfabetizacao` | 0–100 (ex.: `48,98` = 48,98%) | 0–1 (ex.: `0,4898`) — dividido por 100 no FE |
| Taxas do CadÚnico / % urbana e rural | — | 0–1 |
| Metas (`pc_meta_*`, `pc_taxa_alfabetizacao`, participação) | 0–100 | não entram no features |

Proficiência (`vl_proficiencia_*`) fica na **mesma escala numérica** nas duas bases (pontos da prova, em torno de 750).

---

## 1. `wide_analitica_alfabetizacao.csv`

### Chaves e identificação

| Coluna | Tipo | Papel | Descrição |
|---|---|---|---|
| `id_municipio` | int | Chave | Código IBGE do município (7 dígitos, com dígito verificador). No FE, `id_municipio // 10` alinha com `codigo_ibge` do CadÚnico. |
| `nu_ano` | int | Chave | Ano da observação (2023 ou 2024). |
| `ds_rede` | str | Chave / contexto | Rede: Municipal, Estadual ou Privada. |
| `nu_rede` | int | Contexto | Código numérico da rede (par de `ds_rede`). |
| `nu_serie` | int | Contexto | Série escolar. Nesta base vale sempre **2** (2º ano). |
| `id_indicador_municipio` | int | Técnico | Identificador interno do registro do indicador. Não usar como feature. |
| `ts_insercao` | str | Técnico | Data/hora de carga na base. Não usar como feature. |

### Território

| Coluna | Tipo | Papel | Descrição |
|---|---|---|---|
| `nome_uf` | str | Contexto | Nome da unidade federativa. |
| `sigla_uf` | str | Contexto | Sigla da UF (ex.: `MG`). |
| `nome_regiao` | str | Contexto | Grande região: Norte, Nordeste, Centro-Oeste, Sudeste, Sul. |

### Indicador de alfabetização (educacional)

| Coluna | Tipo | Papel | Descrição |
|---|---|---|---|
| `pc_indicador_alfabetizacao` | float | **Alvo** | Percentual de alunos considerados alfabetizados no recorte (0–100). Proxy de label usado no modelo (depois convertido para 0–1). |
| `pc_indicador_alfabetizacao_corte` | float | Relacionado ao alvo | Mesma lógica com corte/limiar alternativo. Em muitos recortes coincide com o indicador principal. Não entra no `features.csv`. |
| `qt_alunos_avaliados` | int | Contexto | Número de alunos avaliados. Volume da amostra; recortes muito pequenos têm mais ruído. |
| `qt_alunos_alfabetizados` | int | Relacionado ao alvo | Contagem de alfabetizados. Com `qt_alunos_avaliados` reconstitui a taxa. Não entra no features (redundante com o alvo). |
| `qt_alunos_alfabetizados_corte` | int | Relacionado ao alvo | Contagem com o critério de corte. Não entra no features. |
| `vl_proficiencia_media` | float | Preditor (modelo) | Média da proficiência em leitura/escrita no recorte. Rendimento geral; relação direta com alfabetização. |
| `vl_proficiencia_mediana` | float | Preditor (modelo) | Mediana da proficiência no recorte. Mesma interpretação da média, menos sensível a extremos. |

### Metas e comparação (não entram no X do modelo)

Derivadas do próprio indicador ou da política de metas. Úteis para avaliar “atingiu a meta?”, não para treinar o regressor (risco de leakage).

| Coluna | Tipo | Papel | Descrição |
|---|---|---|---|
| `pc_taxa_alfabetizacao` | float | Meta / resultado | Taxa de alfabetização na série de metas (0–100). Pode diferir levemente do `pc_indicador_alfabetizacao`. |
| `pc_participacao_meta` | float | Contexto de meta | Percentual de participação associado à meta (0–100). |
| `pc_meta_2024` … `pc_meta_2030` | float | Meta oficial | Trajetória de meta de alfabetização do recorte, ano a ano (0–100). Há nulos em parte da base. |
| `pc_meta_ano_corrente` | float | Meta | Meta do ano da linha. Muitos nulos em 2023 na amostra. |
| `vl_gap_meta_resultado` | float | Resultado | Diferença entre meta e resultado. Muitos nulos; não usar como feature. |

---

## 2. `features.csv`

Gerado em `notebooks/feature_engineering.ipynb`. Colunas da wide selecionadas na EDA + CadÚnico + Censo, já numéricas.

**Papel no modelo de regressão** (lista `DROP_ALWAYS` e split temporal):

- **Alvo:** `pc_indicador_alfabetizacao`
- **Entra em X (17 colunas):** as duas proficiências, alunos avaliados, CadÚnico (exceto a soma), escolas, % urbana, dummies de rede e região, `uf_freq`
- **Sai sempre:** `nu_serie` (constante), `pct_rural` (espelho de urbana), `qtd_fam_ate_meio_sm` (soma de pobreza + baixa renda)
- **Sai só no holdout:** `ano_2024` (separa treino 2023 / teste 2024; se ficasse em X, o modelo saberia o recorte de teste)

### Educacionais (vindas da wide)

| Coluna | Tipo | Papel no modelo | Descrição |
|---|---|---|---|
| `pc_indicador_alfabetizacao` | float | Alvo | Taxa de alfabetização em **0–1**. |
| `vl_proficiencia_media` | float | X | Rendimento médio em leitura/escrita. |
| `vl_proficiencia_mediana` | float | X | Rendimento mediano em leitura/escrita. |
| `qt_alunos_avaliados` | int | X | Alunos avaliados no recorte. |
| `nu_serie` | int | Excluída | Sempre 2; não informa. |

### Socioeconômicas (CadÚnico, estoque de dezembro)

Famílias no Cadastro Único do município na última aferição do ano. A junção é por município/ano (não por rede): o mesmo estoque se repete nas linhas Municipal/Estadual/Privada daquele município.

| Coluna | Tipo | Papel no modelo | Descrição |
|---|---|---|---|
| `qtd_fam_pobreza` | int | X | Famílias em situação de pobreza. |
| `qtd_fam_baixa_renda` | int | X | Famílias de baixa renda. |
| `qtd_fam_ate_meio_sm` | int | Excluída | Famílias com renda até meio salário mínimo. É a **soma** de pobreza + baixa renda. |
| `qtd_fam_renda_zero` | int | X | Famílias com renda zero. |
| `taxa_atualizacao_geral_pct` | float | X | Taxa de atualização cadastral geral (0–1). |
| `taxa_atualizacao_ate_meio_sm_pct` | float | X | Taxa de atualização entre famílias até meio SM (0–1). |

### Escolares (Censo Escolar, agregado no município/ano)

| Coluna | Tipo | Papel no modelo | Descrição |
|---|---|---|---|
| `qtd_escolas` | int | X | Quantidade de escolas no município naquele ano. |
| `pct_urbana` | float | X | Proporção de escolas em área urbana (0–1). |
| `pct_rural` | float | Excluída | Proporção rural (0–1). Vale `pct_urbana + pct_rural = 1`. |

### Dummies e encoding (`pd.get_dummies(..., drop_first=True)` + frequência)

Categorias **omitidas** (todas as dummies do grupo = 0) são a referência.

| Coluna | Tipo | Papel no modelo | Descrição |
|---|---|---|---|
| `ano_2024` | int (0/1) | Só no split | 1 = 2024, 0 = 2023 (referência). |
| `ds_rede_municipal` | int (0/1) | X | 1 = rede municipal. |
| `ds_rede_privada` | int (0/1) | X | 1 = rede privada. **Estadual** = ambos 0. Categoria rara; o campo existe para não misturar Privada com Estadual. |
| `nome_regiao_nordeste` | int (0/1) | X | 1 = Nordeste. |
| `nome_regiao_norte` | int (0/1) | X | 1 = Norte. |
| `nome_regiao_sudeste` | int (0/1) | X | 1 = Sudeste. |
| `nome_regiao_sul` | int (0/1) | X | 1 = Sul. **Centro-Oeste** = todas as dummies de região = 0. |
| `uf_freq` | float | X | Frequency encoding da UF: participação daquela UF nas linhas da base (25 valores distintos; não são 27 UFs). |

### Como ler rede e região (resumo)

| Situação | Como aparece no features |
|---|---|
| Rede Estadual | `ds_rede_municipal = 0` e `ds_rede_privada = 0` |
| Rede Municipal | `ds_rede_municipal = 1` e `ds_rede_privada = 0` |
| Rede Privada | `ds_rede_municipal = 0` e `ds_rede_privada = 1` |
| Centro-Oeste | as quatro `nome_regiao_*` = 0 |
| Ano 2023 | `ano_2024 = 0` |

---

# Padronização de Código e Automação com Pre-commit

Este projeto utiliza **Black** (formatter), **Flake8** (linter) e **pre-commit hooks** para garantir padronização automática do código antes de cada commit.
As dependências são gerenciadas via **Poetry**, e toda a configuração dos linters está centralizada no `pyproject.toml`.

- Ativando os hooks do pre-commit

   Os hooks do pre-commit não são versionados pelo Git, portanto cada pessoa que clonar o repositório precisa ativá-los manualmente:

   ```bash
   poetry run pre-commit install
   ```

- Rodando pre-commit em todos os arquivos (opcional e recomendado)

   Para validar todo o projeto logo após a instalação:

   ```bash
   poetry run pre-commit run --all-files
   ```

   Isso aplica o Black e executa o Flake8 em todos os arquivos existentes.

## Executando a pipeline completa

1. Execute os scripts de extração dos dados

```
poetry run python -m scripts.extrair_dados_cadunico
poetry run python -m scripts.extrair_dados_censo_escolar_escola
poetry run python -m scripts.extrair_dados_indicadores_educacionais_brasil
poetry run python -m scripts.extrair_dados_indicadores_educacionais_uf
```

2. Execute o notebook da [análise exploratória](notebooks\eda_alfabetizacao.ipynb): Nele, está a análise das bases de dados coletadas, exploração dos dados e decisão de quais são as variáveis mais decisivas para serem utilizadas no modelo.

3. Execute o notebook da [engenharia de features](notebooks\feature_engineering.ipynb) para gerar o arquivo .csv com as features de treinamento dos modelos

4. Execute o notebook do treinamento dos modelos:

4.1 [Modelo de Regressão](notebooks\ridge_and_hgb.ipynb) - Prevê a porcentagem de alfabetização de uma determinada escola em um determinado município no ano observado

4.2 Modelo de Classificação - [Regressão Logística (baseline)](notebooks\logistic_regression.ipynb) e [Árvore de Decisão](notebooks\decision_tree.ipynb) - Prevêm se uma determinada escola em um determinado município no ano observado cumprirá sua meta de alfabetização

## Aplicação estratégica e insights

1. Quais fatores mais impactam na alfabetização?

De acordo com a EDA, os fatores de maior impacto são:
- Rendimento médio em dos alunos em leitura/escrita: escolas com maior rendimento tendem a ter índices de alfabetização maior;
- Índices de pobreza e renda no município: municípios mais pobres constumam ter seus índices de alfabetização comprometidos;
- Região do Brasil na qual estão situadas: escolas das regiões Norte e Nordeste, pelo contexto socioeconômico destas regiões, costumam ter taxas menores de alfabetização

2. Quais municipios apresentam maior risco educacional?

Municipios situados nas regiões Norte e Nordeste, com maiores índices de pobreza.

3. Quais regiões possuem padrões semelhantes?

As regiões Sul, Sudeste e Centro-Oeste possuem padrões semelhantes de alfabetização, com índices melhores que as regiões Norte e Nordeste.

4. Como prever municipios que podem não atingir metas futuras?

É possível, a partir do modelo de classificação desenvolvido, prever quais municípios possuem menor probabilidade de atingirem suas metas com uma acurácia de 92%, e o modelo de regressão pode ser utilizado para detalhar ainda mais este número, prevendo, com RMSE de apenas 5%, a porcentagem de alfabetização de uma determinada escola e munícipio.

5. Quais variáveis possuem mais influência nos modelos?

 `vl_proficiencia_media` e `vl_proficiencia_mediana` - Média e mediana da proficiência em leitura/escrita no recorte.