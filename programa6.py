# Coleção configurada para Similaridade/Distância de Cosseno
faq_cosseno = client.create_collection(
    name="faq_cosseno",
    metadata={"hnsw:space": "cosine"}
)
faq_cosseno.add(documents=documentos, ids=ids)

# Coleção configurada para Distância Euclidiana (L2)
faq_l2 = client.create_collection(
    name="faq_l2",
    metadata={"hnsw:space": "l2"}
)
faq_l2.add(documents=documentos, ids=ids)

teste = ["Onde posso almoçar barato?"]

res_cosseno = faq_cosseno.query(query_texts=teste, n_results=1)
res_l2 = faq_l2.query(query_texts=teste, n_results=1)

print("--- COMPARAÇÃO DE MÉTRICAS ---")
print(f"Busca: '{teste[0]}'")
print(f"Cosseno -> Doc: {res_cosseno['ids'][0][0]} | Distância: {res_cosseno['distances'][0][0]:.4f}")
print(f"L2 (Euclidiana) -> Doc: {res_l2['ids'][0][0]} | Distância: {res_l2['distances'][0][0]:.4f}")