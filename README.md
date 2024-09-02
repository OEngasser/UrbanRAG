
# Overview

UrbanRAG is an implementation of a Retrieval-Augmented Generation (RAG) system designed to extract numerical data from urban planning documents (PLU) and insert it into a database. This project includes a pipeline, demonstrated in a Jupyter Notebook, and Python and Ruby classes that integrate into a larger Ruby on Rails production environment for API usage.

# Features

- RAG Pipeline: Extracts data from urban planning PDFs.
- Database Insertion: Automates data integration into a database.
- Cross-Language Support: Utilizes Python and Ruby.

# Installation

1. Clone the repository:
```
git clone https://github.com/OEngasser/UrbanRAG.git
cd UrbanRAG
```

2. Set up the environment:

If you're using `pip`:
```
python3 -m venv venv
source venv/Scripts/activate # on Windows
source venv/bin/activate # on Mac
pip install -r requirements.txt
```

If you're using `Poetry`:
```
poetry install
```

# Usage

- RAG Pipeline: Execute the pipeline using `pipeline_rag.ipynb` to visualize the steps and the logic of the implementation.
- Evaluation: Refer to `evaluation.ipynb` to visualize experimentation and results accross 4 documents.
- Main script: To run the base class that allows a user to ask a question, execute `main.py` using:
```
python main.py
```
- The other classes are intended to be used in production.

# Configuration

- Dependencies: Specified on `pyproject.toml`
- Environment Variables: Configure database connections and other necessary environment variables.
