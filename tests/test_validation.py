import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from pydantic import ValidationError
from app import PredictRequest

def test_valid_text():
    payload = PredictRequest(text="hello")
    assert payload.text == "hello"

def test_invalid_empty_text():
    try:
        PredictRequest(text="")
        assert False
    except ValidationError:
        assert True
