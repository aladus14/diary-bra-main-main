# 📔 Diário do Programador — Projeto da Turma

Projeto feito em **Python (Flask)** para praticar **bancos de dados**: um diário onde cada entrada (cartão) tem título, subtítulo e texto, e fica salva num banco de dados de verdade (SQLite), não só na memória.

Este README foi feito para ajudar você a **rodar o projeto na sua máquina** e **entender onde mexer** para completar a atividade.

---

## ✅ O que você precisa ter instalado

1. **Python 3** — [baixe aqui](https://www.python.org/downloads/) se ainda não tiver.
   - Para conferir se já tem, abra o terminal e digite:
     ```bash
     python --version
     ```
2. **Flask** e **Flask-SQLAlchemy** (a biblioteca que conecta o Flask a um banco de dados) — instalamos no próximo passo.

---

## 🚀 Passo a passo para rodar o projeto

**1. Baixe o projeto** e entre na pasta dele pelo terminal.

**2. Instale as bibliotecas necessárias**
```bash
pip install flask
pip install Flask-SQLAlchemy
```
> Se der erro de "comando não encontrado", tente `pip3 install flask` e `pip3 install Flask-SQLAlchemy`, ou `python -m pip install ...`.

**3. Crie o banco de dados**

O `main.py` define como o banco deve ser (a classe `Card`), mas isso sozinho **não cria o arquivo do banco**. Antes de rodar o projeto pela primeira vez (e depois de completar a Tarefa 1), siga esses passos no terminal, dentro da pasta do projeto:

1. Digite `python` para entrar no modo interativo do Python:
   ```
   python
   ```
2. Importe `app` e `db` do `main`:
   ```python
   >>> from main import app, db
   ```
3. Quando o projeto criar a pasta `instance` dentro dele, digite:
   ```python
   >>> app.app_context().push()
   ```
   Esse comando avisa o Flask que estamos trabalhando no contexto do site. É como ligar o "modo site" para o banco de dados!
4. Por fim, crie o arquivo do banco de dados:
   ```python
   >>> db.create_all()
   ```

Isso cria o arquivo do banco (dentro da pasta `instance/`), já com a tabela `Card` dentro dele. Depois disso, digite `exit()` para sair do modo Python.

> ⚠️ Se você mudar os campos da classe `Card` depois de já ter criado o banco, ele **não** se atualiza sozinho. Apague o arquivo do banco dentro de `instance/` e repita esse passo para recriá-lo do zero.

**4. Rode a aplicação**
```bash
python main.py
```

**5. Abra no navegador**

O terminal vai mostrar algo como:
```
Running on http://127.0.0.1:5000
```
Copie esse endereço e cole no navegador. 🎉

> Para parar a aplicação, volte ao terminal e aperte `Ctrl + C`.

---

## 🧭 Como o projeto está organizado

```
diario-do-programador/
├── main.py              → rotas, conexão com o banco e a classe Card
├── instance/
│   └── diary.db            → banco de dados SQLite (você cria esse arquivo, veja o Passo 3)
├── templates/
│   ├── index.html         → lista todos os cartões do diário
│   ├── card.html          → mostra um cartão específico
│   └── create_card.html   → formulário para criar um novo cartão
└── static/                → CSS e outros arquivos de estilo
```

- **`main.py`**: define o que é um "Card" no banco de dados (classe `Card`) e as rotas que criam, listam e mostram os cartões.
- **`instance/diary.db`**: o banco de dados em si, criado por você no Passo 3. Se você apagar esse arquivo, todos os cartões salvos são perdidos — é preciso repetir o Passo 3 para recriá-lo (vazio).

---

## 🖱️ Como funciona

1. `/` → lista todos os cartões já salvos no banco.
2. `/card/<id>` → mostra um cartão específico, pelo número dele.
3. `/create` → mostra o formulário para criar um novo cartão.
4. `/form_create` → recebe os dados do formulário e salva um novo cartão no banco.

---

## 📝 Atividades — o que precisa ser feito

O arquivo `main.py` já tem **pistas em comentário** em cada lugar que falta completar, explicando em português o que aquela linha precisa fazer. A ideia aqui não é te dar a resposta pronta, mas mostrar o **padrão** que você precisa seguir — você ainda precisa adaptar para cada caso.

### Tarefa 1 — Criar a classe `Card` (a "tabela" do banco de dados)
📄 Local: `main.py`, dentro de `class Card(db.Model):`

Cada linha da classe representa uma coluna da tabela no banco. O padrão de uma coluna é:
```python
nome_do_campo = db.Column(TIPO_DO_CAMPO, OPÇÕES)
```
Onde:
- `TIPO_DO_CAMPO` pode ser `db.Integer` (número inteiro), `db.String(tamanho)` (texto curto, com limite de caracteres) ou `db.Text` (texto longo, sem limite)
- `OPÇÕES` pode ser `primary_key=True` (identifica o registro — só o `id` usa isso) ou `nullable=False` (campo obrigatório, não pode ficar vazio)

O próprio comentário acima de cada campo já diz qual tipo usar:
```python
# id = coluna do banco de dados(inteiro, chave primária)
id = 
```
Esse é o único campo que usa `primary_key=True` em vez de `nullable=False`. Complete esse primeiro para ter um exemplo de referência, e depois siga o mesmo raciocínio para `title`, `subtitle` e `text`, usando o tipo que o comentário de cada um indica.

### Tarefa 2 — Mostrar os cartões ordenados por ID
📄 Local: `main.py`, na rota `/` (função `index`)

O comentário já mostra o padrão, só traduzido:
```python
# cards = Card.query. ordenado por (Card.id).todos()
```
Em inglês (que é como o SQLAlchemy realmente escreve), esse padrão é:
```python
Card.query.order_by(CAMPO).all()
```
Substitua `CAMPO` pela coluna que você quer usar para ordenar (pense: pela ordem em que os cartões foram criados, do mais antigo pro mais novo — qual campo representa isso?).

Depois de completar essa linha, descomente a linha `#cards = cards` dentro do `render_template`, para a lista chegar até o `index.html`.

### Tarefa 2.1 — Mostrar um cartão específico pelo ID
📄 Local: `main.py`, na rota `/card/<int:id>`

De novo, o comentário já traduz o padrão:
```python
#card = Card.query. obter(id)
```
Em código real, "obter" é o método `.get(...)`:
```python
Card.query.get(ARGUMENTO)
```
Substitua `ARGUMENTO` pelo que a própria rota já recebeu como parâmetro (olhe o `def card(id):` logo acima — qual variável guarda o número do cartão?).

### Tarefa 2 (no formulário) — Criar e salvar um novo cartão
📄 Local: `main.py`, na rota `/form_create`

As três variáveis já foram capturadas do formulário:
```python
title = request.form['title']
subtitle = request.form['subtitle']
text = request.form['text']
```
Agora, o comentário mostra como montar o objeto:
```python
# card = Card(titulo=titulo, subtitulo=subtitulo, texto=texto)
```
Esse exemplo está em português só para explicar a ideia — os nomes reais que você deve usar são os mesmos da sua classe `Card` (Tarefa 1) e das variáveis que já foram capturadas acima (`title`, `subtitle`, `text`), não "titulo"/"subtitulo"/"texto". O padrão geral é:
```python
Card(coluna1=valor1, coluna2=valor2, coluna3=valor3)
```
Depois de criar o `card`, salve ele de fato no banco — isso o comentário já entrega pronto, é só adicionar embaixo da linha do `card =`:
```python
db.session.add(card)
db.session.commit()
```

---

## 🛠️ Problemas comuns

| Problema | Possível solução |
|---|---|
| `ModuleNotFoundError: No module named 'flask_sqlalchemy'` | Rode `pip install Flask-SQLAlchemy` novamente, verifique se está na pasta certa |
| `sqlalchemy.exc.OperationalError` ou tabela não encontrada | O `instance/diary.db` não existe ainda ou está desatualizado. Apague-o (se existir) e repita o Passo 3 (`db.create_all()`) |
| Rodei `python main.py` mas não existe a pasta `instance/` | Isso é esperado — `db.create_all()` precisa ser rodado manualmente (Passo 3), `python main.py` sozinho não cria o banco |
| A lista de cartões aparece vazia mesmo depois de criar um | Confira se a Tarefa 2 (mostrar os cartões) foi completada e se a linha `#cards = cards` foi descomentada |
| Erro ao clicar em "criar cartão" | Confira se os nomes usados em `Card(...)` são exatamente os mesmos nomes de colunas definidos na Tarefa 1 |
| Mudei a classe `Card` e nada mudou no banco | O SQLite não atualiza a estrutura de uma tabela já existente sozinho — apague o `instance/diary.db` e repita o Passo 3 |

---

## 📚 Aprendizados desse projeto

- O que é um banco de dados e por que usar um em vez de guardar tudo na memória
- Como definir uma tabela usando uma **classe** (`db.Model`) com o SQLAlchemy
- Como salvar (`add` + `commit`), listar (`query.order_by().all()`) e buscar um registro específico (`query.get()`)
- Como conectar o banco de dados às páginas HTML através do Flask
