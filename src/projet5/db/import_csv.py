import re
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

DB_NAME = "projet5_ml"
DB_USER = "emiliemoissette"
DB_HOST = "localhost"
DB_PORT = 5432

CSV_PATH = "data/dataset_employees_clean.csv"
TABLE_NAME = "employees_dataset"


def sanitize_col(col: str) -> str:
    # 1) strip espaces
    col = col.strip()

    # 2) remplace les caractères non alphanum par underscore
    # (accents inclus, on les vire)
    col = col.lower()
    col = (
        col.replace("é", "e")
        .replace("è", "e")
        .replace("ê", "e")
        .replace("à", "a")
        .replace("ç", "c")
        .replace("ù", "u")
        .replace("ô", "o")
        .replace("î", "i")
        .replace("ï", "i")
        .replace("â", "a")
    )
    col = re.sub(r"[^a-z0-9_]+", "_", col)
    col = re.sub(r"_+", "_", col).strip("_")

    # 3) évite les noms vides
    if not col:
        col = "col"
    return col


def main():
    # --- lecture CSV ---
    df = pd.read_csv(CSV_PATH)
    print(f"{len(df)} lignes lues depuis le CSV")

    # --- sanitize colonnes ---
    original_cols = list(df.columns)
    cleaned_cols = [sanitize_col(c) for c in original_cols]

    # Si doublons après nettoyage -> on suffixe
    seen = {}
    final_cols = []
    for c in cleaned_cols:
        if c not in seen:
            seen[c] = 0
            final_cols.append(c)
        else:
            seen[c] += 1
            final_cols.append(f"{c}_{seen[c]}")

    df.columns = final_cols

    # --- connexion DB ---
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        host=DB_HOST,
        port=DB_PORT,
    )
    cur = conn.cursor()
    print("Connexion à PostgreSQL OK")

    # --- create table (on part du principe que tu as DROP avant) ---
    columns_sql = ",\n  ".join([f'"{c}" TEXT' for c in df.columns])
    create_sql = f"""
    CREATE TABLE {TABLE_NAME} (
      id SERIAL PRIMARY KEY,
      {columns_sql}
    );
    """
    cur.execute(create_sql)
    conn.commit()
    print("Table recréée à partir du CSV OK")

    # --- insertion ---
    cols = [f'"{c}"' for c in df.columns]
    insert_sql = f'INSERT INTO {TABLE_NAME} ({", ".join(cols)}) VALUES %s'

    values = [tuple(None if pd.isna(x) else str(x) for x in row) for row in df.to_numpy()]
    execute_values(cur, insert_sql, values, page_size=1000)
    conn.commit()

    print("Import CSV terminé avec succès")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()

