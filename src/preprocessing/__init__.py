"""Seleção de colunas, split temporal e pré-processamento da regressão."""

from src.preprocessing.features import (
    DEFAULT_META,
    DROP_ALWAYS,
    FEATURES_PATH,
    TARGET,
    YEAR_COL,
    feature_columns,
    load_features,
    split_xy,
    temporal_holdout,
)
from src.preprocessing.transformers import build_preprocessor

__all__ = [
    "DEFAULT_META",
    "DROP_ALWAYS",
    "FEATURES_PATH",
    "TARGET",
    "YEAR_COL",
    "build_preprocessor",
    "feature_columns",
    "load_features",
    "split_xy",
    "temporal_holdout",
]
