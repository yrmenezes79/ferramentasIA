import re
import random

def chatbot_respostas(mensagem):
    mensagem = mensagem.lower()
    
    # Dicionário de regras: Chave (Regex) -> Lista de Respostas
    regras = {
        r'oi|olá|bom dia|boa tarde': 
            ["Olá! Como posso ajudar você hoje?", "Oi! Tudo bem?", "Bem-vindo ao nosso suporte!"],
        r'curso|aula|pós': 
            ["As aulas de pós-graduação ocorrem aos sábados.", "O material está disponível no portal do aluno."],
        r'nota|prova|exame': 
            ["As notas serão lançadas em até 7 dias úteis.", "A prova final será presencial."],
        r'obrigado|vlw|valeu': 
            ["Por nada! Precisando, é só chamar.", "Disponha!", "Até logo!"],
        r'sair|tchau|encerrar': 
            ["Encerrando o atendimento. Até mais!", "Tchau tchau!"]
    }

    # Lógica de busca
    for padrao, respostas in regras.items():
        if re.search(padrao, mensagem):
            return random.choice(respostas)
    
    return "Desculpe, não entendi. Pode repetir de outra forma?"

# Interface simples no console
print("--- Chatbot Acadêmico Iniciado (digite 'sair' para parar) ---")
while True:
    user_input = input("Você: ")
    resposta = chatbot_respostas(user_input)
    print(f"Bot: {resposta}")
    if "sair" in user_input.lower():
        break
