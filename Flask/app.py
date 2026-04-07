from flask import Flask, render_template # estruturas para criar o site
from flask_socketio import SocketIO, send # estruturas para criar o chat

app = Flask(__name__) # cria o site
app.config["SECRET"] = "ajuiahfa12535455fgs7f65" # cahve de segurança
app.config["DEBUG"] = True # para testarmos o codigo, no final tiramos
Socketio = SocketIO(app, cors_allowed_origins="*") # cria a conecção entre diferentes máquinas que estão no site

@Socketio.on("menssage") # define que a função abaixo vai ser acionada quanod o evento menssage acontecer
def gerenciar_mensagens(mensagem):
  print(f"Messagem: {mensagem}")
  send(mensagem, broadcast = True) # envia a mensagem para todo mundo conectado ao site

@app.route("/") # cria a página do site
def home():
  return render_template("index.html") # essa página vai carregar o arquivo html

if __name__ == "__manin__":
  Socketio.run(app, host="localhost") # define que o app vai rodar no seu servido local