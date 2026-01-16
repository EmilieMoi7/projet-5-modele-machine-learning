import gradio as gr
from pydantic import BaseModel, Field, ConfigDict, ValidationError
import joblib
import pandas as pd
from pathlib import Path
from src.projet5.db.db import insert_model_input, insert_model_output


# =========================
# Chargement du modèle (1 seule fois)
# =========================
MODEL_PATH = Path(__file__).resolve().parent / "models" / "model.joblib"
model = joblib.load(MODEL_PATH)

# Le modèle est un Pipeline : on récupère les features finales (après preprocessing)
FEATURES = list(model[:-1].get_feature_names_out())


# =========================
# Schéma Pydantic (validation entrée)
# =========================
class PredictRequest(BaseModel):
    age: int = Field(..., ge=16, le=100)
    genre: str
    revenu_mensuel: float = Field(..., ge=0)
    anciennete_entreprise: int = Field(..., ge=0)
    satisfaction_employe: int = Field(..., ge=1, le=5)

    model_config = ConfigDict(extra="forbid")


# =========================
# Construction de X (53 colonnes attendues)
# On part de 0 partout + quelques valeurs neutres
# =========================
def build_model_input(age, genre, revenu_mensuel, anciennete_entreprise, satisfaction_employe):
    # DataFrame 1 ligne, 53 colonnes, tout à 0
    X = pd.DataFrame(0, index=[0], columns=FEATURES)

    # Numériques simples (si présents dans FEATURES)
    if "age" in X.columns:
        X.loc[0, "age"] = age
    if "revenu_mensuel" in X.columns:
        X.loc[0, "revenu_mensuel"] = revenu_mensuel

    # Selon ton dataset, ça peut s'appeler "anciennete_entreprise" ou autre.
    if "anciennete_entreprise" in X.columns:
        X.loc[0, "anciennete_entreprise"] = anciennete_entreprise
    elif "annees_sous_responsable_actuel" in X.columns:
        # fallback "raisonnable" si tu n'as pas la vraie colonne
        X.loc[0, "annees_sous_responsable_actuel"] = min(anciennete_entreprise, 40)

    # Valeurs "neutres" (si les colonnes existent)
    neutral_defaults = {
        "nombre_experiences_precedentes": 0,
        "nombre_heures_travailless": 35,
        "note_evaluation_precedente": 3,
        "note_evaluation_actuelle": 3,
        "niveau_hierarchique_poste": 1,
        "nombre_participation_pee": 0,
        "nb_formations_suivies": 0,
        "nombre_employee_sous_responsabilite": 0,
        "distance_domicile_travail": 10,
        "annees_depuis_la_derniere_promotion": 0,
        "annes_sous_responsable_actuel": 0,
    }

    for col, val in neutral_defaults.items():
        if col in X.columns:
            X.loc[0, col] = val

    # One-hot genre
    if "genre_M" in X.columns:
        X.loc[0, "genre_M"] = 1 if str(genre).strip().lower().startswith("hom") else 0

    # Satisfaction (tu as plusieurs colonnes de satisfaction, on les met toutes)
    sat_cols = [
        "satisfaction_employee_environnement",
        "satisfaction_employee_nature_travail",
        "satisfaction_employee_equipe",
        "satisfaction_employee_equilibre_pro_perso",
    ]
    for col in sat_cols:
        if col in X.columns:
            X.loc[0, col] = satisfaction_employe

    return X


# =========================
# Fonction de prédiction (appelée par Gradio)
# =========================
def predict(age, genre, revenu_mensuel, anciennete_entreprise, satisfaction_employe):
    try:
        payload = PredictRequest(
            age=int(age),
            genre=str(genre),
            revenu_mensuel=float(revenu_mensuel),
            anciennete_entreprise=int(anciennete_entreprise),
            satisfaction_employe=int(satisfaction_employe),
        )
    except ValidationError as e:
        raise gr.Error(f"Entrée invalide : {e.errors()}")

    model_input_id = insert_model_input(
        payload.age,
        payload.genre,
        payload.revenu_mensuel,
        payload.anciennete_entreprise,
        payload.satisfaction_employe,
    )

    X = build_model_input(**payload.model_dump())

    prediction = bool(model.predict(X)[0])
    proba = float(model.predict_proba(X)[0, 1])

    insert_model_output(model_input_id, prediction, proba)

    return {
        "prediction": prediction,
        "prediction_proba": round(proba, 4),
        "model_input_id": model_input_id,
    }



# =========================
# UI Gradio
# =========================
with gr.Blocks() as demo:
    gr.Markdown("# Projet 5 – Modèle ML 🚀")

    age = gr.Number(label="Âge", precision=0)
    genre = gr.Dropdown(["Homme", "Femme"], label="Genre")
    revenu = gr.Number(label="Revenu mensuel")
    anciennete = gr.Number(label="Ancienneté (années)", precision=0)
    satisfaction = gr.Slider(1, 5, step=1, label="Satisfaction employé")

    out = gr.JSON(label="Résultat")
    btn = gr.Button("Prédire")

    btn.click(
        predict,
        inputs=[age, genre, revenu, anciennete, satisfaction],
        outputs=out,
    )

if __name__ == "__main__":
    demo.launch()
