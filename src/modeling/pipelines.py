"""Pipelines sklearn: pré-processamento + regressor."""

from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline

from src.preprocessing.transformers import build_preprocessor

RANDOM_STATE = 42


def build_ridge_pipeline(feature_names: list[str]) -> Pipeline:
    """Baseline linear para comparação de métricas."""
    return Pipeline(
        [
            ("preprocess", build_preprocessor(feature_names)),
            ("regressor", Ridge(alpha=1.0)),
        ]
    )


def build_hgb_pipeline(feature_names: list[str]) -> Pipeline:
    """Modelo principal: lida melhor com contagens assimétricas."""
    return Pipeline(
        [
            ("preprocess", build_preprocessor(feature_names)),
            (
                "regressor",
                HistGradientBoostingRegressor(
                    max_depth=6,
                    learning_rate=0.08,
                    max_iter=250,
                    l2_regularization=0.1,
                    random_state=RANDOM_STATE,
                ),
            ),
        ]
    )
