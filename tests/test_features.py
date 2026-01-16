import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd
from app import build_model_input, FEATURES


def test_build_model_input_shape_and_columns():
    X = build_model_input(
        age=35,
        genre="Homme",
        revenu_mensuel=2500,
        anciennete_entreprise=5,
        satisfaction_employe=3,
    )

    assert isinstance(X, pd.DataFrame)
    assert X.shape[0] == 1
    assert list(X.columns) == list(FEATURES)
    assert X.shape[1] == len(FEATURES)


def test_build_model_input_sets_core_values():
    X = build_model_input(
        age=42,
        genre="Homme",
        revenu_mensuel=3200,
        anciennete_entreprise=8,
        satisfaction_employe=4,
    )

    if "age" in X.columns:
        assert X.loc[0, "age"] == 42

    if "revenu_mensuel" in X.columns:
        assert X.loc[0, "revenu_mensuel"] == 3200

    if "genre_M" in X.columns:
        assert X.loc[0, "genre_M"] == 1
