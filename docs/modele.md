# Documentation du modèle de Machine Learning

Cette section décrit le modèle de Machine Learning utilisé dans l’application, ses principes de fonctionnement, ses performances, ainsi que les choix techniques réalisés.

---

## Objectif du modèle

Le modèle a pour objectif de **produire une prédiction binaire** à partir de données socio-professionnelles fournies par l’utilisateur.

Il s’inscrit dans un cadre pédagogique visant à :
- comprendre le cycle de vie d’un modèle ML,
- garantir la reproductibilité des prédictions,
- intégrer le modèle dans une application exploitable.

---

## Type de modèle

- **Famille** : modèle de classification
- **Implémentation** : scikit-learn
- **Sortie** :
  - une prédiction binaire (`True` / `False`)
  - une probabilité associée à la prédiction

Le modèle est sauvegardé sous forme sérialisée (`model.joblib`) afin d’être chargé au démarrage de l’application.

---

## Données utilisées

Le modèle a été entraîné à partir d’un jeu de données fourni dans un projet précédent de la formation.

Les données comprennent notamment :
- des variables numériques (âge, revenu, ancienneté, etc.),
- des variables catégorielles (genre),
- des indicateurs de satisfaction.

Aucune donnée sensible ou personnelle n’est exposée dans le dépôt.

---

## Pipeline de features

Le pipeline de prédiction respecte strictement la structure utilisée lors de l’entraînement :

- initialisation d’un vecteur de features complet,
- encodage des variables catégorielles (one-hot encoding),
- insertion de valeurs neutres pour les variables non fournies,
- alignement exact des colonnes attendues par le modèle.

Cette approche garantit :
- la cohérence des entrées,
- l’absence de décalage entre entraînement et prédiction,
- la stabilité des résultats.

---

## Performances du modèle

Les performances du modèle ont été évaluées lors de la phase d’entraînement à l’aide de métriques classiques de classification, telles que :
- l’exactitude (accuracy),
- la probabilité associée à chaque prédiction.

Dans le cadre de ce projet, l’objectif principal n’est pas l’optimisation maximale des performances, mais :
- la fiabilité du pipeline,
- la robustesse du code,
- la reproductibilité des résultats.

---

## Maintenance du modèle

Le modèle actuellement embarqué est **figé** :
- il n’est pas réentraîné automatiquement,
- il est chargé au démarrage de l’application.

Toute mise à jour du modèle nécessiterait :
1. un nouvel entraînement,
2. une validation des performances,
3. une mise à jour du fichier `model.joblib`,
4. une vérification de compatibilité avec le pipeline existant.

---

## Limites connues

- Le modèle dépend fortement du jeu de données d’origine.
- Aucune gestion du concept drift n’est implémentée.
- Le modèle ne s’auto-adapte pas à de nouvelles données.

Ces limites sont acceptées dans le cadre du projet pédagogique.

---

## Conclusion

Le modèle de Machine Learning constitue le cœur du système de prédiction.  
Il est intégré dans une architecture contrôlée, testée et documentée, garantissant une utilisation fiable dans le cadre de l’application développée.
