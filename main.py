# Importar
from flask import Flask, render_template, request, redirect
# Importando a biblioteca de banco de dados

#ANTES DE UTILIZAR UTILIZE O COMANDO: pip install Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Conectando ao SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Criando um Banco de Dados (DB)
db = SQLAlchemy(app)

# TAREFA 1. Criar uma classe Card para o Banco de Dados #############################################


class Card(db.Model):
    # Criando campos
    # id = coluna do banco de dados(inteiro, chave primária)
    id = 
    # Titulo = coluna do banco de dados(string com limite de 100 caracteres, não nula)
    title = 
    # Descrição = coluna do banco de dados(string com limite de 300 caracteres, não nula)
    subtitle = 
    # Texto = coluna do banco de dados(texto, não nula)
    text = 

    # Mostrando o Objeto e o ID
    def __repr__(self):
        return f'<Card {self.id}>'
    
####################################################################################################


# Executando a página com conteúdo
@app.route('/')
def index():
# Exibindo os objetos do Banco de Dados
# TAREFA 2 EXIBIR OS CARTÕES ORDENADOS PELO ID
# cards = Card.query. ordenado por (Card.id).todos() 
    cards = 


    return render_template('index.html',
                           #cards = cards

                           )

####################################################################################################

# Executando a página com o cartão
@app.route('/card/<int:id>')
def card(id):
    # TAREFA 2.1 EXIBIR O CARTÃO PELO ID
    #card = Card.query. obter(id)
    card = 

    return render_template('card.html', card=card)

####################################################################################################


# Executando a página e criando o cartão
@app.route('/create')
def create():
    return render_template('create_card.html')

# O formulário do cartão
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']
        
####################################################################################################

        # Tarefa #2. Criar uma forma de armazenar dados no Banco de Dados
        # card = Card(titulo=titulo, subtitulo=subtitulo, texto=texto)
        card = 
        
        #adicione a sessão com db.session.add(card) e depois faça o commit com db.session.commit()
        
        
####################################################################################################    
        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)
