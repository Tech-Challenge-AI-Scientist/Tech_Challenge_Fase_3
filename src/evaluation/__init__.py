"""Métricas, gráficos, interpretabilidade e ranking de risco."""

from src.evaluation.explain import coefficient_importance, shap_values
from src.evaluation.metrics import regression_metrics
from src.evaluation.plots import plot_pred_vs_actual, plot_residuals
from src.evaluation.ranking import rank_risk

__all__ = [
    "plot_pred_vs_actual",
    "plot_residuals",
    "rank_risk",
    "regression_metrics",
    "coefficient_importance",
    "shap_values",
]
