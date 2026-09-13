"""Treino com validação cruzada no conjunto de 2023 e holdout em 2024."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
from sklearn.model_selection import KFold, cross_validate
from sklearn.pipeline import Pipeline

from src.evaluation.metrics import regression_metrics
from src.modeling.persist import DEFAULT_MODEL_PATH, save_pipeline
from src.modeling.pipelines import RANDOM_STATE, build_hgb_pipeline, build_ridge_pipeline
from src.preprocessing.features import load_features, temporal_holdout

REPO_ROOT = Path(__file__).resolve().parents[2]
REPORTS_DIR = REPO_ROOT / "reports"


def run_cross_validation(model: Pipeline, X, y, n_splits: int = 5) -> dict[str, float]:
    cv = KFold(n_splits=n_splits, shuffle=True, random_state=RANDOM_STATE)
    scores = cross_validate(
        model,
        X,
        y,
        cv=cv,
        scoring=[
            "neg_root_mean_squared_error",
            "neg_mean_absolute_error",
            "r2",
        ],
    )
    return {
        "cv_rmse": float(-scores["test_neg_root_mean_squared_error"].mean()),
        "cv_mae": float(-scores["test_neg_mean_absolute_error"].mean()),
        "cv_r2": float(scores["test_r2"].mean()),
    }


def train_and_evaluate(
    df: pd.DataFrame | None = None,
) -> tuple[Pipeline, Pipeline, dict]:
    """Treina Ridge (baseline) e HistGradientBoosting (oficial); persiste o HGB."""
    data = df if df is not None else load_features()
    X_train, y_train, X_test, y_test = temporal_holdout(data)
    feature_names = list(X_train.columns)

    ridge = build_ridge_pipeline(feature_names)
    hgb = build_hgb_pipeline(feature_names)

    ridge_cv = run_cross_validation(ridge, X_train, y_train)
    hgb_cv = run_cross_validation(hgb, X_train, y_train)

    ridge.fit(X_train, y_train)
    hgb.fit(X_train, y_train)

    summary = {
        "n_train": int(len(X_train)),
        "n_test": int(len(X_test)),
        "features": feature_names,
        "ridge": {
            "cv": ridge_cv,
            "test": regression_metrics(y_test, ridge.predict(X_test)),
        },
        "hist_gradient_boosting": {
            "cv": hgb_cv,
            "test": regression_metrics(y_test, hgb.predict(X_test)),
        },
    }
    return ridge, hgb, summary


def persist_reports(summary: dict, path: Path | None = None) -> Path:
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    output = path or (REPORTS_DIR / "regression_metrics.json")
    output.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return output


def main() -> None:
    _ridge, hgb, summary = train_and_evaluate()
    model_path = save_pipeline(hgb)
    report_path = persist_reports(summary)
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"Modelo salvo em: {model_path}")
    print(f"Métricas salvas em: {report_path}")
    print(f"Artefato padrão: {DEFAULT_MODEL_PATH}")


if __name__ == "__main__":
    main()
