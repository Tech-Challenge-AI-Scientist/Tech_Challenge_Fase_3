"""Função de extração e tratamento de dados dos Indicadores Educacionais do Brasil."""

import os
from google.cloud import bigquery


def extrair_e_tratar_indicadores_educacionais():
    """Função para extrair e tratar dados dos Indicadores Educacionais do Brasil para os anos de 2021 a 2026."""
    caminho_json = "tech-challenge-2-498401-57b424362f56.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = caminho_json

    print("Autenticando no Google BigQuery...")
    client = bigquery.Client()

    # Adicionado o filtro de ano (2023 a 2026) diretamente na query SQL
    query = """
        SELECT *
        FROM `basedosdados.br_inep_indicadores_educacionais.brasil`
        WHERE ano >= 2021 AND ano <= 2026
    """

    print("Executando a extração dos dados (filtrando anos de 2021 a 2026)...")
    try:
        df = client.query(query).to_dataframe()

        # Verifica se a query retornou dados antes de tentar tratar
        if df.empty:
            print(
                "Aviso: A consulta não retornou nenhum dado para o período de 2021 a 2026."
            )
            print(
                "Pode ser que a base do INEP na Base dos Dados ainda não tenha sido atualizada com esses anos mais recentes."
            )
            return df

        print(
            f"✓ {len(df)} registros extraídos. Iniciando tratamento e limpeza..."
        )

        mapeamento_prefixos = {
            "atu_": "alunos_por_turma_",
            "had_": "horas_aula_diarias_",
            "tdi_": "distorcao_idade_serie_pct_",
            "dsu_": "docentes_ensino_superior_pct_",
            "afd_": "adequacao_formacao_docente_",
            "ird_": "regularidade_docente_",
            "ied_": "esforco_docente_",
            "icg_": "complexidade_gestao_",
            "tnr_": "taxa_nao_resposta_pct_",
            "taxa_aprovacao_": "taxa_aprovacao_pct_",
            "taxa_reprovacao_": "taxa_reprovacao_pct_",
            "taxa_abandono_": "taxa_abandono_pct_",
        }

        novas_colunas = {}
        for col in df.columns:
            nova_col = col
            for sigla, significado in mapeamento_prefixos.items():
                if nova_col.startswith(sigla):
                    nova_col = nova_col.replace(sigla, significado)
                    break
            novas_colunas[col] = nova_col

        df = df.rename(columns=novas_colunas)

        df["ano"] = df["ano"].astype(int)
        df["localizacao"] = df["localizacao"].astype(str)
        df["rede"] = df["rede"].astype(str)

        colunas_metricas = [
            col
            for col in df.columns
            if col not in ["ano", "localizacao", "rede"]
        ]

        df[colunas_metricas] = df[colunas_metricas].astype(float).round(1)

        os.makedirs("data", exist_ok=True)
        caminho_arquivo = os.path.join(
            "data", "indicadores_educacionais_brasil_2021_2026.csv"
        )

        df.to_csv(caminho_arquivo, index=False, encoding="utf-8")

        print("\nAmostra das colunas tratadas:")
        print(df.head())
        print(f"\nSucesso! Arquivo salvo em: {caminho_arquivo}")

        return df

    except Exception as e:
        print(f"Ocorreu um erro durante a extração: {e}")
        return None


df_educacao = extrair_e_tratar_indicadores_educacionais()
