import pandas as pd
import requests
import io
import time

def extrair_cadunico_multiplos_anos():
    anos = [2023, 2024, 2025, 2026]
    
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    lista_dfs = []
    
    for ano in anos:
        print(f"Baixando dados do ano: {ano}...")
        
        url = f"https://aplicacoes.mds.gov.br/sagi/servicos/misocial/?fl=codigo_ibge%2Canomes_s%20cadun_qtd_familias_atualizadas_i%20cadun_qtd_familias_atualizadas_pobreza_pbf_i%20cadun_qtd_familias_atualizadas_baixa_renda_i%20cadun_qtd_familias_atualizadas_rfpc_ate_meio_sm_i%20cadun_qtd_familias_atualizadas_rfpc_acima_meio_sm_i%20cadun_qtd_familias_atualizadas_renda_zero_i%20cadun_taxa_atualizacao_cadastral_d%20cadun_taxa_atualizacao_cadastral_rfpc_ate_meio_sm_d&fq=cadun_qtd_familias_cadastradas_i%3A*&q=*%3A*&rows=100000&sort=anomes_s%20desc%2C%20codigo_ibge%20asc&wt=csv&fq=anomes_s:{ano}*"
        
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            df_ano = pd.read_csv(io.BytesIO(response.content))
            lista_dfs.append(df_ano)
            print(f"✓ {len(df_ano)} registros carregados para {ano}.")
        else:
            print(f"Erro na requisição do ano {ano}: Status {response.status_code}")
            
        time.sleep(2)

    if lista_dfs:
        print("\nConsolidando e tratando a base completa...")
        
        df_completo = pd.concat(lista_dfs, ignore_index=True)
        
        colunas_novas = {
            'codigo_ibge': 'codigo_ibge',
            'anomes_s': 'ano_mes',
            'cadun_qtd_familias_atualizadas_i': 'qtd_fam_atualizadas_total',
            'cadun_qtd_familias_atualizadas_pobreza_pbf_i': 'qtd_fam_pobreza',
            'cadun_qtd_familias_atualizadas_baixa_renda_i': 'qtd_fam_baixa_renda',
            'cadun_qtd_familias_atualizadas_rfpc_ate_meio_sm_i': 'qtd_fam_ate_meio_sm',
            'cadun_qtd_familias_atualizadas_rfpc_acima_meio_sm_i': 'qtd_fam_acima_meio_sm',
            'cadun_qtd_familias_atualizadas_renda_zero_i': 'qtd_fam_renda_zero',
            'cadun_taxa_atualizacao_cadastral_d': 'taxa_atualizacao_geral_pct',
            'cadun_taxa_atualizacao_cadastral_rfpc_ate_meio_sm_d': 'taxa_atualizacao_ate_meio_sm_pct'
        }
        df_completo = df_completo.rename(columns=colunas_novas)
        
        df_completo['codigo_ibge'] = df_completo['codigo_ibge'].astype(str)
        
        df_completo['ano_mes'] = pd.to_datetime(df_completo['ano_mes'].astype(str), format='%Y%m').dt.strftime('%Y-%m')
        
        colunas_qtd = [col for col in df_completo.columns if col.startswith('qtd_')]
        df_completo[colunas_qtd] = df_completo[colunas_qtd].fillna(0).astype(int)
        
        colunas_taxa = [col for col in df_completo.columns if col.startswith('taxa_')]
        df_completo[colunas_taxa] = df_completo[colunas_taxa].astype(float).round(2)
        
        df_completo = df_completo.sort_values(by=['ano_mes', 'codigo_ibge'])
        
        print(f"\nTotal de registros na base final: {len(df_completo)}")
        
        nome_arquivo = "dados_cadunico_2023_a_2026.csv"
        df_completo.to_csv(f"./data/{nome_arquivo}", index=False, encoding='utf-8')
        print(f"Sucesso! Arquivo '{nome_arquivo}' salvo na sua máquina.")
        
        return df_completo
    else:
        print("Nenhum dado foi baixado.")
        return None

df_final = extrair_cadunico_multiplos_anos()