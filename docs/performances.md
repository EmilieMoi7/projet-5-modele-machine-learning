# Performances du modèle

Cette section présente une analyse synthétique des performances du modèle de Machine Learning, ainsi que les limites identifiées dans le cadre du projet.

---

## Objectif de l’évaluation

L’évaluation des performances vise à :
- vérifier la cohérence des prédictions produites,
- s’assurer du bon fonctionnement du pipeline de prédiction,
- identifier les limites du modèle dans un contexte réel.

Dans le cadre de ce projet pédagogique, l’objectif principal est la **robustesse du système**, plutôt que l’optimisation extrême des scores.

---

## Métriques utilisées

Le modèle a été évalué lors de la phase d’entraînement à l’aide de métriques classiques de classification, notamment :

- **Accuracy** : proportion de prédictions correctes.
- **Probabilité associée** : score de confiance fourni par le modèle pour chaque prédiction.

La probabilité retournée par l’API permet d’interpréter le degré de confiance du modèle dans sa prédiction.

---

## Interprétation des résultats

Les prédictions fournies par le modèle doivent être interprétées avec précaution :

- une probabilité faible ou élevée indique un degré de confiance,
- la valeur binaire retournée correspond à la classe prédite,
- le modèle reste dépendant des distributions observées lors de l’entraînement.

Le modèle est cohérent pour des profils proches de ceux observés dans le jeu de données d’origine.

---

## Limites des performances

Plusieurs limites ont été identifiées :

- dépendance forte au jeu de données d’entraînement,
- absence de recalibrage automatique,
- absence de gestion du déséquilibre potentiel des classes,
- sensibilité aux valeurs neutres injectées pour certaines features non renseignées.

Ces limites sont connues et assumées dans le cadre du projet.

---

## Reproductibilité

Les performances sont reproductibles dans la mesure où :
- le pipeline de transformation est figé,
- le modèle est chargé à partir d’un fichier sérialisé unique,
- les tests automatisés garantissent la stabilité du comportement du modèle.

Toute modification du modèle ou des features nécessite une nouvelle phase de validation.

---

## Conclusion

Les performances du modèle sont jugées satisfaisantes au regard des objectifs du projet.  
L’accent a été mis sur la fiabilité, la cohérence et la reproductibilité du pipeline de prédiction plutôt que sur l’optimisation des métriques brutes.
