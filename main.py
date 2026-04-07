# Titulo
# input do chat 
# a cada mensagem que o usuario enviar:
  # mostar a mensagem que o usuario enviou
  # pegar a pergunta e enviar pra IA respoder
  # mostrar a resposta da IA

# Streamlit -> apenas com o python e possivel mexer como fullstack
# IA que iremos usar: OpenAI

# comando pra rodar -> python -m streamlit run main.py

import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key="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")

st.write("### Chatbot com IA") # Markdown

# session_state = memoria do streamlit
if "lista_mensagens" not in st.session_state:
  st.session_state["lista_mensagens"] = [] # -> se não tiver uma lista criada ele iriar criar uma

# adicionar uma mensagem
# st.session_state["Lista_mensagens"].append(mensagem)

# exibir o historico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
  role = mensagem['role'] # Pegar o valor do usuario
  content = mensagem['content'] # Pegar a mensagem escrita
  st.chat_message(role).write(content) # Mostrar as mensagens 

text_usuario = st.chat_input("Digite sua mensagem")

if text_usuario:
  # user -> icone de usuario
  # assistant -> icone de IA 
  st.chat_message("user").write(text_usuario)
  mensagem_usuario = {"role": "user", "content": text_usuario} # -> Criando a mensagem do usuario
  ["lista_mensagens"].append(text_usuario) # -> Adicionando na lista

  # resposta da IA
  reposta_modelo = modelo.responses.create(
    messages=st.session_state["lista_mensagens"],
    model="gpt-5.4"
  )

  resposta_ia = reposta_modelo.choices[0].message.content

  #exibir a respota da IA na tela
  st.chat_message("assistant").write(resposta_ia)
  mensagem_ia = {"role": 'assistant', "content": resposta_ia}
  st.session_state["lista_mensagens"].append(mensagem_ia)

