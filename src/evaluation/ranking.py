"""Risco educacional: meta de referência menos a taxa prevista."""

import numpy as np
import pandas as pd

from src.preprocessing.features import DEFAULT_META


def rank_risk(
    X: pd.DataFrame,
    y_pred,
    *,
    y_true=None,
    meta: float = DEFAULT_META,
    top_n: int = 20,
) -> pd.DataFrame:
    """Ordena recortes pelo maior risco de ficar abaixo da meta.

    features.csv não traz id_municipio. O ranking é por recorte do holdout.
    """
    predicted = np.clip(np.asarray(y_pred), 0.0, 1.0)
    frame = X.copy()
    frame["taxa_prevista"] = predicted
    frame["meta_referencia"] = meta
    frame["risco"] = meta - predicted
    if y_true is not None:
        frame["taxa_observada"] = np.asarray(y_true)
    return frame.sort_values("risco", ascending=False).head(top_n)
