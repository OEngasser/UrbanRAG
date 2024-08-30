from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.utils import filter_complex_metadata
from langchain_community.embeddings import FastEmbedEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOllama
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

class RagPLU:
    vector_store = None
    retriever = None
    chain = None

    def __init__(self, model_name="llama2", chunk_size=4096, chunk_overlap=0):
        self.model = ChatOllama(model=model_name, temperature=0, top_k=1, top_p=1)
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.prompt = PromptTemplate.from_template(
            """
            <s> [INST] Vous êtes un assistant chargé de l'analyse des documents d'urbanisme. 
            Votre tâche est d'extraire des chiffres à partir du contexte.
            Donnez uniquement le chiffre, pas de texte. 
            [/INST] </s> 
            [INST] Question: {question} 
            Context: {context} 
            Answer: [/INST]
            """
        )

    def ingest(self, pdf_path: str):
        docs = PyMuPDFLoader(file_path=pdf_path).load()
        chunks = self.text_splitter.split_documents(docs)
        chunks = filter_complex_metadata(chunks)

        vector_store = FAISS.from_documents(documents=chunks, embedding=FastEmbedEmbeddings())
        self.retriever = vector_store.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": 1,
                "score_threshold": 0.6,
            },
        )

        self.chain = ({"context": self.retriever, "question": RunnablePassthrough()}
                      | self.prompt
                      | self.model
                      | StrOutputParser())
        
    def ask(self, query: str):
        if not self.chain:
            return "Please, add a PDF document first."
        
        return self.chain.invoke(query)

    def clear(self):
        self.vector_store = None
        self.retriever = None
        self.chain = None

#### Utilisation de la classe ####

# 1. Instanciation de la classe
pdf_query = RagPLU() # paramètres par défaut

# 2. Ingestion du PDF
pdf_query.ingest("plu_0.pdf")

# 3. Question
answer = pdf_query.ask("Quelle est la hauteur maximum des constructions dans la zone U1 ?")
print(answer)

# 4. Effacer les variables stockées
pdf_query.clear()