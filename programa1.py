import chromadb

# 1. Inicializar o cliente
client = chromadb.Client()
collection = client.create_collection(name="meu_conhecimento")

# 2. Adicionar documentos (o Chroma cria os vetores automaticamente)
collection.add(
    documents=["O Python e otimo para Data Science", "O cafe ajuda a focar", "Kubernetes gerencia containers","Mackenzie e uma boa faculdade"],
    ids=["id1", "id2", "id3", "id4"]
)

# 3. Realizar uma busca semântica
# Note que nao usamos a palavra "Python" na pergunta
results = collection.query(
    query_texts=["Onde devo cursar uma diciplina"],
    n_results=1
)

print(f"Resultado mais próximo: {results['documents'][0]}")