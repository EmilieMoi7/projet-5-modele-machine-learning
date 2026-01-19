# Déploiement de l’application

Cette section décrit les modalités de déploiement de l’application de prédiction, en environnement local et via Docker.

---

## Déploiement en local

Le déploiement en local est destiné au développement, aux tests et à la démonstration du projet.

### Prérequis
- Python 3.10+
- Environnement virtuel Python
- Dépendances listées dans `requirements.txt`

### Installation

```bash
git clone <url-du-repo>
cd projet-5-modele-machine-learning
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
---

## Lancement de l’application
```bash
python app.py
```

L’interface Gradio est ensuite accessible à l’adresse suivante :

http://127.0.0.1:7860

---

## Déploiement via Docker

Le projet peut également être déployé à l’aide de Docker afin de garantir un environnement d’exécution reproductible.

---

## Construction de l’image Docker

```bash
docker build -t projet5-ml .
```

---

## Lancement du conteneur
```bash
docker run -p 7860:7860 projet5-ml
```

L’application est accessible à l’adresse :

http://localhost:7860

---

## Intégration continue et déploiement

Le projet intègre un pipeline CI via GitHub Actions permettant de :
- installer les dépendances,
- exécuter les tests unitaires et fonctionnels,
- vérifier la stabilité du projet avant tout déploiement.

Le déploiement manuel n’est effectué qu’après validation complète de la CI.

---
## Bonnes pratiques de déploiement
- Tester systématiquement avant toute mise en production.
- Versionner les modèles de Machine Learning.
- Utiliser Docker pour garantir la reproductibilité.
- Vérifier la compatibilité des dépendances avant déploiement.

---

## Conclusion

Le déploiement de l’application est volontairement simple et contrôlé.
Cette approche permet d’assurer une exécution fiable tout en facilitant les tests et les évolutions futures du projet.