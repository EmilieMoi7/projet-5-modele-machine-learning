# API de prédiction — Modèle de Machine Learning

> Objectif : Ce projet est réalisé dans le cadre du Projet 5 de la formation AI Engineer. L’objectif est de mettre en place et déployer un modèle de machine learning. C'est également une première approche pour maitriser le système de gestion de versions avec Git et GitHub.

## Vue d’ensemble
Ce projet est réalisé dans le cadre du **Projet 5 de la formation AI Engineer**.  
Il a pour objectif de **déployer un modèle de Machine Learning** au sein d’une application fonctionnelle, testée, documentée et intégrée dans un pipeline CI/CD.

Le projet couvre :
- la mise en place du modèle et de son pipeline de prédiction,
- la validation des entrées et sorties,
- la mise en œuvre de tests unitaires et fonctionnels,
- l’automatisation des tests via une intégration continue,
- la documentation technique et fonctionnelle du projet.

## Objectifs pédagogiques

- Déployer un modèle de Machine Learning dans une application exploitable
- Garantir la fiabilité du code via des tests unitaires et fonctionnels
- Mettre en place un pipeline CI/CD automatisé
- Documenter l’API, le modèle et l’architecture du projet
- Respecter les bonnes pratiques de versioning avec Git et GitHub

---

## Fonctionnalités
- **- **Prédiction** : saisie des données via l’interface Gradio et retour d’une prédiction
- **Validation d’entrée/sortie** : schémas (ex. Pydantic) + contraintes de base.
- **Pipeline de transformation des données** cohérent avec l’entraînement du modèle
- **Calcul de probabilités associées à la prédiction**
- **Interface utilisateur** via Gradio
- **Exécution automatisée des tests** via GitHub Actions
- **Déploiement** : conteneurisation via Docker.


---

## Stack technique
- **Langage** : Python  
- **Machine Learning** : scikit-learn  
- **Validation des données** : Pydantic  
- **Interface applicative** : Gradio  
- **Base de données** : PostgreSQL (local, optionnelle en CI)  
- **Tests** : Pytest, Pytest-cov  
- **CI/CD** : GitHub Actions  

---

## Architecture (vue simple)

```bash
projet-5-modele-machine-learning/
├── src/
│   └── projet5/
│       ├── db/              # Accès base de données
│       ├── model/           # Logique métier et ML
│       └── utils/           # Fonctions utilitaires
├── models/
│   └── model.joblib         # Modèle entraîné
├── tests/
│   ├── test_features.py     # Tests unitaires des features
│   ├── test_validation.py   # Tests de validation Pydantic
│   └── test_sanity.py       # Tests de cohérence globale
├── notebooks/               # Exploration et entraînement
├── requirements.txt
├── .github/workflows/ci.yml # Pipeline CI
└── README.md

---

## Pipeline de traitement (logique)
1. L’utilisateur saisit les données via l’interface Gradio.
2. Les données sont validées à l’aide de schémas Pydantic.
3. Les features sont construites conformément au pipeline d’entraînement.
4. Le modèle de Machine Learning génère une prédiction.
5. Une probabilité associée est calculée.
6. Le résultat est renvoyé à l’utilisateur sous forme structurée.
---

## Installation

```bash
git clone <url-du-repo>
cd projet-5-modele-machine-learning
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Lancement de l'application

```bash
python app.py
```

L’interface Gradio est accessible à l’adresse :  
http://127.0.0.1:7860

---


## Faire une prédiction
Données attendues : 
- age
- genre
- revenu mensuel 
- ancienneté dans l'entreprise
- niveau de satisfaction


Exemple de réponse :
{
  "prediction": false,
  "prediction_proba": 0.0003,
  "model_input_id": 12
}
```

---

## Tests
Des tests unitaires et fonctionnels sont implémentés afin de garantir la fiabilité du modèle et du pipeline :
- validation des entrées avec Pydantic
- vérification de la construction des features
- tests des cas limites et scénarios d’erreur
- tests fonctionnels du pipeline complet de prédiction

Exécution des tests :
```bash
pytest -v
pytest --cov
```

---

## Intégration continue (CI/CD)
Un pipeline CI/CD est configuré via GitHub Actions afin d’installer les dépendances, exécuter les tests et garantir la stabilité du projet à chaque push et pull request.

---
## Conteneurisation avec Docker
Le projet est conteneurisé à l’aide de Docker afin de standardiser l’environnement d’exécution et faciliter le déploiement.

```bash
docker build -t projet5-ml .
docker run -p 7860:7860 projet5-ml

L’application est accessible à l’adresse :
http://localhost:7860

---
## Choix techniques et limites
- Gradio a été choisi pour sa simplicité et sa rapidité de mise en œuvre.
- Le modèle embarqué est figé et n’est pas réentraîné automatiquement.
- Les tests en CI n’utilisent pas la base PostgreSQL afin de garantir leur stabilité.
- Les performances du modèle dépendent du jeu de données utilisé lors de l’entraînement.

---
## Améliorations possibles
- Tests d’intégration complets avec base de données mockée
- Exposition du modèle via une API FastAPI
- Monitoring des prédictions
- Réentraînement automatique du modèle

---
## Contact
Émilie Moissette
Formation AI Engineer


