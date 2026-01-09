import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pytest
from pydantic import ValidationError
from app import PredictRequest


def test_valid_payload():
    payload = PredictRequest(
        age=35,
        genre="Homme",
        revenu_mensuel=2500,
        anciennete_entreprise=3,
        satisfaction_employe=4,
    )

    assert payload.age == 35
    assert payload.genre == "Homme"
    assert payload.satisfaction_employe == 4


def test_invalid_age():
    with pytest.raises(ValidationError):
        PredictRequest(
            age=10,  # trop jeune
            genre="Homme",
            revenu_mensuel=2500,
            anciennete_entreprise=3,
            satisfaction_employe=4,
        )


def test_invalid_satisfaction():
    with pytest.raises(ValidationError):
        PredictRequest(
            age=35,
            genre="Homme",
            revenu_mensuel=2500,
            anciennete_entreprise=3,
            satisfaction_employe=6,  # hors limites
        )
