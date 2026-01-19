# Tests et intégration continue (CI)

Cette section décrit la stratégie de tests mise en place sur le projet ainsi que le fonctionnement de l’intégration continue (CI) via GitHub Actions.

---

## Objectifs des tests

Les tests ont pour objectif de :
- garantir la fiabilité du code,
- prévenir les régressions,
- vérifier la validité des entrées utilisateur,
- assurer la stabilité du pipeline de prédiction.

Les tests permettent également de démontrer la robustesse du projet lors de l’évaluation.

---

## Types de tests

### Tests unitaires

Les tests unitaires vérifient des composants isolés :
- validation des schémas Pydantic (types, bornes),
- cohérence de la construction des features,
- tests de cas limites et scénarios d’erreur.

Objectif : vérifier que chaque composant fonctionne correctement indépendamment des autres.

---

### Tests fonctionnels

Les tests fonctionnels évaluent le pipeline complet :
- saisie d’un jeu d’entrées représentatif,
- passage dans la validation,
- construction des features,
- exécution de la prédiction,
- retour d’une réponse structurée.

Objectif : vérifier que le système complet produit un résultat cohérent selon les spécifications.

---

## Exécution des tests

Les tests se lancent via Pytest :

```bash
pytest -v
```


---

## Couverture de tests

La couverture est mesurée via pytest-cov :

```bash
pytest --cov
```

L’objectif est de démontrer que les parties critiques du pipeline sont bien couvertes (validation, transformation, prédiction).

---

## Intégration continue (CI)

Un workflow GitHub Actions est configuré afin d’exécuter automatiquement les vérifications à chaque push ou pull request.

La CI permet de :
- installer les dépendances,
- exécuter les tests,
- vérifier que le projet reste fonctionnel dans un environnement standardisé.

Cette étape garantit la reproductibilité du projet et limite les erreurs lors du déploiement.

---

## Remarque sur la base de données

En CI, la base PostgreSQL n’est pas utilisée afin de :
- réduire les dépendances externes,
- garantir des tests reproductibles,
- limiter les erreurs liées à l’environnement.

La traçabilité en base est vérifiée et utilisée en environnement local.

--- 
## Conclusion

La stratégie de tests et l’intégration continue assurent un haut niveau de fiabilité du projet.
Chaque modification est validée automatiquement, garantissant la stabilité du pipeline de prédiction.