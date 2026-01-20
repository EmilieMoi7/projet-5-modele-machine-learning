import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app import predict


def test_predict_functional():
    result = predict(
        age=35,
        genre="Homme",
        revenu_mensuel=2500,
        anciennete_entreprise=3,
        satisfaction_employe=4,
    )

    assert "prediction" in result
    assert "prediction_proba" in result
    assert isinstance(result["prediction"], bool)
    assert 0 <= result["prediction_proba"] <= 1
