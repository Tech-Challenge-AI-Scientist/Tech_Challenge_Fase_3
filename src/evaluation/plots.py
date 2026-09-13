"""Gráficos de diagnóstico da regressão."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def plot_pred_vs_actual(y_true, y_pred, path: Path | str | None = None):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(y_true, y_pred, alpha=0.35, s=12, color="#4C72B0")
    lims = [min(y_true.min(), y_pred.min()), max(y_true.max(), y_pred.max())]
    ax.plot(lims, lims, "--", color="black", linewidth=1)
    ax.set_xlabel("Taxa observada")
    ax.set_ylabel("Taxa prevista")
    ax.set_title("Predito vs real — holdout 2024")
    fig.tight_layout()
    if path is not None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=150)
    return fig


def plot_residuals(y_true, y_pred, path: Path | str | None = None):
    residuals = np.asarray(y_true) - np.asarray(y_pred)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(residuals, bins=30, color="#55A868", edgecolor="black")
    ax.axvline(0, color="black", linestyle="--")
    ax.set_xlabel("Resíduo (observado − previsto)")
    ax.set_ylabel("Frequência")
    ax.set_title("Distribuição dos resíduos — holdout 2024")
    fig.tight_layout()
    if path is not None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=150)
    return fig
