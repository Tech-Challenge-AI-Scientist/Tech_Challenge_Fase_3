from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd


def shap_values(
    model,
    X: pd.DataFrame,
    *,
    max_samples: int = 400,
    random_state: int = 42,
):
    """SHAP no regressor sklearn, com features já transformadas pelo pipeline."""
    import shap

    preprocess = model.named_steps["preprocess"]
    regressor = model.named_steps["regressor"]
    if len(X) > max_samples:
        X_sample = X.sample(n=max_samples, random_state=random_state)
    else:
        X_sample = X
    X_transformed = preprocess.transform(X_sample)
    feature_names = list(X.columns)
    explainer = shap.TreeExplainer(regressor)
    explanation = explainer(X_transformed)
    explanation.feature_names = feature_names
    return explanation


def plot_shap_summary(explanation, path: Path | str | None = None):
    import matplotlib.pyplot as plt
    import shap

    plt.figure()
    shap.plots.beeswarm(explanation, show=False)
    fig = plt.gcf()
    if path is not None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=150, bbox_inches="tight")
    return fig


def mean_abs_shap(explanation) -> pd.Series:
    values = np.abs(explanation.values).mean(axis=0)
    names = explanation.feature_names
    return pd.Series(values, index=names).sort_values(ascending=False)


def coefficient_importance(model, feature_names: list[str]) -> pd.Series:
    """Importância pelo módulo dos coeficientes (baseline Ridge)."""
    coef = getattr(model, "coef_", None)
    if coef is None and hasattr(model, "named_steps"):
        coef = getattr(model.named_steps.get("regressor"), "coef_", None)
    if coef is None:
        raise AttributeError("Modelo sem coeficientes para importância linear.")
    return pd.Series(np.abs(np.asarray(coef)).ravel(), index=feature_names).sort_values(
        ascending=False
    )
