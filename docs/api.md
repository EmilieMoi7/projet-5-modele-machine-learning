# Documentation de l’API de prédiction

Cette section décrit le fonctionnement de l’API de prédiction exposée par l’application.  
L’API permet de soumettre des données utilisateur et d’obtenir une prédiction issue d’un modèle de Machine Learning.

L’interface applicative est fournie via **Gradio**, qui sert à la fois de point d’entrée utilisateur et de couche API.

---

## Vue générale

L’API réalise les étapes suivantes :

1. Réception des données d’entrée utilisateur.
2. Validation des données via des schémas Pydantic.
3. Construction des features conformément au pipeline d’entraînement.
4. Prédiction à l’aide du modèle de Machine Learning.
5. Calcul d’une probabilité associée à la prédiction.
6. Retour d’un résultat structuré.

---

## Endpoint de prédiction

### Type
- **Action** : prédiction
- **Méthode logique** : POST
- **Interface** : Gradio (formulaire interactif)

---

## Données d’entrée

Les données suivantes sont requises pour effectuer une prédiction :

| Champ | Type | Description |
|------|------|-------------|
| `age` | entier | Âge de l’utilisateur |
| `genre` | chaîne | Genre de l’utilisateur |
| `revenu_mensuel` | float | Revenu mensuel |
| `anciennete_entreprise` | entier | Ancienneté dans l’entreprise (en années) |
| `satisfaction_employe` | entier | Niveau de satisfaction (1 à 5) |

Les contraintes de validité sont définies à l’aide de **Pydantic** afin de garantir la cohérence des données.

---

## Validation des entrées

Avant toute prédiction :
- les types sont vérifiés,
- les bornes de valeurs sont contrôlées,
- les champs obligatoires sont imposés.

En cas de données invalides, l’API retourne une erreur explicite empêchant l’exécution du modèle.

---

## Traitement des données

Les données validées sont transformées via un pipeline de construction des features :

- initialisation d’un vecteur de features conforme au modèle,
- encodage des variables catégorielles,
- insertion de valeurs neutres pour les features non renseignées,
- alignement strict avec les features utilisées lors de l’entraînement.

Ce mécanisme garantit la reproductibilité des prédictions.

---

## Sortie de l’API

L’API retourne un objet JSON structuré contenant :

| Champ | Type | Description |
|------|------|-------------|
| `prediction` | booléen | Résultat de la prédiction |
| `prediction_proba` | float | Probabilité associée |
| `model_input_id` | entier | Identifiant de la requête |

### Exemple de réponse

```json
{
  "prediction": false,
  "prediction_proba": 0.0003,
  "model_input_id": 12
}
```

---

## Gestion des erreurs

Les erreurs peuvent survenir dans les cas suivants :
- données d’entrée invalides,
- incohérence de format,
- erreur interne du pipeline.
Dans tous les cas, l’API empêche l’exécution du modèle et renvoie un message explicite.

---

## Limitations connues
- L’API ne permet pas le réentraînement du modèle.
- Le modèle embarqué est figé.
- L’interface Gradio ne fournit pas de documentation OpenAPI automatique.
- Ces choix sont assumés dans le cadre du projet pédagogique.

---

## Conclusion

L’API fournit une interface simple, fiable et validée pour interagir avec le modèle de Machine Learning.