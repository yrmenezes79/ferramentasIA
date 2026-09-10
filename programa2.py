import numpy as np

# 1. Definimos o que já temos no "Banco de Dados"
vetor_gato = np.array([0.1, 0.9, 0.8, 0.9, 0.9])
vetor_cao = np.array([0.8, 0.2, 0.1, 0.3, 0.1])

# 2. Chega uma nova imagem (um "gatinho filhote" que o sistema nunca viu)
nova_imagem = np.array([0.15, 0.85, 0.78, 0.82, 0.88])

# 3. Função para calcular a distância matemática
def calcular_distancia(v1, v2):
    return np.sqrt(np.sum((v1 - v2)**2))

dist_para_gato = calcular_distancia(nova_imagem, vetor_gato)
dist_para_cao = calcular_distancia(nova_imagem, vetor_cao)

print(f"Distância até o Gato: {dist_para_gato:.4f}")
print(f"Distância até o Cão: {dist_para_cao:.4f}")

# O Banco retorna o vizinho mais próximo (Nearest Neighbor)
resultado = "GATO" if dist_para_gato < dist_para_cao else "CÃO"
print(f"\nResultado da busca: Esta imagem é um {resultado}!")