"""Salva e carrega o pipeline inteiro (pré-processamento + regressor)."""

from pathlib import Path

import joblib

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_MODEL_PATH = REPO_ROOT / "models" / "regressor_alfabetizacao.joblib"


def save_pipeline(model, path: Path | str | None = None) -> Path:
    """Salva o pipeline inteiro (pré-processamento + regressor)."""
    output = Path(path) if path is not None else DEFAULT_MODEL_PATH
    output.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output)
    return output


def load_pipeline(path: Path | str | None = None):
    """Carrega o pipeline inteiro (pré-processamento + regressor)."""
    output = Path(path) if path is not None else DEFAULT_MODEL_PATH
    return joblib.load(output)
