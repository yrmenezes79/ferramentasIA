import chromadb

# 1. Inicializa o cliente ChromaDB (em memória / local)
client = chromadb.Client()

# 2. Cria a coleção para o FAQ da universidade
colecao_faq = client.create_collection(name="faq_atendimento")

# 3. Base de regras/conhecimento do campus
documentos = [
    "O trancamento de matrícula deve ser solicitado até o dia 15 pelo portal acadêmico.",
    "O restaurante universitário serve almoço de segunda a sexta, das 11h às 14h.",
    "A biblioteca central permite o empréstimo de até 5 livros pelo prazo de 14 dias.",
    "O comprovante de vacinação atualizado deve ser anexado na área do aluno no ato da matrícula.",
    "As solicitações de passe escolar e declarações de matrícula levam até 3 dias úteis.",
]

# IDs únicos para cada documento
ids = ["doc_trancamento", "doc_ru", "doc_biblioteca", "doc_vacina", "doc_passe"]

# O Chroma gera os embeddings automaticamente via modelo padrão
colecao_faq.add(
    documents=documentos,
    ids=ids
)

# 4. Perguntas de teste (usando gírias/sinônimos, sem palavras-chave idênticas)
perguntas = [
    "Como faço para dar um tempo na faculdade?",
    "Que horas posso comer no campus?",
    "Onde consigo pegar material de estudo emprestado?",
    "Preciso levar carteirinha de vacina?",
]

print("--- RESULTADOS DA BUSCA SEMÂNTICA ---\n")
for pergunta in perguntas:
    resposta = colecao_faq.query(
        query_texts=[pergunta],
        n_results=1
    )
    doc_encontrado = resposta["documents"][0][0]
    id_encontrado = resposta["ids"][0][0]
    distancia = resposta["distances"][0][0]
    
    print(f"Pergunta do aluno: '{pergunta}'")
    print(f"Documento retornado ({id_encontrado}): {doc_encontrado}")
    print(f"Distância semântica: {distancia:.4f}\n")