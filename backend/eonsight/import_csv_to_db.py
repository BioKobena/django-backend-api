import csv
import psycopg2

def import_data_from_csv():
    conn = None
    try:
        # Connexion à la base de données PostgreSQL avec sslmode inclus dans l'URL
        conn = psycopg2.connect(
            "postgresql://neondb_owner:Wm9kXEn3cLiP@ep-dry-river-a4yzxi65.us-east-1.aws.neon.tech/bridge_manager?sslmode=require"
        )

        # Ouvrir le fichier CSV
        with open('sample_bridges.csv', 'r') as file:
            reader = csv.reader(file)

            # Passer la ligne d'en-tête
            next(reader)

            # Créer un curseur pour exécuter les requêtes SQL
            with conn.cursor() as cur:
                for row in reader:
                    # Extraire les données de chaque ligne du fichier CSV
                    bridge_id, name, latitude, longitude = row

                    # Insérer les données dans la table
                    cur.execute(
                        """
                        INSERT INTO bridges (bridge_id, name, location)
                        VALUES (%s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))
                        """,
                        (bridge_id, name, longitude, latitude)
                    )
            
            # Valider la transaction
            conn.commit()
            print("Données importées avec succès !")
    except Exception as e:
        print(f"Erreur : {str(e)}")
    finally:
        # Fermer la connexion à la base de données
        if conn is not None:
            conn.close()

# Appeler la fonction pour importer les données
if __name__ == "__main__":
    import_data_from_csv()
