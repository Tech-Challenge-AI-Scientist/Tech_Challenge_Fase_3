"""Exemplos de uso do regressor de alfabetização.

Na raiz do repositório:

    python -m src.modeling.predict_example
"""

from __future__ import annotations

import pandas as pd

from src.evaluation.ranking import rank_risk
from src.modeling.persist import load_pipeline
from src.preprocessing.features import DEFAULT_META, load_features, temporal_holdout


def exemplo_holdout() -> None:
    """Prever a taxa nos recortes do holdout de 2024."""
    model = load_pipeline()
    _, _, X_test, y_test = temporal_holdout(load_features())
    taxa_prevista = model.predict(X_test)

    print("=== Exemplo 1 — holdout 2024 ===")
    print(f"recortes no teste: {len(X_test)}")
    print("primeiras 5 taxas previstas:", [round(float(v), 4) for v in taxa_prevista[:5]])
    print("primeiras 5 taxas observadas:", [round(float(v), 4) for v in y_test.iloc[:5]])

    ranking = rank_risk(X_test, taxa_prevista, y_true=y_test, meta=DEFAULT_META, top_n=5)
    print("\n5 recortes com maior risco (meta 60% - taxa prevista):")
    print(
        ranking[["taxa_prevista", "taxa_observada", "meta_referencia", "risco"]].to_string(
            index=False
        )
    )


def exemplo_recorte_novo() -> None:
    """Prever a taxa de um recorte montado na mão."""
    model = load_pipeline()
    novo = pd.DataFrame(
        [
            {
                "vl_proficiencia_media": 740.0,
                "vl_proficiencia_mediana": 745.0,
                "qt_alunos_avaliados": 120,
                "qtd_fam_pobreza": 1800,
                "qtd_fam_baixa_renda": 500,
                "qtd_fam_renda_zero": 200,
                "taxa_atualizacao_geral_pct": 0.78,
                "taxa_atualizacao_ate_meio_sm_pct": 0.86,
                "qtd_escolas": 18,
                "pct_urbana": 0.65,
                "ds_rede_municipal": 1,
                "ds_rede_privada": 0,
                "nome_regiao_nordeste": 0,
                "nome_regiao_norte": 0,
                "nome_regiao_sudeste": 1,
                "nome_regiao_sul": 0,
                "uf_freq": 0.175,
            }
        ]
    )
    taxa = float(model.predict(novo)[0])
    risco = DEFAULT_META - taxa

    print("\n=== Exemplo 2 — recorte novo ===")
    print(f"taxa prevista: {taxa:.1%}")
    print(f"risco vs meta {DEFAULT_META:.0%}: {risco:+.1%}")
    if risco > 0:
        print("interpretação: deve ficar abaixo da meta de 60%.")
    else:
        print("interpretação: deve atingir ou superar a meta de 60%.")


def main() -> None:
    exemplo_holdout()
    exemplo_recorte_novo()


if __name__ == "__main__":
    main()
