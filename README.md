# tech_challenge_fase_3

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Breve descrição do projeto (Desafio Técnico - Fase 3).

## Organização do Projeto

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

## Fontes de Dados para Enriquecimento

Para enriquecer a base principal do projeto, foram utilizadas as seguintes fontes públicas:

- **MDS — MI Social / Cadastro Único:** dados socioeconômicos dos anos de **2023 a 2026**. ([Acesso](https://aplicacoes.mds.gov.br/sagi/servicos/misocial/?fl=codigo_ibge%2Canomes_s%20cadun_qtd_familias_atualizadas_i%20cadun_qtd_familias_atualizadas_pobreza_pbf_i%20cadun_qtd_familias_atualizadas_baixa_renda_i%20cadun_qtd_familias_atualizadas_rfpc_ate_meio_sm_i%20cadun_qtd_familias_atualizadas_rfpc_acima_meio_sm_i%20cadun_qtd_familias_atualizadas_renda_zero_i%20cadun_taxa_atualizacao_cadastral_d%20cadun_taxa_atualizacao_cadastral_rfpc_ate_meio_sm_d&fq=cadun_qtd_familias_cadastradas_i%3A*&q=*%3A*&rows=100000&sort=anomes_s%20desc%2C%20codigo_ibge%20asc&wt=csv&fq=anomes_s:2026*))
- **Base dos Dados — Censo Escolar (`br_inep_censo_escolar.escola`):** dados de **2024**. ([Acesso](https://basedosdados.org/dataset/dae21af4-4b6a-42f4-b94a-4c2061ea9de5?table=15e428cb-cce2-41f8-aec5-066d685b5bd5))
- **Base dos Dados — Indicadores Educacionais Brasil (`br_inep_indicadores_educacionais.brasil`):** dados de **2021 a 2026**. ([Acesso](https://basedosdados.org/dataset/63f1218f-c446-4835-b746-f109a338e3a1?table=cd65b1d2-45e8-432b-afe8-c3a706addbe8))
- **Base dos Dados — Indicadores Educacionais por UF (`br_inep_indicadores_educacionais.uf`):** dados de **2021 a 2026**. ([Acesso](https://basedosdados.org/dataset/63f1218f-c446-4835-b746-f109a338e3a1?table=95f49a8d-fb99-416c-ab92-10bcb523b3a3))