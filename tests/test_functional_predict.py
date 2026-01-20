import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import app  # noqa: E402


def test_predict_functional(monkeypatch):
    """
    Test fonctionnel: exécute le pipeline complet (validation -> features -> modèle -> JSON)
    sans dépendre de PostgreSQL (on mock les écritures DB).
    """

    # On neutralise la persistance DB pour que la CI passe sans Postgres
    monkeypatch.setattr(app, "insert_model_input", lambda *args, **kwargs: None)
    monkeypatch.setattr(app, "insert_model_output", lambda *args, **kwargs: None)

    result = app.predict(
        age=35,
        genre="Homme",
        revenu_mensuel=2500,
        anciennete_entreprise=3,
        satisfaction_employe=4,
    )

    assert isinstance(result, dict)
    assert "prediction" in result
    assert "prediction_proba" in result
    assert "model_input_id" in result

    assert isinstance(result["prediction"], bool)
    assert isinstance(result["prediction_proba"], float)
    assert 0.0 <= result["prediction_proba"] <= 1.0

    # Comme on a mock la DB, on sait que ça doit être None
    assert result["model_input_id"] is None

