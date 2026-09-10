from sklearn.preprocessing import StandardScaler
import pandas as pd

# Criando dados de exemplo (Idade vs Salário)
data = {'Idade': [25, 33, 42, 54], 'Salario': [2500, 4800, 7100, 12000]}
df = pd.DataFrame(data)

# 1. Instanciar o escalonador
scaler = StandardScaler()

# 2. Fit e Transform
# O 'fit' calcula a média e o desvio padrão.
# O 'transform' aplica a fórmula matemática.
df_scaled = scaler.fit_transform(df)

# Resultado: agora Idade e Salário estão na mesma escala (em torno de 0)
print(df_scaled)