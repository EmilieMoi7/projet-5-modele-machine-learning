-- =====================================================
-- Schéma SQL – Projet 5 Machine Learning
-- Base de données : PostgreSQL
-- =====================================================
-- Ce schéma décrit explicitement la structure de la table
-- `employees_dataset` utilisée par le projet.
--
-- La table est créée dynamiquement par le script Python
-- `src/projet5/db/import_csv.py` à partir du fichier CSV
-- `data/dataset_employees_clean.csv`.
--
-- Toutes les colonnes sont volontairement typées TEXT,
-- afin de garantir une correspondance exacte avec le CSV
-- et d’éviter toute incohérence lors de l’import.
-- =====================================================

CREATE TABLE IF NOT EXISTS employees_dataset (
    id SERIAL PRIMARY KEY,

    id_employee TEXT,
    age TEXT,
    genre TEXT,
    revenu_mensuel TEXT,
    statut_marital TEXT,
    departement TEXT,
    poste TEXT,
    nombre_experiences_precedentes TEXT,
    nombre_heures_travaillees TEXT,
    annee_experience_totale TEXT,
    annees_dans_l_entreprise TEXT,
    annees_dans_le_poste_actuel TEXT,
    satisfaction_employee_environnement TEXT,
    note_evaluation_precedente TEXT,
    niveau_hierarchique_poste TEXT,
    satisfaction_employee_nature_travail TEXT,
    satisfaction_employee_equipe TEXT,
    satisfaction_employee_equilibre_pro_perso TEXT,
    note_evaluation_actuelle TEXT,
    heure_supplementaires TEXT,
    augmentation_salaire_precedente TEXT,
    a_quitte_l_entreprise TEXT,
    nombre_participation_pe TEXT,
    nb_formations_suivies TEXT,
    nombre_employee_sous_responsabilite TEXT,
    distance_domicile_travail TEXT,
    niveau_education TEXT,
    domaine_etude TEXT,
    ayant_enfants TEXT,
    frequence_deplacement TEXT,
    annees_depuis_la_derniere_promotion TEXT,
    annees_sous_responsable_actuel TEXT
);
