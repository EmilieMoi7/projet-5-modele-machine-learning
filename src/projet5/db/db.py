import psycopg2

DB_NAME = "projet5_ml"
DB_USER = "emiliemoissette"
DB_HOST = "localhost"
DB_PORT = 5432


def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        host=DB_HOST,
        port=DB_PORT,
    )


def insert_model_input(age, genre, revenu_mensuel, anciennete_entreprise, satisfaction_employe):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO model_inputs (
            age, genre, revenu_mensuel, anciennete_entreprise, satisfaction_employe
        )
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
        """,
        (age, genre, revenu_mensuel, anciennete_entreprise, satisfaction_employe),
    )

    model_input_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return model_input_id

def insert_model_output(model_input_id, prediction, prediction_proba):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO model_outputs (
            model_input_id,
            prediction,
            prediction_proba
        )
        VALUES (%s, %s, %s)
        """,
        (model_input_id, prediction, prediction_proba)
    )

    conn.commit()
    cur.close()
    conn.close()
