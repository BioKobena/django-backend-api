import psycopg2

def verify_imported_data():
    try:
        # Connexion à la base de données PostgreSQL avec sslmode
        conn = psycopg2.connect(
            "postgresql://neondb_owner:Wm9kXEn3cLiP@ep-dry-river-a4yzxi65.us-east-1.aws.neon.tech/bridge_manager?sslmode=require"
        )

        # Créer un curseur pour exécuter des requêtes SQL
        with conn.cursor() as cur:
            # Exécuter une requête pour récupérer toutes les données de la table bridges
            cur.execute("SELECT bridge_id, name, ST_AsText(location) FROM bridges;")
            
            # Récupérer toutes les lignes de la requête exécutée
            rows = cur.fetchall()
            
            # Afficher les en-têtes de colonnes
            print("bridge_id | name | location")
            print("----------|------|----------")

            # Afficher toutes les lignes
            for row in rows:
                print(f"{row[0]} | {row[1]} | {row[2]}")

    except Exception as e:
        print(f"Erreur : {str(e)}")
    finally:
        # Fermer la connexion à la base de données
        if conn is not None:
            conn.close()

# Appeler la fonction pour vérifier les données importées
if __name__ == "__main__":
    verify_imported_data()
