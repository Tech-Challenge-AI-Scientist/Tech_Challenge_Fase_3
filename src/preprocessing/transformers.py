"""Pré-processamento numérico integrado ao Pipeline do scikit-learn."""


def build_preprocessor(feature_names: list[str]):
    """Imputação mediana + padronização, aplicadas só no fold de treino."""
    from sklearn.compose import ColumnTransformer
    from sklearn.impute import SimpleImputer
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler

    numeric_pipe = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    return ColumnTransformer(
        [("num", numeric_pipe, list(feature_names))],
        remainder="drop",
        verbose_feature_names_out=False,
    )
