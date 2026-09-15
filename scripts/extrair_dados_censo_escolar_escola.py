"""Função de extração de dados do Censo Escolar."""

import os
import pandas as pd
from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()


def extrair_censo_escolar_alfabetizacao():
    """Função para extrair dados do Censo Escolar para os anos de 2023 e 2024."""
    print("Autenticando no Google BigQuery...")
    client = bigquery.Client()

    # Apenas 2023 e 2024 apenas colunas relevantes para modelos de aprendizado/alfabetização
    query = """
        SELECT
            ano, sigla_uf, id_municipio, id_escola, rede,
            tipo_localizacao, tipo_situacao_funcionamento,
            agua_potavel, energia_rede_publica, esgoto_rede_publica,
            biblioteca, sala_leitura, laboratorio_informatica,
            internet, internet_alunos,
            desktop_aluno, computador_portatil_aluno, tablet_aluno,
            quantidade_sala_utilizada, sala_atendimento_especial
        FROM `basedosdados.br_inep_censo_escolar.escola`
        WHERE ano in (2023,2024)
    """

    print("Executando a extração dos dados de 2024...")
    try:
        df = client.query(query).to_dataframe()

        if df.empty:
            print(
                "Aviso: A consulta não retornou nenhum dado para 2024. A base pode não estar atualizada ainda."
            )
            return df

        print(f"✓ {len(df)} escolas extraídas. Tratando os dados...")

        colunas_identificacao = ["sigla_uf", "id_municipio", "id_escola"]
        for col in colunas_identificacao:
            if col in df.columns:
                df[col] = df[col].astype(str)

        if "ano" in df.columns:
            df["ano"] = pd.to_numeric(df["ano"], downcast="integer")

        # Exportação para CSV
        os.makedirs("data", exist_ok=True)
        caminho_arquivo = os.path.join("data", "censo_escolar_2023_2024.csv")

        df.to_csv(caminho_arquivo, index=False, encoding="utf-8")

        print("\nAmostra dos dados extraídos:")
        print(df.head())
        print(
            f"\nSucesso! Arquivo pronto para o modelo salvo em: {caminho_arquivo}"
        )

        return df

    except Exception as e:
        print(f"Ocorreu um erro durante a extração: {e}")
        return None


df_escolas_2024 = extrair_censo_escolar_alfabetizacao()
