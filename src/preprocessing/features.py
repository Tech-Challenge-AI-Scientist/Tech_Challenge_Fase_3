"""Alvo, exclusões de leakage e split temporal do features.csv."""

from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
FEATURES_PATH = REPO_ROOT / "data" / "features" / "features.csv"

TARGET = "pc_indicador_alfabetizacao"
YEAR_COL = "ano_2024"
DEFAULT_META = 0.60

# Mesmo exame que o alvo, constantes, colinearidade ou variação nula.
DROP_ALWAYS = [
    TARGET,
    "vl_proficiencia_media",
    "vl_proficiencia_mediana",
    "nu_serie",
    "ds_rede_privada",
    "pct_rural",
    "qtd_fam_ate_meio_sm",
]


def load_features(path: Path | str | None = None) -> pd.DataFrame:
    """Lê a base já gerada pelo notebook de feature engineering."""
    csv_path = Path(path) if path is not None else FEATURES_PATH
    return pd.read_csv(csv_path)


def feature_columns(df: pd.DataFrame, *, drop_year: bool) -> list[str]:
    """Lista de colunas de X, sem alvo nem leakage."""
    drop = set(DROP_ALWAYS)
    if drop_year:
        drop.add(YEAR_COL)
    return [col for col in df.columns if col not in drop]


def split_xy(
    df: pd.DataFrame, *, drop_year: bool = True
) -> tuple[pd.DataFrame, pd.Series]:
    """Separa preditores e alvo. No holdout temporal, drop_year deve ser True."""
    cols = feature_columns(df, drop_year=drop_year)
    return df[cols].copy(), df[TARGET].copy()


def temporal_holdout(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    """Treino em 2023 (ano_2024==0) e teste em 2024 (ano_2024==1).

    A coluna de ano sai de X para o modelo não saber qual recorte é holdout.
    """
    if YEAR_COL not in df.columns:
        raise KeyError(f"Coluna {YEAR_COL} ausente; não é possível fazer holdout temporal.")

    train_df = df.loc[df[YEAR_COL] == 0].copy()
    test_df = df.loc[df[YEAR_COL] == 1].copy()
    X_train, y_train = split_xy(train_df, drop_year=True)
    X_test, y_test = split_xy(test_df, drop_year=True)
    return X_train, y_train, X_test, y_test
