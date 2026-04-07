# Listas
lista_nova = []
nomes = ['Lira', 'Thalia', 'Guilherme', 'Alon']
nomes.append('Michely') # -> Add informação no final da lista


# Dicionário
# Estrutura do dicionário = {chave: valor, chave: valor}
idades = {'lira': 31, 'Thalia':23, 'Alon': 45}
print(idades['lira']) # Pega informação do dicionario -> dicionario[chave]
idades['Michely'] = 26 # Adicionar
idades['lira'] = 27 # Editar

# role = quem é o usuario
# assistant = IA
# user = pessoa
# content = texto
mensagem_1 = {'role': 'assistant', 'content': 'Bora aprender python'}
mensagem_2 = {'role': 'user', 'content': 'Bora sim'}
mensagem_3 = {'role': 'assistant', 'content': 'Então vamos começar'}

lista_mensagem = [mensagem_1, mensagem_2, mensagem_3]

nova_mensagem = {'role': 'user', 'content': 'Opa, agora bora botar Python pra jogo'}
lista_mensagem.append(nova_mensagem)