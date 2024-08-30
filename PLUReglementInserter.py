import psycopg2
from RagPLU import answers # récupération des données de la variable answers dans le fichier rag

class PLUReglementInserter:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.conn.cursor()

    def insert_data(self, idterritoire, codcom, annee, zone, section, answers):
        for answer in answers:
            self.cursor.execute('''
                INSERT INTO plu_reglement (idterritoire, codcom, annee, zone, section, hauteur, emprise)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (idterritoire, codcom, annee, zone, section, answer['hauteur'], answer['emprise']))
    
    def commit_and_close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()