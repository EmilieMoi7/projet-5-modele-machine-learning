# Maintenance et évolutions du projet

Cette section décrit les bonnes pratiques de maintenance du projet, ainsi que les pistes d’évolution possibles pour garantir sa pérennité et sa fiabilité dans le temps.

---

## Maintenance du modèle

Le modèle de Machine Learning actuellement utilisé est **figé** et chargé à partir d’un fichier sérialisé (`model.joblib`) au démarrage de l’application.

### Mise à jour du modèle

Pour mettre à jour le modèle, les étapes suivantes doivent être respectées :

1. Réentraîner un nouveau modèle à partir de données mises à jour.
2. Évaluer les performances du nouveau modèle.
3. Vérifier la compatibilité des features avec le pipeline existant.
4. Remplacer le fichier `model.joblib` par la nouvelle version.
5. Exécuter l’ensemble des tests unitaires et fonctionnels.
6. Déployer la nouvelle version de l’application.

Aucune mise à jour automatique du modèle n’est implémentée.

---

## Maintenance du code

Le projet est structuré de manière à faciliter la maintenance :

- séparation claire entre logique métier, accès aux données et interface,
- validation des entrées via Pydantic,
- tests automatisés pour prévenir les régressions.

Toute modification du code doit être accompagnée :
- d’un test associé,
- d’une vérification via la pipeline CI/CD.

---

## Surveillance et fiabilité

Dans le cadre du projet, aucune surveillance automatique en production n’est implémentée.

Cependant, plusieurs bonnes pratiques peuvent être envisagées :
- journalisation des prédictions,
- suivi des erreurs applicatives,
- contrôle régulier des performances du modèle.

---

## Évolutions possibles

Plusieurs axes d’amélioration peuvent être envisagés :

- intégration d’une API FastAPI avec documentation OpenAPI,
- ajout de tests d’intégration complets avec base de données mockée,
- mise en place d’un monitoring des prédictions,
- gestion du concept drift,
- automatisation du réentraînement du modèle.

---

## Bonnes pratiques recommandées

- Versionner les modèles de Machine Learning.
- Tester systématiquement avant toute mise en production.
- Documenter toute modification impactant le pipeline.
- Maintenir une cohérence stricte entre entraînement et prédiction.

---

## Conclusion

La maintenance du projet repose sur une approche volontairement simple et maîtrisée.  
Cette stratégie garantit la stabilité du système tout en laissant la possibilité d’évolutions futures dans un cadre contrôlé.
