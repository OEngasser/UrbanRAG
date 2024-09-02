from rag_plu import RagPLU

def main():
    # Initialisation de l'objet RagPLU
    rag_plu = RagPLU(model_name="llama2", chunk_size=4096, chunk_overlap=0)

    # Chemin vers le fichier PDF à ingérer
    pdf_path = "plu_0.pdf"

    # Ingestion du PDF
    print("Ingestion du document...")
    rag_plu.ingest(pdf_path)
    print("Ingestion terminée.")

    # Boucle d'interaction avec l'utilisateur
    while True:
        query = input(str("Posez une question (ou tapez 'exit' pour quitter) : "))

        if query.lower() == "exit":
            print("Fin de l'interaction.")
            break

        # Répondre à la question
        answer = rag_plu.ask(query)
        print(f"Réponse : {answer}")

    # Effacer les données pour libérer de la mémoire
    rag_plu.clear()
    print("Mémoire nettoyée.")

if __name__ == "__main__":
    main()